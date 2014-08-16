# -*- coding: utf-8 -*-
__author__ = 'soroosh'
import strategies
from category_finder import CategoryCrawler
from links_finder import PostLinkCrawler
from repository import insert_product
from Queue import Queue, Empty
from config import POST_READING_STRATEGY,NUMBER_OF_PRODUCTS
import logging

logging.basicConfig(level=logging.INFO)

category_crawler = CategoryCrawler()
selected_category_link = category_crawler.select_random_group()
logging.info('Category:%s selected for crawling' % selected_category_link)
post_link_crawler = PostLinkCrawler(selected_category_link)
selected_links = post_link_crawler.find_links(max=NUMBER_OF_PRODUCTS)
in_queue = Queue()

logging.info('These posts selected: ')
for l in selected_links:
    print l
    in_queue.put(l)

logging.info('Fetching post details...')
out_queue = strategies.strategies[POST_READING_STRATEGY['name']](in_queue, **POST_READING_STRATEGY['kwargs'])
logging.info('%s Posts created' % out_queue.qsize())

try:
    for p in iter(out_queue.get_nowait, None):
        insert_product(p)
except Empty as e:
    pass

logging.info('All posts persisted')


