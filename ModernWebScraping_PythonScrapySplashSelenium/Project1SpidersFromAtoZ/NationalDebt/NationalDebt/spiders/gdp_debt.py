# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            country_name = row.xpath(".//td[1]/a/text()").get()
            country_link = row.xpath(".//td[1]/a/@href").get()
            national_debt_to_GDP = row.xpath(".//td[2]/text()").get()
            
            yield {
                'country_name': country_name,
                'country_link': country_link,
                'national_debt_to_GDP': national_debt_to_GDP
            }