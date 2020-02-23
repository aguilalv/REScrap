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

@pytest.mark.usefixtures('betamax_session')
def test_follows_to_next_page_when_exists(betamax_session):
    url = 'https://www.idealista.com/venta-viviendas/benicasimbenicassim/heliopolis-eurosol/'
    spider = IdealistaSpider()

    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    }
    response = betamax_session.get(url, headers=headers)
    scrapy_response = HtmlResponse(body=response.content, url=url)
    results = spider.parse(scrapy_response)

    for result in results:
        if isinstance(result,Request):
            print(f'---> result.url - {result.url}')
            assert result.url == url+'pagina-2.htm'
            return

    pytest.fail('Did not return request to next page')

@pytest.mark.skip
def test_does_xxx_when_not_exists():
    pass

