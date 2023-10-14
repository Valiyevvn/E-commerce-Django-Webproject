# pull official base image
FROM ubuntu:latest

RUN apt-get update

RUN apt-get install libpq-dev -y
RUN apt-get install python3-dev build-essential -y
RUN apt-get install postgresql-client -y
RUN apt install python3 python3-pip -y
#set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv

#pip requirements

RUN pip3 install --upgrade pip
RUN pip3 install virtualenv && python3 -m virtualenv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY entrypoint.sh /srv/entrypoint.sh
RUN sed -i 's/\r$//g' /srv/entrypoint.sh
RUN chmod +x /srv/entrypoint.sh

COPY . /srv/app
WORKDIR /srv/app

ENTRYPOINT ["/srv/entrypoint.sh"]



