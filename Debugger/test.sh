# this script must be executed under this folder
../py3/bin/python3 -m grpc_tools.protoc --python_out=./ --grpc_python_out=./ --proto_path=../myapp/proto ../myapp/proto/*.proto
../py3/bin/python echo_client.py
