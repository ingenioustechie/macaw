from spider import Spider
from utils import redis, DOMAINS, DOMAINS_WAIT, DOMAINS_DONE

class Scheduler(object):
    """
    Gets  the root url from redis and sends them to spider for crawling
    """
    def __init__(self):
        super(Scheduler, self).__init__()
        
    def crawl(self):
        """
        Crawls the url and returns all the respective urls in dict
        """

        while redis.lrange(DOMAINS, 0,0):
            url = self._get_url()
            print(url)
            if url:
                Spider().get_links(url)
            else:
                print("No domains to crawl", "Seed the domains in redis")

            self._clearWaiting(url)

    def _get_url(self):
        """
        Get URLS from redis
        """
        domain = redis.brpoplpush(DOMAINS, DOMAINS_WAIT)

        return domain.decode("utf-8") if domain else False

    def _clearWaiting(self, url):
        """ Clears waiting """        
        redis.lrem(DOMAINS_WAIT, -1, url)