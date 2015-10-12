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
    allowed_domains = ["monster.com"]
    base_url = "http://jobs.monster.com/v-technology.aspx?"
    start_urls = [
        "http://jobs.monster.com/v-technology.aspx"
        # ,
        # "http://jobs.monster.com/v-technology.aspx?page=2",
        # "http://jobs.monster.com/v-technology.aspx?page=3",
        # "http://jobs.monster.com/v-technology.aspx?page=4",
        # "http://jobs.monster.com/v-technology.aspx?page=5",
        # "http://jobs.monster.com/v-technology.aspx?page=6",
        # "http://jobs.monster.com/v-technology.aspx?page=7",
        # "http://jobs.monster.com/v-technology.aspx?page=8",
        # "http://jobs.monster.com/v-technology.aspx?page=9",
        # "http://jobs.monster.com/v-technology.aspx?page=10",
        # "http://jobs.monster.com/v-technology.aspx?page=11",
        # "http://jobs.monster.com/v-technology.aspx?page=12",
        # "http://jobs.monster.com/v-technology.aspx?page=13",
        # "http://jobs.monster.com/v-technology.aspx?page=14",
        # "http://jobs.monster.com/v-technology.aspx?page=15",
        # "http://jobs.monster.com/v-technology.aspx?page=16",
        # "http://jobs.monster.com/v-technology.aspx?page=17",
        # "http://jobs.monster.com/v-technology.aspx?page=18",
        # "http://jobs.monster.com/v-technology.aspx?page=19"

    ]
    for i in range(1,5):
        start_urls.append(base_url + "page=" + str(i))

    rules = (Rule(SgmlLinkExtractor(allow=("monster.com",))
         , callback = 'parse_items'),)

    def parse_items(self, response):
        # sel = Selector(response)
        # sites = sel.xpath('//div[@class="col-xs-12"]')

        items = []

        # for site in sites.xpath('.//article[@class="js_result_row"]'):

        postings = response.xpath('.//article[@class="js_result_row"]')
        for i in range(0, len(postings)-1):
            item = MonsterItem()
## sites loop

            # item['title'] = site.xpath('.//span[@itemprop = "title"]/text()').extract()
            # item['company'] = site.xpath('.//span[@itemprop = "name"]/text()').extract()
            # #item['city'] = site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()
            # item['city'] = site.xpath('.//span[@itemprop = "jobLocation"]/text()').extract()
            # item['state'] = site.xpath('.//span[@itemprop = "addressRegion"]/text()').extract()
            # item['link'] = site.xpath('.//a[@data-m_impr_a_placement_id= "jsr"]/@href').extract()
            # follow = ''.join(item["link"])
            # request = Request(follow, callback = self.parse_dir_contents)
            # request.meta["item"] =  item
            # yield request

##postings loop
            item['title'] = postings[i].xpath('.//span[@itemprop = "title"]/text()').extract()
            item['company'] = postings[i].xpath('.//span[@itemprop = "name"]/text()').extract()
            item['city'] = postings[i].xpath('.//span[@itemprop = "address"]/text()').extract()
            #item['city'] = postings[i].xpath('.//span[@itemprop = "jobLocation"]/text()').extract()
            #item['state'] = postings[i].xpath('.//span[@itemprop = "addressRegion"]/text()').extract()
            item['link'] = postings[i].xpath('.//a[@data-m_impr_a_placement_id= "jsr"]/@href').extract()
            follow = ''.join(item["link"])
            request = Request(follow, callback = self.parse_dir_contents)
            request.meta["item"] =  item
            yield request
            # items.append(item)
            # return items

    def parse_dir_contents(self, response):
        item = response.meta["item"]
        item['description'] = response.xpath('.//div[@class = "job-details"]/text()').extract()
        return item