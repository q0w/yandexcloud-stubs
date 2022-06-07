"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.operation.operation_pb2
import yandex.cloud.vpc.v1.gateway_pb2
import yandex.cloud.vpc.v1.gateway_service_pb2

class GatewayServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.gateway_service_pb2.GetGatewayRequest,
        yandex.cloud.vpc.v1.gateway_pb2.Gateway]
    """Returns the specified Gateway resource.

    To get the list of all available Gateway resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.gateway_service_pb2.ListGatewaysRequest,
        yandex.cloud.vpc.v1.gateway_service_pb2.ListGatewaysResponse]
    """Retrieves the list of Gateway resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.gateway_service_pb2.CreateGatewayRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a gateway in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.gateway_service_pb2.UpdateGatewayRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified gateway."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.gateway_service_pb2.DeleteGatewayRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified gateway."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.gateway_service_pb2.ListGatewayOperationsRequest,
        yandex.cloud.vpc.v1.gateway_service_pb2.ListGatewayOperationsResponse]
    """List operations for the specified gateway."""

    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.gateway_service_pb2.MoveGatewayRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Move a gateway to another folder"""


class GatewayServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.vpc.v1.gateway_service_pb2.GetGatewayRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.gateway_pb2.Gateway:
        """Returns the specified Gateway resource.

        To get the list of all available Gateway resources, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.vpc.v1.gateway_service_pb2.ListGatewaysRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.gateway_service_pb2.ListGatewaysResponse:
        """Retrieves the list of Gateway resources in the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.vpc.v1.gateway_service_pb2.CreateGatewayRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a gateway in the specified folder."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.vpc.v1.gateway_service_pb2.UpdateGatewayRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified gateway."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.vpc.v1.gateway_service_pb2.DeleteGatewayRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified gateway."""
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.vpc.v1.gateway_service_pb2.ListGatewayOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.gateway_service_pb2.ListGatewayOperationsResponse:
        """List operations for the specified gateway."""
        pass

    @abc.abstractmethod
    def Move(self,
        request: yandex.cloud.vpc.v1.gateway_service_pb2.MoveGatewayRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Move a gateway to another folder"""
        pass


def add_GatewayServiceServicer_to_server(servicer: GatewayServiceServicer, server: grpc.Server) -> None: ...