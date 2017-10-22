# -*- coding: utf-8 -*-
import urlparse

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

from tut.items import TutItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python/407313?fr=aladdin']

    def parse(self, response):
        sel=Selector(response)
        sites=sel.xpath('//div[@class="para"]/a[contains(@href,"item")]')
        for sit in sites:
            item=TutItem()
            link=sit.xpath('@href').extract()
            if link[0]!=' ':
                link=urlparse.urljoin('https://baike.baidu.com/item/Python/407313?fr=aladdin',link[0])
            text = sit.xpath('text()').extract_first()
            item['link']=link
            item['text']=text
            if text!=' ':
                yield item
               # yield Request(link,callback=self.parse)



