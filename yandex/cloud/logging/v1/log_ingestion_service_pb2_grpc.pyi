"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.logging.v1.log_ingestion_service_pb2

class LogIngestionServiceStub:
    """A set of methods for writing to log groups. To make a request use `ingester.logging.yandexcloud.net`."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Write: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteRequest,
        yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteResponse,
    ]
    """Write log entries to specified destination."""

class LogIngestionServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for writing to log groups. To make a request use `ingester.logging.yandexcloud.net`."""

    @abc.abstractmethod
    def Write(
        self,
        request: yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteResponse:
        """Write log entries to specified destination."""

def add_LogIngestionServiceServicer_to_server(servicer: LogIngestionServiceServicer, server: grpc.Server) -> None: ...
