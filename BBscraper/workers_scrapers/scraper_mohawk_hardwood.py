import requests
import json
import csv
from BBscraper.utilities import utilities
from BBscraper.lists import list_mohawk

builds = ["laminate","hardwood"]
species_list = [
    'Acacia',
    'Ebony',
    'Elm',
    'Hickory',
    'Maple',
    'Oak',
    'Walnut'
     ]

def run():
    headers = list_mohawk.ajax_headers
    file_name = utilities.raw_csv_path('mohawk', 'hardwood')
    url = list_mohawk.ajax_url
    with open(file_name, 'w', newline='') as writefile:
        for build in builds:
            for species in species_list:
                body = {"families":[build],"page":0,"pageSize":18,"facets":{"colors.species.name.keyword":[species]},"sorting":"relevance","query":"","useColorsIndex":'false'}
                if build == 'laminate':
                    species = None
                    body = {"families":["laminate","hardwood"],"page":0,"pageSize":18,"facets":{},"sorting":"relevance","query":"","useColorsIndex":'false'}
                body = json.dumps(body)
                response = requests.post(url, body, headers=headers)
                data = json.loads(response.text)
                styles = data['results']
                for style in styles:
                    collection = style['styleName']
                    technology = style['technology']
                    style_id = style['styleId']
                    style_number = style['styleNumber']
                    colors = style['colors']
                    for color in colors:
                        name = color['name']
                        color_url = str(color['url'])
                        color_code = color['colorNumber']
                        color_id = color['colorId']
                        image = color['swatchPathNoCrop']

                        wood = [build, collection, name, technology, style_id, style_number, species, color_url, image, color_code, color_id]
                        print(name)
                        wr = csv.writer(writefile)
                        wr.writerow(wood)
