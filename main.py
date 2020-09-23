import os
import csv
import sys
import argparse
import settings
from BBscraper.workers_cleaners import clean
from BBscraper.workers_scrapers import scrape
from BBscraper.workers_prescrapers import prescrape
from BBscraper.utilities import utilities


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', nargs='*') 
    parsed = parser.parse_args()
    arg_list = parsed.command
    function = arg_list[0]
    if function == 'agg':
        utilities.aggregate()
    elif function == 'run_all_programs':
        pass
    elif function == 'finalize':
        utilities.finalize()
    elif function == 'get_color':
        utilities.get_color()
    elif len(arg_list) < 3:
        print('Need Manufacturer and Subcategory for this command')
    else:
        manufacturer = arg_list[1]
        subcategory = arg_list[2]
        app = f'{manufacturer}_{subcategory}'
        if app not in settings.INSTALLED_APPS:
            print('Manufacturer and Subcategory not installed')
        else:
            if function == 'scrape':
                scrape.scrape(manufacturer, subcategory)
            elif function == 'clean':
                clean.clean(manufacturer, subcategory)
            elif function == 'prescrape':
                print('hello')
                prescrape.prescrape(manufacturer, subcategory)

if __name__ == '__main__':
    main()


    

