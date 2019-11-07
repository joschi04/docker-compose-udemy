FROM python:3.7

RUN pip install pika mysql-connector-python

WORKDIR /app

COPY consume.py .

CMD ["python", "-u", "/app/consume.py"]