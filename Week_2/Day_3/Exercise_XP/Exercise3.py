
brand={
    'name': 'Zara',
    'creation_date': 1975, 
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes':['men',
                       'women',
                       'children',
                       'home'],
    'international_competitors':['Gap',
                                  'H&M' ,
                                  'Benetton',
                                  ],
    'number_stores': 7000 ,
    'major_color': 
        {'France': 'blue', 
        'Spain': 'red', 
        'US': 'pink' 'green'
        }
}
brand['number_stores']=2
print(brand)
print("Zara's clients are cool lil Nig**s")
brand['country_creation']='Spain'
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
brand['creation_date']=''
print(brand['international_competitors'][-1])
print(brand['major_color']['US'].split(" "))
print(len(brand))
print(brand.keys())
more_on_zara={
    'creation_date':1975,
    'number_stores':10000
}

final_dict=brand | more_on_zara
print(final_dict)
print(final_dict['number_stores'])