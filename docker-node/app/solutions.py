import os, sys

SOLVERPATH = "bin/airfoil"

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: solver.py filepath")
    filepath = str(sys.argv[1])

    solve(filepath)


def solve(filepath):
    temp = filepath.replace(".xml", "") + "_results"
    os.system("{} 10 0.9 10 1 {}".format(SOLVERPATH, filepath))
    os.rename(os.path.abspath("results"),  os.path.abspath("results").replace("results", temp))

if __name__ == "__main__":
    main()