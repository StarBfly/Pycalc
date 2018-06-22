import unittest
from pycalc import calculation
from math import *


class OKTest(unittest.TestCase):

    def test_unary_operators(self):
        self.assertEqual(-13, calculation.calculate("-13"))
        self.assertEqual(19, calculation.calculate("6-(-13)"))
        self.assertEqual(0, calculation.calculate("1---1"))
        self.assertEqual(-1, calculation.calculate("-+---+-1"))

    def test_operation_priority(self):
        self.assertEqual(5, calculation.calculate("1+2*2"))
        self.assertEqual(25, calculation.calculate("1+(2+3*2)*3"))
        self.assertEqual(30, calculation.calculate("10*(2+1)"))
        self.assertEqual(1000, calculation.calculate("10**(2+1)"))
        self.assertEqual(100 // 3 ** 2, calculation.calculate("100//3**2"))
        self.assertEqual(100 // 3 % 2 ** 2, calculation.calculate("100//3%2**2"))

    def test_functions_and_constants(self):
        self.assertEqual(pi + e, calculation.calculate("pi+e"))
        self.assertEqual(1, calculation.calculate("log(e)"))
        self.assertEqual(1, calculation.calculate("sin(pi/2)"))
        self.assertEqual(2, calculation.calculate("log10(100)"))
        self.assertEqual(666, calculation.calculate("sin(pi/2)*111*6"))
        self.assertEqual(2, calculation.calculate("2*sin(pi/2)"))

    def test_associative(self):
        self.assertEqual(102 % 12 % 7, calculation.calculate("102%12%7"))
        self.assertEqual(100 // 4 // 3, calculation.calculate("100//4//3"))
        self.assertEqual(2 ** 3 ** 4, calculation.calculate("2**3**4"))

    def test_comparison_operators(self):
        self.assertEqual(1 + 2 * 3 == 1 + 2 * 3, calculation.calculate("1+2*3==1+2*3"))
        self.assertEqual(e ** 5 >= e ** 5 + 1, calculation.calculate("e**5>=e**5+1"))
        self.assertEqual(1 + 2 * 4 // 3 + 1 != 1 + 2 * 4 // 3 + 2, calculation.calculate("1+2*4//3+1!=1+2*4//3+2"))

    def test_common_tests(self):
        self.assertEqual(100, calculation.calculate("(100)"))
        self.assertEqual(666, calculation.calculate("666"))
        self.assertEqual(30, calculation.calculate("10(2+1)"))
        self.assertEqual(-0.1, calculation.calculate("-.1"))
        self.assertEqual(1. / 3, calculation.calculate("1/3"))
        self.assertEqual(1.0/3.0, calculation.calculate("1.0/3.0"))
        self.assertEqual(.1 * 2.0**56.0, calculation.calculate(".1 * 2.0**56.0"))
        self.assertEqual(e**34, calculation.calculate("e**34"))
        self.assertEqual((2.0**(pi/pi+e/e+2.0**0.0)), calculation.calculate("(2.0**(pi/pi+e/e+2.0**0.0))"))
        self.assertEqual((2.0**(pi/pi+e/e+2.0**0.0))**(1.0/3.0), calculation.calculate("(2.0**(pi/pi+e/e+2.0**0.0))**(1.0/3.0)"))
        self.assertEqual(sin(pi/2**1) + log(1*4+2**2+1, 3**2), calculation.calculate("sin(pi/2**1) + log(1*4+2**2+1, 3**2)"))

        self.assertEqual(10*e**0.*log10(.4* -5/ -0.1-10) - -abs(-53//10) + -5, calculation.calculate("10*e^0*log10(.4* -5/ -0.1-10) - -abs(-53//10) + -5"))
        self.assertEqual(sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))+cos(sin(sin(34.0-2.0**2.0))))--cos(1.0)--cos(0.0)**3.0),
                         calculation.calculate("sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))+cos(sin(sin(34.0-2.0**2.0))))--cos(1.0)--cos(0.0)**3.0)"))
        self.assertEqual(2.0**(2.0**2.0*2.0**2.0), calculation.calculate("2.0**(2.0**2.0*2.0**2.0)"))
        self.assertEqual(sin(e**log(e**e**sin(23.0),45.0) + cos(3.0+log10(e**-e))), calculation.calculate("sin(e**log(e**e**sin(23.0),45.0) + cos(3.0+log10(e**-e)))"))


class RaisesTest(unittest.TestCase):
    def runTest(self):
        self.assertRaises(Exception, calculation.calculate, "")
        self.assertRaises(Exception, calculation.calculate, "+")
        self.assertRaises(Exception, calculation.calculate, "1-")
        self.assertRaises(Exception, calculation.calculate, "1 2")
        self.assertRaises(Exception, calculation.calculate, "ee")
        self.assertRaises(Exception, calculation.calculate, "123e")
        self.assertRaises(Exception, calculation.calculate, "==7")
        self.assertRaises(Exception, calculation.calculate, "1 * * 2")
        self.assertRaises(Exception, calculation.calculate, "1 + 2(3 * 4))")
        self.assertRaises(Exception, calculation.calculate, "((1+2)")
        self.assertRaises(Exception, calculation.calculate, "1 + 1 2 3 4 5 6 ")
        self.assertRaises(Exception, calculation.calculate, "log100(100)")
        self.assertRaises(Exception, calculation.calculate, "------")
        self.assertRaises(Exception, calculation.calculate, "5 > = 6")
        self.assertRaises(Exception, calculation.calculate, "5 / / 6")
        self.assertRaises(Exception, calculation.calculate, "6 < = 6")
        self.assertRaises(Exception, calculation.calculate, "6 * * 6")
        self.assertRaises(Exception, calculation.calculate, "(((((")


if __name__ == '__main__':
     unittest.main()
