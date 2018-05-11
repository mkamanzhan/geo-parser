from multiprocessing import Pool


class BaseParser:

    def parse_all(self):
        pool = Pool(self.pool_size)
        self.geo_points = pool.map(self.parse, self.geo_points)

    def parse(self, geo_point):
        geo_point.parse_coord(self.service_keys)
        return geo_point