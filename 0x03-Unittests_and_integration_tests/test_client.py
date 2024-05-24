#!/usr/bin/env python3
"""Unittests for the client module."""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class."""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_class = GithubOrgClient(org)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that the result of _public_repos_url is the expected one."""
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/google/repos'}
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class._public_repos_url,
                         "https://api.github.com/orgs/google/repos")
