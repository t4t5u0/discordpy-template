FROM python:3.9

RUN mkdir /app

WORKDIR /app

ADD ../src /app

RUN pip install -U pip && pip install --trusted-host pypi.python.org -r requirements.txt
