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
        "http://jobs.monster.com/v-technology.aspx?page=10",
        "http://jobs.monster.com/v-technology.aspx?page=11",
        "http://jobs.monster.com/v-technology.aspx?page=12",
        "http://jobs.monster.com/v-technology.aspx?page=13",
        "http://jobs.monster.com/v-technology.aspx?page=14",
        "http://jobs.monster.com/v-technology.aspx?page=15",
        "http://jobs.monster.com/v-technology.aspx?page=16",
        "http://jobs.monster.com/v-technology.aspx?page=17",
        "http://jobs.monster.com/v-technology.aspx?page=18",
        "http://jobs.monster.com/v-technology.aspx?page=19"

    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="col-xs-12"]')
        items = []

        for site in sites.select('..//article[@class="js_result_row"]'):
            item = MonsterItem()
            item['title'] = site.xpath('.//span[@itemprop = "title"]/text()').extract()
            item['company'] = site.xpath('.//span[@itemprop = "name"]/text()').extract()
            item['city'] = site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()
            item['state'] = site.xpath('.//span[@itemprop = "addressRegion"]/text()').extract()
            if item not in items:
                items.append(item)
            #limiting it to 100 does not work, maybe because it's counting
            #the length of the site loop which never exceeds 20?
            #if len(items) > 100:
            #    break
        return items
