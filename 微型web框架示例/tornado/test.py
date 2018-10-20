#__author:  Administrator
#date:  2017/3/10

class Foo:

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass

    def __delitem__(self, key):
        pass

obj = Foo()
obj['is_login']
obj['is_login'] = 123
del obj['is_login']