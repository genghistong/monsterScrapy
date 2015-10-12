from scrapy.spider import Spider
from scrapy.selector import Selector

from monster.items import MonsterItem


class linkedinSpider(Spider):
    name = "linkedin"
    download_delay = 5
    allowed_domains = ["linkedin.com"]
    start_urls = [
        "https://www.linkedin.com/job/information-technology-jobs/",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=2&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=3&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=4&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=5&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=6&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=7&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=8&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=9&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=10&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=11&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=12&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=13&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=14&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=15&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=16&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=17&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=18&trk=jserp_pagination_next",
        # "https://www.linkedin.com/job/information-technology-jobs/?sort=date&page_num=19&trk=jserp_pagination_next",

    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="results-sort"]')
        items = []

        for site in sites.select('..//ul[@class="jobs"]'):
            item = MonsterItem()
            item['title'] = site.xpath('.//a[@itemprop = "title"]/text()').extract()
            item['company'] = site.xpath('.//div[@itemprop = "hiringOrganization"]/text()').extract()
            item['city'] = str(site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()).split(',')[0] + "']"
            item['state'] = "['" + str(site.xpath('.//span[@itemprop = "addressLocality"]/text()').extract()).split(', ')[1]
            item['description'] = site.xpath('.//p[@itemprop = "description"]/text()').extract()
            if item not in items:
                items.append(item)
            #limiting it to 100 does not work, maybe because it's counting
            #the length of the site loop which never exceeds 20?
            #if len(items) > 100:
            #    break
        return items
