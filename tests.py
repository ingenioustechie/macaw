import unittest
from utils import *
class TestCrawlMethods(unittest.TestCase):

    def test_domain(self):
        self.assertEqual('foo'.upper(), 'FOO')


def populate_domain():
    """
    Added to test crawlling 
    """

    redis.delete(DOMAINS)
    redis.delete(DOMAINS_WAIT)
    redis.delete(DOMAINS_DONE)
    redis.delete(URLS)
    redis.delete(URLS_WAIT)
    redis.delete(URLS_DONE)
    redis.delete(URLS_CRAWLLING)

    d = ["https://www.github.com", "https://www.google.com"]
    redis.lpush(DOMAINS, *d)


if __name__ == '__main__':
    populate_domain()
    # unittest.main()