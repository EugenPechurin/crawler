# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.item import Item, Field

class BrainItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    description = scrapy.Field()
    logo = scrapy.Field()
    teacher = scrapy.Field()
    pass

class BrainItemLoader(ItemLoader):  
    url = Field()
    title = Field()
    subtitle = Field()
    