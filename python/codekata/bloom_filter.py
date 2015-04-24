__author__ = 'mehmet'

import math


class BloomFilter:
    def __init__(self, bitset, *hash_functions):
        super().__init__()
        self.__hash_functions = hash_functions
        self.__bitset = bitset

    def contains_item(self, item):
        contains = True
        for hash_function in self.__hash_functions:
            index = hash_function(item)
            contains = contains and self.__bitset.is_set(index)
        return contains

    def add_item(self, item):
        for hash_function in self.__hash_functions:
            index = hash_function(item)
            self.__bitset.set(index)

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


class BitSet:
    def __init__(self, m):
        self.__bits = array.array('I', [0] * m)
        self.__m = m

    def set(self, index):
        self.__bits[index] = 1

    def is_set(self, index):
        return self.__bits[index] == 1


import hashlib


class HashFunction:
    def __init__(self, seed, max_value):
        self.__seed = seed
        self.__max_value = max_value

    def hash_code(self, item):
        m = hashlib.md5(self.__seed.encode('utf-8'))
        m.update(item.encode('utf-8'))
        all_bytes = m.digest()
        hash_code = 0
        for index in range(0, 4):
            hash_code <<= 8
            hash_code |= all_bytes[index]
        return hash_code % self.__max_value


if __name__ == "__main__":
    with open("/usr/share/dict/words") as f:
        lines = f.read().splitlines()
        n = len(lines)
        m = BloomFilter.number_of_required_bits(n, 0.01)
        k = BloomFilter.number_of_required_hash_functions(m, n)
        hash_functions = []
        for i in range(0, k):
            hash_functions.append(HashFunction(lines[i], m).hash_code)
        print("n=", n, "m=", m, "k=", k)
        bloom_filter = BloomFilter(BitSet(m), *hash_functions)

        for l in lines:
            bloom_filter.add_item(l)

        for l in lines:
            if not bloom_filter.contains_item(l):
                print(l, "false negative")

        words = ["hayirli", "sabahlar", "hemserim", "nerden", "gelirsin", "nereye", "gidersin", "bu", "fani", "dunyada", "kac", "dostun", "var"]
        false_positives = []
        for word in words:
            if bloom_filter.contains_item(word):
                false_positives.append(word)

        print("false positives", false_positives)
        negatives = [x for x in words if x not in false_positives]
        negatives = list(filter(lambda x: x not in false_positives, words))
        print("correct negatives", negatives)