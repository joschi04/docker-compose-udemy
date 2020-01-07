FROM python:3.7

WORKDIR /usr/src/app

COPY consumer-requirements.txt ./
RUN pip install --no-cache-dir -r consumer-requirements.txt

COPY consume.py ./

CMD [ "python", "-u","./consume.py" ]

