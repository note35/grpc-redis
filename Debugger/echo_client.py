import grpc

import echo_pb2
import echo_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = echo_pb2_grpc.EchoStub(channel)
        response = stub.Reply(echo_pb2.EchoRequest(message='Hello World!'))
    print("Echo client received: " + response.message)


if __name__ == '__main__':
    run()
