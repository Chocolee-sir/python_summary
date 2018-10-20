#!/usr/bin/env python
__author__ = 'Chocolee'

import pika
import time
credentials = pika.PlainCredentials('lee', 'lee@1234')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.100', credentials=credentials))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.

# 队列持久化 durable
channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    print("-->", ch, method, properties)
    # time.sleep(30)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动向服务端确认收到消息

# 可以在各个消费者端，配置perfetch=1,意思就是告诉RabbitMQ在我这个消费者当前消息还没处理完的时候就不要再给我发新消息了。
channel.basic_qos(prefetch_count=1)

# 消费消息
channel.basic_consume(callback,  # 如果收到消息，就调用callback函数来处理消息
                      queue='hello',
                      # no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()