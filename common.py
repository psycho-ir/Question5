import urllib
import urllib2
from bs4 import BeautifulSoup

__author__ = 'soroosh'


class Post:
    def __init__(self, id, name, url, views, category, description, specifications, download_links):
        self.download_links = download_links
        self.specifications = specifications
        self.description = description
        self.category = category
        self.views = views
        self.url = url
        self.name = name
        self.id = id


class Crawler:
    def _get_soup(self, url):
        response = urllib2.urlopen(urllib.quote(url, safe='/:').encode('utf-8'))
        html = response.read()
        soup = BeautifulSoup(html, from_encoding='utf8')
        print soup
        return soup
