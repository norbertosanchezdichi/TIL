# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com.hk']
    start_urls = ['https://www.tinydeal.com.hk/specials.html']

    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discount_price': str(product.xpath(".//div[@class='p_box_price']/span[1]/text()").get()),
                'original_price': str(product.xpath(".//div[@class='p_box_price']/span[2]/text()").get())
            }