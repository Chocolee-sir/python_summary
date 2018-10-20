#!/usr/bin/env python
__author__ = 'Chocolee'

import pika

# 远程连接输入用户名密码
credentials = pika.PlainCredentials('lee', 'lee@1234')

# 生成一个socket
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.100', credentials=credentials))

# 声明一个管道
channel = connection.channel()

# 声明queue
# channel.queue_declare(queue='hello')
# 队列持久化 durable
channel.queue_declare(queue='hello', durable=True)

# Exchange在定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接收消息
# fanout: 所有bind到此exchange的queue都可以接收消息
# direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
# topic:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息
# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',  # queue名称
                      body='Hello World!',  # 消息体
                      properties=pika.BasicProperties(
                          delivery_mode=2,   # make message persistent  消息持久化
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()