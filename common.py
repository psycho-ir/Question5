import urllib
import urllib2
from bs4 import BeautifulSoup

__author__ = 'soroosh'


class Crawler:
    def _get_soup(self):
        response = urllib2.urlopen(urllib.quote(self.base_url, safe='/:').encode('utf-8'))
        html = response.read()
        soup = BeautifulSoup(html, from_encoding='utf8')
        return soup
