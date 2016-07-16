# -*- coding: utf-8 -*-

import unittest
from fizzbuzz import fizzbuzz

class Test_fizzbuzz(unittest.TestCase):

    def setUp(self):

        self._expects = {
                1: '1',
                2: '2',
                3: 'Fizz',
                4: '4',
                5: 'Buzz',
                6: 'Fizz',
                7: '7',
                8: '8',
                9: 'Fizz',
                10: 'Buzz',
                14: '14',
                15: 'FizzBuzz',
                16: '16',
            }

    def test_fuzzbuzz(self):
        for n, expect in self._expects.items():

            result = fizzbuzz(n)

            self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
