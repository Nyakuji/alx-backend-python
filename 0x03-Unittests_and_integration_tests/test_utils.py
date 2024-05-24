#!/usr/bin/env python3
"""testing utils module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing access_nested_map"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that the function returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError, "'a'"),
        ({'a': 1}, ('a', 'b'), KeyError, "'b'")
    ])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            expected_exception,
            expected_message):
        """Test that the function raises the correct exception"""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(expected_message, str(context.exception))
