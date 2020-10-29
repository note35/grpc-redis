from concurrent import futures
import grpc

from proto import echo_pb2_grpc
from echoer import Echoer


class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        echo_pb2_grpc.add_EchoServicer_to_server(Echoer(), server)
        server.add_insecure_port('[::]:50051')
        print('started listening on 50051...', flush=True)
        server.start()
        server.wait_for_termination()
        print('finished the termination', flush=True)


# if __name__ == '__main__':
def main():
    Server.run()
