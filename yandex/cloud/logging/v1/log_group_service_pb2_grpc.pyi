"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.access.access_pb2
import yandex.cloud.logging.v1.log_group_pb2
import yandex.cloud.logging.v1.log_group_service_pb2
import yandex.cloud.operation.operation_pb2

class LogGroupServiceStub:
    """A set of methods for managing log groups."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupRequest,
        yandex.cloud.logging.v1.log_group_pb2.LogGroup]
    """Returns the specified log group.

    To get the list of all available log groups, make a [List] request.
    """

    Stats: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsResponse]
    """Returns stats for the specified log group."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsResponse]
    """Retrieves the list of log groups in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.CreateLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a log group in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.UpdateLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified log group."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.DeleteLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified log group."""

    ListResources: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesResponse]
    """Retrieves the resources (type and IDs) in the specified log group."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsResponse]
    """Lists operations for the specified log group."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse]
    """Lists existing access bindings for the specified log group."""

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Sets access bindings for the specified log group."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates access bindings for the specified log group."""


class LogGroupServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing log groups."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.logging.v1.log_group_pb2.LogGroup:
        """Returns the specified log group.

        To get the list of all available log groups, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def Stats(self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsResponse:
        """Returns stats for the specified log group."""
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsResponse:
        """Retrieves the list of log groups in the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.CreateLogGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a log group in the specified folder."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.UpdateLogGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified log group."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.DeleteLogGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified log group."""
        pass

    @abc.abstractmethod
    def ListResources(self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesResponse:
        """Retrieves the resources (type and IDs) in the specified log group."""
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsResponse:
        """Lists operations for the specified log group."""
        pass

    @abc.abstractmethod
    def ListAccessBindings(self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.access.access_pb2.ListAccessBindingsResponse:
        """Lists existing access bindings for the specified log group."""
        pass

    @abc.abstractmethod
    def SetAccessBindings(self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Sets access bindings for the specified log group."""
        pass

    @abc.abstractmethod
    def UpdateAccessBindings(self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates access bindings for the specified log group."""
        pass


def add_LogGroupServiceServicer_to_server(servicer: LogGroupServiceServicer, server: grpc.Server) -> None: ...
