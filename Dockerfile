from python:3.7

Run mkdir code

Add consumer.py /code

workdir /code

RUN pip install kafka-python

cmd ['python consumer.py']