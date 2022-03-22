FROM python:3.10.3-slim-buster

ADD . /product
WORKDIR /product

RUN apt-get update
RUN apt-get install -y imagemagick
RUN apt-get update && apt-get install -y --no-install-recommends libmagic1 && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
