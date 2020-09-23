from .product_class import Product


def run(row):
    name = row[0]
    manufacturer = row[1]
    manufacturer_url = row[2]
    color = row[3]
    collection = row[4]
    image = row[5]
    build = row[6]
    thickness = row[7]
    material = row[8]
    finish = row[9]
    width = row[10]
    length = row[11]
    floors = row[12]
    counter_tops = row[13]
    shower_floors = row[14]
    pool = row[15]
    walls = row[16]
    shower_walls = row[17]
    cof = row[18]

    return Product(
        name=name,
        manufacturer_name=manufacturer,
        manufacturer_url=manufacturer_url,
        manufacturer_collection=collection,
        manufacturer_color=color,
        image=image,
        build_label=build,
        thickness=thickness,
        material_label=material,
        length=length,
        width=width,
        finish_label=finish,
        floors=floors,
        countertops=counter_tops,
        shower_floors=shower_floors,
        pool_lining=pool,
        walls=walls,
        shower_walls=shower_walls,
        cof=cof
    )