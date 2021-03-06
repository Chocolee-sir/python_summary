# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.http import Request
from scrapy.http.cookies import CookieJar


class ChoutiSpider(scrapy.Spider):
    name = "chouti"
    allowed_domains = ["chouti.com"]
    start_urls = (
        'http://www.chouti.com/',
    )

    def start_requests(self):
        url = 'http://dig.chouti.com/'
        yield Request(url=url, callback=self.login, meta={'cookiejar': True})

    def login(self, response):
        print(response.headers.getlist('Set-Cookie'))
        req = Request(
            url='http://dig.chouti.com/login',
            method='POST',
            headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            body='phone=8615110111879&password=lyl890625&oneMonth=1',
            callback=self.check_login,
            meta={'cookiejar': True}
        )
        yield req

    def check_login(self, response):
        print(response.text)

