from celery import Celery

import time

import mesh_generator as mesh
import solver as solve

celery = Celery("App", broker="amqp://", result_backend='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

@celery.task(bind=True)
def solve_angle(self, angle):
    path = solve.result_exists(angle)
    if path != None:
        return path # Return the path of the already solved results
    else:
        result = solve_angle_subtask.delay(angle)

        return result.task_id


@celery.task(bind=True)
def solve_angle_subtask(self, angle):
    xmlpath = mesh.generate_mesh_for_angle(angle)
    resultpath = solve.solve(xmlpath)

    return resultpath
