import os, sys, ntpath, shutil

from definitions import *

from helpers import *


def solve_all(srcdir="{}/xml".format(ROOT_DIR), dstdir="{}/result".format(ROOT_DIR), solverpath=AIRFOILBIN):
    if os.path.exists(srcdir):
        for filename in os.listdir(srcdir):
            solve(os.path.abspath("{}/{}".format(srcdir, filename)), dstdir)


def solve(filepath, dstdir="{}/result".format(ROOT_DIR), solverpath=AIRFOILBIN):
    resultsdirname = ntpath.basename(filepath).replace(".xml", "") + "_results"

    if os.path.exists(dstdir):
        if os.path.exists("{}/{}".format(dstdir, resultsdirname)):
            return os.path.abspath("{}/{}".format(dstdir, resultsdirname))
    else:
        os.mkdir(dstdir)                                                                                                                                                                                                                                                

    os.mkdir("{}/{}".format(dstdir, resultsdirname))

    os.system("{} 10 0.9 10 1 {}".format(solverpath, filepath))

    if os.path.exists("results"):
        copytree("results", "{}/{}".format(dstdir, resultsdirname))
        shutil.rmtree("results")

    return os.path.abspath("{}/{}".format(dstdir, resultsdirname))


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
