__author__ = 'mehmet'

import math


class BloomFilter:
    def __init__(self, representation, *hash_functions):
        super().__init__()
        self.__hash_functions = hash_functions
        self.__representation = representation

    def contains_item(self, item):
        contains = True
        for hash_function in self.__hash_functions:
            index = hash_function(item)
            contains = contains and self.__representation.is_set(index)
        return contains

    def add_item(self, item):
        for hash_function in self.__hash_functions:
            index = hash_function(item)
            self.__representation.set(index)

    @staticmethod
    def number_of_required_bits(n, p):
        """
        Calculates number of bit in order to keep false positive at given threshold
        :param n: number of entries
        :param p: false positive probability threshold
        :return:number of bits required
        """
        return math.ceil(-(n * math.log(p)) / ((math.log(2)) ** 2))


    @staticmethod
    def number_of_required_hash_functions(m, n):
        """
        Calculates required number of hash functions for given parameter
        :param m: number of bits
        :param n: number of entries
        :return: number of required hash functions
        """
        return math.ceil((m / n) * math.log(2))


import array


class BitMap:
    def __init__(self, m):
        self.__bits = array.array('I', [0] * m)
        self.__m = m

    def set(self, index):
        self.__bits[index] = 1

    def is_set(self, index):
        return self.__bits[index] == 1


class HashFunction:
    def __init__(self, hash_function, indices, max_value):
        self.__max_value = max_value
        self.__indices = indices
        self.__hash_function = hash_function

    def hash_code(self, item):
        all_bytes = self.__hash_function(item)
        hash_code = 0
        for index in self.__indices:
            hash_code <<= 8
            hash_code |= all_bytes[index]

        return hash_code % self.__max_value


def md5_hash_functions(k, max_value):
    number_of_bytes = math.ceil(math.log2(max_value) / 8)
    # I want to calculate indexes
    # what can I use here
    # we want to use up all available bytes
    # if number of bytes is 2 and k is 2 than we should round up number of bytes to 8
    # if number of bytes 8 and k is 4 than we need to use some bytes twice
    # if bytes are used twice we need to make sure usage patterns are different