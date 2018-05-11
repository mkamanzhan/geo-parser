import csv, time
from geo_parser import SimpleParser, GeoPoint


SERVICE_KEYS = {
    'yandex': None,
    'google': None
}


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_NONNUMERIC
    delimiter = ';'
    lineterminator = '\n'
    quotechar = '"'


def test():
    start_time = time.time()
    geo_points = read_csv('tests/data/data.csv')
    simple_parser = SimpleParser(geo_points[:10], service_keys=SERVICE_KEYS)
    geo_points = simple_parser.parse_all(pool_size=50)
    write_csv(simple_parser.geo_points)
    end_time = time.time()
    print("Size: " + str(len(simple_parser.geo_points)))
    print("Total parse time: " + str(end_time - start_time) + "s")


def read_csv(path):
    geo_points_list = list()
    with open(path) as csv_file:
        data = csv.DictReader(csv_file, delimiter=';')
        for row in data:
            geo_points_list.append(GeoPoint(**row))
    return geo_points_list


def write_csv(geo_points):
    parsed = 0
    failed = 0
    not_found = 0
    with open('tests/data/results.csv', 'w') as csv_file:
        fieldnames = ['status', 'used_map', 'country', 'city', 'address', 'coordinates']

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,dialect=MyDialect)
        for geo_point in geo_points:
            if geo_point.status == 2: parsed += 1
            elif geo_point.status == 3: not_found += 1
            else: failed += 1
            writer.writerow({
                'status': geo_point.status,
                'used_map': geo_point.used_map,
                'country': geo_point.country,
                'city': geo_point.city,
                'address': geo_point.address,
                'coordinates': geo_point.coordinates
            })
    print("Parsed: " + str(parsed))
    print("Failed: " + str(failed))
    print("Not Found: " + str(not_found))