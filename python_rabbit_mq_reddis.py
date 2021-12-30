import celery
import redis
r = redis.StrictRedis(host="redis-16409.c262.us-east-1-3.ec2.cloud.redislabs.com", port=16409, password="TJzXuSqzKniqrVTiByQk5egJWzXiYyji", decode_responses=True)

app=celery.Celery("python_rabbit_mq_reddis", broker="amqps://mbpdudfx:JS2ieSJ1G91r-RsYG1xuwnl-Pf9Y3-qa@toad.rmq.cloudamqp.com/mbpdudfx",backend="redis://:TJzXuSqzKniqrVTiByQk5egJWzXiYyji@redis-16409.c262.us-east-1-3.ec2.cloud.redislabs.com:16409")

@app.task
def rev_name(name):
    return name[::-1]
