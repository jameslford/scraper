import csv
import importlib
from ..utilities import utilities



def clean(manufacturer, subcategory):
    raw = utilities.find_latest_raw(manufacturer, subcategory)
    cleaned = utilities.cleaned_csv_path(manufacturer, subcategory)
    mod = f'.cleaner_{manufacturer}_{subcategory}'
    prog = importlib.import_module(mod, package='BBscraper.workers_cleaners')
    with open(raw) as readfile:
        reader = csv.reader(readfile)
        with open(cleaned, 'w', newline='') as cleaned:
            for row in reader:
                prog.run(row)
                product = prog.run(row)
                writer = csv.DictWriter(cleaned, fieldnames=vars(product).keys())
                try:
                    writer.writerow(vars(product))
                except:
                    print(product.name + ' could not be written')