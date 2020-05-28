import redis
import numpy as np

r = redis.Redis(host='localhost', port=6379, db=0)

def fromRedis(r, n):
    encoded = r.get(n)
    a = np.frombuffer(encoded)
    return a

print(fromRedis(r,'Cook'))