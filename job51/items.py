# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    company_name = scrapy.Field()
    income = scrapy.Field()
    experience = scrapy.Field()
    diploma = scrapy.Field()
    need_num = scrapy.Field()
    post_time = scrapy.Field()
    welfare = scrapy.Field()
    job_msg = scrapy.Field()