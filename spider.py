from parser import Parser
from  urllib.parse import urlparse
import requests
from utils import log, MAX_DEPTH

class Spider(object):
    """docstring for Spider"""
    def __init__(self):
        super(Spider, self).__init__()
        self.crawl_depth_counter = 0
    
    def get_links(self, url, page_depth=0):
        """
        Get the links from url
        """
        if self._is_url(url) and page_depth <= MAX_DEPTH:
            try:
                response = requests.get(url)

                if (response.status_code//100 == 2 and
                    self._is_html(response)):
                    status, links = Parser(self._base_url(url)).parse_href(response.content)

                    print(page_depth, status, links)
                    for link in links:
                        self.get_links(link, page_depth+1)

            except Exception as e:
                log.error(str(e))
                raise

    def _is_html(self, response):
        """
        Checks if content is HTML based on Content Type 
        """
        return 'text/html' in response.headers.get("Content-Type", "")

    def _is_url(self, url):
        """
        Checks if a url is valid or not
        TODO: Add few regex
        """
        return url.startswith("https://") or url.startswith("http://")

    def _base_url(self, url):
        url_path = urlparse(url)
        return url_path[0]+'://'+url_path[1]