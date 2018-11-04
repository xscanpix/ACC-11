from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://'
app.config['CELERY_RESULT_BACKEND'] = 'redis://'

celery = Celery(app.name, broker='amqp://', backend='redis://')
celery.conf.update(app.config)

import routes
