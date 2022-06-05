"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.dataproc.v1.cluster_pb2
import yandex.cloud.dataproc.v1.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

class ClusterServiceStub:
    """A set of methods for managing Data Proc clusters."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.dataproc.v1.cluster_pb2.Cluster]
    """Returns the specified cluster.

    To get the list of all available clusters, make a [ClusterService.List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.dataproc.v1.cluster_service_pb2.ListClustersResponse]
    """Retrieves the list of clusters in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a cluster in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the configuration of the specified cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified cluster."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Starts the specified cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Stops the specified cluster."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.dataproc.v1.cluster_service_pb2.ListClusterOperationsResponse]
    """Lists operations for the specified cluster."""

    ListHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.dataproc.v1.cluster_service_pb2.ListClusterHostsResponse]
    """Retrieves the list of hosts in the specified cluster."""

    ListUILinks: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.cluster_service_pb2.ListUILinksRequest,
        yandex.cloud.dataproc.v1.cluster_service_pb2.ListUILinksResponse]
    """Retrieves a list of links to web interfaces being proxied by Data Proc UI Proxy."""


class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Data Proc clusters."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.GetClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.cluster_pb2.Cluster:
        """Returns the specified cluster.

        To get the list of all available clusters, make a [ClusterService.List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.ListClustersRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.cluster_service_pb2.ListClustersResponse:
        """Retrieves the list of clusters in the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.CreateClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a cluster in the specified folder."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.UpdateClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the configuration of the specified cluster."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.DeleteClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified cluster."""
        pass

    @abc.abstractmethod
    def Start(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.StartClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Starts the specified cluster."""
        pass

    @abc.abstractmethod
    def Stop(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.StopClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Stops the specified cluster."""
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.cluster_service_pb2.ListClusterOperationsResponse:
        """Lists operations for the specified cluster."""
        pass

    @abc.abstractmethod
    def ListHosts(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.cluster_service_pb2.ListClusterHostsResponse:
        """Retrieves the list of hosts in the specified cluster."""
        pass

    @abc.abstractmethod
    def ListUILinks(self,
        request: yandex.cloud.dataproc.v1.cluster_service_pb2.ListUILinksRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.cluster_service_pb2.ListUILinksResponse:
        """Retrieves a list of links to web interfaces being proxied by Data Proc UI Proxy."""
        pass


def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: grpc.Server) -> None: ...
