"""
simple time based rate limiting decorator
only support requests/second limit
"""
import time

from libs.cache import Cache

__all__=['limit']

_current_time_ms = lambda: int(round(time.time() * 1000))

class limiter():

    def __init__(self):
        # key is not expiring
        self.cache = Cache(500)
        self.oldest_timestamp_ms =  _current_time_ms()
        self.prefix = 'limit'
        self.n = 100
        self.time_sec = 5
        self.time_window_ms = 100
        self.buckets = self.time_sec * 1000 // self.time_window_ms

    def limit(self):
        current_time = _current_time_ms()
        id = int(current_time // self.time_window_ms)
        count = 0
        for i in range(self.time_sec):
            k = self.prefix + str(id - i)
            c = self.cache[k]
            if c:
                count += c
        if count >= self.n:
            return False
        key = self.prefix + str(id)
        v = self.cache[key]
        if v:
            self.cache[key] += 1
        else:
            self.cache[key] = 1
        return True


l = limiter()
count = 0
for i in range(1000):
    if l.limit():
        count += 1
print(count)
for k in l.cache.cache_ref.keys():
    print(l.cache[k])



