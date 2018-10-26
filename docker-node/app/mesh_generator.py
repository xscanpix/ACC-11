import os
import shutil
import naca2gmsh_geo as naca

def main():
    angle_start = 0
    angle_stop = 30
    n_angles = 10

    mesh_generate(angle_start, angle_stop, n_angles)

def mesh_generate(angle_start, angle_stop, n_angles):
    # Path on GHSM
    GMSHBIN = "/usr/bin/gmsh"
    # Path to dir where geo files will be stored
    GEODIR = "geo"
    # Path to dir where msh files will be stored
    MSHDIR = "msh"

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
        temp = "msh/r0"+temp
        geo_name = "geo/"+filename
        os.system('/usr/bin/gmsh -v 0 -nopopup -2 -o '+temp+' '+geo_name)
        
        
def msh_convert():
    for filename in os.listdir('/home/fenics/shared/murtazo/cloudnaca/msh'):
        temp = filename.replace(".msh",".XML")
        #msh_convert.delay(filename, temp)
        os.system('dolfin-convert '+filename+' '+temp)
    

if __name__ == '__main__':
    main()