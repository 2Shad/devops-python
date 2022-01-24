i = 375  # int
f = 3.75  # float
c = 2 + 3j  # complex

print((c, type(c)))


### Numeric

add = 3 + 5
subtract = 3 - 5
multiply = 3 * 5
divide = 3 / 5
power = 3 ** 5
modulo = 3 % 5

print(13 % 3)  # 4 * 3 = 12, 13 - 12 = 1
print(12 % 3)  # if divisible then modulo is 0

print(13 // 3, 14 % 3) 
print(13 / 3)

third = 1 / 3
print(third)
print(third * 3)


### Strings!

# single = 'String in single quotes'
# single = "String in single quotes"

# failure = 'This is David's string'

# single_in_double = "This is David's string"
# double_in_single = 'This is a "string"'
# both = 'This is David\'s "string"'


### Indexing and slicing

# hi = 'Hello World!'
# print(hi[0])  # Python starts counting at zero!
# print(hi[6])
# print(hi[-1])
# print(hi[0:6])  # From 0 to 6 (non inclusive ending)

# print(len(hi))

# # print 'lo Wo'
# print(hi[3:8])


### Methods

white_space = "     lots of white space     "
print(len(white_space))
print(white_space.strip())
print(white_space.lstrip())
print(white_space.rstrip())
print(white_space.upper())
print(white_space.lower())
print(white_space.strip().capitalize())
print(white_space.count(" "))
print(white_space.strip().count(" "))
print(white_space.replace('o', 'ooo').replace('i', 'ooo'))

print(white_space) # Original string is unchanged

# F-strings (formatted strings)

pi = 3.14159265359
print(pi)
print(f'Pi to 3dp: {pi:.3f}')
print(f'Pi to 5dp: {pi:.5f}')
print(f'Pi to 0dp: {pi:.0f}')

score = 16
max_score = 26
print(f'You scored {score / max_score:.0%}')


### Boolean

t = True
f = False

print(t, type(t))

print(3 + 2 == 5)
print(12 % 3 == 0)
print(3 != 5)
print(1 < 100)
print(100 < 1)
print(5 <= 5)

age = 19
drink = 'alcohol'

print (age > 18 and drink == 'alcohol')
print (age > 18 or drink == 'alcohol')

hii = 'helloworld'
print(hii.isalpha())
print(hii.islower())
print(hii.isupper())
print(hii.endswith('d'))
print(hii.startswith('h'))


### Bool

print(bool(1))
print(bool(0))


### None

n = None
print(n, type(n))

print(n == None)

print(type(15) is int)