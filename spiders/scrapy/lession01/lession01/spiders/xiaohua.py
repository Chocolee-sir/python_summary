# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request
from ..items import xiaohuaItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-0.html'] #循环url进行抓取

    def parse(self, response):
        print(response.url)
        page_info = Selector(response=response).xpath('//div[@class="page_num"]//a/@href').extract()
        img_info = Selector(response=response).xpath('//div[@id="list_img"]//a/img')
        for item in img_info:
            file_name = item.xpath('./@alt').extract_first()
            file_url = item.xpath('./@src').extract_first()
            if file_url.startswith('/d/file/'):
                file_url = 'http://www.xiaohuar.com%s' % (file_url)
            item_obj = xiaohuaItem(file_name=file_name, file_url=file_url)
            yield item_obj
        for url in page_info:
            yield Request(url=url, callback=self.parse)





