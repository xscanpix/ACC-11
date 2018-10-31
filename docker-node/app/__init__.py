"""
Flask web application
"""

from flask import Flask
from celery import Celery

app = Flask(__name__)

app.config.from_object('app.settings')

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], result_backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)

import app.views.views
