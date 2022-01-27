from shapes import Rectangle, Square
import unittest

class ShapesTests(unittest.TestCase):

    def setUp(self):
        self.john = Rectangle(4, 6)
        self.luke = Square(6)

    def test_rectangle_perimiter(self):
        actual = self.john.get_perimeter()
        expected = 2 * (4 + 6)
        self.assertEqual(actual, expected)
    
    def test_rectangle_area(self):
        actual = self.john.get_area()
        expected = 4 * 6
        self.assertEqual(actual, expected)

    def test_square_perimiter(self):
        actual = self.luke.get_perimeter()
        expected = 6 * 4
        self.assertEqual(actual, expected)
    
    def test_square_area(self):
        actual = self.luke.get_area()
        expected = 6 ** 2
        self.assertEqual(actual, expected)

    def test_square_enclosing(self):
        actual = self.luke.get_number_enclosing(Square(4))
        expected = 1
        self.assertEqual(actual, expected)

    def test_rectangle_width(self):
        actual = self.john.get_width()
        expected = 6
        self.assertEqual(actual, expected)

    def test_rectangle_length(self):
        actual = self.john.get_length()
        expected = 4
        self.assertEqual(actual, expected)

    def test_rectangle_picture(self):
        actual = self.john.get_picture()
        expected = '******\n******\n******\n******\n'
        self.assertEqual(actual, expected)
        4, 6