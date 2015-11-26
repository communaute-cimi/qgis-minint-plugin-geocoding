"""
OpenStreetMaps geocoder, contributed by Alessandro Pasotti of ItOpen.
"""

from geopy.geocoders.base import (
    Geocoder,
    DEFAULT_FORMAT_STRING,
    DEFAULT_TIMEOUT,
    DEFAULT_SCHEME,
    DEFAULT_WKID
)
from geopy.compat import urlencode
from geopy.location import Location
from geopy.util import logger
from geopy.exc import GeocoderQueryError
import pprint

__all__ = ("Soclesig", )


class Soclesig(Geocoder):
    """
    Nominatim geocoder for OpenStreetMap servers. Documentation at:
        https://wiki.openstreetmap.org/wiki/Nominatim

    Note that Nominatim does not support SSL.
    """

    structured_query_params = {
        'street',
        'city',
        'county',
        'state',
        'country',
        'postalcode',
    }

    def __init__(
            self,
            format_string=DEFAULT_FORMAT_STRING,
            timeout=DEFAULT_TIMEOUT,
            proxies=None,
            #domain='nominatim.openstreetmap.org',
            domain='localhost',
            # scheme=DEFAULT_SCHEME
            scheme='http'
    ):  # pylint: disable=R0913
        """
        :param string format_string: String containing '%s' where the
            string to geocode should be interpolated before querying the
            geocoder. For example: '%s, Mountain View, CA'. The default
            is just '%s'.

        :param tuple view_box: Coordinates to restrict search within.

        :param string country_bias: Bias results to this country.

        :param dict proxies: If specified, routes this geocoder's requests
            through the specified proxy. E.g., {"https": "192.0.2.0"}. For
            more information, see documentation on
            :class:`urllib2.ProxyHandler`.

            .. versionadded:: 0.96

        :param string domain: Should be the localized Openstreetmap domain to
            connect to. The default is 'nominatim.openstreetmap.org', but you
            can change it to a domain of your own.

            .. versionadded:: 1.8.2

        :param string scheme: Use 'https' or 'http' as the API URL's scheme.
            Default is https. Note that SSL connections' certificates are not
            verified.

            .. versionadded:: 1.8.2
        """
        super(Soclesig, self).__init__(
            format_string, scheme, timeout, proxies
        )
        self.format_string = format_string
        self.domain = domain.strip('/')

        # self.api = "%s://%s/search" % (self.scheme, self.domain)
        # self.api = "%s://%s/geocode.json" % (self.scheme, self.domain)
        self.api = "http://127.0.0.1:8080/soclesigGeocodeResponse.json"
        self.reverse_api = "http://127.0.0.1:8080/soclesigReverseGeocodeResponse.json"


    def geocode(
            self,
            query,
            timeout=None,
            exactly_one=True,
    ):  # pylint: disable=R0913,W0221
        """
        Geocode a location query.

        """
        params = {'q': self.format_string % query}

        params.update({
            'format': 'json'
        })

        url = "?".join((self.api, urlencode(params)))
        logger.debug("%s.geocode: %s", self.__class__.__name__, url)

        response = self._call_geocoder(url, timeout=timeout)

        # Success; convert from the ArcGIS JSON format.
        if not len(response['candidates']):
            return None
        geocoded = []
        for resource in response['candidates']:
            geocoded.append(
                Location(
                    resource['address'], (resource['location']['y'], resource['location']['x']), resource
                )
            )
            
        if exactly_one is True:
            return geocoded[0]
        return geocoded

    def reverse(
            self,
            query,
            exactly_one=True,
            timeout=None,
            wkid=DEFAULT_WKID
    ):  # pylint: disable=W0221
        """
        Returns a reverse geocoded location.

        """
        try:
            lat, lon = [
                x.strip() for x in
                self._coerce_point_to_string(query).split(',')
                ]  # doh
        except ValueError:
            raise ValueError("Must be a coordinate pair or Point")

        location = {"x": lon, "y": lat}
        
    
        params = {'location' : location,'distance' : 50000, 'inSR':wkid, 'outSR':wkid}

        url = "?".join((self.reverse_api, urlencode(params)))
        
        logger.debug("%s.reverse: %s", self.__class__.__name__, url)
        
        response = self._call_geocoder(url, timeout=timeout)
        
        if not len(response):
            return None
        
        address = (
                   "%(Street)s, %(Postal)s, %(City)s %(Loc_name)s," % response['address']
                   )
        
        return [Location(
            address,
            (response['location']['y'], response['location']['x']),
            response['address']
        )]

    @staticmethod
    def parse_code(candidate):
        """
        Parse each resource.
        """
        
        address = candidate.get('address', None)
        x = candidate['location'].get('x', None)
        y = candidate['location'].get('y', None)
    
        latitude = y
        longitude = x
        placename = address
        
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)
        return Location(placename, (latitude, longitude), candidate)

    def _parse_json(self, doc, exactly_one):
        candidates = doc['candidates']
        # pprint.pprint()
        # return 0

        if candidates is None:
            return None
        if not isinstance(candidates, list):
            candidates = [candidates]
        if not len(candidates):
            return None
        if exactly_one is True:
            return self.parse_code(candidates[0])
        else:
            return [self.parse_code(candidate) for candidate in candidates]
        
    def _parse_reverse_json(self, doc, exactly_one):
        
        addr = doc.get('address').get('Street', None) + " " + doc.get('address').get('Postal', None)
        
        x = doc['location'].get('x', None)
        y = doc['location'].get('y', None)
    
        latitude = y
        longitude = x
        placename = addr
        
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)
        return Location(placename, (latitude, longitude), doc)
        
