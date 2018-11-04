from flask import render_template, request, jsonify
import numpy as np
from app import app

from app import celery

from helpers import result_exists

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/app', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        start_angle = int(request.values.get("start_angle"))
        end_angle  = int(request.values.get("end_angle"))
        n_angles = int(request.values.get("n_angles"))

        angles = np.linspace(start_angle, end_angle, n_angles, dtype=int)

        res = celery.send_task('tasks.solve_angles', [list(angles)])

        return render_template("hold.html", start_angle = start_angle, end_angle = end_angle, n_angles = n_angles, tasks={})

    return render_template("home.html")


@app.route('/results/<int:angle>', methods=['GET'])
def result_angle(angle):
    res = result_exists(angle)

    if res == None:
        return jsonify({'result': "None", 'value':""})

    ## Render result?
    return jsonify({'result': angle, 'value': res})