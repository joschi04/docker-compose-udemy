import pika
import time as t
import mysql.connector as mariadb

print("started the consume service")

conn = ""
try:
    creds = pika.PlainCredentials("user", "user")
    params = pika.ConnectionParameters(credentials=creds, host='bunny', connection_attempts=25, retry_delay=10)
    conn = pika.BlockingConnection(parameters=params)
    no_exit = False
    count = 10
except:
    print("failed to connect")
    exit()


channel = conn.channel()
def consume(ch, meth, props, body):
    print(body.decode())
    con = mariadb.connect(host="database", user="root", password="root", database="docker_teach")
    cursor = con.cursor()
    result = body.decode()
    sql = f"INSERT INTO messages VALUES (DEFAULT, '{result}');"
    cursor.execute(sql)
    ch.basic_ack(delivery_tag=meth.delivery_tag)


channel.queue_declare(queue="py-queue")
channel.queue_bind(exchange="amq.direct", queue="py-queue")
channel.basic_consume(queue="py-queue",on_message_callback=consume)
channel.start_consuming()
