import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) # actual output vs. expected

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-2),-3)
        
    def test_add_zero(self):
        self.assertEqual(self.calc.add(1,0),1)

    # Substract
    def test_stubstct_positive(self):
        self.assertEqual(self.calc.subtract(2,5),3)

    def test_stubstct_negative(self):
        self.assertEqual(self.calc.subtract(2,-8),-10)

    #multiply
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(2,25),50)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-8,5),-40)

    #divide
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(9,3),3)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10,2),-5)

    # modulo
    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(8,6),2)

    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(-15,-9),-6)
        

if __name__ == '__main__':
    unittest.main()