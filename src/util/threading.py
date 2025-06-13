from src import *
from src.util.logger import logger
from src.util.other import other
from curl_cffi import exceptions as curl_exceptions
from curl_cffi.curl import CurlError

class threading:
    def __init__(self, func, tokens=[], args=[], delay=0):
        self.log = logger(module='Threading')
        self.func = func
        self.tokens = tokens
        self.args = args
        self.delay = delay
        self.work()

    def work(self):
        try:
            threads = []
            for token in self.tokens:
                other.delay(self.delay)
                thread: threadinglib.Thread = threadinglib.Thread(target=self.func, args=(token, *self.args))
                threads.append(thread)
                thread.start()
            
            for thread in threads:
                thread.join()

        except CurlError as e:
            self.log.error(e)

        except curl_exceptions.ConnectionError as e:
            self.log.error(e)

        except curl_exceptions.HTTPError as e:
            self.log.error(e)

        except curl_exceptions.ReadTimeout as e:
            self.log.error(e)

        except curl_exceptions.Timeout as e:
            self.log.error(e)

        except curl_exceptions.TooManyRedirects as e:
            self.log.error(e)

        except curl_exceptions.RequestException as e:
            self.log.error(e)

        except Exception as e:
            self.log.error(e)