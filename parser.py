from utils import redis, ONLY_ROOTDOMAIN, log
import lxml.html as lxl
from  urllib.parse import urlparse
from tld import get_tld

# from tld.utils import update_tld_names
# update_tld_names()


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

            # continue if href starts with # as its anchor linking
            if (a.get('href', "").startswith("#")
                or a.get('href', "").lower().startswith("mailto")):
                continue
            
            if (not a.get('href', "").startswith("http")):
                link = self.base_url+a.get('href', "")
            else:
                link = a.get('href')
            
            # if it not valid link don't do anything
            if self._is_valid_link(link):
                urls.add(link) 

        return True, urls


    def _is_valid_link(self, link):
        """
        Return True if given link is non document, Since this is not a perfect way to check
        but it avoids a call to server. 
        """

        # Check ONLY_ROOTDOMAIN

        scheme, netloc, path, params, query, fragment = urlparse(link)

        try:
            if get_tld(self.base_url) == get_tld(link) and not ONLY_ROOTDOMAIN:
            # if get_tld(self.base_url) == get_tld(link):
                return False
        except Exception as e:
            log.error(str(e), self.base_url, link)


        # Need to add more
        DOC_EXT = [".pdf", ".xmls", ".docx", ".odt"]

        try:

            urlPath = [i for i in (path.split('/')) if i]

            file_name = urlPath[-1]
            ext = file_name.split(".")[-1]
        except IndexError:
            # Its just a root URL
            return True
        return ext not in DOC_EXT
