import requests
import json
import csv
from BBscraper.utilities import utilities

builds = ["Frieze (Twist)", "Loop", "Pattern", "Texture"]

def run():
    file_name = utilities.raw_csv_path('mohawk', 'carpet')
    with open(file_name, 'w', newline='') as writefile:
        for build in builds:
            headers = {
                'Host': 'www.mohawkflooring.com',
                'Connection': 'keep-alive',
                'Content-Length': '153',
                'Origin': 'https://www.mohawkflooring.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': 'application/json, text/plain, */*',
                'Request-Id':' |jtQgW.JcHHk',
                'Request-Context': 'appId=cid-v1:4bd04b6a-18c8-4b54-a73f-69caadc9495d',
                'Referer': 'https://www.mohawkflooring.com/carpet/search?page=1&specifications.Style.keyword=' + build,
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cookie': 'ASP.NET_SessionId=flouq2e2ntifrfwgaolav23z; SC_ANALYTICS_GLOBAL_COOKIE=3653867d0b6d4ca39d8cbd6bbda6eaef|False; ai_user=Ty7h2|2018-09-13T20:42:28.847Z; ffvisitorids={"mohawk_flooring":"f4540fd6c1804c8ab0ed0becd58bc9be"}; _hjIncludedInSample=1; _ga=GA1.2.541790398.1536871350; _gid=GA1.2.1955447638.1536871350; __distillery=7fb6149_b5546593-57bd-415c-928f-09c0f9d6177f-2b4ee6130-ca7e159a345e-c649; ai_session=d0/7Z|1536892166794|1536896772368.9'
            }
            body = {"families":["carpet"],"page":0,"pageSize":18,"facets":{"specifications.Style.keyword":[build]},"sorting":"relevance","query":"","useColorsIndex":False}

            url = 'https://www.mohawkflooring.com/api/products/styles'

            response = requests.post(url, body, headers=headers).json()
            data = json.loads(response)
            styles = data['results']
            for style in styles:
                style_name = style['styleName']
                material = style['technology']
                colors = style['colors']
                for color in colors:
                    url = str(color['url'])
                    image = color['swatchPathNoCrop']
                    color_id = color['colorId']
                    color_name = color['name']
                    color_code = color['colorNumber']

                    carpet = [build, style, material, url, image, color_name, color_code, color_id]

                    wr = csv.writer(writefile)
                    wr.writerow(carpet)
                 








