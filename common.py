import urllib
import urllib2
from bs4 import BeautifulSoup

__author__ = 'soroosh'


class Crawler:
    def _get_soup(self, url):
        response = urllib2.urlopen(urllib.quote(url, safe='/:').encode('utf-8'))
        html = response.read()
        soup = BeautifulSoup(html, from_encoding='utf8')
        return soup
