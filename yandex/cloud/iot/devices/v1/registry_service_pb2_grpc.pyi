"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.iot.devices.v1.registry_pb2
import yandex.cloud.iot.devices.v1.registry_service_pb2
import yandex.cloud.operation.operation_pb2

class RegistryServiceStub:
    """A set of methods for managing registry."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.GetRegistryRequest,
        yandex.cloud.iot.devices.v1.registry_pb2.Registry]
    """Returns the specified registry.

    To get the list of available registries, make a [List] request.
    """

    GetByName: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.GetByNameRegistryRequest,
        yandex.cloud.iot.devices.v1.registry_pb2.Registry]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistriesRequest,
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistriesResponse]
    """Retrieves the list of registries in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.CreateRegistryRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a registry in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.UpdateRegistryRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified registry."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.DeleteRegistryRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified registry."""

    ListCertificates: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryCertificatesRequest,
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryCertificatesResponse]
    """Retrieves the list of registry certificates for the specified registry."""

    AddCertificate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.AddRegistryCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Adds a certificate."""

    DeleteCertificate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.DeleteRegistryCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified registry certificate."""

    ListPasswords: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryPasswordsRequest,
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryPasswordsResponse]
    """Retrieves the list of passwords for the specified registry."""

    AddPassword: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.AddRegistryPasswordRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Adds password for the specified registry."""

    DeletePassword: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.DeleteRegistryPasswordRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified password."""

    ListDeviceTopicAliases: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListDeviceTopicAliasesRequest,
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListDeviceTopicAliasesResponse]
    """Retrieves the list of device topic aliases for the specified registry."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryOperationsRequest,
        yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryOperationsResponse]
    """Lists operations for the specified registry."""


class RegistryServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing registry."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.GetRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iot.devices.v1.registry_pb2.Registry:
        """Returns the specified registry.

        To get the list of available registries, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def GetByName(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.GetByNameRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iot.devices.v1.registry_pb2.Registry: ...

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistriesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistriesResponse:
        """Retrieves the list of registries in the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.CreateRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a registry in the specified folder."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.UpdateRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified registry."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.DeleteRegistryRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified registry."""
        pass

    @abc.abstractmethod
    def ListCertificates(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryCertificatesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryCertificatesResponse:
        """Retrieves the list of registry certificates for the specified registry."""
        pass

    @abc.abstractmethod
    def AddCertificate(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.AddRegistryCertificateRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Adds a certificate."""
        pass

    @abc.abstractmethod
    def DeleteCertificate(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.DeleteRegistryCertificateRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified registry certificate."""
        pass

    @abc.abstractmethod
    def ListPasswords(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryPasswordsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryPasswordsResponse:
        """Retrieves the list of passwords for the specified registry."""
        pass

    @abc.abstractmethod
    def AddPassword(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.AddRegistryPasswordRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Adds password for the specified registry."""
        pass

    @abc.abstractmethod
    def DeletePassword(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.DeleteRegistryPasswordRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified password."""
        pass

    @abc.abstractmethod
    def ListDeviceTopicAliases(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.ListDeviceTopicAliasesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iot.devices.v1.registry_service_pb2.ListDeviceTopicAliasesResponse:
        """Retrieves the list of device topic aliases for the specified registry."""
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iot.devices.v1.registry_service_pb2.ListRegistryOperationsResponse:
        """Lists operations for the specified registry."""
        pass


def add_RegistryServiceServicer_to_server(servicer: RegistryServiceServicer, server: grpc.Server) -> None: ...
