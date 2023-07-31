#!/usr/bin/env python3
""" Task 0 """
import unittest
import requests
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Sequence, Union, Dict


access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


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


class TestGetJson(unittest.TestCase):
    """ TestGetJson test class """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """test_get_json"""
        attributes = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**attributes)) as req:
            self.assertEqual(get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)
