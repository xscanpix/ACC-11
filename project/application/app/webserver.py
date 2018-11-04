from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://rabbit:rabbit@10.0.2.15:5672'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:redis@10.0.2.15:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)

import routes