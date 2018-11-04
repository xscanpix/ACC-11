import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GMSHBIN = (os.popen("which gmsh").read()).rstrip()
DOLFINCONVERTBIN = (os.popen("which dolfin-convert").read()).rstrip()
AIRFOILBIN = "{}/bin/airfoil".format(ROOT_DIR)