from geo_parser.settings import YANDEX
import requests


def parse(geo_point, key, attempts=0):
    query = "город " + geo_point.city + " " + geo_point.address

    data = {
        'kind': 'house',
        'format': 'json',
        'sco': 'latlong',
        'geocode': query
    }

    if key:
        data['apikey'] = key

    try:
        response = requests.get(YANDEX.get('PARSE_URL'), data)
        json = response.json()

        if not check_has_results(json):
            geo_point.status = 3
            return

        geo_point.coordinates = get_coordinates(json)
        geo_point.status = 2
        geo_point.used_map = 'yandex'

    except Exception as e:
        print(e)
        if attempts == 3:
            geo_point.status = 1
            return
        parse(geo_point, attempts + 1)


def get_coordinates(json):
    coordinates = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    return tuple(coordinates.split(' '))


def check_has_results(json):
    return len(json['response']['GeoObjectCollection']['featureMember']) > 0
