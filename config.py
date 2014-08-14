__author__ = 'soroosh'

MONGODB = {'host': 'localhost',
           'port': 27017,
           'db': 'p30download',
           'collection': 'products'}

# It can be
# "sequential" When you want to crawl products sequentially ( kwargs is not important  and can be {}
# Example: POST_READING_STRATEGY = {'name': 'sequential', 'kwargs': {}}
# "multithread"
# Example: POST_READING_STRATEGY = {'name': 'multithread', 'kwargs': {'num_of_threads': 4}}
POST_READING_STRATEGY = {'name': 'multithread', 'kwargs': {'num_of_threads': 4}}

NUMBER_OF_PRODUCTS = 20

