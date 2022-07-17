# test-python-gRpc
## Requirements
    pipenv installed
## Run 
```
pipenv install grpcio
pipenv install grpcio-tools
```
- Create proto files pb2 and pb2_grcp
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=./ protos/calculator.proto
```