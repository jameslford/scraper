import csv
import time
import os
import re
import html5lib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from BBscraper.utilities import utilities


driver = webdriver.Chrome()

def run():
    products = []
    file_name = utilities.prescrape_csv_path('formica', 'laminate')
    keys = range(1,5)
    for key in keys:
        main_url = 'http://www.formica.com/en/us/products/formica-laminate?page='+ str(key) + '#swatchesTab'
        driver.get(main_url)
        if key == 1:
            try:
                wait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME ,"acsDeclineButton")))
                button = driver.find_element_by_class_name("acsDeclineButton")
                button.click()
                time.sleep(2)
                scrape_first(file_name)
            except TimeoutException:
                scrape_first(file_name)
        else:
            scrape_first(file_name)


def scrape_first(file_name):
    soup1 = BeautifulSoup(driver.page_source,'html5lib')
    swatch_collection = soup1.find("ul", {"class": "swatch-collection"})
    with open(file_name, 'a+', newline='') as writefile:
        for card in swatch_collection.find_all('li'):
            a_tag = card.find('a')
            if a_tag:
                url = a_tag.get('href')
                wr = csv.writer(writefile)
                wr.writerow([url])
                print(url)
            else:
                pass