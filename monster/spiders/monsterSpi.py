from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import *
import sys

from monster.items import MonsterItem


class MonsterSpider(CrawlSpider):
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

    rules = (Rule(SgmlLinkExtractor(allow=("jobs.monster.com",))
         , callback = 'parse_items'),)

    def parse_items(self, response):
        # sel = Selector(response)
        # sites = sel.xpath('//div[@class="col-xs-12"]')
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="col-xs-12"]')
        #sites = hxs.select('//article[@class="js_result_row"]')

        items = []

        for site in sites.xpath('.//article[@class="js_result_row"]'):
            item = MonsterItem()
            item['title'] = site.xpath('.//span[@itemprop = "title"]/text()').extract()
            item['company'] = site.xpath('.//span[@itemprop = "name"]/text()').extract()
            item['city'] = site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()
            item['state'] = site.xpath('.//span[@itemprop = "addressRegion"]/text()').extract()
            item['link'] = site.xpath('.//a[@data-m_impr_a_placement_id="jsr"]/@href').extract()

            # error that comes up is that it needs a string not a list
            #url = item['link']
            #doing this shoots a valueerror "missing scheme in request url: %s'"
            url = ''.format(''.join(item['link']))
            yield Request(url = url, meta={'item':item}, callback = self.parse_item_page)

    def parse_item_page(self,response):
        hxs = HtmlXPathSelector(response)

        item = response.meta['item']
        item['description'] = hxs.select('//div[@itemprop = "description"]/text()').extract()
            #item['description'] = site.xpath('.//div[@class = "preview"]/text()').extract()
        # if item not in items:
        #     items.append(item)
        return item

