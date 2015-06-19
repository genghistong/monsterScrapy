from scrapy.spider import Spider
from scrapy.selector import Selector

from monster.items import MonsterItem


class MonsterSpider(Spider):
    name = "simply"
    allowed_domains = ["simplyhired.com"]
    start_urls = [
        "http://www.simplyhired.com/search?q=information+technology",
        "http://www.simplyhired.com/search?q=information+technology&pn=2",
        "http://www.simplyhired.com/search?q=information+technology&pn=3",
        "http://www.simplyhired.com/search?q=information+technology&pn=4",
        "http://www.simplyhired.com/search?q=information+technology&pn=5",
        "http://www.simplyhired.com/search?q=information+technology&pn=6",
        "http://www.simplyhired.com/search?q=information+technology&pn=7",
        "http://www.simplyhired.com/search?q=information+technology&pn=8",
        "http://www.simplyhired.com/search?q=information+technology&pn=9",
        "http://www.simplyhired.com/search?q=information+technology&pn=10",
        "http://www.simplyhired.com/search?q=information+technology&pn=11",
        "http://www.simplyhired.com/search?q=information+technology&pn=12",
        "http://www.simplyhired.com/search?q=information+technology&pn=13",
        "http://www.simplyhired.com/search?q=information+technology&pn=14",
        "http://www.simplyhired.com/search?q=information+technology&pn=15",
        "http://www.simplyhired.com/search?q=information+technology&pn=16",
        "http://www.simplyhired.com/search?q=information+technology&pn=17",
        "http://www.simplyhired.com/search?q=information+technology&pn=18",
        "http://www.simplyhired.com/search?q=information+technology&pn=19",

    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class = "results"]')
        items = []

        for site in sites.select('..//div[@class="job"]'):
            item = MonsterItem()
            item['title'] = site.xpath('.//a[@itemprop = "title"]/text()').extract()
            item['company'] = site.xpath('.//h4[@class = "company"]/text()').extract()
            item['city'] = site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()
            item['state'] = site.xpath('.//span[@itemprop = "addressRegion"]/text()').extract()
            item['description'] = site.xpath('.//p[@class = "description"]/text()').extract()
            if items not in items:    
                items.append(item)
            #limiting it to 100 does not work, maybe because it's counting
            #the length of the site loop which never exceeds 20?
            #if len(items) > 100:
            #    break
        return items
