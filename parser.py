from utils import redis
import lxml.html as lxl
import urlparse

class Parser(object):
    """docstring for Parser"""
    def __init__(self, url):
        super(Parser, self).__init__()
        self.base_url = url
      
    def parse_href(self, html):
        """
        Get all the Links from the HTML and return as unique list,
        it append base url if href have relative path
        """
        try: 
            tree = lxl.fromstring(html)
        except Exception as e:
            return False, str(e.msg)

        urls = set([])
        for a in tree.xpath('//a'):

            if not a.get('href', "").startswith("http"):
                link = self.base_url+a.get('href')
            else:
                link = a.get('href')
            
            # if it not valid link don't do anything
            if self._is_valid_link(link):
                urls.add(a.get('href')) 

        return True, urls


    def _is_valid_link(self, link):
        """
        Return True if given link is non document, Since this is not a perfect way to check
        but it avoids a call to server. 
        """

        # Need to add more
        DOC_EXT = [".pdf", ".xmls", ".docx", ".odt"]

         try:
            urlPath = [i for i in (urlparse.urlparse(link)[2].split('/')) if i]

            file_name = urlPath[-1]
            ext = file_name.split(".")[-1]
        except IndexError:
            # Its just a root URL
            return True
        return ext not in DOC_EXT
