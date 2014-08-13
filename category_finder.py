from random import choice
from common import Crawler

__author__ = 'soroosh'


class CategoryCrawler(Crawler):
    def __init__(self):
        self.base_url = 'http://p30download.com'
        self.appropriate_categories = []
        #These links are not suitable for crawling, In fact they are not category!
        self._filtered_links = ['http://lic.p30download.com/',
                                'http://p30download.com/fa/game/page/game-troubleshooting.php',
                                'http://lic.p30download.com/',
                                'http://www.chargechi.com/topup/',
                                'http://forum.p30download.com/forumdisplay.php?54',
                                'http://forum.p30download.com/forumdisplay.php?56',
                                'http://forum.p30download.com/forumdisplay.php?196',
                                'http://forum.p30download.com/forumdisplay.php?193',
                                'http://forum.p30download.com/forumdisplay.php?132',
                                'http://forum.p30download.com/forumdisplay.php?232',
                                'http://p30download.com/fa/main/category/site-news/',
                                'http://p30download.com/fa/main/top-download.php',
                                'http://p30download.com/fa/main/recommend-download.php',
                                'http://p30download.com/update/mcafee/',
                                'http://p30download.com/update/avg/',
                                'http://p30download.com/update/kaspersky/',
                                'http://p30download.com/update/kaspersky-key/',
                                'http://p30download.com/update/norton/',
                                'http://p30download.com/update/avira/',
                                'http://p30download.com/update/bitdefender/',
                                'http://p30download.com/update/avast/',
                                'http://p30download.com/update/pc-cillin/',
                                'http://p30download.com/update/sophos/',
                                'http://p30download.com/update/calm/',
                                'http://p30download.com/update/command/',
                                'http://p30download.com/update/f-secure/',
                                'http://www.chargechi.com/',
                                'http://p30download.com/fa/mobile/page/how-to-install-android-app-game.php',
                                'http://p30download.com/fa/mobile/page/qr-code-androzip-help.php',
                                'http://p30download.com/fa/mobile/page/mobile-graphic-microprocessor-type.php',
                                'http://p30download.com/fa/mobile/page/how-to-install-ios-ipa-app-game.php',
                                'http://p30download.com/fa/mobile/page/how-to-create-apple-id.php']

    def find_all_groups(self):
        """
            finds all categories and after sanitizing links will set approprite_categories field
        :return: None
        """
        soup = self._get_soup(self.base_url)
        nav_wrapper = soup.find_all('div', {'id': 'nav-wrapper'})[0]
        menu_container = nav_wrapper.find_all('nav', {'class': 'clearfix'})[0]
        all_menus = menu_container.find_all('ul', {'class': 'clearfix'})[0]
        all_groups = map(lambda g: g.get('href'), all_menus.find_all('a'))
        self.appropriate_categories = self._santize_groups(all_groups)


    def select_random_group(self):
        """
            return a rondom category link from existed appropriate category links
        :return:
        """
        if len(self.appropriate_categories) == 0:
            self.find_all_groups()
        selected_group = choice(self.appropriate_categories)
        return selected_group

    def _santize_groups(self, groups):
        filtered_groups = filter(lambda l: l not in self._filtered_links, groups)
        return filtered_groups





