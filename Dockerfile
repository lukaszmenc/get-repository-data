FROM python:3.7-alpine

ENV FLASK_APP repositories/app.py

WORKDIR /opt/app
COPY requirements.txt /opt/app/

RUN pip install -r requirements.txt

ADD . /opt/app

EXPOSE 5000

CMD waitress-serve \
    --host=0.0.0.0 \
    --port=5000 \
    repositories.app:app
