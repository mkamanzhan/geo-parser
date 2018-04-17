import csv
    from geo_parser import parse_all, parse, GeoPoint


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_NONNUMERIC
    delimiter = ';'
    lineterminator = '\n'
    quotechar = '"'


def test():
    geo_points = read_csv('tests/data/data.csv')
    parse_all(geo_points)
    write_csv(geo_points)


def read_csv(path):
    geo_points_list = list()
    with open(path) as csv_file:
        data = csv.DictReader(csv_file, delimiter=';')
        for row in data:
            geo_points_list.append(GeoPoint(**row))
    return geo_points_list


def write_csv(geo_points):
    with open('tests/data/results.csv', 'w') as csv_file:
        fieldnames = ['status', 'used_map', 'country', 'city', 'address', 'coordinates']

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,dialect=MyDialect)
        for geo_point in geo_points:
            writer.writerow({
                'status': geo_point.status,
                'used_map': geo_point.used_map,
                'country': geo_point.country,
                'city': geo_point.city,
                'address': geo_point.address,
                'coordinates': geo_point.coordinates
            })
