from cs1410.module0.utilities import *
import unittest

from unittest.mock import patch


class TestUtilityFunctions(unittest.TestCase):
    @patch('builtins.print')
    def test_hello(self, mock_print):
        hello()
        mock_print.assert_called_with('Hello World')
        hello('Jane')
        mock_print.assert_called_with('Hello Jane')

    def test_add(self):
        self.assertEqual(8, add(5,3))
        self.assertEqual(8, add(3,5))
        self.assertEqual(-2, add(-5, 3))
        self.assertEqual(0, add(0,0))

    def test_sub(self):
        self.assertEqual(2, sub(5,3))
        self.assertEqual(-2, sub(3,5))
        self.assertEqual(0, sub(0,0))


if __name__ == '__main__':
    unittest.main()