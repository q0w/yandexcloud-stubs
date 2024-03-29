"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.compute.v1.snapshot_pb2
import yandex.cloud.compute.v1.snapshot_service_pb2
import yandex.cloud.operation.operation_pb2

class SnapshotServiceStub:
    """A set of methods for managing Snapshot resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.GetSnapshotRequest,
        yandex.cloud.compute.v1.snapshot_pb2.Snapshot,
    ]
    """Returns the specified Snapshot resource.

    To get the list of available Snapshot resources, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsRequest,
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsResponse,
    ]
    """Retrieves the list of Snapshot resources in the specified folder."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.CreateSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a snapshot of the specified disk."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.UpdateSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified snapshot.

    Values of omitted parameters are not changed.
    """
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.DeleteSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified snapshot.

    Deleting a snapshot removes its data permanently and is irreversible.
    """
    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsRequest,
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsResponse,
    ]
    """Lists operations for the specified snapshot."""

class SnapshotServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Snapshot resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.GetSnapshotRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.compute.v1.snapshot_pb2.Snapshot:
        """Returns the specified Snapshot resource.

        To get the list of available Snapshot resources, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsResponse:
        """Retrieves the list of Snapshot resources in the specified folder."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.CreateSnapshotRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a snapshot of the specified disk."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.UpdateSnapshotRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified snapshot.

        Values of omitted parameters are not changed.
        """
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.DeleteSnapshotRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified snapshot.

        Deleting a snapshot removes its data permanently and is irreversible.
        """
    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsResponse:
        """Lists operations for the specified snapshot."""

def add_SnapshotServiceServicer_to_server(servicer: SnapshotServiceServicer, server: grpc.Server) -> None: ...
