from BBscraper.workers_cleaners.product_class import Product

def run(row):
    _collection = row[0].split(' ')
    collection = []
    for c in _collection:
        c = ''.join(e for e in c if e.isalnum())
        collection.append(c)
    collection = ' '.join(collection)
    sku = row[1]
    material = row[2]
    variant_content = row[3]
    image = 'https:' + row[4]
    url = row[5]
    strip_list = ['[', ']', '\\', 'xa0x', 'xa0', "'\\'"]
    collection_sizes = [item.strip() for item in row[6].split("', '") if item]
    for strip in strip_list:
        collection_sizes = [item.replace(strip, '') for item in collection_sizes]
        collection_sizes = [item.strip(strip) for item in collection_sizes if item]
    collection_sizes = [item for item in collection_sizes if item]
    info_list = [item.strip() for item in row[7].split('], [')]
    info_list[0] = info_list[0].strip('[[')
    info_list[-1] = info_list[-1].strip(']]')
    info_dict = {}
    for info in info_list:
        sub_list = info.split(', ')
        key = sub_list[0].strip('"')
        key = key.strip("'")
        values = [item.strip("'") for item in sub_list[1:] if item]
        values = [val.replace('\\xa0', '') for val in values if val]
        if not values:
            values = [None]
        info_dict[key] = values
    variant_content = [item for item in variant_content.split(' ') if item]
    variant_content = [item.split('x ') for item in variant_content if item]
    content = []
    for item in variant_content:
        for i in item:
            content.append(i)
    content = [item.strip() for item in content if item != '/']
    content = [item.strip('"') for item in content if item != 'X']
    content = [item.strip("''") for item in content if item != 'x']
    content = [item.replace('"', '!') for item in content if item]
    content = [item.replace('”x', '!') for item in content if item]
    content = [item.replace('”', '!') for item in content if item]
    content = [item.split('!') for item in content if item]
    variant_content = []
    for item in content:
        for i in item:
            if i:
                variant_content.append(i.strip())
    variant_content = [item.strip('x') for item in variant_content]
    indexes = []
    size = []
    for item in variant_content:
        if item.isnumeric():
            index = variant_content.index(item)
            indexes.append(index)
            size.append(int(item))
    manu_color = ' '.join(variant_content[:indexes[0]])
    other = variant_content[indexes[-1] + 1:]
    standard_color = other[-1]
    other = other[:-1]
    other = [item for item in other if item.isalpha()]
    other = ' '.join(item for item in other if item)

    size_keys = [item.split('x') for item in info_dict.pop('Nominal Size (in.)')]
    thickness_keys =  [item for item in info_dict.pop('Thickness (in.)*')]
    finish_keys = [item for item in info_dict.pop('Finish')]
    edge_keys = [item for item in info_dict.pop('Edge Detail')]
    grout_keys = [item for item in info_dict.pop('Grout Joint Width (in.)')]

    keys_list = []
    qcount = 0
    for hsize in size_keys:
        tk = thickness_keys[qcount]
        fk = finish_keys[qcount]
        ek = edge_keys[qcount]
        gk = grout_keys[qcount]
        key_list = [
            hsize,
            tk,
            fk,
            ek,
            gk,
            qcount
        ]
        qcount += 1
        keys_list.append(key_list)

    for keys in keys_list:
        nsize = keys[0]
        nsize = [item.replace(' ','') for item in nsize]
        nsize = [int(item) for item in nsize]
        keys[0] = nsize

    finish = None
    thickness = None
    grout_width = None
    edge_detail = None
    hit = False

    for key in keys_list:
        if key[0] == size:
            if other == key[2]:
                hit = True
                thickness = key[1]
                finish = key[2]
                edge_detail = key[3]
                grout_width = key[4]
                keys_list.remove(key)

    if hit == False:
        for key in keys_list:
            if key[0] == size:
                thickness = key[1]
                finish = key[2]
                edge_detail = key[3]
                grout_width = key[4]
            
    if not other or other == finish:
        other = 'Tile'
    
    default_thickness = thickness_keys[0]
    
    if not thickness:
        thickness = default_thickness

    width = size[0]
    length = size[1]

    th_num = thickness.split('/')[0]
    th_den = thickness.split('/')[1]
    thickness = int(th_num)/int(th_den)
    shade_variation = info_dict.pop('Shade Variation', None)
    cof = info_dict.pop('DCOF AcuTest WET', None)

    new_dict = {}
    for app, value in info_dict.items():
        value = ''.join(value)
        value = value.split('\\n')
        new_dict[app] = value

    final_dict = {}
    for key, value1 in new_dict.items():
        if len(value1) > 1:
            for val in value1:
                val = val.split(':')
                if len(val) > 1:
                    if finish == val[0]:
                        if val[1] == 'Yes':
                            final_dict[key] = True
                        else:
                            final_dict[key] = False
                    else:
                        final_dict[key] = 'no match'
                else:
                    final_dict[key] = 'no semi'
        else:
            if value1[0] == 'Yes':
                final_dict[key] = True
            else:
                final_dict[key] = False
    floor = False
    walls = False
    counter_tops = False
    exterior = False
    covered = False
    shower_walls = False
    shower_floors = False
    pool_lining = False


    if final_dict['COMMERCIAL FLOOR'] == True:
        floor = True
    if final_dict['COMMERCIAL FLOOR*'] == True:
        floor = True
    if final_dict['RESIDENTIAL FLOOR'] == True:
        floor = True
    if final_dict['INSIDE POOL'] == True:
        pool_lining = True
    if final_dict['KITCHEN COUNTER'] == True:
        counter_tops = True
    if final_dict['RESIDENTIAL AND COMMERCIAL WALL'] == True:
        walls = True
    if final_dict['SHOWER FLOOR'] == True:
        shower_floors = True
    if final_dict['SHOWER WALL'] == True:
        shower_walls = True
    if final_dict['UNCOVERED EXTERIOR WALL FREEZING CLIMATES'] == True:
        exterior = True
    if final_dict['UNCOVERED EXTERIOR FLOOR NON-FREEZING CLIMATES'] == True:
        exterior = True
    if final_dict['COVERED EXTERIOR WALL FREEZING CLIMATES'] == True:
        covered = True
    if final_dict['COVERED EXTERIOR WALL NON-FREEZING CLIMATES'] == True:
        covered = True

    size = str(width) + 'x' + str(length)

    name_label = finish
    if not name_label:
        name_label = other

    mc_split = manu_color.split(' ')
    if len(mc_split) >1:
        if mc_split[0].upper() == collection:
            manu_color = ' '.join(mc_split[1:])
        if mc_split[-1] == finish:
            manu_color = ' '.join(mc_split[:-1])
    
    notes = [['Shade Variation', shade_variation], ['Edge Detail', edge_detail], ['Grout Width', grout_width]]

    name = f"{collection} {manu_color} {name_label} {size}"
    
    return Product(
        name=name,
        manufacturer_name='Emser',
        manufacturer_url=url,
        manufacturer_collection=collection,
        manufacturer_color=manu_color,
        image=image,
        build_label=other,
        thickness=thickness,
        material_label='Porcelain',
        manufacturer_sku=sku,
        length=length,
        width=width,
        cof=cof,
        residential_warranty='1 Year',
        commercial_warranty='1 Year',
        walls=walls,
        countertops=counter_tops,
        floors=floor,
        shower_floors=shower_floors,
        shower_walls=shower_walls,
        exterior=exterior,
        covered=covered,
        pool_lining=pool_lining,
        notes=notes
    )
