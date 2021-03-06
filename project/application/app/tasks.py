from celery import group, shared_task

from mesh_generator import *
from solver import *
from helpers import *

from webserver import celery

# Solve severalk angles at once, returning list of AsyncResult objects (with task_ids). [task_id, task_id, task_id, ...]
@shared_task(bind=True)
def solve_angles(self, angles):

    result = group(solve_angle.s(angle) for angle in angles).delay()

    task_ids = []

    for res in result.results:
        task_ids.append(res.task_id)

    return task_ids

# Task starting the solving of an angle, returning the task_id of the task.
@shared_task(bind=True)
def solve_angle(self, angle):
    resultpath = result_exists(angle)

    if resultpath == None: 
        xmlpath = generate_mesh_for_angle(angle)
        resultpath = solve(xmlpath)

    return resultpath
