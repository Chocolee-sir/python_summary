#!/usr/bin/env python
__author__ = 'Chocolee'


import redis
import time

pool = redis.ConnectionPool(host='192.168.31.100', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)
pipe.multi()
pipe.set('name1', 'alex')
time.sleep(15)
pipe.set('role1', 'sb')

pipe.execute()