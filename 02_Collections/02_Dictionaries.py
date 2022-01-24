### Dictionaries

## Key-Value Pairs

my_dict = {'key': 'value'}

table = {
    'name': 'The Table',
    'colour': 'light brown',
    'height': 120,
    'length': 200,
    'width': 150
}

print(table)
print(table['colour']) # DICTIONARY NAME [ KEY ]

table['height'] = 125
table['price'] = 99.99
print(table)

table.update({'price': 199.99, 'width': 180})

print(table.get('price'))
print(table['price'])


chairs = {
    'Chair A': {
        'name': 'chair A',
        'colour': 'white',
        'size': 'Adult'
    },
    'Chair B': {
        'name': 'chair B',
        'colour': 'red',
        'size': 'Child'
    }
}

print(chairs.get('Chair A').get('colour'))

print(table)
print(table.keys())
print(table.values())
print(table.items())