FROM python:3.7

RUN pip install pika

WORKDIR /app

COPY produce.py .
RUN chmod +x produce.py

CMD ["python", "/app/produce.py"]