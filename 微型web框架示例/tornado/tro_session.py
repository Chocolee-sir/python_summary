#__author:  Administrator
#date:  2017/3/10
import uuid


class Session(object):
    container = {
        # “asdf”: {}
    }

    def __init__(self,handler):
        # 获取用户cookie，如果有，不操作，否则，给用户生成随即字符串
        # - 写给用户
        # - 保存在session
        nid = handler.get_cookie('session_id')
        if nid:
            if nid in Session.container:
                pass
            else:
                nid = str(uuid.uuid4())
                Session.container[nid] = {}
        else:
            nid = str(uuid.uuid4())
            Session.container[nid] = {}

        handler.set_cookie('session_id', nid, max_age=1000)
        # nid当前访问用户的随即字符串
        self.nid = nid
        # 封装了所有用户请求信息
        self.handler = handler

    def __setitem__(self, key, value):
        Session.container[self.nid][key] =value

    def __getitem__(self, item):
        return Session.container[self.nid].get(item)

    def __delitem__(self, key):
        del Session.container[self.nid][key]

class RedisSession(object):

    def __init__(self,handler):
        # 获取用户cookie，如果有，不操作，否则，给用户生成随即字符串
        # - 写给用户
        # - 保存在session
        nid = handler.get_cookie('session_id')
        if nid:
            if nid in Session.container:
                pass
            else:
                nid = str(uuid.uuid4())
                # Session.container[nid] = {}
                # 连接redis写值
                # redis 服务器IP，端口（6379）
                # 根据Nid是字符串 => 6871237123
                # 6871237123 % 3 = 0,1,2
                # ['10.1.11.2','10.1.11.3','10.1.11.4']
        else:
            nid = str(uuid.uuid4())
            # Session.container[nid] = {}
            # 连接redis写值

        handler.set_cookie('session_id', nid, max_age=1000)
        # nid当前访问用户的随即字符串
        self.nid = nid
        # 封装了所有用户请求信息
        self.handler = handler

    def __setitem__(self, key, value):
        # Session.container[self.nid][key] =value
        pass

    def __getitem__(self, item):
        # return Session.container[self.nid].get(item)
        pass

    def __delitem__(self, key):
        # del Session.container[self.nid][key]
        pass
