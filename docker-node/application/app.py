from flask import Flask, request, render_template
from celery import Celery

import tasks

app = Flask(__name__)
app.config.from_object('settings')

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], result_backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)

@app.route('/app', methods=['GET', 'POST'])
def start():    
    if request.method == 'POST':
        start_angle = request.values.get("start_angle")
        end_angle  = request.values.get("end_angle")
        n_angles = request.values.get("n_angles")


        return render_template("hold.html", start_angle = start_angle, end_angle = end_angle,
				 n_angles = n_angles )

    return render_template("home.html")


@app.route('/test', methods=['GET'])
def test():
	res = tasks.solve_angle(0).delay()

	return res


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
