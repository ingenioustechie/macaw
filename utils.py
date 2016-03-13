import logging
import redis

logging.getLogger('')
logging.basicConfig(filename='macaw.log',level=logging.DEBUG, filemode="w")

log = logging 

redis = redis.StrictRedis(host='localhost', port=6379, db=20)