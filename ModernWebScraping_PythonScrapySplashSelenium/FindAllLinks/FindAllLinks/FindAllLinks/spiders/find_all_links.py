# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class FindAllLinksSpider(scrapy.Spider):
    name = 'find_all_links'
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
    
    def start_requests(self):
        yield SplashRequest(url='https://www.maximintegrated.com/en', callback=self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        origin_url = response.url
        links = response.xpath('//a')
        links_dictionary = {}
        
        for link in links:
            link_url = response.urljoin(link.xpath('.//@href').get())
            
            if link.xpath('.//img').get():
                link_text = link.xpath('.//img/@alt').get()
            else:
                link_text = link.xpath('.//text()').get()
                
            links_dictionary[link_url] = link_text
                
        for link_url, link_text in links_dictionary:
        
            yield SplashRequest(url=link_url, endpoint='execute', args={'lua_source': self.script})
        
            yield {
                'link_text': link_text,
                'link_url': link_url,
                'link_title': response.xpath('//title/text()').get(),
                'HTTP status code': response.status,
                'origin_url': origin_url
            }