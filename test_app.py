import unittest
from app import add, multiply, divide, subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(4,2),6)
    
    def test_subtract(self):
        self.assertEqual(subtract(1,1),0)
        self.assertEqual(subtract(1,1),0)
        self.assertEqual(subtract(1,1),0)
    
    def test_multiply(self):
        self.assertEqual(multiply(3,1),3)
        self.assertEqual(multiply(4,2),8)
        self.assertEqual(multiply(3,3),9)

    def test_divide(self):
        self.assertEqual(divide(4,2),2)
        self.assertEqual(divide(3,1),3)
        self.assertEqual(divide(9,3),3)

if __name__ == '__main__':
    unittest.main()
