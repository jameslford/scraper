
from .product_class import Product



def get_arguments(horizontal, vertical, thickness, *notes):
    return {
        'horizontal': horizontal,
        'vertical': vertical,
        'thickness': thickness,
        'notes': list(notes)
    }

post_forming = 'Post-forming'
fire_rated = 'Fire Rated'


grades = {
    'Grade 10': get_arguments(True, True, .044),
    'Grade 12': get_arguments(True, True, .035, post_forming),
    'Grade 20': get_arguments(False, True, .027, post_forming),
    'Grade 32': get_arguments(False, True, .029, fire_rated),
    'Grade 50': get_arguments(True, True, .045, fire_rated),
    'Grade V4': get_arguments(False, True, .027),
    'Grade V5': get_arguments(True, True, .35)
    }


def run(row):
    name = row[0]
    sku = row[1]
    grade = row[2]
    size = row[3]
    finish = row[4]
    image = row[5]
    url = row[6]
    grade_info = grades.get(grade)
    thickness = grade_info.get(grade)
    counter_tops = grade_info.get(grade)
    notes = grade_info.get(grade)
    splits = size.split('x')
    landw = []
    for split in splits:
        if "''" in split:
            split.replace("''", '')
            fandi = split.split("'")
            landw.append(int(fandi[0])*12 + int(fandi[1]))
        else:
            feet = split.replace("'", '').strip()
            landw.append(int(feet)*12)
    width = landw[0]
    length = landw[1]
    name = f'{name} {grade} {width}x{length}'
    return Product(
        name=name,
        manufacturer_name='Formica',
        manufacturer_url=url,
        manufacturer_collection=grade,
        manufacturer_color=name,
        image=image,
        build_label='Cabinet Laminate',
        thickness=grade_info['thickness'],
        material_label='Laminate',
        manufacturer_sku=sku,
        length=length,
        width=width,
        finish_label=finish,
        countertops=counter_tops,
        cabinet_fronts=True,
        walls=True,
        notes=notes
    )

