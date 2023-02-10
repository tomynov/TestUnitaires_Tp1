import unittest
import sys
sys.path.append("C:\\Users\\Tom\\Desktop\\YnovParis\\Ynov2022\\TestUnitaires\\app")
from MyCalcul import Calculator

class TestCalculatorMethods(unittest.TestCase):
    def test_add(self):
        # Test adding two positive numbers
        result = Calculator.add(5, 5)
        self.assertEqual(result, 10)

        # Test adding two negative numbers
        result = Calculator.add(-1, -2)
        self.assertEqual(result, -3)

        # Test adding a positive and a negative number
        result = Calculator.add(1, -3)
        self.assertEqual(result, -2)

    def test_substract(self):
        # Test substraction two positive numbers
        result = Calculator.substract(2, 1)
        self.assertEqual(result, 1)

        # Test substract two negative numbers
        result = Calculator.substract(-1, -6)
        self.assertEqual(result, 5)

        # Test substract a positive and a negative number
        result = Calculator.substract(2, -4)
        self.assertEqual(result, -2)

    def test_multiply(self):
        # Test multiplication two positive numbers
        result = Calculator.multiply(2, 4)
        self.assertEqual(result, 8)

        # Test multiply two negative numbers
        result = Calculator.multiply(-2, -4)
        self.assertEqual(result, 8)

        # Test multiply a positive and a negative number
        result = Calculator.multiply(2, -4)
        self.assertEqual(result, -8)

    def test_divide(self):
        # Test divide two positive numbers
        result = Calculator.divide(4, 2)
        self.assertEqual(result, 2)

        # Test divide two negative numbers
        result = Calculator.divide(-4, -2)
        self.assertEqual(result, 2)

        # Test divide a positive and a negative number
        result = Calculator.divide(4, -2)
        self.assertEqual(result, -2)

        # Test divide by zero
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(6, 0)

    def test_power(self):
        # Test power two positive numbers
        result = Calculator.power(5, 3)
        self.assertEqual(result, 15)

        # Test power two negative numbers
        result = Calculator.power(-2, 2)
        self.assertEqual(result, 4)

    def test_square_root(self):
       # Test square_root positive numbers
        result = Calculator.square_root(9)
        self.assertAlmostEqual(result, 3)

    def test_calculate(self):
        # Test the calculate function with add operation
        result = Calculator.calculate("add", 1, 1)
        self.assertEqual(result, 2)
        
        # Test the calculate function with substract operation
        result = Calculator.calculate("substract", 8, 3)
        self.assertEqual(result, 5)
        
        # Test the calculate function with multiply operation
        result = Calculator.calculate("multiply", 2, 2)
        self.assertEqual(result, 4)
        
        # Test the calculate function with divide operation
        result = Calculator.calculate("divide", 9, 3)
        self.assertEqual(result, 3)
        
        # Test the calculate function with power operation
        result = Calculator.calculate("power", 3, 2)
        self.assertEqual(result, 9)

        # Test the calculate function with square_root operation
        result = Calculator.calculate("square_root", 25)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
