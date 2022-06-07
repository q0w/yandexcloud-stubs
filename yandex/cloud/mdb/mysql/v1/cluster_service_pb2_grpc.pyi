"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import typing
import yandex.cloud.mdb.mysql.v1.cluster_pb2
import yandex.cloud.mdb.mysql.v1.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

class ClusterServiceStub:
    """A set of methods for managing MySQL clusters."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.mysql.v1.cluster_pb2.Cluster]
    """Retrieves information about a cluster."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClustersResponse]
    """Retrieves the list of clusters in a folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a cluster in a folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates a cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes a cluster."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Starts a cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Stops a cluster."""

    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Moves a cluster to a folder."""

    Backup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a backup for a cluster.

    To get information about a backup, make a [BackupService.Get] request.
    """

    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Restores a backup to a new cluster.

    See [the documentation](/docs/managed-mysql/concepts/backup) for details.
    """

    RescheduleMaintenance: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Reschedules planned maintenance operation."""

    StartFailover: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StartClusterFailoverRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Starts a manual failover for a cluster."""

    ListLogs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterLogsResponse]
    """Retrieves logs for a cluster.

    Alternatively, logs can be streamed using [StreamLogs].
    """

    StreamLogs: grpc.UnaryStreamMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StreamLogRecord]
    """Retrieves a log stream for a cluster.

    This method is similar to [ListLogs], but uses server-side streaming, which allows for the `tail -f` command semantics.
    """

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterOperationsResponse]
    """Retrieves a list of operations for a cluster."""

    ListBackups: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterBackupsResponse]
    """Retrieves a list of backups for a cluster.

    To list all backups in a folder, make a [BackupService.List] request.
    """

    ListHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterHostsResponse]
    """Retrieves a list of hosts for a cluster."""

    AddHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Adds new hosts in a cluster."""

    UpdateHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified hosts."""

    DeleteHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified hosts for a cluster."""


class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing MySQL clusters."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.GetClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mysql.v1.cluster_pb2.Cluster:
        """Retrieves information about a cluster."""
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClustersRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClustersResponse:
        """Retrieves the list of clusters in a folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.CreateClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a cluster in a folder."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.UpdateClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates a cluster."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.DeleteClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes a cluster."""
        pass

    @abc.abstractmethod
    def Start(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StartClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Starts a cluster."""
        pass

    @abc.abstractmethod
    def Stop(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StopClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Stops a cluster."""
        pass

    @abc.abstractmethod
    def Move(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.MoveClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Moves a cluster to a folder."""
        pass

    @abc.abstractmethod
    def Backup(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.BackupClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a backup for a cluster.

        To get information about a backup, make a [BackupService.Get] request.
        """
        pass

    @abc.abstractmethod
    def Restore(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.RestoreClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Restores a backup to a new cluster.

        See [the documentation](/docs/managed-mysql/concepts/backup) for details.
        """
        pass

    @abc.abstractmethod
    def RescheduleMaintenance(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Reschedules planned maintenance operation."""
        pass

    @abc.abstractmethod
    def StartFailover(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StartClusterFailoverRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Starts a manual failover for a cluster."""
        pass

    @abc.abstractmethod
    def ListLogs(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterLogsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterLogsResponse:
        """Retrieves logs for a cluster.

        Alternatively, logs can be streamed using [StreamLogs].
        """
        pass

    @abc.abstractmethod
    def StreamLogs(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StreamClusterLogsRequest,
        context: grpc.ServicerContext,
    ) -> typing.Iterator[yandex.cloud.mdb.mysql.v1.cluster_service_pb2.StreamLogRecord]:
        """Retrieves a log stream for a cluster.

        This method is similar to [ListLogs], but uses server-side streaming, which allows for the `tail -f` command semantics.
        """
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterOperationsResponse:
        """Retrieves a list of operations for a cluster."""
        pass

    @abc.abstractmethod
    def ListBackups(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterBackupsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterBackupsResponse:
        """Retrieves a list of backups for a cluster.

        To list all backups in a folder, make a [BackupService.List] request.
        """
        pass

    @abc.abstractmethod
    def ListHosts(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mysql.v1.cluster_service_pb2.ListClusterHostsResponse:
        """Retrieves a list of hosts for a cluster."""
        pass

    @abc.abstractmethod
    def AddHosts(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.AddClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Adds new hosts in a cluster."""
        pass

    @abc.abstractmethod
    def UpdateHosts(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified hosts."""
        pass

    @abc.abstractmethod
    def DeleteHosts(self,
        request: yandex.cloud.mdb.mysql.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified hosts for a cluster."""
        pass


def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: grpc.Server) -> None: ...