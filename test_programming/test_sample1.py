# -*- coding: utf-8 -*-

try:
    from unittest import mock
except ImportError:
    import mock

import unittest

import sample


class Test_Sample(unittest.TestCase):

    def test_do_something(self):

        obj = sample.Sample()

        obj._take_a_log_time = mock.Mock()

        result = obj.do_something()

        self.assertEqual(result, 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
