from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
from scrapy.selector import Selector


class BrokenItem(Item):
    url = Field()
    referer = Field()
    status = Field()


class BrokenLinksSpider(CrawlSpider):
    name = "github404"
    allowed_domains = ["github.com"]
    start_urls = ["https://www.github.de"]
    handle_httpstatus_list = [404]
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def parse_item(self, response):
        if response.status == 404:
            item = BrokenItem()
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')
            item['status'] = response.status

            return item
