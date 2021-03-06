from common import Crawler
import re

__author__ = 'soroosh'


class PostLinkCrawler(Crawler):
    def __init__(self, category_link):
        self.category_link = category_link
        self._soup = self._get_soup(self.category_link)

    def find_links(self, max=20):
        links = self._find_page_links(self._soup)
        other_existed_pages = self._find_pages()
        if len(other_existed_pages) > 0:
            for page in other_existed_pages:
                page_links = self._find_page_links(self._get_soup(page))
                for p in page_links:
                    if len(links) < max:
                        links.append(p)
                    else:
                        return links
        return links


    def _find_page_links(self, soup):
        try:
            posts = soup.find_all('article', {'class': 'post'})
            selected_links = filter(lambda x: not re.match('http://shop.*', x), map(lambda p: p.find('h1').find('a').get('href'), posts))
        except Exception as e:
            posts = soup.find_all('h3')
            selected_links = filter(lambda x: not re.match('http://shop.*', x), map(lambda p: p.find('a').get('href'), posts))
        return selected_links

    def _find_pages(self):
        """
        A heuristic for finding some first pages to find required posts
        :return:
        """
        pagination_container = self._soup.find('div', {'class': 'pagination'})
        if pagination_container is None:
            return []

        links =pagination_container.find_all('a')

        return map(lambda l: l.get('href'), links)


if __name__ == '__main__':
    crawler = PostLinkCrawler('http://p30download.com/fa/mobile/tag/lg')
    links = crawler.find_links(max=20)
    print(len(links))
    print links




