# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com.hk']
    start_urls = ['https://www.tinydeal.com.hk/specials.html']

    def parse(self, response):
        pass
