# Web Scraping Trial task for the urge:

Theurge.com product spider with 2 rules and 6 items

### Task:

1. Build a Scrapy spider by making use of the 'crawlSpider'.
2. Use rules to traverse from theurge.com through to the category pages, and then yield the products found on the product pages.
3. Make good use of the scrapy 'Item Loader' to create items from the page.
4. Use processors to clean some of the data fields.
4. Make use of the Scrapy settings to limit the number of items crawled to 100.

### Required fields:

- Product Name [Titlecase]
- Brand [Uppercase]
- Category [Separate categories by >> ]
- Image links [ These should be the largest size images you are able to obtain]
- Price [Remove '$' and return in decimals i.e $99.95 should be returned as 9995 ]
- Sale Price [If available, remove '$' and return in decimals i.e $99.95 should be returned as 9995 ]

### Dependencies

- Python3
- Scrapy

### Make Initial Setup

1. virtualenv -p python3 test_task
2. cd test_task
3. activate it (source bin/activate)
4. git clone https://github.com/w-e-ll/theurge.git
5. cd theurge
6. pip install -r requirements.txt
7. cd crawlSpider
8. scrapy crawl test

made by: https://w-e-ll.com
