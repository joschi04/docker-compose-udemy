import pika
import time as t

try:
    print("try connect")
    creds = pika.PlainCredentials("user", "user")
    params = pika.ConnectionParameters(credentials=creds, host='bunny', connection_attempts=25, retry_delay=10)
    conn = pika.BlockingConnection(parameters=params)
    print("connect")
except Exception as e:
    print(e)

channel = conn.channel()
channel.queue_declare(queue="py-queue")
channel.queue_bind(exchange="amq.direct", queue="py-queue")

while (True):
    print("do publish")
    channel.basic_publish(exchange="", routing_key="py-queue", body="hello compose".encode())
    t.sleep(5)

channel.close()

