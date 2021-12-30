import redis

# r = redis.Redis(
#     host='redis-16409.c262.us-east-1-3.ec2.cloud.redislabs.com:16409',
#     port=6379, 
#     password='TJzXuSqzKniqrVTiByQk5egJWzXiYyji')
def hello_redis():
    """Example Hello Redis Program"""
   
    # step 3: create the Redis Connection object
    try:
   
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host="redis-16409.c262.us-east-1-3.ec2.cloud.redislabs.com", port=16409, password="TJzXuSqzKniqrVTiByQk5egJWzXiYyji", decode_responses=True)
   
        # step 4: Set the hello message in Redis
        r.set("msg:hello", "Hello Redis!!!")

        # step 5: Retrieve the hello message from Redis
        msg = r.get("msg:hello")
        print(msg)        
   
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()