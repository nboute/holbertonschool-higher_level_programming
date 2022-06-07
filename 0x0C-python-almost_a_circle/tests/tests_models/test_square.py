#!/usr/bin/python3
"""Module square"""

import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


"""
Unit test for the size setter/getter methods of the Square class
"""


class TestSquareSize(unittest.TestCase):
    """ tests for size setter/getter of square.py """

    def test_square_size1(self):
        """ test without args """
        with self.assertRaises(TypeError):
            Square.size()

    def test_square_size2(self):
        """test getter"""
        my_square = Square(2)
        self.assertEqual(my_square.size, 2)

    def test_square_size3(self):
        """test setter"""
        my_square = Square(2)
        my_square.size = 7
        self.assertEqual(my_square.size, 7)

    def test_square_size4(self):
        """test setter with 0"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = 0

    def test_square_size5(self):
        """test setter with negative value"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = -5

    def test_square_size6(self):
        """test setter with wrong type: float"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = 4.5

    def test_square_size7(self):
        """test setter with wrong type: string"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = "School"

    def test_square_size8(self):
        """test setter with wrong type: list"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = [4]

    def test_square_size9(self):
        """test setter with wrong type: tuple"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = (4, )

    def test_square_size10(self):
        """test setter with wrong type: dictionary"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = {4}


"""
    Unittest for to_dictionary square
"""


class TestSquareDict(unittest.TestCase):
    """
        tests for square to dictionary
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dict_square_ok(self):
        """
            tests for dictionary for a normal square
        """
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 1, 'x': 2, 'size': 10, 'y': 1})
        s1 = Square(10, 2, 1, 8)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 8, 'x': 2, 'size': 10, 'y': 1})
        s5 = Square(3, 12)
        self.assertEqual(s5.to_dictionary(), {
                         'id': 2, 'x': 12, 'size': 3, 'y': 0})
        s6 = Square(3)
        self.assertEqual(s6.to_dictionary(), {
                         'id': 3, 'size': 3, 'x': 0, 'y': 0})

    def test_to_dict_square_value_error(self):
        """
            tests for value error of the square
        """
        with self.assertRaises(ValueError):
            s2 = Square(-2, 3, 12)
            s2.to_dictionary()
        with self.assertRaises(ValueError):
            s3 = Square(2, -3, 12)
            s3.to_dictionary()
        with self.assertRaises(ValueError):
            s4 = Square(2, 3, -12)
            s4.to_dictionary()

    def test_to_dict_square_type_error(self):
        """
            test for type error of the square
        """
        with self.assertRaises(TypeError):
            s7 = Square()
            s7.to_dictionary()
        with self.assertRaises(TypeError):
            s8 = Square(2.3, 3, 12)
            s8.to_dictionary()
        with self.assertRaises(TypeError):
            s9 = Square(2, 3.2, 12)
            s9.to_dictionary()
        with self.assertRaises(TypeError):
            s10 = Square(2, (3, 2, 3), 12)
            s10.to_dictionary()
        with self.assertRaises(TypeError):
            s11 = Square((2, 8, 9), 3, 12)
            s11.to_dictionary()
        with self.assertRaises(TypeError):
            s12 = Square(2, 3, (2, 8, 7))
            s12.to_dictionary()
        with self.assertRaises(TypeError):
            s13 = Square((), 3, 12)
            s13.to_dictionary()
        with self.assertRaises(TypeError):
            s14 = Square(2, (), 12)
            s14.to_dictionary()
        with self.assertRaises(TypeError):
            s15 = Square(2, 3, ())
            s15.to_dictionary()
        with self.assertRaises(TypeError):
            s16 = Square(float('inf'), 3, 12)
            s16.to_dictionary()
        with self.assertRaises(TypeError):
            s17 = Square(2, float('inf'), 12)
            s17.to_dictionary()
        with self.assertRaises(TypeError):
            s18 = Square(2, 12, float('inf'))
            s18.to_dictionary()


if __name__ == '__main__':
    unittest.main()
