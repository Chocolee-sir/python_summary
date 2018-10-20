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

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()