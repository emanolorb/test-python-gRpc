import grpc
import sys
from grpc import Channel
from abc import ABC

class BaseGRpc(ABC):

    _channel : Channel

    def get_insecure_channel(self, host, port, timeout=10):
        channel = grpc.insecure_channel('{0}:{1}'.format(host, port))
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit('Error connecting to server')
        return channel

    def get_secure_channel(self, host, port, timeout=10):
        channel = grpc.secure_channel('{0}:{1}'.format(host, port))
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit('Error connecting to server')
        return channel
