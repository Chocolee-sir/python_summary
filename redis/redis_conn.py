#!/usr/bin/env python
__author__ = 'Chocolee'

import redis

# 普通连接
r = redis.Redis(host='192.168.31.100', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))

# 通过连接池连接
pool = redis.ConnectionPool(host='192.168.31.100', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('foo1', 'Bar1')
print(r.get('foo1'))
