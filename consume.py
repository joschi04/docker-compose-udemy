import pika
import time as t
import mysql.connector as mariadb

print("started the produce service")

count = 0
conn = ""
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


channel = conn.channel()
def consume(ch, meth, props, body):
    print(body.decode())
    con = mariadb.connect(user="root", password="root", database="docker_teach")
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO messages VALUES (DEFAULT, {body.decode()});")
    ch.basic_ack(delivery_tag=meth.delivery_tag)


channel.queue_declare(queue="py-queue", durable=True)
channel.queue_bind(exchange="amq.direct", queue="py-queue")
channel.basic_consume(queue="py-queue",on_message_callback=consume)
channel.start_consuming()
