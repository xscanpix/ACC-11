from celery import Celery, group

import mesh_generator as mesh
import solver as solve

celery = Celery("App", broker="amqp://", result_backend='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')


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


@celery.task(bind=True)
def testtask2(self, a):
    return "Result!"


@celery.task(bind=True)
def testtask(self, l):

    result = group(testtask2.s(a) for a in l).delay()

    return result

    