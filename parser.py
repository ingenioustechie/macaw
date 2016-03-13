from utils import redis
import lxml.html as lxl

class Parser(object):
    """docstring for Parser"""
    def __init__(self, url):
        super(Parser, self).__init__()
        self.url = url
      
    def parse_href(self, html):
        """
        Get all the Links from the HTML and return as unique list
        """
        try: 
            tree = lxl.fromstring(html)
        except Exception as e:
            return False, str(e.msg)

        urls = set([])
        for a in tree.xpath('//a'):

            if not a.get('href', "").startswith("http"):
                urls.add(self.url+a.get('href'))
            else:
                urls.add(a.get('href'))

        return True, urls
