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

def ask_value(value):
    return input(f'What do you want the {value} to be?\n')

def game(start, end, fizz, buzz):
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



prompt_start_end = True
prompt_decision = True

while prompt_start_end:
    # Asks user for start and end point
    start = ask_value('start')
    end = ask_value('end')
    # checks if user given values are digits
    if start.isdigit() and end.isdigit():
        if int(start) < int(end):
            prompt_start_end = False
        else:
            print('Your start number needs to be lower than your end number.')
    else:
        # message to user if user inputted inappropriate start and end point
        print('\nPlease use sensible start and end point')

fizz = 'fizz'
buzz = 'buzz'
        
        
while prompt_decision:
    # asks user if he wants to change fizzbuzz
    response = input('do you want to customize the words fizzbuzz? (y/N): ').lower()
    # checks user's decision, and gives the option if he wants to mod the game, if the user is trying to break the code, it doesn't let him play the game
    if response in ('y', 'n'):
        prompt_decision = False
    else:
        print('\nPlease be decisive.')
if response == 'y':
    fizz = ask_value('fizz')
    buzz = ask_value('buzz')

# fizzbuzz game
game(start, end, fizz, buzz)