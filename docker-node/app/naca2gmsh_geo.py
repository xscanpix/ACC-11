#!/usr/bin/python
###########################################################################
#
# Name: naca2gmsh_geo.py
# Argumenmts (7):
#   naca1: first digit NACA four digit
#   naca2: second digit NACA four digit
#   naca3: third digit NACA four digit
#   naca4: fourth digit NACA four digit
#   angle: angle of attack
#   n_nodes: number of nodes in x-wise direction
#   outfile: file to write to
# Output: write to file
# Example: ./naca2gmsh_geo.py 0 0 1 2 10 100 mygeo.geo
#
###########################################################################
import re, sys, numpy as np

###########################################################################
# Rotating airfoil
# Arguments coordinates x,y and angle a in degrees
###########################################################################
def rot(x,y,a):
  ar = -a*3.14159/180
  xa = x*np.cos(ar)-y*np.sin(ar)
  ya = y*np.cos(ar)+x*np.sin(ar)
  return xa, ya

###########################################################################
# Generate coordinates for NACA four digit airfoil
# n0,n1,n2,n3 are the four digits (standard airfoirl 0,0,1,2
# x is the desired x-coordinates array
###########################################################################
def naca4(n0,n1,n2,n3,x):
  m = n0 / 100.0
  p = n1 / 10.0
  t = (10 * n2 + n3) / 100.0
  c = 1.0
# Closed trailing edge, change -0.1036 to -0.1015 for original def
  yt = 5*t*c*(0.2969*np.sqrt(x/c)+(-0.1260)*x/c+(-0.3516)*pow(x/c,2)+0.2843*pow(x/c,3)+(-0.1036)*pow(x/c,4))
  yc = x.copy()
  i = 0
  for xx in x:
    if xx < p*c:
      yc[i]=m*xx/p/p*(2*p-xx/c)
    else:
      yc[i]=m*(c-xx)/pow(1-p,2)*(1+xx/c-2*p)
    i += 1
  upper = yt+yc
  lower = -yt+yc
  xreturn = np.append(x,x[x.size-2:0:-1])
  yreturn = np.append(upper,lower[lower.size-2:0:-1])
  return xreturn,yreturn

###########################################################################
# Generate GMSH geo format from coordinates
###########################################################################
def dat2gmsh(x,y,outfile):
  with open(outfile, 'w') as out:
    lc1 = 0.01
    lc2 = 1.00
    i = 0
    while i < x.size:
      out.write("Point(" + str(i+1) + ") = {" + str(x[i]) + "," + str(y[i])+",0,"+str(lc1)+"};\n")
      i += 1 
    ntot = x.size
    i = 1
    while i < ntot:
      out.write("Line(" + str(i) + ")={" + str(i) + "," + str(i+1) +"};\n")
      i += 1
    out.write("Line(" + str(ntot) + ")={" + str(ntot) + "," + "1};\n")
    out.write("Line Loop(%s)={" % (ntot+1)),
    i = 1
    while i < ntot:
      out.write(" %d," % (i)),
      i += 1 
    out.write(" " + str(ntot) + "};\n")
  # Outer domain boundary
    out.write("Point(100000) = {-10,0,0,"+str(lc2)+"};\n")
    out.write("Point(101000) = {0,10,0,"+str(lc2)+"};\n")
    out.write("Point(102000) = {10,0,0,"+str(lc2)+"};\n")
    out.write("Point(103000) = {0,-10,0,"+str(lc2)+"};\n")
    out.write("Point(104000) = {0,0,0,"+str(lc2)+"};\n")
    out.write("Circle(105000) = {100000,104000,101000};\n")
    out.write("Circle(106000) = {101000,104000,102000};\n")
    out.write("Circle(107000) = {102000,104000,103000};\n")
    out.write("Circle(108000) = {103000,104000,100000};\n")
    out.write("Line Loop(109000) = {105000,106000,107000,108000};\n")
    out.write("Plane Surface(110000) = {109000,"+str(ntot+1)+"};\n")


def generate(n1, n2, n3, n4, angle, n_nodes, outfile):
    xs = np.linspace(0.0,1.0,n_nodes)
    x, y = naca4(n1,n2,n3,n4,xs)
    xa, ya = rot(x,y,angle)
    dat2gmsh(xa,ya,outfile)

def main():
    if len(sys.argv) != 8:
        sys.exit("Usage: naca2gmsh_geo.py angle n_nodes outfile")
    n1 = float(sys.argv[1])
    n2 = float(sys.argv[2])
    n3 = float(sys.argv[3])
    n4 = float(sys.argv[4])
    angle = float(sys.argv[5])
    n_nodes = int(sys.argv[6])
    outfile = str(sys.argv[7])

    xs = np.linspace(0.0,1.0,n_nodes)
    x, y = naca4(n1,n2,n3,n4,xs)
    xa, ya = rot(x,y,angle)
    dat2gmsh(xa,ya,outfile)

if __name__ == '__main__':
    main()