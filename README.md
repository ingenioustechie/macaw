# macaws
Yet another web crawler
  This is a very simple crawler, which can be run on multiple machines with sync. Crawl information is stored in the redis which is a dependancy. 
Once can define the MAX_DEPTH in utils.py file for crawling. 

Gets the HTML and parses the links and stores them.  
scheduler: Sends links and unparsed html to parser  
spider: Gets the data from internet and sends to parser   

