__author__ = 'mehmet'

import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import call

from codekata.bloom_filter import BloomFilter
from codekata.bloom_filter import BitSet
from codekata.bloom_filter import HashFunction


class TestStringMethods(unittest.TestCase):
    # provide data with previously known hashes and check bit pattern matches is correct
    def test_load_data(self):
        mock_hash_1 = MagicMock(side_effect=lambda x: {"mehmet": 1, "ali": 5}.get(x))
        mock_hash_2 = MagicMock(side_effect=lambda x: {"mehmet": 3, "ali": 8}.get(x))
        mock_bit_map = Mock()
        bloom_filter = BloomFilter(mock_bit_map, mock_hash_1, mock_hash_2)
        bloom_filter.add_item("mehmet")
        bloom_filter.add_item("ali")

        self.assertEquals(mock_bit_map.set.call_args_list, [call(1), call(3), call(5), call(8)])

    # This test can be done in two ways first of which is providing bit set and checking it for additional words
    def test_positive(self):
        mock_hash_1 = MagicMock(side_effect=lambda x: {"mehmet": 1}.get(x))
        mock_hash_2 = MagicMock(side_effect=lambda x: {"mehmet": 3}.get(x))
        mock_bit_map = Mock()
        mock_bit_map.is_set = Mock(side_effect=lambda x: {1: True, 3: True}.get(x, False))

        bloom_filter = BloomFilter(mock_bit_map, mock_hash_1, mock_hash_2)

        contains_item = bloom_filter.contains_item("mehmet")

        self.assertTrue(contains_item)

    def test_negative(self):
        mock_hash_1 = MagicMock(side_effect=lambda x: {"mehmet": 1}.get(x))
        mock_hash_2 = MagicMock(side_effect=lambda x: {"mehmet": 5}.get(x))
        mock_bit_map = Mock()
        mock_bit_map.is_set = Mock(side_effect=lambda x: {1: True, 5: False}.get(x, False))

        bloom_filter = BloomFilter(mock_bit_map, mock_hash_1, mock_hash_2)

        contains_item = bloom_filter.contains_item("mehmet")

        self.assertFalse(contains_item)

    def test_representation(self):
        bit_map = BitSet(10)
        bits_set = (0, 3, 5, 9)
        # Set bits
        for index in bits_set:
            bit_map.set(index)
        # verify bits set
        for index in bits_set:
            self.assertTrue(bit_map.is_set(index))
        # verify bits unset
        bits_unset = [index for index in range(10) if index not in bits_set]
        for index in bits_unset:
            self.assertFalse(bit_map.is_set(index))

    def test_hash_function(self):
        h1 = HashFunction("hello", 100)
        h2 = HashFunction("roj bas", 100)
        r1 = h1.hash_code("ali")
        r2 = h2.hash_code("ali")
        print(r1, r2)
        self.assertTrue(r1 != r2)

    def test_number_of_bits(self):
        n = 99171
        m = BloomFilter.number_of_required_bits(n, 0.01)
        k = BloomFilter.number_of_required_hash_functions(m=m, n=n)
        print(m, k)

if __name__ == '__main__':
    unittest.main()