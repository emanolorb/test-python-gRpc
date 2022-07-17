import grpc
from base_grpc_service import BaseGRpc
# import the generated classes
from protos import calculator_pb2, calculator_pb2_grpc


class CalculatorClientClass(BaseGRpc):

    def __init__(self):
        # open a gRPC channel
        self._channel = self.get_insecure_channel('localhost', '50051')
        # create a stub (client)
        self.stub = calculator_pb2_grpc.CalculatorStub(self._channel)

    def get_square_root(self, number: float) -> float:
        # create a valid request message
        number_request_message = calculator_pb2.Number(value=number)

        # make the call
        response = self.stub.SquareRoot(number_request_message)
        return response.value

number = input('A que numero le quieres sacar la raiz cuadrada?? \n')

response_value = CalculatorClientClass().get_square_root(int(number))

# Se hizo la luz!
print(response_value)
