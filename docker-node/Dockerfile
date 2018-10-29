FROM python:3

ADD ./app ./app

RUN apt-get update && apt-get install -y \
  gmsh \
  python-numpy

RUN pip install -r requirements.txt
