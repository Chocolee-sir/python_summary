#!/usr/bin/env python
__author__ = 'Chocolee'


import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        # v = self.get_argument('p')
        # print(v)
        # self.request 封装了所有用户的请求

        # 5.获取用户请求相关信息
        # self.get_cookie()
        # v = self.get_argument('p')
        # print(v)
        # self.request 封装了用户发来的所有请求
        # print(type(self.request))
        # from tornado.httputil import HTTPServerRequest

        # 6. 额外相应内容
        # self.set_cookie('k1','v1')
        # self.set_header('h1','v1')


        # 4. 返回页面+模板引擎
        self.render('login.html', **{'k1': 'v1', 'k2': [1,2,3], 'k3':{'name':'root', 'age':18}})

        # 7. 重定向
        #self.redirect()

    def post(self, *args, **kwargs):
        v = self.get_argument('user')
        print(v)
        self.redirect('http://www.baidu.com')

# 8. 配置
settings = {
    'static_path': 'static',
    'static_url_prefix': '/sss/',
    'template_path': 'templates',

}

# 1. 生成路由规则
application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/login", LoginHandler),

], **settings,)


if __name__ == "__main__":
    # 2.创建socket对象8888
    # 将socket对象添加到select或epoll中
    application.listen(8888)
    # 3.将select或epoll开始死循环
    tornado.ioloop.IOLoop.instance().start()