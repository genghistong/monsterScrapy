# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class MonsterItem(scrapy.Item):

	title =  scrapy.Field()
	company = scrapy.Field()
	city = scrapy.Field()
	state = scrapy.Field()
	link = scrapy.Field()
	description = scrapy.Field()