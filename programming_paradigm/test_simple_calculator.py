import unittest
from programming_paradigm.unit_tests.simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Set up test fixture"""
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        """Test addition operation"""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative and positive numbers
        self.assertEqual(self.calc.add(0, 5), 5)  # Zero addition
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)  # Floating point
        self.assertEqual(self.calc.add(-2, -3), -5)  # Negative numbers
        
    def test_subtraction(self):
        """Test subtraction operation"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        self.assertEqual(self.calc.subtract(-2, -3), 1)  # Negative numbers
        
    def test_multiply(self):
        """Test multiplication operation"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Negative numbers
        
    def test_divide(self):
        """Test division operation"""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero should return None
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(-6, -3), 2)  # Negative numbers
        
if __name__ == '__main__':
    unittest.main()