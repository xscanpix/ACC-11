import os, sys, shutil, ntpath
import naca2gmsh_geo as naca

def main():
    if len(sys.argv) != 4:
        sys.exit("Usage: mesh_generator.py angle_start angle_stop n_angles")
    angle_start = int(sys.argv[1])
    angle_stop = int(sys.argv[2])
    n_angles = int(sys.argv[3])

    generate_meshes(angle_start, angle_stop, n_angles)
    convert_all_msh_xml()

def generate_meshes(angle_start, angle_stop, n_angles, gmshbin="/usr/bin/gmsh", geodir="geo", mshdir="msh", naca1=0, naca2=0, naca3=1, naca4=2, n_nodes=200, n_levels=0):
    anglediff = ((angle_stop-angle_start)/n_angles)

    if os.path.exists(geodir):
        shutil.rmtree(geodir)
    if os.path.exists(mshdir):
        shutil.rmtree(mshdir)

    os.mkdir(geodir)
    # Create Geo-files
    for i in  range(n_angles + 1):
        angle = angle_start + anglediff*i
        geofile = "{}/a{}n{}.geo".format(geodir, angle, n_nodes)
        naca.generate(naca1, naca2, naca3, naca4, angle, n_nodes, geofile)

    os.mkdir(mshdir)
    # Create Msh-files
    for filename in os.listdir('geo'):
        temp = filename.replace(".geo","")
        temp = "{}/r0{}.msh".format(mshdir, temp)
        geo_name = "{}/{}".format(geodir, filename)
        os.system("{} -format auto -v 0 -2 -o {} {}".format(gmshbin, temp, geo_name))


def convert_all_msh_xml(srcdir="msh", dstdir="xml", dolfinconvertpath="/usr/bin/dolfin-convert"):
    if os.path.exists(dstdir):
        shutil.rmtree(dstdir)
    os.mkdir(dstdir)
    
    mshabspath = os.path.abspath(srcdir)
    xmlabspath = os.path.abspath(dstdir)
    
    for filename in os.listdir(srcdir):
        srcfilepath = "{}/{}".format(mshabspath, filename)
        convert_one_msh_xml(srcfilepath, xmlabspath, dolfinconvertpath)


def convert_one_msh_xml(filepath, dstdir, dolfinconvertpath):
    absfilepath = os.path.abspath(filepath)
    absdstdir = os.path.abspath(dstdir)
    basename = ntpath.basename(filepath).replace(".msh", ".xml")
    os.system("{} {} {}/{}".format(dolfinconvertpath, absfilepath, absdstdir, basename))


if __name__ == '__main__':
    main()