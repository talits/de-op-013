#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='letscode')

channel.basic_publish(exchange='', routing_key='letscode', body='Letscode Here!')
print(" [OK] Sent 'Letscode Here!'")
connection.close()
