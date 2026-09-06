from cs2130.module_01.logic import *
from cs2130.module_01.boolean import *
import unittest


class TestLogicFunctions(unittest.TestCase):
    def test_conjunction(self):
        self.assertEqual('T', conjunction('T', 'T'))
        self.assertEqual('F', conjunction('T', 'F'))
        self.assertEqual('F', conjunction('F', 'T'))
        self.assertEqual('F', conjunction('F', 'F'))

    def test_disjunction(self):
        self.assertEqual('T', disjunction('T', 'T'))
        self.assertEqual('T', disjunction('T', 'F'))
        self.assertEqual('T', disjunction('F', 'T'))
        self.assertEqual('F', disjunction('F', 'F'))

    def test_negation(self):
        self.assertEqual('F', negation('T'))
        self.assertEqual('T', negation('F'))

    def test_conditional(self):
        self.assertEqual('T', conditional('T', 'T'))
        self.assertEqual('F', conditional('T', 'F'))
        self.assertEqual('T', conditional('F', 'T'))
        self.assertEqual('T', conditional('F', 'F'))

    def test_biconditional(self):
        self.assertEqual('T', biconditional('T', 'T'))
        self.assertEqual('F', biconditional('T', 'F'))
        self.assertEqual('F', biconditional('F', 'T'))
        self.assertEqual('T', biconditional('F', 'F'))

    def test_proposition1(self):
        self.assertEqual('F', proposition1('T', 'T', 'T'))
        self.assertEqual('F', proposition1('T', 'T', 'F'))
        self.assertEqual('T', proposition1('T', 'F', 'T'))
        self.assertEqual('F', proposition1('T', 'F', 'F'))
        self.assertEqual('T', proposition1('F', 'T', 'T'))
        self.assertEqual('T', proposition1('F', 'T', 'F'))
        self.assertEqual('T', proposition1('F', 'F', 'T'))
        self.assertEqual('F', proposition1('F', 'F', 'F'))

    def test_proposition2(self):
        self.assertEqual('T', proposition2('T', 'T', 'T'))
        self.assertEqual('F', proposition2('T', 'T', 'F'))
        self.assertEqual('T', proposition2('T', 'F', 'T'))
        self.assertEqual('T', proposition2('T', 'F', 'F'))
        self.assertEqual('T', proposition2('F', 'T', 'T'))
        self.assertEqual('F', proposition2('F', 'T', 'F'))
        self.assertEqual('T', proposition2('F', 'F', 'T'))
        self.assertEqual('T', proposition2('F', 'F', 'F'))

    def test_proposition3(self):
        self.assertEqual('F', proposition3('T', 'T', 'T'))
        self.assertEqual('T', proposition3('T', 'T', 'F'))
        self.assertEqual('T', proposition3('T', 'F', 'T'))
        self.assertEqual('T', proposition3('T', 'F', 'F'))
        self.assertEqual('F', proposition3('F', 'T', 'T'))
        self.assertEqual('F', proposition3('F', 'T', 'F'))
        self.assertEqual('T', proposition3('F', 'F', 'T'))
        self.assertEqual('F', proposition3('F', 'F', 'F'))


class TestBooleanFunctions(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(0, multiply(0, 0))  # x is 0, y is 0, expected result is 0
        self.assertEqual(0, multiply(0, 1))  # x is 0, y is 1, expected result is 0
        self.assertEqual(0, multiply(1, 0))  # x is 1, y is 0, expected result is 0
        self.assertEqual(1, multiply(1, 1))  # x is 1, y is 1, expected result is 1

    def test_add(self):
        self.assertEqual(0, add(0, 0))  # x is 0, y is 0, expected result is 0
        self.assertEqual(1, add(0, 1))  # x is 0, y is 1, expected result is 1
        self.assertEqual(1, add(1, 0))  # x is 1, y is 0, expected result is 1
        self.assertEqual(1, add(1, 1))  # x is 1, y is 1, expected result is 1

    def test_complement(self):
        self.assertEqual(1, complement(0))  # x is 0, expected result is 1
        self.assertEqual(0, complement(1))  # x is 1, expected result is 0

    def test_expression1(self):
        self.assertEqual(0, expression1(0, 0, 0))  # x is 0, y is 0, z is 0, expected result is 0
        self.assertEqual(0, expression1(0, 0, 1))  # x is 0, y is 0, z is 1, expected result is 0
        self.assertEqual(0, expression1(0, 1, 0))  # x is 0, y is 1, z is 0, expected result is 0
        self.assertEqual(1, expression1(0, 1, 1))  # x is 0, y is 1, z is 1, expected result is 1
        self.assertEqual(0, expression1(1, 0, 0))  # x is 1, y is 0, z is 0, expected result is 0
        self.assertEqual(0, expression1(1, 0, 1))  # x is 1, y is 0, z is 1, expected result is 0
        self.assertEqual(1, expression1(1, 1, 0))  # x is 1, y is 1, z is 0, expected result is 1
        self.assertEqual(1, expression1(1, 1, 1))  # x is 1, y is 1, z is 1, expected result is 1

    def test_expression2(self):
        self.assertEqual(1, expression2(0, 0, 0))  # x is 0, y is 0, z is 0, expected result is 1
        self.assertEqual(0, expression2(0, 0, 1))  # x is 0, y is 0, z is 1, expected result is 0
        self.assertEqual(1, expression2(0, 1, 0))  # x is 0, y is 1, z is 0, expected result is 1
        self.assertEqual(0, expression2(0, 1, 1))  # x is 0, y is 1, z is 1, expected result is 0
        self.assertEqual(1, expression2(1, 0, 0))  # x is 1, y is 0, z is 0, expected result is 1
        self.assertEqual(1, expression2(1, 0, 1))  # x is 1, y is 0, z is 1, expected result is 1
        self.assertEqual(1, expression2(1, 1, 0))  # x is 1, y is 1, z is 0, expected result is 1
        self.assertEqual(1, expression2(1, 1, 1))  # x is 1, y is 1, z is 1, expected result is 1

    def test_expression3(self):
        self.assertEqual(1, expression3(0, 0, 0))  # x is 0, y is 0, z is 0, expected result is 1
        self.assertEqual(0, expression3(0, 0, 1))  # x is 0, y is 0, z is 1, expected result is 0
        self.assertEqual(0, expression3(0, 1, 0))  # x is 0, y is 1, z is 0, expected result is 0
        self.assertEqual(1, expression3(0, 1, 1))  # x is 0, y is 1, z is 1, expected result is 1
        self.assertEqual(0, expression3(1, 0, 0))  # x is 1, y is 0, z is 0, expected result is 0
        self.assertEqual(0, expression3(1, 0, 1))  # x is 1, y is 0, z is 1, expected result is 0
        self.assertEqual(0, expression3(1, 1, 0))  # x is 1, y is 1, z is 0, expected result is 0
        self.assertEqual(0, expression3(1, 1, 1))  # x is 1, y is 1, z is 1, expected result is 0


if __name__ == '__main__':
    unittest.main()
