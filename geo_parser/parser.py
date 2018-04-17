from multiprocessing import Pool


def parse_all(geo_points, pool_size=20):
    pool = Pool(pool_size)
    pool.map(parse, geo_points)


def parse(geo_point):
    geo_point.parse_coord()
