__author__ = 'soroosh'
from Queue import Queue, Empty
from threading import Thread, current_thread
from post_reader import PostCrawler
import logging

def read_sequentially(in_q, **kwargs):
    post_crawler = PostCrawler()
    out_q = Queue()
    try:
        for l in iter(in_q.get_nowait, None):
            p = post_crawler.get_post(l)
            out_q.put(p)
            logging.info('Post: %s created' % l)
    except Empty as e:
        pass

    return out_q


def read_multithread(in_q, **kwargs):
    num_of_threads = kwargs.get('num_of_threads', 2)

    def _get_post(crawler, in_q, out_q):
        try:
            for l in iter(in_q.get_nowait, None):
                p = crawler.get_post(l)
                out_q.put(p)
                logging.info('Post: %s created with thread:%s' % (l, current_thread().getName()))
        except Empty as e:
            pass

    post_crawler = PostCrawler()
    out_q = Queue()
    threads = [Thread(target=_get_post, args=(post_crawler, in_q, out_q), name='T-' + str(i)) for i in range(num_of_threads)]
    map(lambda t: t.start(), threads)
    map(lambda t: t.join(), threads)
    return out_q


strategies = {'sequential': read_sequentially,
              'multithread': read_multithread}










