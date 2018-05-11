# Geo-Parser


### Description
Geo-Parser is a python package that returns 
coordinates for given address

Geo-Parser uses Yandex & Google geocoder API
to identify given address and get coordinates

Package uses multithreading to parse 
multiple addresses in one time. It means that package
can be used to parse large datasets of addresses


### Usage

Clone project to temp folder:
```bash
git clone https://github.com/mkamanzhan/geo-parser
```

Install package:
```bash
pip install package_dir/
```

Create GeoPoint object from given address:

```python
from geo_parser import GeoPoint

geo_point = GeoPoint(
    address='просп. Абылай хана, 1/1',
    city='Каскелен',
    country='Казахстан',
)
```

Parse its coordinates:

```python
geo_point.parse_coord()

print(geo_point.coordinates)
```
Result in (lat, long):
```pythonstub
('43.208022', '76.669525')
```

Also its possible to parse multiple GeoPoints:
```python
from geo_parser import SimpleParser

# geo_points: list of GeoPoints

# optional arguments 
#   pool_size: number of threads running one time. default=20
#   service_keys: apikeys of Yandex & Google geocoder Service
simple_parser = SimpleParser(geo_points)
simple_parser.parse_all()
print(simple_parser.geo_points)
```
Result in list:
```pythonstub
[GeoPoint, GeoPoint, ...]
```

GeoPoint parse status can be retrieved by ```geo_point.status``` attribute
* 1 for not parsed/failed on request GeoPoints
* 2 for success parsed GeoPoints
* 3 for GeoPoints that can't retrieve coordinates fro services(services returns zero result)


### Used Instruments and Links

Requests: http://docs.python-requests.org/en/master/
<br>
Used to make http GET requests to service API's

Multithreading: https://docs.python.org/2/library/multiprocessing.html
<br>
Used to parse addresses in threads for performance

Yandex API: https://tech.yandex.ru/maps/doc/geocoder/desc/concepts/input_params-docpage/


Google API: https://developers.google.com/maps/documentation/geocoding/intro?hl=ru

Similar projects:
* [GeoParser](https://geoparser.io/docs.html)
* [Mordecai](https://github.com/openeventdata/mordecai)

