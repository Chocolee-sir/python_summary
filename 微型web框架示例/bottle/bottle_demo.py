#!/usr/bin/env python
__author__ = 'Chocolee'


from bottle import template, Bottle, static_file, request, redirect
import bottle
bottle.TEMPLATE_PATH.append('./templates/')

root = Bottle()

# 默认情况下去目录：['./', './views/']中寻找模板文件 hello_template.html
# 配置在 bottle.TEMPLATE_PATH 中
# return "Hello World"
# return template('<b>Hello {{name}}</b>!', name="Chocolee"


@root.route('/login/', method=['POST', 'GET'])
def login():
    if request.method == "GET":
        return template('login.html')
    elif request.method == "POST":
        # v = request.forms
        # v = request.query  GET发来的请求数据
        # v = request.body  POST发来的请求
        u = request.forms.get('user')
        p = request.forms.get('pwd')
        print(u, p)
        return redirect('/index/')


def lee():
    return '<h1>测试函数传递</h1>'

@root.route('/index/', method=['POST', 'GET'])
def index():
    user_list = [
        {'id': 1, 'name': 'root1', 'age': 18},
        {'id': 2, 'name': 'root2', 'age': 28},
        {'id': 3, 'name': 'root3', 'age': 38},
    ]
    return template('index.html',name='root', user_list=user_list, jj=lee)


@root.route('/static/<path:path>')
def callback(path):
    return static_file(path, root='static')

root.run(host='localhost', port=8080)