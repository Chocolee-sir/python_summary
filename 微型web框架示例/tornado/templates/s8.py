#__author:  Administrator
#date:  2017/3/10

import tornado.web
import re
class StringField:
    def __init__(self,name):
        self.rex = "^\w+$"
        self.name = name
        self.value = ''
        self.error = ""

    def __str__(self):
        return "<input type='text' name='%s' value='%s' />" %(self.name,self.value,)
class EmailField:
    def __init__(self,name):
        self.rex = "^\w+@.*$"
        self.name = name
        self.value = ''
        self.error = ""
    def __str__(self):
        return "<input type='text' name='%s' value='%s' />" %(self.name,self.value,)

class LoginForm:
    def __init__(self):
        self.user = StringField(name='user')
        self.email = EmailField(name='email')

    def is_valid(self,handler):
        value_dict = {}
        flag = True
        for k,v in self.__dict__.items():
            inp = handler.get_argument(k)
            # 1: k=user,  inp='asdf'  v ="\w+" => StringField(name='user')
            # 1: k=email,  inp='asdfasdf'  v ="^\w+@.*$" => EmailField(name='email')
            rex = re.match(v.rex,inp)
            v.value = inp
            if rex:
                value_dict[k] = inp
            else:
                v.error = '%s 错误了..' %k
                flag = False
        return flag,value_dict

class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        obj = LoginForm()
        self.render('login.html',**{'obj': obj})

    def post(self, *args, **kwargs):
        obj = LoginForm()
        valid,value_dict = obj.is_valid(self)
        print(valid,value_dict)
        if valid:
            print(value_dict)
        else:
            return self.render('login.html',**{'obj': obj})



settings = {
    'static_path': 'static',
    'static_url_prefix': '/sss/',
    'template_path':'templates',
}
application = tornado.web.Application([
    (r"/login", LoginHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()