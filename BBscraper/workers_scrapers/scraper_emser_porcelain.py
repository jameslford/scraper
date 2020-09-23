import csv
import time
import os
import html5lib
import requests

from selenium import webdriver
from bs4 import BeautifulSoup
from BBscraper.lists import list_emser
from BBscraper.utilities import utilities



def run():
    urls = []
    main_url = 'https://www.emser.com/collections/porcelain?page=1'
    main_page = requests.get(main_url)
    file_name = utilities.raw_csv_path('emser', 'porcelain')
    soup_level1 = BeautifulSoup(main_page.text, 'html5lib')

    list1 = soup_level1.find_all('div', {'class': 'four columns alpha thumbnail even'})
    list2 = soup_level1.find_all('div', {'class': 'four columns alpha thumbnail odd'})
    list3 = soup_level1.find_all('div', {'class': 'four columns thumbnail odd'})
    list4 = soup_level1.find_all('div', {'class': 'four columns thumbnail even'})
    list5 = soup_level1.find_all('div', {'class': 'four columns omega thumbnail even'})
    list6 = soup_level1.find_all('div', {'class': 'four columns omega thumbnail odd'})

    full_list = list1 + list2 + list3 + list4 + list5 + list6

    for item in full_list:
        href  = item.find('a')['href']
        collection = item.find('span', {'class': 'title'}).text
        full_url = 'https://www.emser.com' + href
        urls.append([full_url, collection])

    driver = webdriver.Chrome()
    with open(file_name, 'w', newline='') as writefile:
        for url in urls:
            time.sleep(1)
            driver.get(url[0])
            soup_level2 = BeautifulSoup(driver.page_source, 'html5lib')
            tabs = soup_level2.find('div', {'id': 'tabs'})
            size_tab = tabs.find('div', {'id': 'tabs-4'})
            sizes = [size.text.strip() for size in size_tab.find_all('p')]
        
            app_list = list_emser.app_list

            aList = []
            for app in app_list:
                answer =  soup_level2.find('td', string=app)
                if answer:
                    siblings = answer.find_next_siblings('td')
                    response = []
                    for sib in siblings:
                        if sib:
                            sib = sib.text.strip()
                            sib = sib.replace('\\u2265','')
                            sib = sib.replace('\\u2264','')
                            response.append(sib.strip())
                    response = [app] + response
                    aList.append(response)
                else:
                    response = [app, 'none']
                    aList.append(response)

            selections_div = soup_level2.find('select', {'class':'multi_select'})
            selections = selections_div.find_all('option')
            variants = []
            for selection in selections:
                variant = selection['value']
                sku = selection['data-sku']
                content = selection.text.strip()
                variant_list = [variant, sku, content]
                variants.append(variant_list)
            for v in variants:
                new_url = url[0].rsplit('?', 1)[0] + '?variant=' + v[0]
                driver.get(new_url)
                soup_level3 = BeautifulSoup(driver.page_source, 'html5lib')
                image_slides = soup_level3.find('ul', {'class': 'slides'})
                image_li = image_slides.find('li', {'class': 'flex-active-slide'})
                image = image_li.find('img')['src']
                contents = v[2]
                sku = v[1]
                collection = url[1].strip()


                item_list = [collection, sku, 'Porcelain', contents, image, new_url, sizes, aList]
                try:
                    wr = csv.writer(writefile)
                    wr.writerow(item_list)
                except: 
                    pass
