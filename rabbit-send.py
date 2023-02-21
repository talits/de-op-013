import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                                55001))
channel = connection.channel()

channel.queue_declare(queue='hello2')

channel.basic_publish(exchange='', routing_key='hello', body='Hello Ada!')
print(" [x] Mensagem Enviada'")
connection.close()
