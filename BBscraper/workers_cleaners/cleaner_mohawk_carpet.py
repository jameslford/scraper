from .product_class import Product

def run(row):
    image = row[4]
    collection = row[1]
    color = row[5]
    build = row[0]
    material = row[2]
    url = 'https://www.mohawkflooring.com' + row[3]
    name = row[1] + ' ' + row[5]
    return Product(
        name=name,
        manufacturer_name='Mohawk',
        manufacturer_url=url,
        manufacturer_collection=collection,
        manufacturer_color=color,
        image=image,
        build_label=build,
        thickness=None,
        material_label=material,
        floors=True
    )
