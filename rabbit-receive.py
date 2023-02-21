import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                                55001))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Recebendo mensagens %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Aguardando mais mensagens. Aperte CTRL+ para sair')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
