from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import *
import sys
from monster.items import MonsterItem


class indeedSpider(Spider):
    name = "indeed"
    allowed_domains = ["indeed.com"]
    start_urls = [
        "http://www.indeed.com/q-technology-jobs.html",
        "http://www.indeed.com/jobs?q=technology&start=10",
        "http://www.indeed.com/jobs?q=technology&start=20",
        "http://www.indeed.com/jobs?q=technology&start=30",
        "http://www.indeed.com/jobs?q=technology&start=40",
        "http://www.indeed.com/jobs?q=technology&start=50",
        "http://www.indeed.com/jobs?q=technology&start=60",
        "http://www.indeed.com/jobs?q=technology&start=70",
        "http://www.indeed.com/jobs?q=technology&start=80",
        "http://www.indeed.com/jobs?q=technology&start=90",
        "http://www.indeed.com/jobs?q=technology&start=100",
        "http://www.indeed.com/jobs?q=technology&start=110",
        "http://www.indeed.com/jobs?q=technology&start=120",
        "http://www.indeed.com/jobs?q=technology&start=130",
        "http://www.indeed.com/jobs?q=technology&start=140",
        "http://www.indeed.com/jobs?q=technology&start=150",
        "http://www.indeed.com/jobs?q=technology&start=160",
        "http://www.indeed.com/jobs?q=technology&start=170",
        "http://www.indeed.com/jobs?q=technology&start=180"

    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="  row  result"]')
        items = []

        for site in sites:
            item = MonsterItem()
            item['title'] = site.xpath('.//a[@itemprop = "title"]/text()').extract()
            item['company'] = site.xpath('.//span[@class = "company"]//span[@itemprop = "name"]/text()').extract()
            item['city'] = str(site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()).split(',')[0] + "']"
            item['state'] = "['" + str(site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()).split(', ')[1]
            item['description'] = site.xpath('.//span[@class = "summary"]/text()').extract()
            if item not in items:
                items.append(item)
            #limiting it to 100 does not work, maybe because it's counting
            #the length of the site loop which never exceeds 20?
            #if len(items) > 100:
            #    break
        return items


