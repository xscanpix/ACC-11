import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GMSHBIN = "/usr/bin/gmsh"
DOLFINCONVERTBIN = "/usr/bin/dolfin-convert"#"{}/airfoil/bin/dolfin-convert".format(ROOT_DIR)
AIRFOILBIN = "{}/airfoil/bin/airfoil".format(ROOT_DIR)