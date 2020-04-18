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
        yield SplashRequest(url='https://www.maximintegrated.com/en', callback=self.parse_page, endpoint='execute', args={'lua_source': self.script})

    def parse_page(self, response):
        origin_url = response.url
        links = response.xpath('//a')
        links_dictionary = {}
        
        for link in links:
            link_relative_url = link.xpath('.//@href').get()
            link_text = link.xpath('.//text()').get()
            
            if not link_text:
                link_text = link.xpath('.//img/@alt').get()
            if not link_text:
                link_text = link.xpath('.//img/@title').get()

            links_dictionary[link_relative_url] = link_text
                
        for link_relative_url, link_text in links_dictionary.items():
            link_absolute_url = response.urljoin(link_relative_url)
            
            try:
                yield SplashRequest(url=link_absolute_url, endpoint='execute', args={'lua_source': self.script})
                link_title = response.xpath('//title/text()').get()
                link_http_status = response.status
            except:
                link_title = ''
                link_http_status = ''
                
            yield {
                'link_text': link_text,
                'link_relative_url': link_relative_url,
                'link_absolute_url': link_absolute_url,
                'link_title': link_title,
                'HTTP status code': link_http_status,
                'origin_url': origin_url
            }