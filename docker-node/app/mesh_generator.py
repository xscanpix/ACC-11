import os, sys
import shutil
import naca2gmsh_geo as naca

# Path on GHSM
GMSHBIN = "/usr/bin/gmsh"
# Path to dir where geo files will be stored
GEODIR = "geo"
# Path to dir where msh files will be stored
MSHDIR = "msh"
XMLDIR = "xml"
DOLFINCONVERTPATH = "/usr/bin/dolfin-convert"

def main():
    if len(sys.argv) != 4:
        sys.exit("Usage: mesh_generator.py angle_start angle_stop n_angles")
    angle_start = int(sys.argv[1])
    angle_stop = int(sys.argv[2])
    n_angles = int(sys.argv[3])

    mesh_generate(angle_start, angle_stop, n_angles)
    msh_convert()

def mesh_generate(angle_start, angle_stop, n_angles):
    # Shape of airfoil
    NACA1 = 0
    NACA2 = 0
    NACA3 = 1
    NACA4 = 2

    n_nodes = 200
    n_levels = 0
    anglediff = ((angle_stop-angle_start)/n_angles)

    if os.path.exists(GEODIR):
        shutil.rmtree(GEODIR)
    if os.path.exists(MSHDIR):
        shutil.rmtree(MSHDIR)
    os.mkdir(GEODIR)
    os.mkdir(MSHDIR)

    # Create Geo-files
    for i in  range(n_angles + 1):
        angle = angle_start + anglediff*i
        geofile = "{}/a{}n{}.geo".format(GEODIR, angle, n_nodes)
        naca.generate(NACA1, NACA2, NACA3, NACA4, angle, n_nodes, geofile)

    # Create Msh-files
    for filename in os.listdir('geo'):
        temp = filename.replace(".geo","")
        temp = "{}/r0{}.msh".format(MSHDIR, temp)
        geo_name = "{}/{}".format(GEODIR, filename)
        os.system("{} -format auto -v 0 -2 -o {} {}".format(GMSHBIN, temp, geo_name))
        
        
def msh_convert():
    if os.path.exists(XMLDIR):
        shutil.rmtree(XMLDIR)
    os.mkdir(XMLDIR)

    xmlabspath = os.path.abspath(XMLDIR)
    mshabspath = os.path.abspath(MSHDIR)
    
    for filename in os.listdir(MSHDIR):
        temp = filename.replace(".msh",".xml")
        os.system("{} {}/{} {}/{}".format(DOLFINCONVERTPATH, mshabspath, filename, xmlabspath, temp))


if __name__ == '__main__':
    main()