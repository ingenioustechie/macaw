import logging
import redis

logging.getLogger('')
logging.basicConfig(filename='macaw.log',level=logging.DEBUG, filemode="w")

log = logging 

redis = redis.StrictRedis(host='localhost', port=6379, db=20)

MAX_DEPTH=2

# make it False if you want to crawl other domain linked
ONLY_ROOTDOMAIN=True