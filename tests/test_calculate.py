import unittest
from unittest.mock import patch
from calculate import calc


class TestCalculate(unittest.TestCase):

    def test1(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [3, -3, 5])
        self.assertIn(
            "Стороны треугольника не могут быть отрицательными",
            str(context.exception)
        )

    def test2(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [1, 2, 10])
        self.assertIn(
            "Не выполняется неравенство треугольника", str(context.exception)
        )

    def test3(self):
        with self.assertRaises(ValueError) as context:
            calc('hexagon', 'area', [5])
        self.assertIn(
            "Фигура 'hexagon' недоступна", str(context.exception)
        )

    def test4(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'volume', [5])
        self.assertIn(
            "Функция 'volume' недоступна", str(context.exception)
        )

    def test5(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'area', [-5])
        self.assertIn(
            "Радиус отрицательный", str(context.exception)
        )

    def test6(self):
        with self.assertRaises(ValueError) as context:
            calc('square', 'area', [-4])
        self.assertIn(
            "Сторона отрицательная",
            str(context.exception)
        )

    def test7(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'area', [3, 4])
        self.assertIn(
            "Для фигуры 'circle' требуется 1 величина",
            str(context.exception)
        )

    def test8(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [3, 4])
        self.assertIn(
            "Для фигуры 'triangle' нужно 3 стороны",
            str(context.exception)
        )

    def test9(self):
        with patch('builtins.print') as mocked_print:
            result = calc('circle', 'area', [4])
            self.assertAlmostEqual(result, 50.26548245743669)
            mocked_print.assert_called_with(
                'Area of circle with size(s) [4] is '
                '50.26548245743669'
            )

    def test10(self):
        with patch('builtins.print') as mocked_print:
            result = calc('circle', 'perimeter', [4])
            self.assertAlmostEqual(result, 25.13274122871835)
            mocked_print.assert_called_with(
                'Perimeter of circle with size(s) [4] is '
                '25.13274122871835'
            )

    def test11(self):
        with patch('builtins.print') as mocked_print:
            result = calc('square', 'area', [4])
            self.assertEqual(result, 16)
            mocked_print.assert_called_with(
                'Area of square with size(s) [4] is '

                '16'
            )

    def test12(self):
        with patch('builtins.print') as mocked_print:
            result = calc('square', 'perimeter', [4])
            self.assertEqual(result, 16)
            mocked_print.assert_called_with(
                'Perimeter of square with size(s) [4] is '
                '16'
            )

    def test13(self):
        with patch('builtins.print') as mocked_print:
            result = calc('triangle', 'area', [3, 4, 5])
            self.assertAlmostEqual(result, 6.0)
            mocked_print.assert_called_with(
                'Area of triangle with size(s) [3, 4, 5] is '
                '6.0'
            )

    def test14(self):
        with patch('builtins.print') as mocked_print:
            result = calc('triangle', 'perimeter', [3, 4, 5])
            self.assertEqual(result, 12)
            mocked_print.assert_called_with(
                'Perimeter of triangle with size(s) [3, 4, 5] is '
                '12'
            )


if __name__ == "__main__":
    unittest.main()
