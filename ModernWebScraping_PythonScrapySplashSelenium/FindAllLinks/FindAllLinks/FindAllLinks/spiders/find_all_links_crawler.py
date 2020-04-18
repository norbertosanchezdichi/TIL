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
        Rule(LinkExtractor(restrict_xpaths='//a'), callback='parse_item', follow=True, process_request='use_splash'),
    )
    
    def use_splash(self, request):
        request.meta.update(splash={
          'args': {
              'wait': 1,
          },
          'endpoint': 'render.html',           
        })
        return request
    
    def start_requests(self):
        url = 'https://www.maximintegrated.com/en'
        yield SplashRequest(url=url, callback=self.parse_m, endpoint='execute', dont_filter=True,args={
                'url': url, 'lua_source': self.script
            })

    def _requests_to_follow(self, response):
        if not isinstance(response, (HtmlResponse, SplashJsonResponse, SplashTextResponse)):
            return
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
        yield {
            'link_url': response.url,
            'link_title': response.xpath('//title/text()').get(),
            'HTTP status code': response.status
        }
            
            
#yield scrapy.Request("http://localhost:8050/render.html?url=" + page_url, self.parse_page)