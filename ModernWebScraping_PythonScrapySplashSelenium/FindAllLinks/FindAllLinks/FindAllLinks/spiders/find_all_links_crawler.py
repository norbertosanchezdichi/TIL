# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest


class FindAllLinksCrawlerSpider(CrawlSpider):
    name = 'find_all_links_crawler'
    allowed_domains = ['www.maximintegrated.com/en']
    
    script = '''
        function main(splash, args)
      
            splash.private_mode_enabled = false
          
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
          
            return splash:html()
        end
    '''
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a'), callback='parse_item', follow=True),
    )
    
    def start_requests(self):
        yield SplashRequest(url='https://www.maximintegrated.com/en', callback=self.parse_item, endpoint='execute', args={'lua_source': self.script})

    def parse_item(self, response):
            yield {
                'link_url': response.url,
                'link_title': response.xpath('//title/text()').get(),
                'HTTP status code': response.status
            }