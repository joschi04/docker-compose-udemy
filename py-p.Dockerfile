FROM python:3.7

RUN pip install pika

WORKDIR /app

COPY produce.py /app

CMD ["python", "/app/produce.py"]