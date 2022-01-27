class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    
    def get_perimeter(self):
        return 2 * (self.length + self.width)


    def get_area(self):
        return self.length * self.width

    
    def get_width(self):
        return self.width


    def get_length(self):
        return self.length


    def get_picture(self):
        line = '*' * self.width + '\n'
        return self.length * line

        
    def __repr__(self):
        return f'Rectangle (l={self.length}, w={self.width})'


    def __str__(self):
        return f'Rectangle with length: {self.length} and width: {self.width}'


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    
    def get_number_enclosing(self, square):
        return int(self.length / square.length) ** 2

    
    def __repr__(self):
        return f'Square (l={self.length})'


    def __str__(self):
        return f'Rectangle with length: {self.length}'