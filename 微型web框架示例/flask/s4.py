#__author:  Administrator
#date:  2017/3/10
from flask import Flask, flash, redirect, render_template, request,get_flashed_messages
app = Flask(__name__)


@app.route('/')
def index1():
    # 12. 获取消息
    v = get_flashed_messages()
    print(v)
    return render_template('s4.html')


@app.route('/set')
def index2():
    v = request.args.get('p')
    # 13. 设置消息
    flash('kkkk')
    return 'ok'


if __name__ == "__main__":
    app.run()