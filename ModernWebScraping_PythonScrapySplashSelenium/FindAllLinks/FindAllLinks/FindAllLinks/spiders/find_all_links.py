# -*- coding: utf-8 -*-
import scrapy


class FindAllLinksSpider(scrapy.Spider):
    name = 'find_all_links'
    allowed_domains = ['www.maximintegrated.com']
    start_urls = ['http://www.maximintegrated.com/']

    def parse(self, response):
        pass
