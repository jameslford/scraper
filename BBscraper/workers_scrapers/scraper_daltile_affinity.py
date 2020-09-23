import csv
import os
import html5lib
import requests

from bs4 import BeautifulSoup
from BBscraper.utilities import utilities
from BBscraper.lists import list_daltile


def run():
    main_url = 'https://www.daltile.com/products/tile/affinity'
    root_url = 'https://www.daltile.com'
    main_page = requests.get(main_url)
    raw = utilities.raw_csv_path('daltile', 'affinity')
    mosaics = []
    others = []
    soup_level1 = BeautifulSoup(main_page.text, 'html5lib')
    pictures = soup_level1.find_all('div', {'class': 'section__item gridItem'})
    for pic in pictures:
        href = pic.find('a')['href']
        link = root_url + href
        image = pic.find('img')['data-src']
        name = pic.find('div', {'class': 'section__item--heading'}).text.strip()
        sub_heading = pic.find('div', {'class': 'section__item--subheading'}).text.strip()
        build = None
        pic_list = [name, sub_heading, link, image, build]
        if sub_heading == 'Mosaic':
            mosaics.append(pic_list)
        else:
            others.append(pic_list)


    with open(raw, 'w', newline='') as writefile:
        for size in list_daltile.affinity:
            manu_color = size[0]
            color = size[1]
            finish = size[2]
            material = size[3]
            nom_size = size[4]
            pre_thick = size[7].split('/')
            tnum = int(pre_thick[0])
            tden = int(pre_thick[1])
            thickness = tnum/tden
            width = nom_size.split('x')[0]
            length = nom_size.split('x')[1]
            call_color = color + ' ' + manu_color
            build = 'Tile'
            pool = False
            shower_floor = False
            floors = True
            counter_tops = True
            cof = .42
            add_details = []
            if nom_size == '2x2':
                build = 'Mosaic'
                pool = True
                shower_floor = True
                for mos in mosaics:
                    if mos[0] == call_color:
                        add_details = mos
            else:
                for pic in others:
                    if pic[0] == call_color:
                        add_details = pic
            if nom_size == '10x14':
                floors = False
                counter_tops = False
                cof = ''
            manufacturer_url = add_details[2]
            image = add_details[3]
            name = "%s %s %s %s" %(call_color, finish, material, nom_size)
            item_list = [
                name,
                'Daltile',
                manufacturer_url,
                call_color,
                'Affinity',
                image,
                build,
                thickness,
                material,
                finish,
                width,
                length,
                floors,
                counter_tops,
                shower_floor,
                pool,
                True,
                True,
                cof
            ]
            try:
                wr = csv.writer(writefile)
                wr.writerow(item_list)
            except:
                pass
