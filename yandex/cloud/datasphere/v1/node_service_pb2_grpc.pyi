"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.datasphere.v1.node_service_pb2

class NodeServiceStub:
    """A set of methods for managing Node resources."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Execute: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.node_service_pb2.NodeExecutionRequest,
        yandex.cloud.datasphere.v1.node_service_pb2.NodeExecutionResponse]
    """Executes deployed Node."""


class NodeServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Node resources."""
    @abc.abstractmethod
    def Execute(self,
        request: yandex.cloud.datasphere.v1.node_service_pb2.NodeExecutionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.datasphere.v1.node_service_pb2.NodeExecutionResponse:
        """Executes deployed Node."""
        pass


def add_NodeServiceServicer_to_server(servicer: NodeServiceServicer, server: grpc.Server) -> None: ...
