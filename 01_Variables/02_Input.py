# name = input('What is your name?\n')

# print('Hello, ' + name)

# Ask 3 questions
# Use the stored variables somehow, and print out a response
# Can you ask questions with numerical answars?

name = input('What is your name?\n')
age = input('What is your age?\n')
favorite_colour = input('What is your favorite colour?\n')

print('Hello, ' + name + ', You are ' + age + ', and you seem to really like ' + favorite_colour + '.')
print(type(age))


# If you use input to get a number, what data type is stored?
# How could we make sure we can use it as an appropriate data type?

print()

age_forecast = int(age) + 10

print('In 10 years you will be ' + str(age_forecast) + ' Years old.')

# f string (can take integers)
print(f'You will be {age_forecast} years old in 10 years.')