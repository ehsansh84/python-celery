FROM python:3.7-alpine
RUN mkdir /app && mkdir /temp
WORKDIR /app
RUN apk update
RUN apk add ansible vim
RUN pip install -r requirements.txt
CMD python main.py

