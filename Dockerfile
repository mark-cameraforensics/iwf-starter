FROM python:3.11-buster

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r ./requirements.txt
COPY app.py app.py