i = 1

while i < 10:
    print(i)
    if i == 5:
        print('FIVE PARTY!')
        break
    i += 1

print('Loop finished')

for x in ['a', 'b', 'c', 'd', 'e']:
    break_for = False
    j = 100
    while j < 110:
        print(x, j)
        if i == 105:
            break_for = True
            break
        i += 1
    if break_for:
        break

prompt_user = True
while prompt_user:
    age = input('What is your age?\n')
    if age.isdigit():
        if int(age) > 119:
            print('Please use a sensible age')
        else:
            prompt_user = False
    else:
        print('Please enter age in digits')
print(f'Double of your age is {int(age) * 2}.')

# try:
#     age = int(input('What is your age?\n'))
# except:
#     print('Please enter age in digits')