from celery import Celery
import os
import time
import sqlite3
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app=Celery("tasks", broker_url="amqps://mbpdudfx:JS2ieSJ1G91r-RsYG1xuwnl-Pf9Y3-qa@toad.rmq.cloudamqp.com/mbpdudfx", backend="redis://redis-16409.c262.us-east-1-3.ec2.cloud.redislabs.com:16409")

@app.task
def rev_name(name):
    time.sleep(5)
    return name[::-1]
