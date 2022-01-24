### For Loops

l = ['a', 'b', 'c']

for index, letter in enumerate(l):
    print(f'{letter} is in position {index}')

for letter in l:
    if letter == 'b':
        print(letter.upper())
    else:
        print(letter)

for i in range(1, 11):
    for letter in l:
        print(i, letter)

me = {'name': 'David', 'age': 375, 'job': 'trainer'}

for key, value in me.items():
    print(f'My {key} is {value}')

for char in 'Hello World!':
    print(char)

