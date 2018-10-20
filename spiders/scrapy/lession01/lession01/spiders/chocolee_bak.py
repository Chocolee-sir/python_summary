# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request
# from ..items import ChocoleeItem


class ChocoleeSpider(scrapy.Spider):
    name = 'chocolee111'
    allowed_domains = ['chocolee.cn']
    start_urls = ['http://www.chocolee.cn/']

    def parse(self, response):
        # print(response.url)
        # 找到文档所有的A标签
        # hxs = Selector(response=response).xpath('//a')
        # 对象转字符串
        # hxs = Selector(response=response).xpath('//div[@id="container-inner"]/div[#id="primary"]').extract()

        # 标签对象列表
        # hxs = Selector(response=response).xpath('//div[@id="container-inner"]/div[@id="primary"]')
        # for obj in hxs:
        #     a = obj.xpath('.//h2/a/text()').extract()
        #     for i in a:
        #         print(i.strip())

        # 选择器：
        """
        //   表示子孙中
        .//  当前对象的子孙中
        /    儿子
        /div 儿子中的div标签
        /div[@id="i1"]  儿子中的div标签且id=i1
        /div[@id="i1"]  儿子中的div标签且id=i1
        obj.extract()         # 列表中的每一个对象转换字符串 =》 []
        obj.extract_first()   # 列表中的每一个对象转换字符串 => 列表第一个元素
        //div/text()    获取某个标签的文本
       """

       # 获取当前页所有的标题和URL
        hxs1 = Selector(response=response).xpath('//div[@id="container-inner"]/div[@id="primary"]')
        for obj in hxs1:
            title = obj.xpath('.//h2/a/text()').extract_first().strip()
            herf = obj.xpath('.//h2/a/@href').extract_first().strip()
            item_obj = ChocoleeItem(title=title, href=herf)

            # 将item对象传递给pipeline
            yield item_obj


       # 获取页面的所有页码
        hxs2 = Selector(response=response).xpath('//div[@class="pagenavi"]//a/@href').extract()
        for url in hxs2:
            yield Request(url=url, callback=self.parse)

        # a/@href  获取属性
        # //a[starts-with(@href, "/all/hot/recent/")]/@href'  已xx开始
        # //a[re:test(@href, "/all/hot/recent/\d+")]          正则
        # yield Request(url=url,callback=self.parse)          # 将新要访问的url添加到调度器
        # 重写start_requests，指定最开始处理请求的方法



    