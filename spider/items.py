# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# -*- coding: utf-8 -*-


class bookItem(scrapy.Item):
    bd = scrapy.Field()
    itm_text = scrapy.Field()
    item = scrapy.Field()
    itm_href = scrapy.Field()
    title = scrapy.Field()
    zj = scrapy.Field()
    zs = scrapy.Field()
    # province = scrapy.Field()
    # category = scrapy.Field()
    # score = scrapy.Field()
