import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Basic positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        
        # Adding zero
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 7), -3)
        
        # Decimal numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=7)
        self.assertAlmostEqual(self.calc.add(-1.5, 2.5), 1.0, places=7)
        
        # Large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Basic positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        
        # Subtracting zero
        self.assertEqual(self.calc.subtract(8, 0), 8)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Negative numbers
        self.assertEqual(self.calc.subtract(-3, -1), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        
        # Decimal numbers
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.3), 3.2, places=7)
        self.assertAlmostEqual(self.calc.subtract(-1.5, -2.5), 1.0, places=7)
        
        # Same numbers (result should be zero)
        self.assertEqual(self.calc.subtract(7, 7), 0)
        self.assertEqual(self.calc.subtract(-4, -4), 0)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Basic positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 6), 42)
        
        # Multiplying by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 8), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Multiplying by one
        self.assertEqual(self.calc.multiply(9, 1), 9)
        self.assertEqual(self.calc.multiply(1, 15), 15)
        
        # Negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(5, -2), -10)
        self.assertEqual(self.calc.multiply(-4, -3), 12)
        
        # Decimal numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0, places=7)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2.0), -3.0, places=7)
        
        # Large numbers
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Basic positive numbers
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(15, 3), 5)
        
        # Division resulting in decimal
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=7)
        
        # Dividing zero by a number
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -3), 0)
        
        # Division by zero (should return None)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Negative numbers
        self.assertEqual(self.calc.divide(-8, 2), -4)
        self.assertEqual(self.calc.divide(12, -3), -4)
        self.assertEqual(self.calc.divide(-15, -5), 3)
        
        # Decimal numbers
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)
        self.assertAlmostEqual(self.calc.divide(-9.6, 3.2), -3.0, places=7)
        
        # Division by one
        self.assertEqual(self.calc.divide(42, 1), 42)
        self.assertEqual(self.calc.divide(-7, 1), -7)
        
        # Self-division (number divided by itself)
        self.assertEqual(self.calc.divide(5, 5), 1)
        self.assertEqual(self.calc.divide(-8, -8), 1)

    def test_edge_cases_and_special_values(self):
        """Test edge cases and special values across all operations."""
        # Very small numbers
        small_num = 1e-10
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2e-10, places=15)
        self.assertAlmostEqual(self.calc.multiply(small_num, 2), 2e-10, places=15)
        
        # Very large numbers
        large_num = 1e10
        self.assertEqual(self.calc.add(large_num, large_num), 2e10)
        self.assertEqual(self.calc.subtract(large_num, large_num), 0)
        
        # Mixed operations with the same calculator instance
        result1 = self.calc.add(10, 5)
        result2 = self.calc.multiply(result1, 2)
        result3 = self.calc.divide(result2, 3)
        self.assertAlmostEqual(result3, 10.0, places=7)

    def test_type_consistency(self):
        """Test that operations maintain type consistency where expected."""
        # Integer operations
        self.assertIsInstance(self.calc.add(2, 3), int)
        self.assertIsInstance(self.calc.subtract(5, 2), int)
        self.assertIsInstance(self.calc.multiply(3, 4), int)
        
        # Float operations
        self.assertIsInstance(self.calc.add(2.0, 3.0), float)
        self.assertIsInstance(self.calc.divide(6, 2), float)  # Division always returns float
        
        # Mixed type operations
        self.assertIsInstance(self.calc.add(2, 3.0), float)
        self.assertIsInstance(self.calc.multiply(2.5, 4), float)


if __name__ == '__main__':
    # Run the tests
    print("Running SimpleCalculator unit tests...")
    unittest.main(verbosity=2)
