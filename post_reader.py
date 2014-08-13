# -*- coding: utf-8 -*-
from common import Crawler

__author__ = 'soroosh'

class PostCrawler(Crawler):
    def get_post(self, url):
        post_soup = self._get_soup(url)
        header = post_soup.header.h1.a.string
        print header
        views = post_soup.find('li', {'class': 'hit'})
        category = reduce(lambda x, y: x + '/' + y, map(lambda a: a.string, post_soup.find('li', {'class': 'cat'}).find_all('a')))
        description = str(post_soup.find('div', {'id': 'yiv2931868296yui_3_13_0_ym1_1_1389000431840_2408'}))
        if description == 'None':
            description = str(post_soup.find('p', {'itemprop': 'text'}))

        dl_links = post_soup.find('div', {'class': 'download-links'}).find_all('a')
        titles = post_soup.find('div', {'class': 'extra-info'}).find_all('strong')
        for t in titles:
            print {t: t.next_sibling.next_sibling.string}

        pass




c = PostCrawler()
c.get_post('http://p30download.com/fa/entry/39455/')



