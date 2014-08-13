from random import choice
from common import Crawler

__author__ = 'soroosh'


class CategoryCrawler(Crawler):
    def __init__(self):
        self.base_url = 'http://p30download.com'
        self.appropriate_categories = []
        self._filtered_links = ['http://lic.p30download.com/',
                                'http://p30download.com/fa/game/page/game-troubleshooting.php']

    def find_all_groups(self):
        soup = self._get_soup(self.base_url)
        nav_wrapper = soup.find_all('div', {'id': 'nav-wrapper'})[0]
        menu_container = nav_wrapper.find_all('nav', {'class': 'clearfix'})[0]
        all_menus = menu_container.find_all('ul', {'class': 'clearfix'})[0]
        all_groups = map(lambda g: g.get('href'), all_menus.find_all('a'))
        self.appropriate_categories = self._santize_groups(all_groups)


    def select_random_group(self):
        if len(self.appropriate_categories) == 0:
            self.find_all_groups()
        selected_group = choice(self.appropriate_categories)
        return selected_group

    def _santize_groups(self, groups):
        filtered_groups = filter(lambda l: l not in self._filtered_links, groups)
        return filtered_groups





