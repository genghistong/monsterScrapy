from scrapy.spider import Spider
from scrapy.selector import Selector

from monster.items import MonsterItem


class MonsterSpider(Spider):
    name = "monster"
    allowed_domains = ["jobs.monster.com"]
    start_urls = [
        "http://jobs.monster.com/v-technology.aspx",
        "http://jobs.monster.com/v-technology.aspx?page=2",
        "http://jobs.monster.com/v-technology.aspx?page=3",
        "http://jobs.monster.com/v-technology.aspx?page=4",
        "http://jobs.monster.com/v-technology.aspx?page=5",
        "http://jobs.monster.com/v-technology.aspx?page=6",
        "http://jobs.monster.com/v-technology.aspx?page=7",
        "http://jobs.monster.com/v-technology.aspx?page=8",
        "http://jobs.monster.com/v-technology.aspx?page=9",
        "http://jobs.monster.com/v-technology.aspx?page=10"
    ]

    def parse(self, response):
        sel = Selector(response)
        #sites = sel.xpath('//section[@class="jobTitle"]')
        sites = sel.xpath('//div[@class="col-xs-12"]')
        #//div[@class="col-xs-12"]
        #sites = sel.xpath('//article[@class ="js_result_row"]')
        items = []

        for site in sites:
            item = MonsterItem()
            item ['title'] = site.xpath('//span[@itemprop="title"]/text()').extract()
            item['city'] = site.xpath('//span[@itemprop="addressLocality"]/text()').extract()
            item['state'] = site.xpath('//span[@itemprop="addressRegion"]/text()').extract()
            items.append(item)

        return items

    