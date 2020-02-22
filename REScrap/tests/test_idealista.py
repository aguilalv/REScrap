"""
Tests for idealista spider

List of tests in the module
- xxx
"""

import pytest
import requests
import betamax
from betamax_serializers import pretty_json

from scrapy import Request
from scrapy.http import HtmlResponse

from REScrap.spiders.idealista import IdealistaSpider


CASSETTE_LIBRARY_DIR = 'REScrap/tests/cassettes/'

def test_follows_to_next_page_when_exists():
    url = 'https://www.idealista.com/venta-viviendas/benicasimbenicassim/heliopolis-eurosol/'
    spider = IdealistaSpider()

    session = requests.Session()

    betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)
    recorder = betamax.Betamax(
        session, cassette_library_dir=CASSETTE_LIBRARY_DIR
    )

    with recorder.use_cassette('test_idealista'):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
#            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#            'Accept-Encoding': 'none',
#            'Accept-Language': 'en-US,en;q=0.8',
#            'Connection': 'keep-alive',
        }
        response = session.get(url, headers=headers)

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

