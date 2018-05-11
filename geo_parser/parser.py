from geo_parser.base_parser import BaseParser


class SimpleParser(BaseParser):

    def __init__(self, geo_points, service_keys=None):
        self.service_keys = service_keys
        self.geo_points = geo_points
