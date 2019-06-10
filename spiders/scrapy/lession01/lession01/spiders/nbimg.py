# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request
from ..items import nbimgItem


class NbimgSpider(scrapy.Spider):
    name = 'nbimg'
    allowed_domains = ['97ccb.pw']
    start_urls = ['http://xxxx']

    def parse(self, response):
        #print(response.url)
        url_list = Selector(response=response).xpath('//h3/a')
        for href in url_list:
            url = href.xpath('./@href').extract_first()
            url = 'http://339.97ccb.pw/pw/%s' %url
            yield Request(url=url, callback=self.get_img)

    def get_img(self, response):
        print(response.url)
        img_list = Selector(response=response).xpath('//div[@id="read_tpc"]/img')
        for img in img_list:
            img_src = img.xpath('./@src').extract_first()
            item_obj = nbimgItem(img_src=img_src)
            yield item_obj




