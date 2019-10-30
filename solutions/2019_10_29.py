#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 [Anselmos](github.com/anselmos) <anselmos@users.noreply.github.com>
#
# Distributed under terms of the MIT license.

"""

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.abs
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

import unittest

import unittest

def problem(number_list, k):
    for elt in number_list:
        if k - elt in number_list:
            return True
    return False

class TestNumbers(unittest.TestCase):
    """ Testing"""

    def test_example(self):
        example_list = [10, 15, 3, 7]
        k = 17
        self.assertTrue(problem(example_list, k))
        example_list = [10, 7]
        k = 17
        self.assertTrue(problem(example_list, k))
        example_list = [10]
        k = 17
        self.assertFalse(problem(example_list, k))
        example_list = [-1, 25, 2, 46]
        k = 26
        self.assertFalse(problem(example_list, k))
        example_list = [-1, -5, 2, 46]
        k = 7
        self.assertFalse(problem(example_list, k))



if __name__ == '__main__':
    unittest.main()
