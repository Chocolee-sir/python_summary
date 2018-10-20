#!/usr/bin/env python
__author__ = 'Chocolee'

import pika

# 远程连接输入用户名密码
credentials = pika.PlainCredentials('lee', 'lee@1234')

# 生成一个socket
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.100', credentials=credentials))

# 声明一个管道
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True) #不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()