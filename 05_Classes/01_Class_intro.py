### OOP - Object Oriented Programming

class Dog:

    animal_kind = 'canine' # class variable

    def bark(self, number_of_woofs):  # method
        return 'Woof! ' * number_of_woofs
    

    def loud_bark(self, number_of_woofs):
        return self.bark(number_of_woofs).upper()


class Parrot:

    animal_kind = 'bird'

    def tweet(self):
        return 'Tweet! '
    
    # def repeat(self, chatter):
    #     for letter in chatter:


fido = Dog()  # Instantiation - i.e. crating an INSTANCE of a class
lassie = Dog()
Pluto = Dog()

print(fido, type(fido))
print(fido.animal_kind)
print(fido.loud_bark(4))
fido.animal_kind = 'feline'
print(fido.animal_kind)
print(lassie.animal_kind)

Dog.animal_kind = 'arachnid'
print(Pluto.animal_kind)

