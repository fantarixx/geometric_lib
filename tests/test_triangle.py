import unittest
from triangle import area, perimeter
import math


class TestTriangle(unittest.TestCase):

    def test1(self):
        a, b, c = 0, 0, 5
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test2(self):
        a, b, c = 1, 2, 3
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test3(self):
        a, b, c = 3, -3, 5
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test4(self):
        a, b, c = 3, 4, 5
        s = (a + b + c) / 2
        correct = math.sqrt(s * (s - a) * (s - b) * (s - c))
        self.assertAlmostEqual(area(a, b, c), correct)

    def test5(self):
        a, b, c = 3, 3, 5
        correct = a + b + c
        self.assertEqual(perimeter(a, b, c), correct)

    def test6(self):
        a, b, c = 0, 3, 5
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test7(self):
        a, b, c = 1, 2, 3
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test8(self):
        a, b, c = -3, 3, 5
        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == '__main__':
    unittest.main()
