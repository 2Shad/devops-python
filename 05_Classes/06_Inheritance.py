# Inheritance and Polymorphism

class Mammal:
    def __init__(self, name):
        self.warm_blooded = True
        self.name = name

    
    def reproduce(self):
        print('Giving birth to live young')


class Horse(Mammal):
    def __init__(self, name, jockey):
        super().__init__(name)
        self.legs = 4
        self.jockey = jockey

    def reproduce(self):
        print('Giving birth to live foals')


class Pony(Horse):
    def __init__(self, pony_name, cuteness_rating=10):
        super().__init__(pony_name, None)


class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.poisonous_barb = True

    def reproduce(self):
        print('Laying eggs')

m = Mammal('Charlie')

h = Horse()
print(h.warm_blooded)
h.reproduce()