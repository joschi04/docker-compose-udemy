import pika

creds = pika.PlainCredentials("guest", "guest")
params = pika.ConnectionParameters(credentials=creds, host="bunny")
conn = pika.BlockingConnection(parameters=params)

channel = conn.channel()

while(True):
    channel.queue_declare(queue="py-queue")
    channel.queue_bind(queue="py-queue", exchange="amq.direct")
    channel.basic_publish(exchange="amq.direct", routing_key="py-queue", body="hello world".encode())
    val = input()