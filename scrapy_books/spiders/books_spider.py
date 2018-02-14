# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy_books.items import BooksItem

class BooksSpider(scrapy.Spider):
    '''图书爬虫类'''
    # 这个name不能重复
    name = 'books'
    # allowed_domains = ['202.116.174.108:8080']
    start_urls = ["http://202.116.174.108:8080/top/top_lend.php?cls_no=ALL"]

    def parse(self, response):
        '''处理下载的response的默认方法'''
        books = []
        for item in response.xpath('//tr')[1:]:
            book = BooksItem()
            book_name = item.xpath('td[2]/a/text()').extract()
            book_author = item.xpath('td[3]/text()').extract()
            book_call_number = item.xpath('td[5]/text()').extract()
            book['name'] = book_name[0]
            book['author'] = book_author[0]
            book['call_number'] = book_call_number[0]
            books.append(book)
        return books
