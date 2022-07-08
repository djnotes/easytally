FROM docker.io/library/alpine:3.16.0

RUN apk update \
&& apk add python3 py3-pip

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt



CMD [ "python3", "app.py" ]