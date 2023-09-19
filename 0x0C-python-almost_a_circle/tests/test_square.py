#!/usr/bin/python3

"""Defines unittests for models/square.py"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

        s = Square(10, 2, 3, 4)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_str(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 10")

    def test_update(self):
        s = Square(10, 2, 3, 4)
        s.update(5, 20, 30, 40)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

        s.update(x=50, y=60)
        self.assertEqual(s.x, 50)
        self.assertEqual(s.y, 60)

    def test_to_dictionary(self):
        s = Square(10, 2, 3, 4)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {'id': 4, 'size': 10, 'x': 2, 'y': 3})


if __name__ == "__main__":
    unittest.main()