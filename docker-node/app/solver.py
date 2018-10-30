import os, sys

SOLVERPATH = "bin/airfoil"

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: solver.py xmlsrcdir")
    xmlsrcdir = str(sys.argv[1])

    solve_all(xmlsrcdir)


def solve_all(srcdir):
    for filename in os.listdir(srcdir):
        solve(filename)


def solve(filename):
    temp = filename.replace(".xml", "") + "_results"
    os.system("{} 10 0.9 10 1 {}".format(SOLVERPATH, os.path.abspath(filename)))
    os.rename(os.path.abspath("results"),  os.path.abspath("results").replace("results", temp))


if __name__ == "__main__":
    main()