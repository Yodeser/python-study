# -*- coding: utf-8 -*-
# //todo
# Created 21:16, 2018/5/25 by Yodes Yang
import redis
import base64
from q0001_Generate_activeCode import ActiveCode


class RedisCase(object):
    redis = redis.StrictRedis(host="localhost", port=6379, db=1,
                              password=bytes.decode(base64.b64decode(b'MDIyMEBSZWRpcw=='), "utf8"),
                              errors='strict', decode_responses=True, charset='utf-8',
                              socket_timeout=None, connection_pool=None)

    def update(self):
        r = self.redis
        codes_list = ActiveCode.generate_code()
        for code in codes_list:
            r.lpush("codes", code)
        print(r.llen("codes"))


test = RedisCase()
test.update()
