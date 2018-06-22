# coding:utf-8

from redis import *

r = StrictRedis(host='localhost', port=6379)
# 写
#pipe = r.pipeline()

#pipe.set('py10', 'hello1')
#pipe.set('py11', 'world')
#pipe.execute()

# 读
#temp = r.get('py10')
#print(temp)


class redisHelper(object):

    def __init__(self, host, port):
        self.__redis = StrictRedis(host, port)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        return self.__redis.get(key)
