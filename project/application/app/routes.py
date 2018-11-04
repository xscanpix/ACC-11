from flask import render_template, request, jsonify
import numpy as np

from webserver import app, celery

from helpers import result_exists
import tasks

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_angle = int(request.values.get("start_angle"))
        end_angle  = int(request.values.get("end_angle"))
        n_angles = int(request.values.get("n_angles"))

        angles = np.linspace(start_angle, end_angle, n_angles, dtype=int)

        res = celery.send_task('tasks.solve_angles', [list(angles)])

        print(celery.AsyncResult(res.task_id))

        return render_template("home.html", start_angle = start_angle, end_angle = end_angle, n_angles = n_angles, tasks=[celery.AsyncResult(res.task_id).task_id])

    return render_template("home.html")


@app.route('/results/<int:angle>', methods=['GET'])
def result_angle(angle):
    res = result_exists(angle)

    if res == None:
        return jsonify({'result': "None", 'value':""})

    ## Render result?
    return jsonify({'result': angle, 'value': res})