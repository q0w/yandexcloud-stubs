"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.k8s.v1.version_service_pb2

class VersionServiceStub:
    """A set of methods for managing Kubernetes versions."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.k8s.v1.version_service_pb2.ListVersionsRequest,
        yandex.cloud.k8s.v1.version_service_pb2.ListVersionsResponse,
    ]
    """Retrieves the list of versions in the specified release channel."""

class VersionServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Kubernetes versions."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.k8s.v1.version_service_pb2.ListVersionsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.k8s.v1.version_service_pb2.ListVersionsResponse:
        """Retrieves the list of versions in the specified release channel."""

def add_VersionServiceServicer_to_server(servicer: VersionServiceServicer, server: grpc.Server) -> None: ...
