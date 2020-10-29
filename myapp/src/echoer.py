import time
import redis

from proto import echo_pb2
from proto import echo_pb2_grpc


class Echoer(echo_pb2_grpc.EchoServicer):

    def __init__(self):
        self.redis_client = redis.Redis(
            host='myapp-redis',
            port=6379,
            db=0,
            password='password',
            socket_timeout=None
        )

    def Reply(self, request, context):
        print(request.message, flush=True)
        key = hash(request.message)
        if self.redis_client.get(key) is None:
            time.sleep(1)
            self.redis_client.mset({key: 1})
        print(f'received request: {request} with context {context}', flush=True)
        return echo_pb2.EchoReply(message=f'You said: {request.message}')
