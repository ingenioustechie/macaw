import logging
import redis

logging.getLogger('')
logging.basicConfig(filename='macaw.log',level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

log = logging 

redis = redis.StrictRedis(host='localhost', port=6379, db=2)

MAX_DEPTH=0

# make it False if you want to crawl other domain linked
ONLY_ROOTDOMAIN=True


DOMAINS='domains'
DOMAINS_WAIT='domains:wait'
DOMAINS_DONE='domains:done'

URLS='urls'
URLS_WAIT='urls:wait'
URLS_DONE='urls:done'

URLS_CRAWLLING='ulrs:crawlling'

