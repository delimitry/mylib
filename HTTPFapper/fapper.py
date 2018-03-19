import tornado
from tornado import gen, httpclient, queues
import logging

class Fapper:

    __slots__ = ['hand', 'concurrency', 'total', 'args']

    def __init__(self, *args, hand=None, concurrency=10, total=None):
        self.hand = hand or self.__default_hand
        self.concurrency = concurrency
        self.total = total
        self.args = args

    def fap(self):
        loop = tornado.ioloop.IOLoop.instance()
        loop.run_sync(self.__main)

    @gen.coroutine
    def __default_hand(self, url):
        try:
            response = yield httpclient.AsyncHTTPClient().fetch(url)
            print(response.body)
        except Exception as e:
            logging.exception(e)

    @gen.coroutine
    def __main(self):
        #q = queues.Queue(maxsize=self.concurrency)

        def worker():
            while True:
                yield hand_wrapper()

        def hand_wrapper():
            try:
                yield self.hand(*self.args)
            except Exception as e:
                logging.exception(e)


        for _ in range(self.concurrency):
            yield worker()


class Params:
    __slots__ = ['parameters']

    def __init__(self, parameters):
        import urllib
        self.parameters = urllib.parse.urlencode(parameters)

    def dispatch(self):
        return self.parameters
