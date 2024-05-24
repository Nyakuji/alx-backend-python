#!/usr/bin/env python3
"""testing utils module"""
import unittest
import utils
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """Class for testing"""
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test that the function returns the expected result"""
        test_cases = [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
        for test_url, test_payload in test_cases:
            mock_get.return_value = Mock(json=Mock(return_value=test_payload))

            # call the function with the test URL
            response = utils.get_json(test_url)

            # assert that the mock was called with the test URL
            mock_get.assert_called_once_with(test_url)

            # assert that the response is what is expected
            self.assertEqual(response, test_payload)

            # reset the mock
            mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """Class for testing"""

    def test_memoize(self):
        """Test that the function returns the expected result"""
        class TestClass:
            """Class for testing"""

            def a_method(self):
                """Method for testing"""
                return 42

            @memoize
            def a_property(self):
                """Method for testing"""
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test_object = TestClass()
            self.assertEqual(test_object.a_property, 42)

            # call the property once
            self.assertEqual(test_object.a_property, 42)

            # call the property again
            self.assertEqual(test_object.a_property, 42)

            # verify that the method was called only once
            mock_method.assert_called_once()
