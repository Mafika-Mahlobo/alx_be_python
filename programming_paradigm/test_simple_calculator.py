import unittest
from simple_calculator import SimpleCalculator

class TestCalc(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(4, 5), 9)
        self.assertEqual(self.calc.add(-2, 2), 0)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(-1, -1), -2)
        with self.assertRaises(TypeError):
            self.calc.add("ten", "five")
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-3, 2), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(3, -2), 5)
        with self.assertRaises(TypeError):
            self.calc.subtract("ten", "five")
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(3, 0), 0)
        self.assertEqual(self.calc.multiply(4, -1), -4)
        self.assertEqual(self.calc.multiply(-1, -5), 5)
        with self.assertRaises(TypeError):
            self.calc.multiply("ten", "five")
        
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 5), 1)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(2, 0)
        with self.assertRaises(TypeError):
            self.calc.divide("ten", "five")
            
if __name__ == "__main__":
    unittest.main()
