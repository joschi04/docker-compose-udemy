FROM python:3.7

RUN pip install pika
RUN pip install mysql-connector-python

WORKDIR /app

COPY consume.py .

CMD [ "python", "/app/consume.py" ]