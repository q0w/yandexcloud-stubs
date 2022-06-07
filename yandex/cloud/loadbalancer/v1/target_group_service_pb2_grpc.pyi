"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.loadbalancer.v1.target_group_pb2
import yandex.cloud.loadbalancer.v1.target_group_service_pb2
import yandex.cloud.operation.operation_pb2

class TargetGroupServiceStub:
    """A set of methods for managing TargetGroup resources."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.GetTargetGroupRequest,
        yandex.cloud.loadbalancer.v1.target_group_pb2.TargetGroup]
    """Returns the specified TargetGroup resource."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.ListTargetGroupsRequest,
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.ListTargetGroupsResponse]
    """Retrieves the list of TargetGroup resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.CreateTargetGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a target group in the specified folder and adds the specified targets to it."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.UpdateTargetGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified target group."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.DeleteTargetGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified target group."""

    AddTargets: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.AddTargetsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Adds targets to the target group."""

    RemoveTargets: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.RemoveTargetsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Removes targets from the target group."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.ListTargetGroupOperationsRequest,
        yandex.cloud.loadbalancer.v1.target_group_service_pb2.ListTargetGroupOperationsResponse]
    """Lists operations for the specified target group."""


class TargetGroupServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing TargetGroup resources."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.loadbalancer.v1.target_group_service_pb2.GetTargetGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.loadbalancer.v1.target_group_pb2.TargetGroup:
        """Returns the specified TargetGroup resource."""
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.loadbalancer.v1.target_group_service_pb2.ListTargetGroupsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.loadbalancer.v1.target_group_service_pb2.ListTargetGroupsResponse:
        """Retrieves the list of TargetGroup resources in the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.loadbalancer.v1.target_group_service_pb2.CreateTargetGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a target group in the specified folder and adds the specified targets to it."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.loadbalancer.v1.target_group_service_pb2.UpdateTargetGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified target group."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.loadbalancer.v1.target_group_service_pb2.DeleteTargetGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified target group."""
        pass

    @abc.abstractmethod
    def AddTargets(self,
        request: yandex.cloud.loadbalancer.v1.target_group_service_pb2.AddTargetsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Adds targets to the target group."""
        pass

    @abc.abstractmethod
    def RemoveTargets(self,
        request: yandex.cloud.loadbalancer.v1.target_group_service_pb2.RemoveTargetsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Removes targets from the target group."""
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.loadbalancer.v1.target_group_service_pb2.ListTargetGroupOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.loadbalancer.v1.target_group_service_pb2.ListTargetGroupOperationsResponse:
        """Lists operations for the specified target group."""
        pass


def add_TargetGroupServiceServicer_to_server(servicer: TargetGroupServiceServicer, server: grpc.Server) -> None: ...