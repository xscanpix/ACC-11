import os, sys, shutil, ntpath

from naca2gmsh_geo import *

from definitions import ROOT_DIR, GMSHBIN, DOLFINCONVERTBIN

def generate_mesh_for_angle(angle):
    geofile = generate_geo(int(angle))
    mshfile = convert_geo_to_msh(geofile)
    xmlfile = convert_msh_to_xml(mshfile)

    return xmlfile


# Generate GEO file if it does not exist already
def generate_geo(angle, dstdir="{}/geo".format(ROOT_DIR), naca1=0, naca2=0, naca3=1, naca4=2, n_nodes=200, n_levels=0):
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)

    geofilename = "a{}n{}.geo".format(int(angle), n_nodes)

    if os.path.exists("{}/{}".format(dstdir, geofilename)):
        return os.path.abspath("{}/{}".format(dstdir, geofilename))

    generate(naca1, naca2, naca3, naca4, int(angle), n_nodes, "{}/{}".format(dstdir, geofilename))

    return os.path.abspath("{}/{}".format(dstdir, geofilename))


# Generate GEO file for every angle
def generate_every_geo(angle_start, angle_stop, n_angles, dstdir="{}/geo".format(ROOT_DIR), naca1=0, naca2=0, naca3=1, naca4=2, n_nodes=200, n_levels=0):
    anglediff = ((angle_stop-angle_start) / n_angles)

    for i in  range(n_angles + 1):
        angle = angle_start + anglediff*i
        generate_geo(int(angle), dstdir, naca1, naca2, naca3, naca4, n_nodes, n_levels)


# Convert GEO file to MSH file if it does not exist already
def convert_geo_to_msh(filepath, dstdir="{}/msh".format(ROOT_DIR), gmshbin=GMSHBIN):
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)
    
    mshfilename = "r0" + ntpath.basename(filepath).replace(".geo", ".msh")

    dstpath = os.path.abspath("{}/{}".format(dstdir, mshfilename))

    if os.path.exists(dstpath):
        return dstpath

    os.system("{} -format auto -v 2 -2 -o {} {}".format(gmshbin, dstpath, filepath))

    return dstpath


# Convert every GEO file in a directory to a MSH file
def convert_every_geo_to_msh(srcdir, dstdir="{}/xml".format(ROOT_DIR), gmshbin=GMSHBIN):
    for filename in os.listdir(srcdir):
        filepath = os.path.abspath("{}/{}".format(srcdir, filename))
        convert_geo_to_msh(filepath, dstdir)


# Convert MSH file to XML file if it does not exist already
def convert_msh_to_xml(filepath, dstdir="{}/xml".format(ROOT_DIR), dolfinconvertpath=DOLFINCONVERTBIN):
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)

    xmlfilename = ntpath.basename(filepath).replace(".msh", ".xml")
    
    dstpath = os.path.abspath("{}/{}".format(dstdir, xmlfilename))

    if os.path.exists(dstpath):
        return dstpath

    os.system("{} {} {}".format(dolfinconvertpath, filepath, dstpath))

    return dstpath


# Convert every MSH file in directory to XML
def convert_every_msh_to_xml(srcdir, dstdir="{}/xml".format(ROOT_DIR), dolfinconvertpath=DOLFINCONVERTBIN):
    for filename in os.listdir(srcdir):
        filepath = os.path.abspath("{}/{}".format(srcdir, filename))
        convert_msh_to_xml(filepath, dstdir)