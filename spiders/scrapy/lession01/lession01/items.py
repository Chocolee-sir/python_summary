# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChocoleeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()

class xiaohuaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_name = scrapy.Field()
    file_url = scrapy.Field()

class nbimgItem(scrapy.Item):
    img_src = scrapy.Field()
