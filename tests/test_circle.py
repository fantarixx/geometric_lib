import unittest
from circle import area, perimeter
import math


class TestCircle(unittest.TestCase):

    def test1(self):
        r = -52
        with self.assertRaises(ValueError):
            perimeter(r)


    def test2(self):
        r = -52
        with self.assertRaises(ValueError):
            area(r)


    def test3(self):
        r = 0
        correct = 0
        self.assertEqual(area(r), correct)


    def test4(self):
        r = 0
        correct = 0
        self.assertEqual(perimeter(r), correct)


    def test5(self):
        r = 52
        correct = math.pi * r * r
        self.assertAlmostEqual(area(r), correct)


    def test6(self):
        r = 52
        correct = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), correct)


if __name__ == '__main__':
    unittest.main()
