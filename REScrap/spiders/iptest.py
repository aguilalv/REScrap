# -*- coding: utf-8 -*-
import scrapy
import re

class IptestSpider(scrapy.Spider):
    name = 'iptest'
    allowed_domains = ['atomurl.net']
    start_urls = ['http://atomurl.net/myip/']

    def parse(self, response):
        ip = response.css("tr input::attr(value)").get()
        
        ua_text = response.css("table")[1].css("tr")[2].css("td::text").get()
        ua = re.search('Your browser User Agent: (.*)', ua_text, re.IGNORECASE).group(1)

        print(f"------------> {ip}")
        print(f"------------> {ua}")
    
