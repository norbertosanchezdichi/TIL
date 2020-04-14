# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.geekbuying.com/deals']
    start_urls = ['http://www.geekbuying.com/deals/']

    def parse(self, response):
        pass
