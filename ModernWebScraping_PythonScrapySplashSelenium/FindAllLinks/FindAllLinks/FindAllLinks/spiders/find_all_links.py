# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class FindAllLinksSpider(scrapy.Spider):
    name = 'find_all_links'
    allowed_domains = ['www.maximintegrated.com']
    
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
        yield SplashRequest(url='https://www.maximintegrated.com', callback=self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        links = response.xpath('//a')
        
        for link in links:
            link_text = link.xpath('.//text()').get()
            if not link_text:
                continue
            link_url = link.xpath('.//@href').get()
            
            yield {
                    'link_text': link_text,
                    'link_url': link_url,#response.urljoin(link_url),
                    'parent_url': response.url,
                    'HTTP status code': response.status
            }
            
        
# if link_text has valid text (using regex. [a-zA-z\d]+)