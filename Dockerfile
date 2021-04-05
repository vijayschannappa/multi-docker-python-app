FROM python:3.8-slim-buster

WORKDIR /usr/app
COPY ./requirements.txt /usr/app
RUN pip3 install -r requirements.txt
COPY ./ ./
CMD ["python", "-u", "helloworld.py"]