from flask import render_template, request
import numpy as np
from . import app

from application.worker import tasks

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

        angles = np.linspace(start_angle, end_angle, n_angles, int)

        res = tasks.solve_angles(angles)

        return render_template("hold.html", start_angle = start_angle, end_angle = end_angle, n_angles = n_angles, tasks=res)

    return render_template("home.html")