# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meijutt.items import MeijuttItem
class MeijuSpider(CrawlSpider):
    name = 'meiju'
    start_urls = ['http://www.meijutt.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.meijutt.com/file/list.*?html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MeijuttItem()
        item['name'] = response.xpath('//a[@class="B font_16"]/@title').extract()
        yield item
