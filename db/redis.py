import json
from io import IOBase
from redis import BlockingConnectionPool, StrictRedis

pool0 = BlockingConnectionPool(max_connections=100,timeout=1,host='localhost',port=6379,db=0)

def get_redis_connection():
    try:
        return StrictRedis(connection_pool=pool0)
    except:
        print('Connection redis error')


class RedisImageStorage (IOBase) :
    def __init__ (self,filename):
        self.filename = filename
        self._redis = StrictRedis(connection_pool=pool0)

    def write(self,data):
        self._redis.append('attendance:api:image:' + self.filename,data)
