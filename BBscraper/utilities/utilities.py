import datetime
import csv
import os
import glob
from PIL import Image
import requests
from BBscraper.workers_cleaners.product_class import FinalProduct
from .colors import colors

PATH = os.getcwd()
TODAY = datetime.datetime.today()

def date_string():
    year = str(TODAY.year)
    month = str(TODAY.month)
    day = str(TODAY.day)
    hour = str(TODAY.hour)
    minute = str(TODAY.minute)
    return f"{year}_{month}_{day}_{hour}_{minute}"

def cleaned_csv_path(manufacturer, subcategory):
    date = date_string()
    return PATH + f'\\BBscraper\\data_cleaned\\{manufacturer}_{subcategory}\\{manufacturer}_{subcategory}_cleaned_{date}.csv'

def raw_csv_path(manufacturer, subcategory):
    date = date_string()
    print('raw')
    return PATH + f'\\BBscraper\\data_raw\\{manufacturer}_{subcategory}\\{manufacturer}_{subcategory}_raw_{date}.csv'

def prescrape_csv_path(manufacturer, subcategory):
    date = date_string()
    return PATH + f'\\BBscraper\\data_prescrape\\{manufacturer}_{subcategory}\\{manufacturer}_{subcategory}_prescrape_{date}.csv'

def find_latest_raw(manufacturer, subcategory):
    folder = PATH + f'\\BBscraper\\data_raw\\{manufacturer}_{subcategory}\\*.csv'
    files = glob.glob(folder)
    latest = max(files, key=os.path.getctime)
    return latest

def find_latest_prescrape(manufacturer, subcategory, ext):
    folder = PATH + f'\\BBscraper\\data_prescrape\\{manufacturer}_{subcategory}\\*.{ext}'
    files = glob.glob(folder)
    if files:
        latest = max(files, key=os.path.getctime)
        print(latest)
        return latest
    else:
        return

def find_latest_clean(manufacturer, subcategory):
    folder = PATH + f'\\BBscraper\\data_cleaned\\{manufacturer}_{subcategory}\\*.csv'
    files = glob.glob(folder)
    latest = max(files, key=os.path.getctime)
    return latest

def create_final():
    date = date_string()
    return PATH + f'\\BBscraper\\data_final\\final_{date}.csv'

        
def aggregate():
    from settings import INSTALLED_APPS
    final = create_final()
    cleaned_files = []
    for app in INSTALLED_APPS:
        manufacturer = app.split('_')[0]
        subcategory = app.split('_')[1]
        cleaned = find_latest_clean(manufacturer, subcategory)
        cleaned_files.append(cleaned)
        print(cleaned)

    with open(final, 'w', newline='') as final:
        for clean in cleaned_files:
            with open(clean) as cleaned:
                reader = csv.reader(cleaned)
                for row in reader:
                    writer = csv.writer(final)
                    writer.writerow(row)


def finalize():
    date = date_string()
    path_in = PATH + '\\BBscraper\\data_final\\*.csv'
    final_path = PATH + f'\\downloaded_final_{date}.csv'
    final_error_log = PATH + f'\\downloaded_error_log_{date}.csv'
    image_out = f'D:\\BBdata\\product_images\\'
    files = glob.glob(path_in)
    latest = max(files, key=os.path.getctime)
    with open(latest) as readfile:
        reader = csv.reader(readfile)
        with open(final_path, 'w', newline='') as final, open(final_error_log, 'w', newline='') as error_log:
            for row in reader:
                name = row[0]
                manu = row[1]
                bbsku = row[-2].replace(' ', '').strip()
                image = row[5]
                characters = ['=','.','\\','/',':','?','&','#','%']
                image_name = image
                for ch in characters:
                    image_name = image_name.replace(ch,'')
                image_loc = image_out + image_name + '.jpg'
                if not os.path.isfile(image_loc):
                    try:
                        r = requests.get(image)
                        with open(image_loc, 'wb') as image_file:
                            image_file.write(r.content)
                    except:
                        error_row = [name, bbsku]
                        writer2 = csv.writer(error_log)
                        write.writerow(error_row)
                        continue
                row = [image_loc] + row
                writer = csv.writer(final)
                writer.writerow(row)

def get_color():
    image = "C:\\Users\\james\\Desktop\\test_images\\100155607_1.jpg"
    image2 = "C:\\Users\\james\\Desktop\\test_images\\07008.jpg"
    image3 = "C:\\Users\\james\\Desktop\\test_images\\O_27630_939.png"
    image4 = "C:\\Users\\james\\Desktop\\test_images\\DTN_M722_2x2_Tum_Msc.jpg"
    image5 = "C:\\Users\\james\\Desktop\\test_images\\DAL_G329_SapphireBlue_Swatch.jpg"
    im = Image.open(image5)
    width, height = im.size
    left = int(width/6)
    right = int(width - width/6)
    top = int(height/6)
    bottom = int(height - height/6)
    im_new = im.convert('RGBA')
    r_total = 0
    g_total = 0
    b_total = 0
    count = 0

    for x in range(left, right):
        for y in range(top, bottom):
            new_x = float(x)
            new_y = float(y)
            r, g, b, a = im_new.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    rgb = (int(round(r_total/count)), int(round(g_total/count)), int(round(b_total/count)))

    manhattan = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) 
    distances = {k: manhattan(v, rgb) for k, v in colors.items()}
    color = min(distances, key=distances.get)

    print(color)

    # new_im = im.crop((left,top,right,bottom))
    # new_path = "C:\\Users\\james\\Desktop\\test_images\\newimage.png"
    # new_im.save(new_path)
    # print(left,top, right, bottom)

               # product = FinalProduct(*row, final_image=image_loc, original_scraped=original_scraped, bbsku=bbsku)
                # writer = csv.DictWriter(final, fieldnames=vars(product).keys())
                # try:
                #     writer.writerow(vars(product))
                # except:
                #     print(product.name + ' could not be written')