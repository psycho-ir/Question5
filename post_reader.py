# -*- coding: utf-8 -*-
from common import Crawler, Post
import re

__author__ = 'soroosh'


class PostCrawler(Crawler):
    def __init__(self):
        self._excluded_dl_links = [
            'http://p30download.com/fa/game/page/game-troubleshooting.php',
            'http://forum.p30download.com/',
            'http://shop.p30download.com/.*']

    def _not_in_excelude_links(self, link):
        for exc_link in self._excluded_dl_links:
            print 'comparing %s with %s' % (exc_link,link)
            if re.match(exc_link, link):
                return False
        return True

    def get_post(self, url):
        post_soup = self._get_soup(url)
        header = post_soup.header.h1.a.string
        views = re.match('.*UserVisits:([0-9]+).*', str(post_soup.find('li', {'class': 'hit'})).replace(',', '')).group(
            1)
        id = re.match('.*/([0-9]+)/.*', url).group(1)

        category = reduce(lambda x, y: x + '/' + y,
                          map(lambda a: a.string, post_soup.find('li', {'class': 'cat'}).find_all('a')))
        description = str(post_soup.find('div', {'id': 'yiv2931868296yui_3_13_0_ym1_1_1389000431840_2408'}))
        if description == 'None':
            description = str(post_soup.find('p', {'itemprop': 'text'}))

        dl_links = filter(lambda l: self._not_in_excelude_links(l), map(lambda l: l.get('href'), post_soup.find('div', {
        'class': 'download-links'}).find_all('a')))

        titles = post_soup.find('div', {'class': 'extra-info'}).find_all('strong')
        spec = []
        for t in titles:
            sibling = t.next_sibling.next_sibling
            if sibling.name == 'br':
                sibling = sibling.previous_sibling.string.strip()
            elif sibling.name == 'span':
                sibling = sibling.span.string.strip()
            elif not sibling.name == 'img':
                sibling = sibling.string.strip()

            spec.append({t.string: unicode(sibling)})

        return Post(id, header, url, views, category, description, spec, dl_links)


if __name__ == '__main__':
    c = PostCrawler()
    p = c.get_post('http://p30download.com/fa/entry/39455/')
    print p



