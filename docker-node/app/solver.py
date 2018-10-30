import os, sys

SOLVERPATH = "bin/airfoil"

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: solver.py xmlsrcdir")
    xmlsrcdir = str(sys.argv[1])

    solve_all(xmlsrcdir)


def solve_all(srcdir):
    for filename in os.listdir(srcdir):
        solve(os.path.abspath(srcdir), filename)


def solve(srcpath, filename):
    resultsdirname = filename.replace(".xml", "") + "_results"
    os.system("{} 10 0.9 10 1 {}".format(SOLVERPATH, "{}/{}".format(srcpath, filename)))
    os.rename(os.path.abspath("results"),  os.path.abspath("results").replace("results", resultsdirname))


if __name__ == "__main__":
    main()