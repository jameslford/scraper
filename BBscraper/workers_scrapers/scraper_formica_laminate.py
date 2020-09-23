import csv
import time
import os
import re
import lxml
import requests

from bs4 import BeautifulSoup
from BBscraper.utilities import utilities



def run():
    urls = []
    read_file = utilities.find_latest_prescrape('formica', 'laminate')
    write_file = utilities.raw_csv_path('formica', 'laminate')
    with open(read_file) as readfile:
        reader = csv.reader(readfile)
        for row in reader:
            urls.append(row)
    with open(write_file, 'w', newline='') as writefile:
        for url in urls:
            url = url[0]
            variations = second_getinfo(url)
            for variation in variations:
                wr = csv.writer(writefile)
                wr.writerow(variation)


def second_getinfo(url):
    main_page = requests.get(url).text
    soup2 = BeautifulSoup(main_page, 'lxml')
    image_wrapper = soup2.find("div", {"class": "image-wrapper"})
    product_details = soup2.find("div", {"class": "product-details"})
    options_div = soup2.find('div', {'id':'phmain_0_phcontent_0_phproductdetails_0_pnlStandardGradeDropDown'})
    drop_down = soup2.find_all('div', class_='drop-down-content')[0]
    if product_details and image_wrapper and options_div and drop_down:
        code =strip_code(product_details.find("span", {"class": "decor-code"}).text)
        color = str(product_details.find("h1").text).strip()
        img = image_wrapper.find("img")["src"]
        options = options_div.find_all('option')
        divs = drop_down.find_all('div')
        tables = drop_down.find_all('table')
        page1 = []
        page2 = []
        if options:
            grade1 = options[0].text.strip()
            page1 = strip_rows(divs[0], grade1, code, color, img, url)
        else:
            return []
        if len(options) > 1:
            grade2 = options[1].text.strip()
            page2 = strip_rows(divs[1], grade2, code, color, img, url)
        return page1 + page2
    else:
        return []

    
def strip_code(code):
    new = code.replace('\\n', '')
    new2 = new.replace('\\t','')
    return new2.strip()


def strip_rows(div, grade, code, color, img, url):
    variations = []
    rows = div.find_all('tr')
    for row in rows:
        size = row.find('th').text.strip()
        finishes = row.find('td').text.strip()
        finish_list = finishes.split('  ')
        for finish in finish_list:
            finish1 = strip_code(finish)
            if finish1:
                append = [color, code, grade, size, finish1, img, url]
                variations.append(append)
    return (variations)

