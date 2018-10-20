#!/usr/bin/env python
__author__ = 'Chocolee'

from flask import Flask, render_template, request
# 1.静态文件和模板路径配置
app = Flask(__name__)

# 5. 自定义模板函数
def leesir():
    return "<a>666</a>"

# 6.设置请求方式methods=['GET', 'POST']
@app.route("/index/", methods=['GET', 'POST'])
def hello():
    # 3.返回字符串
    # return 'hello world'
    # 4.返回模板

    # 7.获取用户请求数据
    print(request.args)
    """
    request.method
    request.args
    request.form
    request.values
    request.files
    request.cookies
    request.headers
    request.path
    request.full_path
    request.script_root
    request.url
    request.base_url
    request.url_root
    request.host_url
    request.host
    """
    # Python ORM框架 SQLAchemy
    # pymysql
    # obj = HttpResponse('内容')
    # obj.set_cookie(k1=123)
    # obj['h1'] = 'v1'
    # return obj

    # 10.session
    # session['username']
    # session['username']="asdf"

    return render_template('index.html', k1='root', k2=[1, 2, 3], k3={'id': 1, 'age': 18, 'name': 'lee'}, k4=leesir)
    # 8. 响应额外的数据
    # obj = make_response(render_template('index.html', k1='root', k2=[1, 2, 3], k3={'name': 'alex', 'age': 73}, k4=jinxin))
    # obj.set_cookie(k1='v1')
    # return obj

    # 9.重定向，类似于Django的reverse功能：url_for
    # return redirect('/test/about')
    # url = url_for('test') # /test/
    # return redirect(url)

@app.route('/test/<any(about,help,import,class):page_name>')
def test(page_name):
    return page_name

if __name__ == "__main__":
    # app.wsgi_app()
    # 2.IP和端口的配置
    app.run()