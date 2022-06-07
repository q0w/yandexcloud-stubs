"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.logging.v1.log_reading_service_pb2

class LogReadingServiceStub:
    """A set of methods for reading from log groups. To make a request use `reader.logging.yandexcloud.net`."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Read: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_reading_service_pb2.ReadRequest,
        yandex.cloud.logging.v1.log_reading_service_pb2.ReadResponse]
    """Read log entries from the specified log group."""


class LogReadingServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for reading from log groups. To make a request use `reader.logging.yandexcloud.net`."""
    @abc.abstractmethod
    def Read(self,
        request: yandex.cloud.logging.v1.log_reading_service_pb2.ReadRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.logging.v1.log_reading_service_pb2.ReadResponse:
        """Read log entries from the specified log group."""
        pass


def add_LogReadingServiceServicer_to_server(servicer: LogReadingServiceServicer, server: grpc.Server) -> None: ...