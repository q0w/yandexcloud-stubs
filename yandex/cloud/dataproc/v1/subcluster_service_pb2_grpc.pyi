"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.dataproc.v1.subcluster_pb2
import yandex.cloud.dataproc.v1.subcluster_service_pb2
import yandex.cloud.operation.operation_pb2

class SubclusterServiceStub:
    """A set of methods for managing Data Proc subclusters."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.subcluster_service_pb2.GetSubclusterRequest,
        yandex.cloud.dataproc.v1.subcluster_pb2.Subcluster]
    """Returns the specified subcluster.

    To get the list of all available subclusters, make a [SubclusterService.List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.subcluster_service_pb2.ListSubclustersRequest,
        yandex.cloud.dataproc.v1.subcluster_service_pb2.ListSubclustersResponse]
    """Retrieves a list of subclusters in the specified cluster."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.subcluster_service_pb2.CreateSubclusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a subcluster in the specified cluster."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.subcluster_service_pb2.UpdateSubclusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified subcluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.subcluster_service_pb2.DeleteSubclusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified subcluster."""


class SubclusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Data Proc subclusters."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.dataproc.v1.subcluster_service_pb2.GetSubclusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.subcluster_pb2.Subcluster:
        """Returns the specified subcluster.

        To get the list of all available subclusters, make a [SubclusterService.List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.dataproc.v1.subcluster_service_pb2.ListSubclustersRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.subcluster_service_pb2.ListSubclustersResponse:
        """Retrieves a list of subclusters in the specified cluster."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.dataproc.v1.subcluster_service_pb2.CreateSubclusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a subcluster in the specified cluster."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.dataproc.v1.subcluster_service_pb2.UpdateSubclusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified subcluster."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.dataproc.v1.subcluster_service_pb2.DeleteSubclusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified subcluster."""
        pass


def add_SubclusterServiceServicer_to_server(servicer: SubclusterServiceServicer, server: grpc.Server) -> None: ...