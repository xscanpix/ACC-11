import celery

import airfoil.mesh_generator as mesh
import airfoil.solver as solve


# Solve severalk angles at once, returning list of AsyncResult objects (with task_ids). [task_id, task_id, task_id, ...]
@celery.task(bind=True)
def solve_angles(self, angles=list()):

    result = group(solve_angle.s(angle) for angle in angles).delay()

    task_ids = []

    for res in result.results:
        task_ids.append(res.task_id)

    return task_ids


# Task starting the solving of an angle, returning the task_id of the task.
@celery.task(bind=True)
def solve_angle(self, angle):
    resultpath = solve.result_exists(angle)

    if resultpath == None: 
        xmlpath = mesh.generate_mesh_for_angle(angle)
        resultpath = solve.solve(xmlpath)

    return resultpath

    
