# -*- coding: utf-8 -*-
__author__ = 'soroosh'
from common import Post

import config
import re

from pymongo import MongoClient

client = MongoClient(config.MONGODB['host'], config.MONGODB['port'])
db = client[config.MONGODB['db']]
collection = db[config.MONGODB['collection']]


def insert_product(p):
    p_dic = p.__dict__
    p_dic['_id'] = p_dic['id']
    del p_dic['id']
    collection.update({'_id': p_dic['_id']}, p_dic, True)


def find(keyword):
    find_result = []
    regex = re.compile('.*%s.*' % keyword)
    for p in collection.find({'$or': [{'url': {'$regex': regex}},
                                      {'category': {'$regex': regex}},
                                      {'description': {'$regex': regex}},
                                      {'name': {'$regex': regex}}]}):
        find_result.append(Post(p['_id'], p['name'], p['url'], p['views'], p['category'], p['description'], p['specifications'], p['download_links']))

    return find_result


if __name__ == '__main__':
    result = find('موب')
    print len(result)
    result = find('چ')
    print len(result)


