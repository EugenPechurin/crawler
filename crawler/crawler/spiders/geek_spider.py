import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import BrainItemLoader, BrainItem


class GeekSpider(CrawlSpider):
    name = 'geek_spider'
    allowed_domains = ['geekbrains.ru']
    start_urls = ['https://geekbrains.ru/courses']
    
    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="gb-profession-cards-grid__content js-gb-profession-cards-grid-content"]'
                                '//div[@class="gb-profession-cards-grid__item js-grid-item"]'],
                allow=r'https://geekbrains.ru/\w+/\w+$'
            ), 'parse_item'
        ),
    )
    
    def parse_item(self, response):
        selector = Selector(response)
        l = BrainItemLoader(BrainItem)
        l.add_value('url', response.url)