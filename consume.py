import pika

creds = pika.PlainCredentials("guest", "guest")
params = pika.ConnectionParameters(credentials=creds, host="bunny")
conn = pika.BlockingConnection(parameters=params)

channel = conn.channel()

def consume(ch, meth, props, body):
    print(body.decode())
    ch.basic_ack(delivery_tag=meth.delivery_tag)

channel.basic_consume(queue="py-queue",on_message_callback=consume)

channel.start_consuming()