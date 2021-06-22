import connexion
import six
from datetime import date, datetime
import pytz
from swagger_server.models.player_list import PlayerList  # noqa: E501
from swagger_server.models.dff_scraper import DFFScraper
from swagger_server import util


def get_date():  # noqa: E501
    """Get contest date

    Get contest date # noqa: E501


    :rtype: str
    """
    d = datetime.now()
    timezone = pytz.timezone("America/New_York")
    d_aware = timezone.localize(d)
    return d_aware.strftime('%Y-%m-%d')


def get_player_list(provider, platform, sport, _date):  # noqa: E501
    """Get list of daily fantasy players for a specified sport, platform and slate

    Get list of valid players # noqa: E501

    :param provider: Daily fatansy sports data provider
    :type provider: str
    :param platform: Daily fatansy sports contest website
    :type platform: str
    :param sport: Supported sport
    :type sport: str
    :param _date: Date
    :type _date: str

    :rtype: PlayerList
    """

    return DFFScraper(sport, platform, _date).scrape()


def get_supported_platforms():  # noqa: E501
    """Get list of supported contest platforms

    Get list of supported daily fantasy contest platforms # noqa: E501


    :rtype: List[str]
    """
    return ["Draftkings", "Fanduel"]


def get_supported_providers():  # noqa: E501
    """Get list of supported data providers

    Get list of supported daily fantasy data providers # noqa: E501


    :rtype: List[str]
    """
    return ["Daily Fantasy Fuel"]


def get_supported_sports():  # noqa: E501
    """Get list of supported sports

    Get list of supported sport codes # noqa: E501


    :rtype: List[str]
    """
    return ["MLB", "NBA"]
