#__author:  Administrator
#date:  2017/3/10

import config
import tornado.web



class BaseHandler(object):
    def initialize(self):
        # 获取用户cookie，如果有，不操作，否则，给用户生成随即字符串
        # - 写给用户
        # - 保存在session
        from tro_session import Session
        cls = getattr(session, config.session_key)
        self.session = cls(self)
        super(BaseHandler,self).initialize()

class IndexHandler(BaseHandler, tornado.web.RequestHandler):

    def get(self):
        if self.session['is_login']:
            self.write("Hello, world")
        else:
            self.redirect('/login')


class LoginHandler(BaseHandler, tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('login.html')
    def post(self, *args, **kwargs):
        v = self.get_argument('user')
        if v == 'root':
            self.session['is_login'] = True
            self.redirect('/index')
        else:
            self.redirect('/login')

settings = {
    'static_path': 'static',
    'static_url_prefix': '/sss/',
    'template_path':'templates',
}
application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/login", LoginHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()