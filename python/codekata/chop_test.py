__author__ = 'mehmet'

import unittest

from codekata.chop import BinarySearch


class TestStringMethods(unittest.TestCase):
    def test_chop(self):
        self.assertEqual(-1, BinarySearch.chop(3, []))
        self.assertEqual(-1, BinarySearch.chop(3, [1]))
        self.assertEqual(0, BinarySearch.chop(1, [1]))
        self.assertEqual(0, BinarySearch.chop(1, [1, 3, 5]))
        self.assertEqual(1, BinarySearch.chop(3, [1, 3, 5]))
        self.assertEqual(2, BinarySearch.chop(5, [1, 3, 5]))
        self.assertEqual(-1, BinarySearch.chop(0, [1, 3, 5]))
        self.assertEqual(-1, BinarySearch.chop(2, [1, 3, 5]))
        self.assertEqual(-1, BinarySearch.chop(4, [1, 3, 5]))
        self.assertEqual(-1, BinarySearch.chop(6, [1, 3, 5]))
        self.assertEqual(0, BinarySearch.chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, BinarySearch.chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, BinarySearch.chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, BinarySearch.chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, BinarySearch.chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, BinarySearch.chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, BinarySearch.chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, BinarySearch.chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, BinarySearch.chop(8, [1, 3, 5, 7]))


if __name__ == '__main__':
    unittest.main()