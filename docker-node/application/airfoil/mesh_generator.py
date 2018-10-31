import os, sys, shutil, ntpath

from airfoil.naca2gmsh_geo import *

def main():
    if len(sys.argv) != 4:
        sys.exit("Usage: mesh_generator.py angle_start angle_stop n_angles")
    angle_start = int(sys.argv[1])
    angle_stop = int(sys.argv[2])
    n_angles = int(sys.argv[3])

    generate_meshes(angle_start, angle_stop, n_angles)
    convert_all_msh_xml()


def generate_mesh_for_angle(angle):
    geofile = generate_geo(angle)
    mshfile = convert_geo_to_msh(geofile)
    xmlfile = convert_msh_to_xml(mshfile)

    return xmlfile


# Generate GEO file if it does not exist already
def generate_geo(angle, dstdir="geo", naca1=0, naca2=0, naca3=1, naca4=2, n_nodes=200, n_levels=0):
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)

    geofilename = "a{}n{}.geo".format(angle, n_nodes)

    if os.path.exists("{}/{}".format(dstdir, geofilename)):
        return os.path.abspath("{}/{}".format(dstdir, geofilename))

    generate(naca1, naca2, naca3, naca4, angle, n_nodes, "{}/{}".format(dstdir, geofilename))

    return os.path.abspath("{}/{}".format(dstdir, geofilename))


# Generate GEO file for every angle
def generate_every_geo(angle_start, angle_stop, n_angles, dstdir="geo", naca1=0, naca2=0, naca3=1, naca4=2, n_nodes=200, n_levels=0):
    anglediff = ((angle_stop-angle_start) / n_angles)

    for i in  range(n_angles + 1):
        angle = angle_start + anglediff*i
        generate_geo(angle, dstdir, naca1, naca2, naca3, naca4, n_nodes, n_levels)


# Convert GEO file to MSH file if it does not exist already
def convert_geo_to_msh(filepath, dstdir="msh", gmshbin="/usr/bin/gmsh"):
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)
    
    mshfilename = "r0" + ntpath.basename(filepath).replace(".geo", ".msh")

    dstpath = os.path.abspath("{}/{}".format(dstdir, mshfilename))

    if os.path.exists(dstpath):
        return dstpath

    os.system("{} -format auto -v 2 -2 -o {} {}".format(gmshbin, dstpath, filepath))

    return dstpath


# Convert every GEO file in a directory to a MSH file
def convert_every_geo_to_msh(srcdir, dstdir="xml", gmshbin="/usr/bin/gmsh"):
    for filename in os.listdir(srcdir):
        filepath = os.path.abspath("{}/{}".format(srcdir, filename))
        convert_geo_to_msh(filepath, dstdir)


# Convert MSH file to XML file if it does not exist already
def convert_msh_to_xml(filepath, dstdir="xml", dolfinconvertpath="/usr/bin/dolfin-convert"):
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)

    xmlfilename = ntpath.basename(filepath).replace(".msh", ".xml")
    
    dstpath = os.path.abspath("{}/{}".format(dstdir, xmlfilename))

    if os.path.exists(dstpath):
        return dstpath

    os.system("{} {} {}".format(dolfinconvertpath, filepath, dstpath))

    return dstpath


# Convert every MSH file in directory to XML
def convert_every_msh_to_xml(srcdir, dstdir="xml", dolfinconvertpath="/usr/bin/dolfin-convert"):
    for filename in os.listdir(srcdir):
        filepath = os.path.abspath("{}/{}".format(srcdir, filename))
        convert_msh_to_xml(filepath, dstdir)


if __name__ == '__main__':
    main()