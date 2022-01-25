print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def find_divisors(number):
    divisors = [1]
    for i in range(2, round(number / 2) + 1):
        if number % i == 0:
            divisors.append(i)
    divisors.append(number)
    return divisors


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factors(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet


# A2a:
def alpha_pos(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter) + 1


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def name_ID_converter(name):
    ID = ''
    for letter in name.lower():
        ID = ID + str(alpha_pos(letter))
    return ID


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password_generator(name):
    ID = name_ID_converter(name)
    sum = 0
    for number in ID:
        sum += int(number)
    return int(ID) - sum


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def isprime(number):
    prime = True
    for i in range(2, round(number/4)):
        if number % i == 0:
            prime = False
            break
    if prime:
        return True
    else:
        return False


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def isprime_without_error(number):
    if number.isdigit():
        prime = True
        for i in range(2, round(number/4)):
            if number % i == 0:
                prime = False
                break
        if prime:
            return True
        else:
            return False
    else:
        return False


# -------------------------------------------------------------------------------------- #