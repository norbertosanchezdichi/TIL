# -*- coding: utf-8 -*-
import scrapy


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.en']
    start_urls = ['http://www.livecoin.en/']

    def parse(self, response):
        pass
