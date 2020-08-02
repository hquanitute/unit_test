import unittest

def factorial(n): 
      
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

class TestMethod(unittest.TestCase):
    def test_should_return_number(self):
        self.assertEqual(type(factorial(3)) is int, True)
        
    def test_case1(self):
        self.assertEqual(factorial(5), 120)

    def test_case2(self):
        self.assertEqual(factorial(10), 3628800)

    def test_case3(self):
        self.assertEqual(factorial(20), 2432902008176640000)
    
    def test_case4(self):
        self.assertEqual(factorial(0), 1)

if __name__ == '__main__':
    unittest.main()
