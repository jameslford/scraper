import requests
import json
import csv
from BBscraper.utilities import utilities
from BBscraper.lists import list_mohawk

builds = ["Frieze (Twist)", "Loop", "Pattern", "Texture"]

def run():
    headers = list_mohawk.ajax_headers
    file_name = utilities.raw_csv_path('mohawk', 'carpet')
    url = list_mohawk.ajax_url
    with open(file_name, 'w', newline='') as writefile:
        for build in builds:
            body = {"families":["carpet"],"page":0,"pageSize":18,"facets":{"specifications.Style.keyword":[build]},"sorting":"relevance","query":"","useColorsIndex":'false'}
            body = json.dumps(body)
            response = requests.post(url, body, headers=headers)
            data = json.loads(response.text)
            styles = data['results']
            for style in styles:
                style_name = style['styleName']
                material = style['technology']
                colors = style['colors']
                for color in colors:
                    color_url = str(color['url'])
                    image = color['swatchPathNoCrop']
                    color_id = color['colorId']
                    color_name = color['name']
                    color_code = color['colorNumber']

                    carpet = [build, style_name, material, color_url, image, color_name, color_code, color_id]

                    # print(carpet)
                    wr = csv.writer(writefile)
                    wr.writerow(carpet)

 