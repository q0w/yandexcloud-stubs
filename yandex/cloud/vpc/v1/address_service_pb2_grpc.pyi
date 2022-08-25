"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.operation.operation_pb2
import yandex.cloud.vpc.v1.address_pb2
import yandex.cloud.vpc.v1.address_service_pb2

class AddressServiceStub:
    """A set of methods for managing Address resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.address_service_pb2.GetAddressRequest,
        yandex.cloud.vpc.v1.address_pb2.Address,
    ]
    """Returns the specified Address resource.

    To get the list of all available Address resources, make a [List] request.
    """
    GetByValue: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.address_service_pb2.GetAddressByValueRequest,
        yandex.cloud.vpc.v1.address_pb2.Address,
    ]
    """Returns the specified Address resource by a given value.

    To get the list of all available Address resources, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.address_service_pb2.ListAddressesRequest,
        yandex.cloud.vpc.v1.address_service_pb2.ListAddressesResponse,
    ]
    """Retrieves the list of Address resources in the specified folder."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.address_service_pb2.CreateAddressRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an address in the specified folder and network."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.address_service_pb2.UpdateAddressRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified address."""
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.address_service_pb2.DeleteAddressRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified address."""
    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.address_service_pb2.ListAddressOperationsRequest,
        yandex.cloud.vpc.v1.address_service_pb2.ListAddressOperationsResponse,
    ]
    """List operations for the specified address."""
    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.address_service_pb2.MoveAddressRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Move an address to another folder"""

class AddressServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Address resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.vpc.v1.address_service_pb2.GetAddressRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.address_pb2.Address:
        """Returns the specified Address resource.

        To get the list of all available Address resources, make a [List] request.
        """
    @abc.abstractmethod
    def GetByValue(
        self,
        request: yandex.cloud.vpc.v1.address_service_pb2.GetAddressByValueRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.address_pb2.Address:
        """Returns the specified Address resource by a given value.

        To get the list of all available Address resources, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.vpc.v1.address_service_pb2.ListAddressesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.address_service_pb2.ListAddressesResponse:
        """Retrieves the list of Address resources in the specified folder."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.vpc.v1.address_service_pb2.CreateAddressRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates an address in the specified folder and network."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.vpc.v1.address_service_pb2.UpdateAddressRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified address."""
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.vpc.v1.address_service_pb2.DeleteAddressRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified address."""
    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.vpc.v1.address_service_pb2.ListAddressOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.address_service_pb2.ListAddressOperationsResponse:
        """List operations for the specified address."""
    @abc.abstractmethod
    def Move(
        self,
        request: yandex.cloud.vpc.v1.address_service_pb2.MoveAddressRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Move an address to another folder"""

def add_AddressServiceServicer_to_server(servicer: AddressServiceServicer, server: grpc.Server) -> None: ...
