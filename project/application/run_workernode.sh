#!/bin/sh

export FENICS_ID=$(docker run -td -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current)
docker exec -t -i $FENICS_ID apt update
docker exec -t -i $FENICS_ID apt install gmsh -y
docker exec -t -i $FENICS_ID apt install libdolfin2017.2 -y
docker exec -t -i $FENICS_ID pip install celery
docker exec -t -i $FENICS_ID pip install flask
docker exec -t -i $FENICS_ID pip install redis
docker exec -t -i $FENICS_ID celery worker -A tasks.celery