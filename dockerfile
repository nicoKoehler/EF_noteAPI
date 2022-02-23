FROM alpine:latest

RUN apk update
RUN apk add py-pip
RUN apk add python3-dev
RUN pip install --upgrade pip

WORKDIR /api
COPY . /api

RUN pip install -r requirements.txt

CMD ["python3", "-m", "flask", "run"]