
from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from bs4 import BeautifulSoup
from typing import List, Dict  # noqa: F401
from swagger_server.models.player import Player  # noqa: F401,E501
import requests


class DFFScraper():
    def __init__(self, sport: str = None, platform: str = None, _date: str = None):
        self._url = 'https://www.dailyfantasyfuel.com/{}/projections/{}/{}/'.format(
            sport.lower(), platform.lower(), _date)

    def toPlayerObject(self, row):
        return Player(0, row["data-start_date"], row["data-name"], row["data-fn"], row["data-ln"], row["data-pos"], row["data-inj"], row["data-team"], int(row["data-salary"]), float(row["data-ppg_proj"]), float(row["data-value_proj"]))

    def toPlayerList(self, rows):
        return list(map(self.toPlayerObject, rows))

    def scrape(self):
        rows = []
        page = requests.get(self._url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for tr in soup.findAll("tr", class_="projections-listing"):
            rows.append(tr.attrs)
        return self.toPlayerList(rows)
