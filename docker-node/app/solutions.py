import os, sys

SOLVERPATH = "bin/airfoil"

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: solver.py filepath")
    filepath = str(sys.argv[1])
    solve(filepath)
    

def solve(filepath):
    os.system("{} 10 0.1 10 1 {}".format(SOLVERPATH, filepath))


if __name__ == "__main__":
    main()