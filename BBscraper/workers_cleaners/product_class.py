
import csv
import datetime

TODAY = datetime.datetime.today()

class Product():
    def __init__(self,
        name, 
        manufacturer_name,
        manufacturer_url,
        manufacturer_collection,
        manufacturer_color,
        image,
        build_label,
        thickness,
        material_label,
        manufacturer_sku=None,
        length=None,
        width=None,
        look_label=None,
        finish_label=None,
        lrv=None,
        cof=None,
        residential_warranty=None,
        commercial_warranty=None,
        walls=False,
        countertops=False,
        floors=False,
        cabinet_fronts=False,
        shower_floors=False,
        shower_walls=False,
        exterior=False,
        covered=False,
        pool_lining=False,
        notes=None,
        ):
        self.name = name
        self.manufacturer_name = manufacturer_name
        self.manufacturer_url = manufacturer_url
        self.manufacturer_color = manufacturer_color
        self.manufacturer_collection = manufacturer_collection
        self.image = image
        self.build_label = build_label
        self.thickness = thickness
        self.material_label = material_label
        self.manufacturer_sku = manufacturer_sku
        self.length = length
        self.width = width
        self.look_label = look_label
        self.finish_label = finish_label
        self.lrv = lrv
        self.cof = cof
        self.residential_warranty = residential_warranty
        self.commercial_warranty = commercial_warranty
        self.walls = walls
        self.countertops = countertops
        self.floors = floors
        self.cabinet_fronts = cabinet_fronts
        self.shower_floors = shower_floors
        self.shower_walls = shower_walls
        self.exterior = exterior
        self.covered = covered
        self.pool_lining = pool_lining
        self.date_scraped = str(TODAY.year) + '-' + str(TODAY.month) + '-' + str(TODAY.day) + '-' + str(TODAY.hour) + '-' + str(TODAY.minute)
        self.bb_sku = '%s %s %s %s %s %s %s' %(
                                            self.manufacturer_name,
                                            self.manufacturer_collection, 
                                            self.manufacturer_color, 
                                            self.build_label, 
                                            self.material_label, 
                                            self.width, 
                                            self.finish_label
                                            ) 
        self.notes = notes,

class FinalProduct(Product):
    def __init__(self, 
        name, 
        manufacturer_name, 
        manufacturer_url, 
        manufacturer_collection, 
        manufacturer_color, 
        image, 
        build_label, 
        thickness, 
        material_label, 
        manufacturer_sku = None, 
        length = None, 
        width = None, 
        look_label = None, 
        finish_label = None, 
        lrv = None, 
        cof = None, 
        residential_warranty = None, 
        commercial_warranty = None, 
        walls = False, 
        countertops = False, 
        floors = False, 
        cabinet_fronts = False, 
        shower_floors = False, 
        shower_walls = False, 
        exterior = False, 
        covered = False, 
        pool_lining = False, 
        notes = None, 
        final_image = None,
        original_scraped = None,
        bbsku = None,
        ):
        self.final_image = final_image
        self.original_scraped = original_scraped
        self.bbsku = bbsku
        return super().__init__(name, manufacturer_name, manufacturer_url, manufacturer_collection, manufacturer_color, image, build_label, thickness, material_label, manufacturer_sku, length, width, look_label, finish_label, lrv, cof, residential_warranty, commercial_warranty, walls, countertops, floors, cabinet_fronts, shower_floors, shower_walls, exterior, covered, pool_lining, notes)


