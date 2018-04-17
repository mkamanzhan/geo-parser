from geo_parser.settings import GOOGLE
import requests


def parse(geo_point, attempts=0):
    query = geo_point.country + " город " + geo_point.city + " " + geo_point.address

    data = {
        'language': 'ru',
        'address': query
    }
    try:
        response = requests.get(GOOGLE.get('PARSE_URL'), data)
        json = response.json()

        if not check_response(json):
            geo_point.status = 1

        if not check_has_results(json):
            geo_point.status = 3
            return

        geo_point.coordinates = get_coordinates(json)
        geo_point.status = 2
        geo_point.used_map = 'google'

    except Exception as e:
        if attempts == 3:
            geo_point.status = 1
            return
        parse(geo_point, attempts + 1)


def get_coordinates(json):
    coordinates = (
        json['results'][0]['geometry']['location']['lat'],
        json['results'][0]['geometry']['location']['lng']
    )
    return coordinates


def check_has_results(json):
    return len(json['results']) > 0


def check_response(json):
    return json['status'] in ('OK', 'ZERO_RESULTS')