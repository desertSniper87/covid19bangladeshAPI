from api.dictionary import iedcr2bcc_district

import requests
import json
from collections import OrderedDict
from copy import deepcopy

arcGis_district_url = "https://services3.arcgis.com/nIl76MjbPamkQiu8/arcgis/rest/services/districts_wise_corona_data/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&maxRecordCountFactor=4&orderByFields=confirmed%20DESC&outSR=102100&resultOffset=0&resultRecordCount=8000&cacheHint=true&quantizationParameters=%7B%22mode%22%3A%22view%22%2C%22originPosition%22%3A%22upperLeft%22%2C%22tolerance%22%3A1.0583354500042312%2C%22extent%22%3A%7B%22xmin%22%3A9826319.17328554%2C%22ymin%22%3A2444041.9364330745%2C%22xmax%22%3A10283573.777836105%2C%22ymax%22%3A3040113.3163954075%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D"


def getDistrictConfirmDict():
    district_response = requests.get(arcGis_district_url)
    district_json = json.loads(district_response.text)
    district_confirm_dict = OrderedDict()

    dhaka_city_count = 0
    for attr in district_json['features']:
        name = attr['attributes']['name']
        confirmed = attr['attributes']['confirmed']
        if name in ['Dhaka City', 'Dhaka (District)']:
            dhaka_city_count += confirmed
        elif name in iedcr2bcc_district.keys():
            district_confirm_dict[iedcr2bcc_district[name]] = confirmed
        else:
            district_confirm_dict[name] = confirmed

    district_confirm_dict['Dhaka'] = dhaka_city_count

    return district_confirm_dict

def getDistrictCsvJson(district_confirm_dict):
    inital_json = scrape_districts(district_confirm_dict)
    return [x.get('properties') for x in inital_json.get('features')]

def scrape_districts(district_confirm_dict):
    base_json = json.load(open('base.json'))
    final_json = deepcopy(base_json)

    for fx, f in enumerate(base_json['features']):
    #     print(fx, f)
        key = f['properties']['key']
        final_json['features'][fx]['properties']['confirmed'] = str(district_confirm_dict[key])

    return final_json
