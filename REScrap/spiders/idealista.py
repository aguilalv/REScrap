# -*- coding: utf-8 -*-
import scrapy


class IdealistaSpider(scrapy.Spider):
    name = 'idealista'
    allowed_domains = ['https://www.idealista.com/venta-viviendas/benicasimbenicassim/heliopolis-eurosol/']
    start_urls = ['http://https://www.idealista.com/venta-viviendas/benicasimbenicassim/heliopolis-eurosol//']

    def parse(self, response):
        pass
