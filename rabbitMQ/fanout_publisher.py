#!/usr/bin/env python
__author__ = 'Chocolee'

import pika
import sys

# 远程连接输入用户名密码
credentials = pika.PlainCredentials('lee', 'lee@1234')

# 生成一个socket
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.100', credentials=credentials))

# 声明一个管道
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()