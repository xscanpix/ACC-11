import mesh_generator as mesh
import solver as solve


def solve_angle(angle):
    if solve.result_exists(angle):
        return "Results already exists" # Return the already solved results
    else:
        xmlpath = mesh.generate_mesh_for_angle(angle)
        print xmlpath
        return solve.solve(xmlpath)

