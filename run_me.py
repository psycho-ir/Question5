# -*- coding: utf-8 -*-
__author__ = 'soroosh'
from category_finder import CategoryCrawler
from links_finder import PostLinkCrawler
from persistence import insert_product
from post_reader import PostCrawler

category_crawler = CategoryCrawler()
selected_category_link = category_crawler.select_random_group()
print 'Category:%s selected for crawling' % selected_category_link
post_link_crawler = PostLinkCrawler(selected_category_link)
selected_links = post_link_crawler.find_links(max=1)
print 'These posts selected: '
for l in selected_links:
    print l

print 'Fetching post details...'

post_crawler = PostCrawler()
result = []

for l in selected_links:
    print 'Fetching post: %s' % l
    post_crawler = PostCrawler()
    p = post_crawler.get_post(l)
    print(p.__dict__)
    result.append(p)
    print 'Post: %s created' % l

print '%s Posts created' % len(result)

for p in result:
    insert_product(p)


