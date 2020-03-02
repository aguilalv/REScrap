# -*- coding: utf-8 -*-
import scrapy


class IdealistaSpider(scrapy.Spider):
    name = 'idealista'
    #allowed_domains = ['idealista.com']
    start_urls = ['https://www.idealista.com/venta-viviendas/benicasimbenicassim/heliopolis-eurosol/']

#    def parse_list(self,response):


    def parse(self, response):
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
