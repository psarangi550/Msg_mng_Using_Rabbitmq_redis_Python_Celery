import celery

app=celery.Celery("python_celery_redis_message_broker", broker="redis://:TJzXuSqzKniqrVTiByQk5egJWzXiYyji@redis-16409.c262.us-east-1-3.ec2.cloud.redislabs.com:16409")

@app.task
def rev_name(name):
    return name[::-1] 