from __future__ import absolute_import
from celery import Celery
from NASA2GmSH_geo import *

#Broker = what?
app = Celery('test_celery', broker = 'amqp://guest@localhost', backend = 'rpc://')

@app.task
void geofun()
    n1 = float(arg_n1)
    n2 = float(arg_n2)
    n3 = float(arg_n3)
    n4 = float(arg_n4)
    angle = float(arg_angle)
    n_nodes = float(arg_nodes)

    return null

@app.task
void generate_mesh()
#Call gmsh
    return null

@app.task
void angle_aux()
#Gmsh help function
    return null

@app.task
void convert(var mesh)
#Convert one file form gmsh to XML with Dolfin-xml
    return null

@app.task
void calculate(var xml)
#Calculate the values
    return null
