import unittest
from utils import redis, DOMAINS, DOMAINS_WAIT, DOMAINS_DONE

class TestCrawlMethods(unittest.TestCase):

    def test_domain(self):
        self.assertEqual('foo'.upper(), 'FOO')


def populate_domain():
    d = ["https://www.github.com"]
    redis.lpush(DOMAINS, *d)

if __name__ == '__main__':
    populate_domain()
    # unittest.main()