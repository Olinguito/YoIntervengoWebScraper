# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LocationItem(scrapy.Item):
    deparment = scrapy.Field()
    cities = scrapy.Field()
    address = scrapy.Field()

class PublicWorkItem(scrapy.Item):
    organization = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    process = scrapy.Field()
    location = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()


