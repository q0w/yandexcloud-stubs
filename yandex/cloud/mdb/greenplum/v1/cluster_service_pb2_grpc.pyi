"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import typing
import yandex.cloud.mdb.greenplum.v1.cluster_pb2
import yandex.cloud.mdb.greenplum.v1.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

class ClusterServiceStub:
    """A set of methods for managing Greenplum® clusters."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.greenplum.v1.cluster_pb2.Cluster]
    """Returns the specified Greenplum® cluster.

    To get the list of available Greenplum® clusters, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClustersResponse]
    """Retrieves a list of Greenplum® clusters that belong to the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a Greenplum® cluster in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified Greenplum® cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified Greenplum® cluster."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Starts the specified Greenplum® cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Stops the specified Greenplum® cluster."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterOperationsResponse]
    """Retrieves the list of Operation resources for the specified cluster."""

    ListMasterHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterHostsResponse]
    """Retrieves a list of master hosts for the specified cluster."""

    ListSegmentHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterHostsResponse]
    """Retrieves a list of segment hosts for the specified cluster."""

    ListLogs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterLogsResponse]
    """Retrieves logs for the specified Greenplum® cluster."""

    StreamLogs: grpc.UnaryStreamMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.StreamLogRecord]
    """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""

    ListBackups: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterBackupsResponse]
    """Retrieves the list of available backups for the specified Greenplum cluster."""

    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a new Greenplum® cluster using the specified backup."""


class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Greenplum® clusters."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.GetClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.greenplum.v1.cluster_pb2.Cluster:
        """Returns the specified Greenplum® cluster.

        To get the list of available Greenplum® clusters, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClustersRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClustersResponse:
        """Retrieves a list of Greenplum® clusters that belong to the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.CreateClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a Greenplum® cluster in the specified folder."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.UpdateClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified Greenplum® cluster."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.DeleteClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified Greenplum® cluster."""
        pass

    @abc.abstractmethod
    def Start(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.StartClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Starts the specified Greenplum® cluster."""
        pass

    @abc.abstractmethod
    def Stop(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.StopClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Stops the specified Greenplum® cluster."""
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterOperationsResponse:
        """Retrieves the list of Operation resources for the specified cluster."""
        pass

    @abc.abstractmethod
    def ListMasterHosts(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterHostsResponse:
        """Retrieves a list of master hosts for the specified cluster."""
        pass

    @abc.abstractmethod
    def ListSegmentHosts(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterHostsResponse:
        """Retrieves a list of segment hosts for the specified cluster."""
        pass

    @abc.abstractmethod
    def ListLogs(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterLogsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterLogsResponse:
        """Retrieves logs for the specified Greenplum® cluster."""
        pass

    @abc.abstractmethod
    def StreamLogs(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.StreamClusterLogsRequest,
        context: grpc.ServicerContext,
    ) -> typing.Iterator[yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.StreamLogRecord]:
        """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""
        pass

    @abc.abstractmethod
    def ListBackups(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterBackupsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.ListClusterBackupsResponse:
        """Retrieves the list of available backups for the specified Greenplum cluster."""
        pass

    @abc.abstractmethod
    def Restore(self,
        request: yandex.cloud.mdb.greenplum.v1.cluster_service_pb2.RestoreClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a new Greenplum® cluster using the specified backup."""
        pass


def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: grpc.Server) -> None: ...
