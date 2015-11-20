"""
Based on
OpenStreetMaps geocoder, contributed by Alessandro Pasotti of ItOpen.
Adaptation par le groupe carto du ST(SI)2
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
    Point d'entree de l'API : 
    http://host.minint.fr/{token}/rest/services/geocoding/v1/[geocode|reversegeocode]
    """

    def __init__(
            self,
            format_string=DEFAULT_FORMAT_STRING,
            timeout=DEFAULT_TIMEOUT,
            proxies=None,
            domain='localhost',
            scheme='http',
            port = '8080'
    ):  # pylint: disable=R0913
        """

        """
        super(Soclesig, self).__init__(
            format_string, scheme, timeout, proxies
        )
        self.format_string = format_string
        self.domain = domain.strip('/')
        self.port = port
        self.token = "" # token QGIS sur le socleSIG
        self.api = "%s://%s:%s/soclesigGeocodeResponse.json" % (self.scheme, self.domain, self.port)
        self.reverse_api = "%s://%s:%s/soclesigReverseGeocodeResponse.json" % (self.scheme, self.domain, self.port)


    def geocode(
            self,
            query,
            exactly_one=True,
            timeout=None
    ):  # pylint: disable=R0913,W0221
        """
        Geocode une adresse

        :param query: L'adresse a geocoder
        
        
        """

        params = {'q': self.format_string % query}

        params.update({
            'format': 'json'
        })

        url = "?".join((self.api, urlencode(params)))
        
        logger.debug("%s.geocode: %s", self.__class__.__name__, url)

        response = self._call_geocoder(url, timeout=timeout)

        if 'error' in response:
            raise GeocoderServiceError(str(response['error']))
        
        if not len(response):
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
            timeout=None
    ):  # pylint: disable=W0221
        """
        Retourne une geolocalisation inverse

        """
        try:
            lat, lon = [
                x.strip() for x in
                self._coerce_point_to_string(query).split(',')
            ]
        except ValueError:
            raise ValueError("Must be a coordinate pair or Point")
        params = {
            'lat': lat,
            'lon': lon,
            'location' : ('{"x":"%s","y":"%s"}', lat, lon),
            'distance' : 100, #KM ?
            'inSR' : 4326,
            'outSR' : 4326,
            'format': 'json',
        }

        url = "?".join((self.reverse_api, urlencode(params)))
        logger.debug("%s.reverse: %s", self.__class__.__name__, url)
        
        response = self._call_geocoder(url, timeout=timeout)
        
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
        
