import pika
import time as t

print("started the produce service")
conn = ""
count = 0
no_exit = True
while count < 15:
    try:
        creds = pika.PlainCredentials("guest", "guest")
        params = pika.ConnectionParameters(credentials=creds)
        conn = pika.BlockingConnection(parameters=params)
        no_exit = False
        count = 10
    except Exception as e:
        count+=1
        print(f"tried to connect: {count}")
        print(e)
        t.sleep(1500)

channel = conn.channel()
channel.queue_declare(queue="py-queue", durable=True)
channel.queue_bind(exchange="amq.direct", queue="py-queue")

print("do publish")
channel.basic_publish(exchange="", routing_key="py-queue", body="hello compose".encode())

channel.close()

