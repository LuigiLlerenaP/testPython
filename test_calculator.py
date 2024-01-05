import unittest
from calculate import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(2.5, 2.5), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(2.5, 2.5), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(2.5, 2.5), 6.25)
    
    def test_divide(self):
        self.assertEqual(divide(8, 4), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(10, 0), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
