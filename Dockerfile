FROM docker.io/library/fedora:36

RUN dnf update -y \
&& dnf install -y pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt



CMD [ "python3", "app.py" ]