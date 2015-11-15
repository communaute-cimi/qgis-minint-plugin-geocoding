"""
OpenStreetMaps geocoder, contributed by Alessandro Pasotti of ItOpen.
"""

from geopy.geocoders.base import (
    Geocoder,
    DEFAULT_FORMAT_STRING,
    DEFAULT_TIMEOUT,
    DEFAULT_SCHEME
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
            view_box=(-180, -90, 180, 90),
            country_bias=None,
            timeout=DEFAULT_TIMEOUT,
            proxies=None,
            #domain='nominatim.openstreetmap.org',
            domain='localhost',
            # scheme=DEFAULT_SCHEME
            scheme='http',
            port = '8080'
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
        self.country_bias = country_bias
        self.format_string = format_string
        self.view_box = view_box
        self.country_bias = country_bias
        self.domain = domain.strip('/')
        self.port = port
        
        # self.api = "%s://%s/search" % (self.scheme, self.domain)
        self.api = "%s://%s:%s/soclesigGeocodeResponse.json" % (self.scheme, self.domain, self.port)
        # self.reverse_api = "%s://%s/reverseGeocode.json" % (self.scheme, self.domain)
        self.reverse_api = "%s://%s:%s/soclesigReverseGeocodeResponse.json" % (self.scheme, self.domain, self.port)


    def geocode(
            self,
            query,
            exactly_one=True,
            timeout=None,
            addressdetails=False,
            language=False,
            geometry=None
    ):  # pylint: disable=R0913,W0221
        """
        Geocode a location query.

        :param query: The address, query or structured query to geocode
            you wish to geocode.

            For a structured query, provide a dictionary whose keys
            are one of: `street`, `city`, `county`, `state`, `country`, or
            `postalcode`. For more information, see Nominatim's
            documentation for "structured requests":

                https://wiki.openstreetmap.org/wiki/Nominatim

        :type query: dict or string

            .. versionchanged:: 1.0.0

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

            .. versionadded:: 0.97

        :param addressdetails: If you want in *Location.raw* to include
            addressdetails such as city_district, etc set it to True
        :type addressdetails: bool

        :param string language: Preferred language in which to return results.
            Either uses standard
            `RFC2616 <http://www.ietf.org/rfc/rfc2616.txt>`_
            accept-language string or a simple comma-separated
            list of language codes.
        :type addressdetails: string

            .. versionadded:: 1.0.0

        :param string geometry: If present, specifies whether the geocoding
            service should return the result's geometry in `wkt`, `svg`,
            `kml`, or `geojson` formats. This is available via the
            `raw` attribute on the returned :class:`geopy.location.Location`
            object.

            .. versionadded:: 1.3.0

        """

        if isinstance(query, dict):
            params = {
                key: val
                for key, val
                in query.items()
                if key in self.structured_query_params
            }
        else:
            params = {'q': self.format_string % query}

        params.update({
            # `viewbox` apparently replaces `view_box`
            'viewbox': self.view_box,
            'format': 'json'
        })

        if self.country_bias:
            params['countrycodes'] = self.country_bias

        if addressdetails:
            params['addressdetails'] = 1

        if language:
            params['accept-language'] = language

        if geometry is not None:
            geometry = geometry.lower()
            if geometry == 'wkt':
                params['polygon_text'] = 1
            elif geometry == 'svg':
                params['polygon_svg'] = 1
            elif geometry == 'kml':
                params['polygon_kml'] = 1
            elif geometry == 'geojson':
                params['polygon_geojson'] = 1
            else:
                raise GeocoderQueryError(
                    "Invalid geometry format. Must be one of: "
                    "wkt, svg, kml, geojson."
                )

        url = "?".join((self.api, urlencode(params)))
        logger.debug("%s.geocode: %s", self.__class__.__name__, url)
        print url
    
        return self._parse_json(
            self._call_geocoder(url, timeout=timeout), exactly_one
        )

    def reverse(
            self,
            query,
            exactly_one=True,
            timeout=None,
            language=False,
    ):  # pylint: disable=W0221
        """
        Returns a reverse geocoded location.

        :param query: The coordinates for which you wish to obtain the
            closest human-readable addresses.
        :type query: :class:`geopy.point.Point`, list or tuple of (latitude,
            longitude), or string as "%(latitude)s, %(longitude)s"

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

            .. versionadded:: 0.97

        :param string language: Preferred language in which to return results.
            Either uses standard
            `RFC2616 <http://www.ietf.org/rfc/rfc2616.txt>`_
            accept-language string or a simple comma-separated
            list of language codes.
        :type addressdetails: string

            .. versionadded:: 1.0.0

        """
        try:
            lat, lon = [
                x.strip() for x in
                self._coerce_point_to_string(query).split(',')
            ]  # doh
        except ValueError:
            raise ValueError("Must be a coordinate pair or Point")
        params = {
            'lat': lat,
            'lon': lon,
            'format': 'json',
        }
        if language:
            params['accept-language'] = language
        url = "?".join((self.reverse_api, urlencode(params)))
        logger.debug("%s.reverse: %s", self.__class__.__name__, url)
        return self._parse_json_rev(
            self._call_geocoder(url, timeout=timeout), exactly_one
        )
    
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

    def _parse_json_rev(self, places, exactly_one):
        
        if places is None:
            return None
        if not isinstance(places, list):
            places = [places]
        if not len(places):
            return None
        if exactly_one is True:
            return self.parse_code_rev(places[0])
        else:
            return [self.parse_code_rev(place) for place in places]

    @staticmethod
    def parse_code_rev(place):
        """
        Parse each resource.
        """
        latitude = place.get('location').get('y', None)
        longitude = place.get('location').get('x', None)
        placename = place['address'].get('Street', None) + " " + place['address'].get('Postal', None) + " " + place['address'].get('City', None)
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)
        return Location(placename, (latitude, longitude), place)

    def _parse_json(self, doc, exactly_one):
        candidates = doc['candidates']

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
        
        # addr = doc.get('address').get('Street', None) + " " + doc.get('address').get('Postal', None)
        addr = doc.get('address').get('Postal', None)
        x = doc['location'].get('x', None)
        y = doc['location'].get('y', None)
    
        latitude = y
        longitude = x
        placename = addr
        
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)
        return Location(placename, (latitude, longitude), doc)
        
