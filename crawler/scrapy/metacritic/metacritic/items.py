# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class metacriticItem(scrapy.Item):
    # define the fields for your item here like:
    artist = scrapy.Field()
    album = scrapy.Field()
    metascore = scrapy.Field()
    userscore = scrapy.Field()
    release_date = scrapy.Field()
    pass
