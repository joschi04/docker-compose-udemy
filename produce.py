import pika
import time as t

print("started the produce service")
conn = ""
count = 0
no_exit = True
while count < 5 and no_exit:
    try:
        creds = pika.PlainCredentials("guest", "guest")
        params = pika.ConnectionParameters(credentials=creds, host='rabbit')
        conn = pika.BlockingConnection(parameters=params)
        no_exit = False
        count = 10
    except:
        count+=1
        t.sleep(15000)
        print(f"tried to connect: {count}")

queue = 'py-queue'
channel = conn.channel()
channel.queue_declare(queue=queue, durable=True)
channel.queue_bind(exchange="amq.direct", queue=queue)
channel.basic_publish(exchange="", routing_key=queue, body="hello compose".encode())



