# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request,FormRequest
from scrapy.http.cookies import CookieJar
from fake_useragent import UserAgent


class ChocoleeSpider(scrapy.Spider):
    name = 'chocolee'
    allowed_domains = ['chocolee.cn']
    start_urls = ['http://www.chocolee.cn/']

    def parse(self, response):
        ua = UserAgent()
        header = {'User-Agent': ua.random}
        url = 'http://www.chocolee.cn/'
        yield Request(url=url, callback=self.login, meta={'cookiejar': True}, headers=header)

    def login(self, response):
        cookie_obj = CookieJar()
        cookie_obj.extract_cookies(response, response.request)
        self.cookie_dict = cookie_obj._cookies
        print(self.cookie_dict)

        req = FormRequest(
            url="http://www.chocolee.cn/wp-login.php",
            formdata={'log':'leesir', 'pwd':'Lyl890625!', 'submit':'登录', 'redirect_to':'http://www.chocolee.cn/wp-admin/', 'testcookie': '1'},
            callback=self.check_login,
            cookies=cookie_obj._cookies,
        )
        yield req

    def check_login(self,response):
        print(response.text)
        # yield Request(url="http://www.chocolee.cn/wp-admin/",callback=self.good)

    def good(self,response):
        print(response.text)
        # id_list = Selector(response=response).xpath('//div[@share-linkid]/@share-linkid').extract()
        # for nid in id_list:
        #     print(nid)
        #     url = "http://dig.chouti.com/link/vote?linksId=%s" % nid
        #     yield Request(
        #         url=url,
        #         method="POST",
        #         cookies=self.cookie_dict,
        #         callback=self.show
        #     )



