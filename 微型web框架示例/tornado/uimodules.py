#__author:  Administrator
#date:  2017/3/10
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tornado.web import UIModule
from tornado import escape

class Custom(UIModule):
    def embedded_css(self):
        return "body{color:blue;}"
    def css_files(self):
        return "a.css"
    def render(self, *args, **kwargs):
        print(args,kwargs)
        # return '<h1>wupeiqi</h1>'
        return escape.xhtml_escape('<h1>wupeiqi</h1>')
        #return escape.xhtml_escape('<h1>wupeiqi</h1>')