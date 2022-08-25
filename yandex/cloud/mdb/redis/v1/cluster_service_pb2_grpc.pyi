"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import grpc
import yandex.cloud.mdb.redis.v1.cluster_pb2
import yandex.cloud.mdb.redis.v1.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

class ClusterServiceStub:
    """A set of methods for managing Redis clusters."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.redis.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified Redis cluster.

    To get the list of available Redis clusters, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of Redis clusters that belong
    to the specified folder.
    """
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a Redis cluster in the specified folder."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified Redis cluster."""
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified Redis cluster."""
    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Start the specified Redis cluster."""
    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stop the specified Redis cluster."""
    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves a Redis cluster to the specified folder."""
    Backup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified Redis cluster."""
    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new Redis cluster using the specified backup."""
    RescheduleMaintenance: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Reschedules planned maintenance operation."""
    StartFailover: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.StartClusterFailoverRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Start a manual failover on the specified Redis cluster."""
    ListLogs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified Redis cluster."""
    StreamLogs: grpc.UnaryStreamMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.StreamLogRecord,
    ]
    """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""
    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of operations for the specified cluster."""
    ListBackups: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified Redis cluster."""
    ListHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified cluster."""
    AddHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates new hosts for a cluster."""
    DeleteHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified hosts for a cluster."""
    UpdateHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified hosts."""
    GetShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.GetClusterShardRequest,
        yandex.cloud.mdb.redis.v1.cluster_pb2.Shard,
    ]
    """Returns the specified shard."""
    ListShards: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterShardsRequest,
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterShardsResponse,
    ]
    """Retrieves a list of shards."""
    AddShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.AddClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new shard."""
    DeleteShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.DeleteClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified shard."""
    Rebalance: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.cluster_service_pb2.RebalanceClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Rebalances the cluster. Evenly distributes all the hash slots between the shards."""

class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Redis clusters."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.GetClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.cluster_pb2.Cluster:
        """Returns the specified Redis cluster.

        To get the list of available Redis clusters, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClustersRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClustersResponse:
        """Retrieves the list of Redis clusters that belong
        to the specified folder.
        """
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.CreateClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a Redis cluster in the specified folder."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.UpdateClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified Redis cluster."""
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.DeleteClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified Redis cluster."""
    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.StartClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Start the specified Redis cluster."""
    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.StopClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Stop the specified Redis cluster."""
    @abc.abstractmethod
    def Move(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.MoveClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Moves a Redis cluster to the specified folder."""
    @abc.abstractmethod
    def Backup(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.BackupClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a backup for the specified Redis cluster."""
    @abc.abstractmethod
    def Restore(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.RestoreClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a new Redis cluster using the specified backup."""
    @abc.abstractmethod
    def RescheduleMaintenance(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Reschedules planned maintenance operation."""
    @abc.abstractmethod
    def StartFailover(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.StartClusterFailoverRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Start a manual failover on the specified Redis cluster."""
    @abc.abstractmethod
    def ListLogs(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterLogsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterLogsResponse:
        """Retrieves logs for the specified Redis cluster."""
    @abc.abstractmethod
    def StreamLogs(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.StreamClusterLogsRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[yandex.cloud.mdb.redis.v1.cluster_service_pb2.StreamLogRecord]:
        """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""
    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterOperationsResponse:
        """Retrieves the list of operations for the specified cluster."""
    @abc.abstractmethod
    def ListBackups(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterBackupsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterBackupsResponse:
        """Retrieves the list of available backups for the specified Redis cluster."""
    @abc.abstractmethod
    def ListHosts(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterHostsResponse:
        """Retrieves a list of hosts for the specified cluster."""
    @abc.abstractmethod
    def AddHosts(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.AddClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates new hosts for a cluster."""
    @abc.abstractmethod
    def DeleteHosts(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified hosts for a cluster."""
    @abc.abstractmethod
    def UpdateHosts(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified hosts."""
    @abc.abstractmethod
    def GetShard(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.GetClusterShardRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.cluster_pb2.Shard:
        """Returns the specified shard."""
    @abc.abstractmethod
    def ListShards(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterShardsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.cluster_service_pb2.ListClusterShardsResponse:
        """Retrieves a list of shards."""
    @abc.abstractmethod
    def AddShard(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.AddClusterShardRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a new shard."""
    @abc.abstractmethod
    def DeleteShard(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.DeleteClusterShardRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified shard."""
    @abc.abstractmethod
    def Rebalance(
        self,
        request: yandex.cloud.mdb.redis.v1.cluster_service_pb2.RebalanceClusterRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Rebalances the cluster. Evenly distributes all the hash slots between the shards."""

def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: grpc.Server) -> None: ...
