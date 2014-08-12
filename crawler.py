# -- coding: utf-8 --
import urllib
import urllib2
from bs4 import BeautifulSoup
from random import choice

__author__ = 'soroosh'


class P30DownloadCrawler:
    def __init__(self):
        self.base_url = 'http://p30download.com'
        self.all_groups = []

    def find_all_groups(self):
        soup = self._get_soup()
        nav_wrapper = soup.find_all('div', {'id': 'nav-wrapper'})[0]
        menu_container = nav_wrapper.find_all('nav', {'class': 'clearfix'})[0]
        all_menus = menu_container.find_all('ul', {'class': 'clearfix'})[0]
        self.all_groups = all_menus.find_all('a')

    def select_random_group(self):
        selected_group = choice(self.all_groups)
        return selected_group


    def _get_soup(self):
        response = urllib2.urlopen(urllib.quote(self.base_url, safe='/:').encode('utf-8'))
        html = response.read()
        soup = BeautifulSoup(html, from_encoding='utf8')
        return soup


c = P30DownloadCrawler()

c.find_all_groups()
print c.select_random_group()




