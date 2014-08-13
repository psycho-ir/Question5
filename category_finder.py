from random import choice
from common import Crawler

__author__ = 'soroosh'


class CategoryCrawler(Crawler):
    def __init__(self):
        self.base_url = 'http://p30download.com'
        self.appropriate_categories = []

    def find_all_groups(self):
        soup = self._get_soup()
        nav_wrapper = soup.find_all('div', {'id': 'nav-wrapper'})[0]
        menu_container = nav_wrapper.find_all('nav', {'class': 'clearfix'})[0]
        all_menus = menu_container.find_all('ul', {'class': 'clearfix'})[0]
        all_groups = all_menus.find_all('a')
        self.appropriate_categories = self._santize_groups(all_groups)


    def select_random_group(self):
        if len(self.appropriate_categories) == 0:
            self.find_all_groups()
        selected_group = choice(self.appropriate_categories)
        return selected_group

    def _santize_groups(self, groups):
        return groups




