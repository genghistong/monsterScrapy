from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from monster.items import MonsterItem
from scrapy.selector import *
import re


class simplySpider(Spider):
    name = "simply"
    allowed_domains = ["simplyhired.com"]
    end_url = "&pn="
    base_url = "http://www.simplyhired.com/search?q=information+technology"
    start_urls = [
        "http://www.simplyhired.com/search?q=information+technology"
    ]

    for i in range(1,5):
        start_urls.append(base_url + end_url + str(i))

    rules = (Rule(SgmlLinkExtractor(allow=("simplyhired.com",))
         , callback = 'parse'),)

    def parse(self, response):

        postings = response.xpath('.//div[@class="job"]')
        for i in range(0, len(postings)-1):
            item = MonsterItem()
            item['title'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]", "", str(postings[i].xpath('.//a[@itemprop = "title"]/text()').extract())).strip()
            item['company'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]", "", str(postings[i].xpath('.//a[@class = "company"]/text()').extract()))
            item['city'] = postings[i].xpath('.//span[@itemprop = "addressLocality"]/text()').extract()
            item['state'] = postings[i].xpath('.//span[@itemprop = "addressRegion"]/text()').extract()
            item['link'] = postings[i].xpath('.//div[@class = "tools"]/a[@rel = "nofollow"]/@href').extract()
            follow = ''.join(item['link'])
            request = Request(follow, callback = self.parse_dir_contents)
            request.meta["item"] =  item
            yield request


        # for site in sites.select('..//div[@class="job"]'):
        #     item = MonsterItem()
        #     item['title'] = site.xpath('.//a[@itemprop = "title"]/text()').extract()
        #     item['company'] = site.xpath('.//h4[@class = "company"]/text()').extract()
        #     item['city'] = site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()
        #     item['state'] = site.xpath('.//span[@itemprop = "addressRegion"]/text()').extract()
        #     item['description'] = site.xpath('.//p[@class = "description"]/text()').extract()
        #     if items not in items:    
        #         items.append(item)
        #     #limiting it to 100 does not work, maybe because it's counting
        #     #the length of the site loop which never exceeds 20?
        #     #if len(items) > 100:
        #     #    break
        # return items

    def parse_dir_contents(self, response):
        item = response.meta["item"]
        item['description'] = re.sub(r"\\t|\\n|,|u'|'|\[|\]|\\xa0|[^\x00-\x7F]+", "", str(response.xpath('.//div[@class = "job-description"]//text()').extract())).strip()
        return item