from .yandex_parser import parse as yandex_parse
from .google_parser import parse as google_parse

STATUS_CODE = {
    1: 'not_parsed',
    2: 'successful',
    3: 'coord_not_found',
}


class GeoPoint:
    """
    Attributes:
        address (str)
        country (str)
        city (str)

        coordinates (tuple): (longitude, latitude) coordinate of point

        status (int): status of geo_point parsing

        used maps (string): map that parsed successful
    """

    def __init__(self, address, country, city):
        self.address = address
        self.country = country
        self.city = city

        self.coordinates = None

        self.status = 1
        self.used_map = None

    def parse_coord(self, service_keys):
        yandex_parse(self, service_keys.get('yandex'))
        if self.status == 3:
            google_parse(self, service_keys.get('google'))

    def __str__(self):
        return str(self.__dict__)