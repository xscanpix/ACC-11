from __future__ import absolute_import
from celery import Celery

#Broker = what?
app = Celery('test_celery', broker = 'amqp://guest@localhost', backend = 'rpc://')


@app.task
void generate_mesh()
    return null

@app.task
void convert(var mesh)
    return null

@app.task
void calculate(var xml)
    return null
