# macaw
Yet another web crawler
  This is a very simple crawler, which can be run on multiple machines with sync. Crawl information is stored in the redis which is a dependancy. 
Once can define the MAX_DEPTH in utils.py file for crawling. 

### How to run 
1. Clone the repository  
2. Install dependency 
3. Fill the redis list KEY `domains` with urls. 

Redis's `ulrs:crawlling` will be having all the urls as base64 encoded as key and html as its value. 


### Testing 
`python tests.py && python macaw.py`
NB: This is not a good a way to test, need to add proper testing. 

## TODO:  
1. Add better testing.   
2. Add multi threading to make it faster.   
3. Add a word filtering, to select only desired links