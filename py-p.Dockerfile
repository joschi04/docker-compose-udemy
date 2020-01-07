FROM python:3.7

WORKDIR /usr/src/app

COPY producer-requirements.txt ./
RUN pip install --no-cache-dir -r producer-requirements.txt

COPY produce.py ./

CMD [ "python", "-u" ,"./produce.py" ]