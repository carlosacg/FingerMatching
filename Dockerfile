FROM ubuntu:latest as base

RUN apt-get -y update

ENV PYTHONUNBUFFERED=1

ENV DJANGO_DIR=/metodos

WORKDIR $DJANGO_DIR

RUN apt-get -y install python3

RUN apt-get -y install python3-pip

RUN pip3 install --upgrade pip

FROM base as with-requirements

COPY requirements.txt $DJANGO_DIR/

RUN pip3 install -r requirements.txt

RUN apt -y update

RUN apt-get install -y libgl1-mesa-glx 

RUN apt-get install -y libatlas-base-dev gfortran