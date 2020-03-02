"""
Tests for idealista spider

List of tests in the module
- xxx
"""

import pytest
import requests
import betamax

from scrapy import Request
from scrapy.http import HtmlResponse

from REScrap.spiders.idealista import IdealistaSpider

CASSETTE_LIBRARY_DIR = 'REScrap/tests/cassettes/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} 

@pytest.mark.usefixtures('betamax_session')
def test_creates_request_for_next_page_when_present(betamax_session):
    url = 'https://www.idealista.com/venta-viviendas/benicasimbenicassim/heliopolis-eurosol/'
    spider = IdealistaSpider()

    response = betamax_session.get(url, headers=HEADERS)
    scrapy_response = HtmlResponse(body=response.content, url=url)
    results = spider.parse(scrapy_response)

    for result in results:
        if isinstance(result,Request):
            assert result.url == url+'pagina-2.htm'
            return

    pytest.fail('Did not return request to next page')

@pytest.mark.usefixtures('betamax_session')
def test_uses_parse_for_next_page(betamax_session):
    url = 'https://www.idealista.com/venta-viviendas/benicasimbenicassim/heliopolis-eurosol/'
    spider = IdealistaSpider()

    response = betamax_session.get(url, headers=HEADERS)
    scrapy_response = HtmlResponse(body=response.content, url=url)
    results = spider.parse(scrapy_response)

    for result in results:
        if isinstance(result,Request):
            assert result.callback == spider.parse 
            return

    pytest.fail('Did not return request to next page')

#@pytest.mark.skip
@pytest.mark.usefixtures('betamax_session')
def test_does_not_create_request_in_last_page(betamax_session):
    url = 'https://www.idealista.com/venta-viviendas/benicasimbenicassim/heliopolis-eurosol/pagina-7.htm'

    spider = IdealistaSpider()

    response = betamax_session.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception()

    scrapy_response = HtmlResponse(body=response.content, url=url)
    results = spider.parse(scrapy_response)

    for result in results:
        assert not isinstance(result,Request)

