"""
Starting point for the module, It calls the scheduler which will fetch 
urls to be Crawlled from DB
"""

from scheduler import Scheduler


scheduler = Scheduler()

scheduler.crawl()
