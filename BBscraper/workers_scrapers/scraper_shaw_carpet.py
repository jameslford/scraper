import csv
import os
import html5lib
import lxml
import requests

from bs4 import BeautifulSoup
from BBscraper.utilities import utilities
from BBscraper.lists import list_daltile

def run():
    print('scraper not built yet')
    # for key in range(2,3): # 32
    #     main_url = 'https://shawfloors.com/flooring/carpet/' +str(key)
    #     print(main_url)
    #     main_page = requests.get(main_url)
    #     soup = BeautifulSoup(main_page.text, 'html5lib')
    #     spans = soup.find_all('span', class_='stand-out')
    #     for span in spans:
    #         print(span.content)
        # swatches = soup.find_all('div', class_='swatch')
        # for swatch in swatches:
        #     name = swatch.find('h2').contents
        #     print(swatch.contents)