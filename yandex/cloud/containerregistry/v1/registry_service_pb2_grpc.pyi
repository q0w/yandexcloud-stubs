"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.access.access_pb2
import yandex.cloud.containerregistry.v1.registry_pb2
import yandex.cloud.containerregistry.v1.registry_service_pb2
import yandex.cloud.operation.operation_pb2

class RegistryServiceStub:
    """A set of methods for managing Registry resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.registry_service_pb2.GetRegistryRequest,
        yandex.cloud.containerregistry.v1.registry_pb2.Registry,
    ]
    """Returns the specified Registry resource.

    To get the list of available Registry resources, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.registry_service_pb2.ListRegistriesRequest,
        yandex.cloud.containerregistry.v1.registry_service_pb2.ListRegistriesResponse,
    ]
    """Retrieves the list of Registry resources in the specified folder."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.registry_service_pb2.CreateRegistryRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a registry in the specified folder."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.registry_service_pb2.UpdateRegistryRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified registry."""
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.registry_service_pb2.DeleteRegistryRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified registry."""
    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the specified registry.
    """
    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the specified registry."""
    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified registry."""
    ListIpPermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.registry_service_pb2.ListIpPermissionRequest,
        yandex.cloud.containerregistry.v1.registry_service_pb2.ListIpPermissionsResponse,
    ]
    """ip permissions

    List ip permissions for the specified registry.
    """
    SetIpPermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.registry_service_pb2.SetIpPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Set ip permissions for the specified registry."""
    UpdateIpPermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.registry_service_pb2.UpdateIpPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update ip permissions for the specified registry."""

class RegistryServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Registry resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.containerregistry.v1.registry_service_pb2.GetRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.registry_pb2.Registry:
        """Returns the specified Registry resource.

        To get the list of available Registry resources, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.containerregistry.v1.registry_service_pb2.ListRegistriesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.registry_service_pb2.ListRegistriesResponse:
        """Retrieves the list of Registry resources in the specified folder."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.containerregistry.v1.registry_service_pb2.CreateRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a registry in the specified folder."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.containerregistry.v1.registry_service_pb2.UpdateRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified registry."""
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.containerregistry.v1.registry_service_pb2.DeleteRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified registry."""
    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.access.access_pb2.ListAccessBindingsResponse:
        """access

        Lists access bindings for the specified registry.
        """
    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Sets access bindings for the specified registry."""
    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates access bindings for the specified registry."""
    @abc.abstractmethod
    def ListIpPermission(
        self,
        request: yandex.cloud.containerregistry.v1.registry_service_pb2.ListIpPermissionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.registry_service_pb2.ListIpPermissionsResponse:
        """ip permissions

        List ip permissions for the specified registry.
        """
    @abc.abstractmethod
    def SetIpPermission(
        self,
        request: yandex.cloud.containerregistry.v1.registry_service_pb2.SetIpPermissionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Set ip permissions for the specified registry."""
    @abc.abstractmethod
    def UpdateIpPermission(
        self,
        request: yandex.cloud.containerregistry.v1.registry_service_pb2.UpdateIpPermissionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Update ip permissions for the specified registry."""

def add_RegistryServiceServicer_to_server(servicer: RegistryServiceServicer, server: grpc.Server) -> None: ...
