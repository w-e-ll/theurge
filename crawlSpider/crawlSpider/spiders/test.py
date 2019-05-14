# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawlSpider.items import CrawlspiderItem


class TestSpider(CrawlSpider):
    """Theurge.com product spider with 2 rules and 6 items"""
    name = 'test'
    allowed_domains = ['theurge.com']
    start_urls = ['https://theurge.com/en-au/']

    rules = (
        # traverse from theurge.com through to the category pages
        Rule(LinkExtractor(
            allow=(r'cat=\w+')),
            follow=True),
        # yield the products found on the product pages.
        Rule(LinkExtractor(
            allow='/product/',
            allow_domains=('theurge.com')),
            callback='parse_product'),
    )

    def parse_product(self, response):
        """Getting all required product data"""
        item = CrawlspiderItem()
        item['ProductName'] = response.xpath('//h1[@class="oF0RP"]/span[@class="YkPyN"]/text()')[-1].extract()
        item['Brand'] = response.xpath('//h1[@class="oF0RP"]/span/text()').extract_first()
        item['Category'] = response.xpath('//div[@class="_2KICV"]/ol/li/a/span/text()').extract()
        item['Imagelinks'] = response.xpath('//ul/li/picture[@class="_1qrmV"]/img/@srcset').extract()
        item['Price'] = response.xpath('//span[@class="_2_9Ep"]/text()').extract()
        item['SalePrice'] = response.xpath('//span[@class="_2CNhD"]/text()').extract()
        yield item
