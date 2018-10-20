# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests, uuid

class Lession01Pipeline(object):

    def __init__(self, conn_str):
        self.conn_str = conn_str

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        conn_str = crawler.settings.get('DB')
        return cls(conn_str)

    def open_spider(self,spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        # self.conn = open(self.conn_str, 'a')
        # print('000000')
        pass

    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        # self.conn.close()
        # print('111111')
        pass

    def process_item(self, item, spider):

        """每当数据需要持久化时，就会被调用"""

        if spider.name == 'chocolee':
            tpl = "%s\n%s\n\n" %(item['title'], item['href'])
            f = open('chocolee.json', 'a')
            f.write(tpl)
            f.close()

        if spider.name == 'xiaohua':
            img = requests.get(item['file_url'], stream=True)
            if img.status_code == 200:
                f = open('./xiaohua/%s.jpg' %(item['file_name']), 'wb')
                for chunk in img:
                    f.write(chunk)
                f.close()
            else:
                return False

        if spider.name == 'nbimg':
            img = requests.get(item['img_src'], stream=True)
            if img.status_code == 200:
                f = open('./NBimg/%s.jpg' %(uuid.uuid4()), 'wb')
                for chunk in img:
                    f.write(chunk)
                f.close()


        # 交给下一个pipeline处理
        # return item
        # 丢弃item，不交给
        # raise DropItem()
