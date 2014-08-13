from common import Crawler

__author__ = 'soroosh'


class PostLinkCrawler(Crawler):
    def __init__(self, category_link):
        self.category_link = category_link

    def find_links(self, max=20):
        pass

