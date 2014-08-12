__author__ = 'soroosh'

import urllib
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen(urllib.quote('http://p30download.com/fa/entry/51105/', safe='/:').encode('utf-8'))
html = response.read()
soup = BeautifulSoup(html, from_encoding='utf8')

page_posts = soup.find_all('article', {'class': 'post'})
first_link = page_posts[0].find('h1').find('a')
print first_link.get('href')

# print(page_posts)
print 'Number of posts in this page: %s' % str(len(page_posts))
# first_link.get('href')
response = urllib2.urlopen(urllib.quote('http://p30download.com/fa/entry/51105/', safe='/:').encode('utf-8'))
html = response.read()
soup = BeautifulSoup(html, from_encoding='utf8')

page_post = soup.find('article')

header = page_post.header.h1.a.string
views = page_post.find('li', {'class': 'hit'})
url = first_link
category = reduce(lambda x, y: x + '/' + y, map(lambda a: a.string, page_post.find('li', {'class': 'cat'}).find_all('a')))
description = str(page_post.find('div', {'id': 'yiv2931868296yui_3_13_0_ym1_1_1389000431840_2408'}))
if description == 'None':
    description = str(page_post.find('p', {'itemprop': 'text'}))
dl_links = page_post.find('div', {'class': 'download-links'}).find_all('a')
print header
print views
print url
print category
print description
print dl_links
print len(dl_links)




