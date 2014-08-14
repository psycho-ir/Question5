__author__ = 'soroosh'
import config

from pymongo import MongoClient

client = MongoClient(config.MONGODB['host'], config.MONGODB['port'])
db = client[config.MONGODB['db']]
collection = db[config.MONGODB['collection']]


def insert_product(p):
    p_dic = p.__dict__
    p_dic['_id'] = p_dic['id']
    del p_dic['id']
    collection.update({'_id': p_dic['_id']}, p_dic, True)

