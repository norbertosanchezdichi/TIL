import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from find_all_links.spiders.contries import FindAllLinksSpider


process = CrawlerProcess(settings=get_project_settings())
process.crawl(FindAllLinksSpider)
process.start()