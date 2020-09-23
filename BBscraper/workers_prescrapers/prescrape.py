import importlib


def prescrape(manufacturer, subcategory):
    mod = f'.prescraper_{manufacturer}_{subcategory}'
    print(mod)
    prog = importlib.import_module(mod, package='BBscraper.workers_prescrapers')
    prog.run()
