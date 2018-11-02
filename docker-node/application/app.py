from flask import Flask, request, render_template
from celery import Celery
from celery.result import AsyncResult
import numpy as np

from tasks import *
from helpers import result_exists

app = Flask(__name__)
app.config.from_object('settings')

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], result_backend='redis://localhost')
celery.conf.update(app.config)

@app.route('/app', methods=['GET', 'POST'])
def start():    
    if request.method == 'POST':
        start_angle = int(request.values.get("start_angle"))
        end_angle  = int(request.values.get("end_angle"))
        n_angles = int(request.values.get("n_angles"))

        angles = np.linspace(start_angle, end_angle, n_angles, int)

        res = solve_angles(angles)

        print(res)

        return render_template("hold.html", start_angle = start_angle, end_angle = end_angle, n_angles = n_angles)

    return render_template("home.html")


@app.route('/resultspath/task_id/<task_id>', methods=['GET'])
def get_results(task_id):
    res = AsyncResult(task_id).result

    print(res)

    return res


@app.route('/resultspath/angle/<int:angle>', methods=['GET'])
def get_results_angle(angle):
    path = result_exists(int(angle))

    return str(path) + "\n"    


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
