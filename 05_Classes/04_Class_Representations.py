class Location:
    def __init__(self, latitude, longetude):
        self.latitude = latitude
        self.longetude = longetude
    

    def __repr__(self):
        return f'Location(latitude={self.latitude}, longetude={self.longetude})'


    def __str__(self):
        return f'({self.latitude}, {self.longetude})'


bham_academy = Location(52.488647, -1.887249)
print(repr(bham_academy))
print(bham_academy)

print(f'Sparta Global Birmingham academy is located at coo-ordinates {bham_academy}')


class Dog:
    def __init__(self, age):
        self.age = age


    def __str__(self):
        return f'A {self.age} year old Dog'

    
    def __format__(self, format_spec):
        if format_spec == 'dog':
            return  f'A {self.age * 7} year old Dog'
        else:
            return self.__str__(self)


fido = Dog(5)
print(fido)