import connexion
import six

from swagger_server.models.player_list import PlayerList  # noqa: E501
from swagger_server.models.provider import Provider  # noqa: E501
from swagger_server.models.dff_scraper import DFFScraper
from swagger_server import util


def get_player_list(body=None):  # noqa: E501
    """Get list of daily fantasy players for a specified sport, platform and slate

    Get list of valid players # noqa: E501

    :param body: Scraper schema
    :type body: dict | bytes

    :rtype: PlayerList
    """
    if connexion.request.is_json:
        provider = Provider.from_dict(connexion.request.get_json())
    return DFFScraper(provider).scrape()
