# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlspiderItem(scrapy.Item):
    # Product Items (Required fields)
    ProductName = scrapy.Field()
    Brand = scrapy.Field()
    Category = scrapy.Field()
    Imagelinks = scrapy.Field()
    Price = scrapy.Field()
    SalePrice = scrapy.Field()
