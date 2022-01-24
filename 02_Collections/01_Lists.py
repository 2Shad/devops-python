### Lists

shopping_list = ['eggs', 'bread', 'bananas', 'tea']
print(shopping_list, type(shopping_list))

print(len(shopping_list))

print(shopping_list[0])
print(shopping_list[-1])

shopping_list[2] = 'milk'
print(shopping_list)

shopping_list.append('biscuits')
print(shopping_list)

shopping_list.append('bread')
shopping_list.append('bread')
print(shopping_list)
shopping_list.remove('bread')
print(shopping_list)

print(shopping_list.pop(2))
print(shopping_list)


mixed = [1, 2, 'three', True, None, ['another', 'list'], 6, 7, 8]
print(mixed)

mixed[1] = 2.0
print(mixed)

## LIST ARE MUTABLE

print(mixed[2:4])
print(mixed[2:])
print(mixed[:4])
print(mixed[2:7:2])
print(mixed[7:2:-1])
print(mixed[::3])

print(mixed[5][1])
print(mixed[5][1][2])


sublist = mixed[5]
print(sublist)
mixed[5] = ['a', 'b']
print(sublist)


### Tuples

colours = ('red', 'blue', 'green')
print(colours, type(colours))

print(colours[0])

## Tuples  are IMMUTABLE

print(colours.count('red'))
print(colours.index('green'))


list_in_tuple = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(len(list_in_tuple))

list_in_tuple[0][-1] = 'SUCCESS'
print(list_in_tuple)