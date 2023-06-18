#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """test class for the max_integer function
    """

    def test_docstring(self):
        doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(doc) > 1)

    def test_function(self):
        function = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(function) > 1)

    def test_max_int_float(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([0, -1, 2]), 2)
        self.assertEqual(max_integer([0, 1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0.0]), 0.0)
        self.assertEqual(max_integer([1.0, 2.0, 3.0]), 3.0)
        self.assertEqual(max_integer([0.0, -1.0]), 0.0)
        self.assertEqual(max_integer([0.0, 1.0, 2.0, 3.0, 4.0]), 4.0)
        self.assertEqual(max_integer([{1, 9}, {2, 3}, {1}, {2}]), {1, 9})

    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [3, 4], [5, 6]]), [5, 6])

    def test_string(self):
        self.assertEqual(max_integer("abcd"), "d")
        self.assertEqual(max_integer("123456789"), "9")
        self.assertEqual(max_integer(["a", "b", "c", "d", "e"]), "e")
        self.assertEqual(max_integer(["abdc", "d"]), "d")

    def test_other(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {3, 4, 5, 6})
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([-9, "str", -5.5, 10, 11])
        with self.assertRaises(TypeError):
            max_integer([None, True])

    def test_None(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    if __name__ == "__main__":
        unittest.main()
