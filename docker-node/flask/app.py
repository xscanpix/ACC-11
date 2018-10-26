#!flask/bin/python
from flask import Flask, render_template
import subprocess
import sys

app = Flask(__name__)


@app.route('/app', methods=['GET'])
def start():    
    return render_template("home.html")






if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
