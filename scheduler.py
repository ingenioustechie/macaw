from spider import Spider

class Scheduler(object):
    """
    Scheduler
    """
    def __init__(self):
        super(Scheduler, self).__init__()
        
    def crawl(self):
        """
        Crawls the url and returns all the respective urls in dict
        """
        url = self._get_url()
        links = Spider().get_links(url)

        return links

    def _get_url(self):
        """
        Get URLS from redis
        """
        return "https://www.github.com"