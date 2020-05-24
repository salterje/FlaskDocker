FROM ubuntu:18.04

MAINTAINER Jason Salter "salter.je@gmail.com"

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3"]

CMD [ "app/app.py"]
