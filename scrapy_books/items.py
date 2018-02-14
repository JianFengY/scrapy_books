# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BooksItem(scrapy.Item):
    '''定义要存储的字段'''
    # 书名
    name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 索引号
    call_number = scrapy.Field()
