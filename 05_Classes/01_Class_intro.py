# ## OOP - Object Oriented Programming

class Dog:
    def __init__(self, breed, hair_length, legs=4, criminal_record=None):   # Initialisation, dunder (double underscore)
        self.animal_kind = 'canine'
        self.legs = legs
        self.breed = breed
        self.criminal_record = criminal_record
        if hair_length in ('short', 'medium', 'long'):
            self.hair_length = hair_length
        else:
            print('Hair Length must be short, medium or long. Defalt is medium')
            self.hair_length = 'medium'
        print(self.bark())

    def bark(self, number_of_woofs=1):  # method
        return 'Woof! ' * number_of_woofs

    def loud_bark(self, number_of_woofs):
        return self.bark(number_of_woofs).upper()


class Parrot:
    def __init__(self, colour):
        self.animal_kind = 'bird'
        self.colour = colour

    def tweet(self):
        return 'Tweet! '
    
    def repeat(self, chatter: str):
        return chatter.replace('o', 'aa')


fido = Dog('Dalmatian', 'yes')  # Instantiation - i.e. crating an INSTANCE of a class
lassie = Dog('Collie', 'yes')
Pluto = Dog('Dalmatian', 'yes')

print(fido, type(fido))
print(fido.animal_kind)
print(fido.loud_bark(4))
fido.animal_kind = 'feline'
print(fido.animal_kind)
print(lassie.animal_kind)

Dog.animal_kind = 'arachnid'
print(Pluto.animal_kind)

fido.legs = 3
print(fido.legs)

print(fido.breed)
print(lassie.breed)

birdie = Parrot('green')
print(birdie.repeat('hello'))