# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.player_list import PlayerList  # noqa: E501
from swagger_server.models.scraper import Scraper  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDFSScraperAPIController(BaseTestCase):
    """DFSScraperAPIController integration test stubs"""

    def test_get_player_list(self):
        """Test case for get_player_list

        Get list of daily fantasy players for a specified sport, platform and slate
        """
        body = Scraper()
        response = self.client.open(
            '/v1/getPlayerList',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
