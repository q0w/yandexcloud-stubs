"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.compute.v1.disk_pb2
import yandex.cloud.compute.v1.disk_service_pb2
import yandex.cloud.operation.operation_pb2

class DiskServiceStub:
    """A set of methods for managing Disk resources."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_service_pb2.GetDiskRequest,
        yandex.cloud.compute.v1.disk_pb2.Disk]
    """Returns the specified Disk resource.

    To get the list of available Disk resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_service_pb2.ListDisksRequest,
        yandex.cloud.compute.v1.disk_service_pb2.ListDisksResponse]
    """Retrieves the list of Disk resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_service_pb2.CreateDiskRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a disk in the specified folder.

    You can create an empty disk or restore it from a snapshot or an image.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_service_pb2.UpdateDiskRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified disk."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_service_pb2.DeleteDiskRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified disk.

    Deleting a disk removes its data permanently and is irreversible. However, deleting a disk does not delete
    any snapshots or images previously made from the disk. You must delete snapshots and images separately.

    It is not possible to delete a disk that is attached to an instance.
    """

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_service_pb2.ListDiskOperationsRequest,
        yandex.cloud.compute.v1.disk_service_pb2.ListDiskOperationsResponse]
    """Lists operations for the specified disk."""

    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_service_pb2.MoveDiskRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Moves the specified disk to another folder of the same cloud."""


class DiskServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Disk resources."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.compute.v1.disk_service_pb2.GetDiskRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.compute.v1.disk_pb2.Disk:
        """Returns the specified Disk resource.

        To get the list of available Disk resources, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.compute.v1.disk_service_pb2.ListDisksRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.compute.v1.disk_service_pb2.ListDisksResponse:
        """Retrieves the list of Disk resources in the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.compute.v1.disk_service_pb2.CreateDiskRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a disk in the specified folder.

        You can create an empty disk or restore it from a snapshot or an image.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.compute.v1.disk_service_pb2.UpdateDiskRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified disk."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.compute.v1.disk_service_pb2.DeleteDiskRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified disk.

        Deleting a disk removes its data permanently and is irreversible. However, deleting a disk does not delete
        any snapshots or images previously made from the disk. You must delete snapshots and images separately.

        It is not possible to delete a disk that is attached to an instance.
        """
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.compute.v1.disk_service_pb2.ListDiskOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.compute.v1.disk_service_pb2.ListDiskOperationsResponse:
        """Lists operations for the specified disk."""
        pass

    @abc.abstractmethod
    def Move(self,
        request: yandex.cloud.compute.v1.disk_service_pb2.MoveDiskRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Moves the specified disk to another folder of the same cloud."""
        pass


def add_DiskServiceServicer_to_server(servicer: DiskServiceServicer, server: grpc.Server) -> None: ...