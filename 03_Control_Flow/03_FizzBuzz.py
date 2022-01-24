# Basic Version

# For the numbers 1 to 100
# Play fizzbuzz
# Print the number
# If divisible by 3, fizz
# If by 5, buzz
# if both, fizzbuzz

# What can you add?
# Can we customize the end number?
# Or the start number?
# Can we get those from player input?
# Can we input alternate words for fizz and buzz?


start = input('Please input a start number: ')
end = input('Please input an end number: ')

if start.isdigit()() or end.isdigit():
    fizz = 'fizz'
    buzz = 'buzz'
    response = input('do you want to customize the words fizzbuzz? (y/n): ').lower()
    if response not in ('y', 'n'):
        print('I assume that means you don\'t actually want to play')
    else:
        if response == 'y':
            fizz = input('Please type what you want fizz to be: ')
            buzz = input('Please type what you want buzz to be: ')

        fizzbuzz = fizz + buzz

        for number in range(int(start), int(end) + 1):
            if number % 15 == 0:
                print(fizzbuzz)
            elif number % 3 == 0:
                print(fizz)
            elif number % 5 == 0:
                print(buzz)
            else:
                print(number)
else:
    print('Please use sensible start and end point')
    print('No FizzBuzz for you')