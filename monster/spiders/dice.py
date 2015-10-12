from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from monster.items import MonsterItem
from scrapy.selector import *
import re

class DiceSpider(Spider):
    name = "dice"
    allowed_domains = ["dice.com"]
    base_url = "https://www.dice.com/jobs/sort-date-startPage-"
    end_url = "-limit-100-jobs"
    start_urls = [
        "https://www.dice.com/jobs/sort-date-startPage-1-limit-100-jobs"
        ]

    for i in range(1,5):
        start_urls.append(base_url + str(i) + end_url)

    rules = (Rule(SgmlLinkExtractor(allow=("dice.com",))
         , callback = 'parse'),)

    def parse(self, response):
         
        postings = response.xpath('.//div[@class="serp-result-content"]')
        for i in range(0, len(postings)-1):
            item = MonsterItem()
            item['title'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]", "", str(postings[i].xpath('.//h3/a[@class = "dice-btn-link"]/text()').extract()))
            item['link'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]", "", str(postings[i].xpath('.//h3/a[@class = "dice-btn-link"]/@href').extract()))
            item['company'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]", "", str(postings[i].xpath('.//li[@class = "employer"]/a[@class = "dice-btn-link"]/text()').extract()))
            item['city'] = re.sub(r"\\t|\\n|u'|'|\[|\]", "", str(postings[i].xpath('.//li[@class = "location"]/text()').extract()).split(',')[0])
            item['state'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]", "", str(postings[i].xpath('.//li[@class = "location"]/text()').extract()).split(', ')[1])
            follow = ''.join(item['link'])
            request = Request(follow, callback = self.parse_dir_contents)
            request.meta["item"] =  item
            yield request

    def parse_dir_contents(self, response):
        item = response.meta["item"]
        #desc = response.xpath('.//div[@id = "jobdescSec"]')
        # for p in desc.xpath('.//br'):
        #     p.extract()
        item['description'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]|\\xa0|[^\x00-\x7F]+", "", str(response.xpath('.//div[@id = "jobdescSec"]//text()').extract())).strip()
        #item['description'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]", "", str(response.xpath('.//div[@id = "jobdescSec"]//text()').extract()))
        return item