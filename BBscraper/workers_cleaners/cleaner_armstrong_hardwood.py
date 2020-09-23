from .product_class import Product

def run(row):
    collection = row[0]
    name = row[1]
    sku = row[2]
    build = row[3]
    gloss = row[4]
    edge = row[5]
    size = row[6]
    manu_url = row[7]
    image_url = row[8]
    species = name.split(' ')[0]
    color = name.split('-')[-1].strip()
    if species == 'Red':
        species = 'Oak'
    if species == 'White':
        species = 'Oak'
    if species == 'Yellow':
        species = 'Birch'
    if species == 'Northern':
        species = 'Oak'
    sizes = size.split('x')
    cleaned_sizes = []
    for unit in sizes:
        for ch in ['in.', 'Wide', 'Varying Lengths', 'Long', 'Thick', ':']:
            unit = unit.replace(ch, '')
        cleaned_sizes.append(unit.strip())
    width = cleaned_sizes[0]
    length = cleaned_sizes[1]
    thickness = cleaned_sizes[2]
    split = thickness.split('/')
    num = int(split[0])
    den = int(split[1])
    thickness = num/den
    widths = width.split(',')
    for w in widths:
        new_line = [name, w, collection, thickness, sku, length, gloss, build, edge, image_url, manu_url, species]
        w = w.strip()
        seps = w.split(' ')
        if len(seps) > 1:
            sep1 = int(seps[0])
            fracs = seps[1].split('/')
            num = int(fracs[0])
            den = int(fracs[1])
            dec = sep1 + num/den
            new_width = str(dec)
        else:
            new_width = str(seps[0])

        return Product(
            name=name,
            manufacturer_name='Armstrong',
            manufacturer_url=manu_url,
            manufacturer_collection=collection,
            manufacturer_color=color,
            image=image_url,
            build_label=build,
            thickness=thickness,
            material_label=species,
            manufacturer_sku=sku,
            length=length,
            width=new_width,
            look_label='Wood',
            finish_label=gloss,
            floors = True
        )




          



