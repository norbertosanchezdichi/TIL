# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest


class FindAllLinksCrawlerSpider(CrawlSpider):
    name = 'find_all_links_crawler'
    allowed_domains = ['www.maximintegrated.com']
    start_urls = ['http://www.maximintegrated.com/']
    
    script = '''
        function main(splash, args)
      
            splash.private_mode_enabled = false
          
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
          
            return splash:html()
        end
    '''
    
    link_counter = 0

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a'), callback='parse_item', follow=True),
    )
    
    def start_requests(self):
        yield SplashRequest(url='https://www.maximintegrated.com', callback=self.parse_item, endpoint='execute', args={'lua_source': self.script})

    def parse_item(self, response):
        links = response.xpath('//a')
        origin_url = response.url
        for link in links:
            self.link_counter += 1
            if self.link_counter > 500:
                break
            
            if link.xpath('.//img').get():
                link_text = link.xpath('.//img/@alt').get()
            else:
                link_text = link.xpath('.//text()').get()
            
            link_url = response.urljoin(link.xpath('.//@href').get())
            
            yield SplashRequest(url=link_url, callback=self.parse_item, endpoint='execute', args={'lua_source': self.script})
            
            yield {
                'link_text': link_text,
                'link_url': link_url,
                'link_title': response.xpath('//title/text()').get(),
                'HTTP status code': response.status,
                'origin_url': origin_url
            }