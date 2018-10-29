import os

SOLVERPATH = "./airfoil"
MSHDIR = "./msh"
XMLDIR = "./xml"

def main():

def solve(filename):
    abspath = os.path.abspath(XMLDIR)
    for filename in os.listdir(XMLDIR):
        solution_name = filename.replace("r0a","")
        solution_name = filename.replace("n200.xml","")
        os.system('./airfoil 10 0.001 10. 1 '+temp+' ' + solution_name):
