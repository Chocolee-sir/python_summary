
class RepeatFilter(object):
    def __init__(self):
        """2.对象初始化"""
        self.visited_set = set()

    @classmethod
    def from_settings(cls, settings):
        """1.创建对象"""
        return cls()

    def request_seen(self, request):
        """4.检查是否访问过"""
        if request.url in self.visited_set:
            return True
        self.visited_set.add(request.url)
        return False

    def open(self):  # can return deferred
        """3.开始爬取"""
        # print('open')
        pass

    def close(self, reason):  # can return a deferred
        """5.关闭服务"""
        # print('close')
        pass
    def log(self, request, spider):  # log that a request has been filtered
        # print('log....')
        pass