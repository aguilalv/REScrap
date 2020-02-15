# -*- coding: utf-8 -*-
import scrapy


class IptestSpider(scrapy.Spider):
    name = 'iptest'
    allowed_domains = ['atomurl.net']
    start_urls = ['http://atomurl.net/myip/']

    def parse(self, response):
        ip = response.css("tr input::attr(value)").get()
        print(f"------------> {ip}")
