# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlspiderPipeline(object):
    """Processing product items one by one"""
    def process_item(self, item, spider):
        if item['ProductName']:
            # Product Name [Titlecase]
            item['ProductName'] = item['ProductName'].title()
        if item['Brand']:
            # Brand [Uppercase]
            item['Brand'] = item['Brand'].upper()
        if item['Category']:
            # Category [Separate categories by >> ]
            item['Category'] = ' >> '.join(item['Category'])
        if item['Imagelinks']:
            # Image links [ These should be the largest size images you are able to obtain]
            img_links = []
            for i in item['Imagelinks']:
                urls = i.split(',')
                url = urls[-1].replace(' 1.5x', '')
                img_links.append(url)
            item['Imagelinks'] = img_links
        if item['Price']:
            # Price [Remove '$' and return in decimals i.e $99.95 should be returned as 9995 ]
            price = item['Price'][-1]
            if '.' in price:
                price = price.replace('.', '')
            item['Price'] = price
        if item['SalePrice']:
            # Sale Price [If available, remove '$' and return in decimals i.e $99.95 should be returned as 9995 ]
            sale_price = item['SalePrice'][-1]
            if '.' in sale_price:
                sale_price = sale_price.replace('.', '')
            item['SalePrice'] = sale_price

        return item
