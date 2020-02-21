import pytest

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import json

## CAREFUL!!! - The test overwrites the pipelines configuration!! ##

### IS IT BETTER TO HAVE A FIXTURE RUN THE CRAWLING AND STORING IN A VARIABLE THE RESULTS THAT I AM INSTERESTED IN (e.g. User Agent) AND THEN USE TEST METHODS TO JUST CHECK THAT VARIABLE?

## Consider mocking requests or using betamax and looking at the request objec to avoid depending on the network

NUMBER_REQUESTS = 5
user_agents = []

class UASpider(scrapy.Spider):
    name = 'uaspider'
    
    start_urls = []
    for i in range(0,NUMBER_REQUESTS):
        start_urls.append('http://httpbin.org/user-agent')

    def parse(self, response):
        payload = json.loads(response.body.decode(response.encoding))
        yield {'ua':payload}

class TempStoragePipeline(object):

    def process_item(self, item, spider):
        user_agents.append(item.get('ua').get('user-agent'))
        return item

def runCrawler():
    settings = get_project_settings()
    
    o = TempStoragePipeline()
    module = o.__class__.__module__
    if module is None or module == str.__class__.__module__:
        pipeline_module = f'{o.__class__.__name__}'  # Avoid reporting __builtin__
    else:
        pipeline_module = f'{module}.{o.__class__.__name__}'    
    

    settings.set('ITEM_PIPELINES', {
        pipeline_module: 100
    })

    process = CrawlerProcess(settings)
    process.crawl(UASpider)
    process.start() # the script will block here until the crawling is finished

def test_user_agent_changes():
    runCrawler()
    # DELETE FOR/PRINT ONCE CHECKED THAT THE CODE MAKES THE TEST PASS
    for agent in user_agents:
        print(f'>>>>>> {agent}')
    assert len(user_agents) == len(set(user_agents))
