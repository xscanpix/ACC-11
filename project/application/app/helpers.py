import os

from definitions import ROOT_DIR

def result_exists(angle, n_nodes=200, resultdir="{}/result".format(ROOT_DIR)):
    if os.path.exists("{}/r0a{}n{}_results".format(resultdir, angle, n_nodes)):
        return os.path.abspath("{}/r0a{}n{}_results".format(resultdir, angle, n_nodes))
    else:
        return None