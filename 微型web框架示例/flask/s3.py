#__author:  Administrator
#date:  2017/3/10
from flask import Flask,render_template,request,make_response,redirect,url_for,session

app = Flask(__name__)

@app.route("/index/",methods=['GET','POST'])
def hello():
    print('...')
    return 'OK'

def my_wsgi_app(environ, start_response):
    print('my_wsgi_app')
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<h1>Hello</h1>', encoding='utf-8'), ]

class Foo:
    def __init__(self,w):
        self.w = w
    def __call__(self, environ, start_response):

        obj = self.w(environ, start_response)

        return obj


if __name__ == "__main__":
    # app.wsgi_app = my_wsgi_app
    # 11. 自定制中间件
    app.wsgi_app = Foo(app.wsgi_app)
    app.run()
