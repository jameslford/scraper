import csv
# import time
# import lxml
# import os
import json
import requests

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from bs4 import BeautifulSoup
from BBscraper.utilities import utilities
from BBscraper.lists import list_armstrong



def run():
    header = list_armstrong.headers
    file_name = utilities.raw_csv_path('armstrong', 'hardwood')
    with open(file_name, 'w', newline='') as writefile:
        for x in range(1,23):
            hardwood_ajax = 'https://www.armstrongflooring.com/residential/en-us/hardwood-flooring/_jcr_content.browseresults.json?pageSize=18&currPageIndex=' + str(x)
            response = requests.get(hardwood_ajax).text
            data = json.loads(response)
            items = data['items']
            for item in items:
                url = item['link']
                sku = item['sku']
                img = item['src']
                line_name = item['lineName']
                name = item['longName']
                attributes = item['attributeList']
                size = attributes[0]
                build = attributes[1]
                finish = attributes[2]
                edge = attributes[3]
                row = [line_name, name, sku, build, finish, edge, size, url, img]
                try:
                    print(row)
                    wr = csv.writer(writefile)
                    wr.writerow(row)
                except:
                    pass


#     urls = []
#     file_name = utilities.raw_csv_path('armstrong', 'hardwood')
#     main_url = 'https://www.armstrongflooring.com/residential/en-us/hardwood-flooring'
#     driver = webdriver.Chrome()
#     driver.get(main_url)
#     try:
#         load_more = driver.find_element_by_xpath("//button[contains(text(),'Load More')]")
#         if load_more.is_displayed():
#             load_more.click()
#             time.sleep(2)
#             run()
#         else:
#             time.sleep(2)
#             scrape_first()
#     except:
#         time.sleep(2)
#         scrape_first()


# def scrape_first():
#     soup_level1 = BeautifulSoup(driver.page_source,'lxml')
#     cards = soup_level1.find_all("div", {"class": "card card--item"})

#     for card in cards:
#         a_div = card.find('a')
#         details_div = card.find('div', {'class': 'card__details'})
#         details_list = details_div.find("ul")
#         residential_warranty = None
#         commercial_warranty = None
#         shade_variation = None

#         url = "https://www.armstrongflooring.com" + str(a_div.get('href'))
#         name = str(details_div.find('a').text.strip())
#         collection = str(details_div.find("span", {"class": "card__type"}).text.strip())

#         sku = str(card.find("span", {"class": "card__sku"}).text.strip())
#         swatch = str(card.find('img')['src'])

#         size = str(details_list.contents[1].contents[0])
#         construction = str(details_list.contents[2].contents[0])
#         gloss = str(details_list.contents[3].contents[0])
#         edges = str(details_list.contents[4].contents[0])

#         item_list = [url, name, collection, sku, swatch, size, construction, gloss, edges]

#         with open(FILE, 'a+', newline='') as writefile:
#             try:
#                 wr = csv.writer(writefile)
#                 wr.writerow(item_list)
#             except:
#                 pass
