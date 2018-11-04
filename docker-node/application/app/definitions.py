import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GMSHBIN = "/usr/bin/gmsh"
DOLFINCONVERTBIN = "/usr/bin/dolfin-convert"
AIRFOILBIN = "{}/bin/airfoil".format(ROOT_DIR)