#!/usr/bin/env python
__author__ = 'Chocolee'

import pika
import uuid
import time

class FibonacciRpcClient(object):

    def __init__(self):
        self.credentials = pika.PlainCredentials('lee', 'lee@1234')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='192.168.31.100', credentials=self.credentials))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,   # 只要已经收到消息就调用self.on_response
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to=self.callback_queue,
                                         correlation_id=self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()    # 非阻塞的start_consuming()
            print('no msg...')
            time.sleep(1)
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(7)
print(" [.] Got %r" % response)