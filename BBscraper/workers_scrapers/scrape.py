import importlib
from BBscraper.utilities import utilities


def scrape(manufacturer, subcategory):
    # prescrape = utilities.find_latest_prescrape(manufacturer, subcategory)
    mod = f'.scraper_{manufacturer}_{subcategory}'
    prog = importlib.import_module(mod, package='BBscraper.workers_scrapers')
    prog.run()
