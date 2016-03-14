# macaws
Yet another web crawler
  This is a very simple crawler, which can be run on multiple machines with sync. Crawl information is stored in the redis which is a dependancy. 
Once can define the MAX_DEPTH in utils.py file for crawling. 

To run and test 

`python tests.py && python macaw.py`

TODO: 
1. Add better testing. 
2. Add multi threading to make it faster. 


