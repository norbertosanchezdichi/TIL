# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.geekbuying.com']
    start_urls = ['https://www.geekbuying.com/deals']

    def parse(self, response):
        products = response.xpath("//div[@class='category_li']")
        for product in products:
            product_name = product.xpath(".//a[@class='category_li_link']/text()").get()
            product_url = product.xpath(".//a[@class='category_li_link']/@href").get()
            product_price = product.xpath(".//div[@class='category_li_price']/span/text()").get()
            promotion_ends = product.xpath(".//div[@class='category_li_claibg']/span/text()").get()
            
        yield {
            'name': product_name,
            'url': product_url,
            'price': product_price,
            'promotion': promotion_ends
        }