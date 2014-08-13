__author__ = 'soroosh'
import config

from pymongo import MongoClient

client = MongoClient(config.mongodb['host'], config.mongodb['port'])
db = client[config.mongodb['db']]
collection = db[config.mongodb['collection']]


def insert_product(p):
    p_dic = p.__dict__
    p_dic['_id'] = p_dic['id']
    del p_dic['id']
    collection.update({'_id': p_dic['_id']}, p_dic, True)

