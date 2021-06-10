# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.player_list import PlayerList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDFSScraperAPIController(BaseTestCase):
    """DFSScraperAPIController integration test stubs"""

    def test_get_date(self):
        """Test case for get_date

        Get contest date
        """
        response = self.client.open(
            '/api/v1/getDate',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_player_list(self):
        """Test case for get_player_list

        Get list of daily fantasy players for a specified sport, platform and slate
        """
        response = self.client.open(
            '/api/v1/getPlayerList/{provider}/{platform}/{sport}/{date}'.format(provider='provider_example', platform='platform_example', sport='sport_example', _date='_date_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_supported_platforms(self):
        """Test case for get_supported_platforms

        Get list of supported contest platforms
        """
        response = self.client.open(
            '/api/v1/getSupportedPlatforms',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_supported_providers(self):
        """Test case for get_supported_providers

        Get list of supported data providers
        """
        response = self.client.open(
            '/api/v1/getSupportedProviders',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_supported_sports(self):
        """Test case for get_supported_sports

        Get list of supported sports
        """
        response = self.client.open(
            '/api/v1/getSupportedSports',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
