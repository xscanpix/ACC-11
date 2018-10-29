import sys

import mesh_generator as mesh
import solutions as solver

def main():
    if len(sys.argv) != 4:
        sys.exit("Usage: mesh_generator.py angle_start angle_stop n_angles")
    angle_start = int(sys.argv[1])
    angle_stop = int(sys.argv[2])
    n_angles = int(sys.argv[3])

    mesh.mesh_generate(angle_start, angle_stop, n_angles)
    mesh.msh_convert()

    # Solve files
    solver.solve("xml/r0a0n200.xml")


if __name__ == "__main__":
    main()