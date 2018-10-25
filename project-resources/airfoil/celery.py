from __future__ import absolute_import
from celery import Celery

#Broker = what?
app = Celery('test_celery', broker = 'amqp://guest@localhost', backend = 'rpc://')


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
