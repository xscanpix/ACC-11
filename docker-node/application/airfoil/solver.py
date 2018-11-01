import os, sys, ntpath, shutil

from definitions import ROOT_DIR, GMSHBIN, AIRFOILBIN, DOLFINCONVERTBIN

def result_exists(angle, n_nodes=200, resultdir="{}/result".format(ROOT_DIR)):
    if os.path.exists("{}/r0a{}n{}_results".format(resultdir, angle, n_nodes)):
        return os.path.abspath("{}/r0a{}n{}_results".format(resultdir, angle, n_nodes))
    else:
        return None


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

    copytree("results", "{}/{}".format(dstdir, resultsdirname))

    if os.path.exists("results"):
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
