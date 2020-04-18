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
    
    link_counter = 0

    def start_requests(self):
        yield SplashRequest(url='https://www.maximintegrated.com', callback=self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        links = response.xpath('//a')
        origin_url = response.url
        for link in links:
            self.link_counter += 1
            if self.link_counter > 1000:
                break
            
            if link.xpath('.//img').get():
                link_text = link.xpath('.//img/@alt').get()
            else:
                link_text = link.xpath('.//text()').get()
            
            link_url = response.urljoin(link.xpath('.//@href').get())
            if "javascript" not in link_url:
                yield SplashRequest(url=link_url, callback=self.parse, endpoint='execute', args={'lua_source': self.script})
            else:
                continue
            
            yield {
                'link_text': link_text,
                'link_url': link_url,
                'link_title': response.xpath('//title/text()').get(),
                'HTTP status code': response.status,
                'origin_url': origin_url
            }    
        
# if link_text has valid text (using regex. [a-zA-z\d]+)