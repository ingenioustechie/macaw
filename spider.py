from parser import Parser
import requests
from utils import log

class Spider(object):
    """docstring for Spider"""
    def __init__(self):
        super(Spider, self).__init__()
    
    def get_links(self, url):
        """
        Get the links from url
        """
        if self._is_url(url):
            try:
                response = requests.get(url)

                if (response.status_code//100 == 2 and
                    self._is_html(response)):
                    status, links = Parser(url).parse_href(response.content)
                    print("Status ", status, links)
                    
            except Exception as e:
                print(str(e))
                log.error(str(e))

    def _is_html(self, response):
        """
        Checks if content is HTML based on Content Type 
        """
        return 'text/html' in response.headers.get("Content-Type")

    def _is_url(self, url):
        """
        Checks if a url is valid or not
        TODO: Add few regex
        """
        return url.startswith("https://") or url.startswith("http://")