"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.dataproc.manager.v1.manager_service_pb2

class DataprocManagerServiceStub:
    """Data Proc manager service definition."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Report: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.manager.v1.manager_service_pb2.ReportRequest,
        yandex.cloud.dataproc.manager.v1.manager_service_pb2.ReportReply]
    """Sends a status report from a host."""


class DataprocManagerServiceServicer(metaclass=abc.ABCMeta):
    """Data Proc manager service definition."""
    @abc.abstractmethod
    def Report(self,
        request: yandex.cloud.dataproc.manager.v1.manager_service_pb2.ReportRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.manager.v1.manager_service_pb2.ReportReply:
        """Sends a status report from a host."""
        pass


def add_DataprocManagerServiceServicer_to_server(servicer: DataprocManagerServiceServicer, server: grpc.Server) -> None: ...