# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class WeeklyAddressItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    mp4_url = Field()
    mp3_url = Field()
    date = Field()
    transcribe = Field()

