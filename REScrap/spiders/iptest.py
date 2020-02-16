# -*- coding: utf-8 -*-
import scrapy
import re

class IptestSpider(scrapy.Spider):
    name = 'iptest'
    allowed_domains = ['atomurl.net']

    def __init__(self, iterations=None, *args, **kwargs):
        super(IptestSpider, self).__init__(*args, **kwargs)
        if iterations is not None:
            for i in range(0,int(iterations)):
                self.start_urls.append('http://atomurl.net/myip/')
        else:
            self.start_urls = ['http://atomurl.net/myip/']

    def parse(self, response):
        ip = response.css("tr input::attr(value)").get()
        
        ua_text = response.css("table")[1].css("tr")[2].css("td::text").get()
        ua = re.search('Your browser User Agent: (.*)', ua_text, re.IGNORECASE).group(1)

        yield {'ip':ip,'user_agent':ua}
