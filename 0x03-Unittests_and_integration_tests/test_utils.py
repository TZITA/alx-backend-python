#!/usr/bin/env python3
""" Task 0 """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Union


access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap test class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               result: Union[Mapping, int]):
        """ test_access_nested_map method """
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, result)

    @parameterized.expand([
        ({}, ("a",), KeyError("a")),
        ({"a": 2}, ("a", "b"), KeyError("b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         exp_exc: Exception):
        """test_access_nested_map_exception """
        with self.assertRaises(type(exp_exc)) as ex:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ex.exception), str(exp_exc))
