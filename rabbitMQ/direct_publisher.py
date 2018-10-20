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

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 级别
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

# 消息
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()