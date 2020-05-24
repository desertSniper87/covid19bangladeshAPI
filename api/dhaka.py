from api.dictionary import iedcr2bcc_district, en2bn_dhk_area

import requests
import json
from collections import OrderedDict
from copy import deepcopy

arcGis_dhaka_url = "https://services3.arcgis.com/nIl76MjbPamkQiu8/arcgis/rest/services/confirmed_cases_dhaka_city/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&maxRecordCountFactor=4&orderByFields=cases%20DESC&outSR=102100&resultOffset=0&resultRecordCount=8000&cacheHint=true&quantizationParameters=%7B%22mode%22%3A%22view%22%2C%22originPosition%22%3A%22upperLeft%22%2C%22tolerance%22%3A1.0583354500043074%2C%22extent%22%3A%7B%22xmin%22%3A10035936.00083909%2C%22ymin%22%3A2713650.347400964%2C%22xmax%22%3A10156039.823972352%2C%22ymax%22%3A2755460.149106408%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D"

def scrape_dhaka_area():
    dhaka_response = requests.get(arcGis_dhaka_url)
    dhaka_json = json.loads(dhaka_response.text)
    dhaka_confirm_dict = OrderedDict()

    for attr in dhaka_json['features']:
        name = attr['attributes']['city']
        confirmed = attr['attributes']['cases']
        
        dhaka_confirm_dict[name] = confirmed

    dhaka_json_final_dict = []

    for a in dhaka_confirm_dict:
        area_data = {}
        
        area_data['name'] = a
        area_data['confirmed'] = dhaka_confirm_dict[a]
        area_data['bnName'] = en2bn_dhk_area.get(a.lower())
        
        dhaka_json_final_dict.append(area_data)

    return dhaka_json_final_dict
        
