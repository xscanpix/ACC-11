#!flask/bin/python
from flask import Flask, render_template, request
import subprocess
import sys

app = Flask(__name__)


@app.route('/app', methods=['GET', 'POST'])
def start():    
    if request.method == 'POST':
        start_angle = request.values.get("start_angle")
        end_angle  = request.values.get("end_angle")
        n_angles = request.values.get("n_angles")


        return render_template("hold.html", start_angle = start_angle, end_angle = end_angle,
				 n_angles = n_angles )

    return render_template("home.html")



if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
