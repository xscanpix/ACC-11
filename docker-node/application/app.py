from flask import Flask, request, render_template
from celery import Celery
import numpy as np

from tasks import *

app = Flask(__name__)
app.config.from_object('settings')

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], result_backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)

@app.route('/app', methods=['GET', 'POST'])
def start():    
    if request.method == 'POST':
        start_angle = int(request.values.get("start_angle"))
        end_angle  = int(request.values.get("end_angle"))
        n_angles = int(request.values.get("n_angles"))

        angles = np.linspace(start_angle, end_angle, n_angles)

        res = solve_angles(angles)

        print(res)

        return render_template("hold.html", start_angle = start_angle, end_angle = end_angle,
				 n_angles = n_angles )

    return render_template("home.html")


@app.route('/test', methods=['GET'])
def test():
	res = solve_angle.delay(1)

	return "Test"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
