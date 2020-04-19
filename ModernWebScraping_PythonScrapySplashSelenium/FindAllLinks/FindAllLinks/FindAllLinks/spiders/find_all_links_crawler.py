# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest


class FindAllLinksCrawlerSpider(CrawlSpider):
    name = 'find_all_links_crawler'
    allowed_domains = ['www.maximintegrated.com/en']
    links= {}
    links_crawled = []
    
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
        Rule(LinkExtractor(restrict_xpaths='//a'), callback='parse_item', follow=True, process_request='use_splash'),
    )
    
    def use_splash(self, request):
        request.meta.update(splash={
          'args': {
              'lua_source': self.script,
          },
          'endpoint': 'execute',           
        })
        return request
    
    def start_requests(self):
        url = 'https://www.maximintegrated.com/en'
        #yield SplashRequest(url=url, callback=self.parse_item, endpoint='execute', dont_filter=True,args={'url': url, 'lua_source': self.script})
        
        yield scrapy.Request(url=url, callback=self.parse_item, meta={'splash': {'args': {'lua_source': self.script}}})

    def _requests_to_follow(self, response):
        #if not isinstance(response, (HtmlResponse, SplashJsonResponse, SplashTextResponse)):
        #   return
        seen = set()
        for n, rule in enumerate(self._rules):
            links = [lnk for lnk in rule.link_extractor.extract_links(response)
                     if lnk not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = self._build_request(n, link)
                yield rule.process_request(r)

    def _build_request(self, rule, link):
        r = SplashRequest(url=link.url, callback=self._response_downloaded, meta={'rule': rule, 'link_text': link.text},
                          args={'url': link.url, 'lua_source': self.script})
        r.meta.update(rule=rule, link_text=link.text)
        return r
            
    def parse_item(self, response):
        origin_url = response.url
        links = response.xpath('//a')
        
        for link in links:
            link_relative_url = link.xpath('.//@href').get()
            link_text = link.xpath('.//text()').get()
            
            if not link_text:
                link_text = link.xpath('.//img/@alt').get()
            if not link_text:
                link_text = link.xpath('.//img/@title').get()

            self.links[link_relative_url] = link_text
                
        for link_relative_url, link_text in self.links.items():
            link_absolute_url = response.urljoin(link_relative_url)
            
            if link_absolute_url not in self.links_crawled:
                self.links_crawled.append(link_absolute_url)
                try:
                    yield scrapy.Request(url=url, callback=self.parse_item, meta={'splash': {'args': {'lua_source': self.script}}})
                    #yield SplashRequest(url=link_absolute_url, callback=self.parse_item, endpoint='execute', args={'lua_source': self.script})
                    link_title = response.xpath('//title/text()').get()
                    link_http_status = response.status
                except:
                    link_title = ''
                    link_http_status = ''
            else:
                continue
                
            yield {
                'link_text': link_text,
                'link_relative_url': link_relative_url,
                'link_absolute_url': link_absolute_url,
                'link_title': link_title,
                'HTTP status code': link_http_status,
                'origin_url': origin_url
            }
            
        print(f"links_crawled length: {len(self.links_crawled)}")