from __future__ import absolute_import
from celery import Celery

#Broker = what?
app = Celery('test_celery', broker = 'amqp://guest@localhost', backend = 'rpc://')
