from __future__ import absolute_import
from celery import Celery
from nasa2gmsh_geo import *
from mesh_generator import *
import numpy as np

#Broker = what? Backend = Redis (later)
app = Celery('celery', broker = 'amqp://guest@localhost', backend = 'rpc://')

@app.task
def geofun(geofile, arg_n1, arg_n2, arg_n3, arg_n4, arg_angle, arg_nodes):
    n1 = float(arg_n1)
    n2 = float(arg_n2)
    n3 = float(arg_n3)
    n4 = float(arg_n4)
    angle = float(arg_angle)
    n_nodes = float(arg_nodes)

    xs = np.linspace(0.0, 1.0, n_nodes)
    x, y = naca4(n1, n2, n3, n4, xs)
    xa, xy = rot(x,y, angle)
    dat2gmsh(xa,ya)

#Call gmsh
@app.task
def generate_mesh(angle_start, angle_stop, n_angles):
    mesh_generate(angle_start, angle_stop, n_angles)

#Convert one file form gmsh to XML with Dolfin-xml
@app.task
def convert():
    msh_convert()

#Calculate the values
@app.task
def calculate(var xml):
    return null
