import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import BrainItemLoader, BrainItem


class GeekSpider(CrawlSpider):
    name = 'geek_spider'
    
    start_url = ['https://geekbrains.ru/courses']
    allowed_domains = ['geekbrains.ru']
    
    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="gb-profession-cards-grid__content js-gb-profession-cards-grid-content"]'
                                '//div[@class="gb-profession-cards-grid__item js-grid-item"]'],
                allow=r'geekbrains.ru/\w+/\w+$'
            ),
            callback='parse_item'
        ),
    )
    
    def parse_item(self, response):
        selector = Selector(response)
        l = BrainItemLoader(BrainItem)
        l.add_value('url', response.url)