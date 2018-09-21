'''
Sample python lab for Unit Testing
'''

"""
Write a site of tests to validate the behaviour of your calculator.
If you wish, you could use a TDD approach to developing the calculator and the tests.
"""

import calculator

from unittest import TestCase
from unittest import TestSuite

from unittest import main

# define unit tests for calculator
class test_calculator(TestCase):
    def setUp(self):
        print("In Setup ...")

    def tearDown(self):
        print("In terDown ...")

    def test_initial_value(self):
        calc = calculator()
        self.assertEquals(calc.total, 0, "initial value not set!!")

    def test_add_2_3(self):
        pass

    def test_subtract_2_3(self):
        pass

    def test_multiply_2_3(self):
        pass

    def test_divide_2_3(self):
        pass


# define test suite for the calculator functions
def suite():
    suite = TestSuite()
    suite.addTest(TestAdditionOperations('test_add_1_and_1'))
    suite.addTest(TestSubtractionOperations('test_sub_1_and_1'))
    return suite

# main method to run the tests!
if __name__ == '__main__':
 mySuite = suite()
 unittest.TextTestRunner(verbosity=0).run(mySuite)
