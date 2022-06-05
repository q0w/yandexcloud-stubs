"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.access.access_pb2
import yandex.cloud.iam.v1.service_account_pb2
import yandex.cloud.iam.v1.service_account_service_pb2
import yandex.cloud.operation.operation_pb2

class ServiceAccountServiceStub:
    """A set of methods for managing ServiceAccount resources."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.GetServiceAccountRequest,
        yandex.cloud.iam.v1.service_account_pb2.ServiceAccount]
    """Returns the specified ServiceAccount resource.

    To get the list of available ServiceAccount resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsRequest,
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsResponse]
    """Retrieves the list of ServiceAccount resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.CreateServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a service account in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.UpdateServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified service account."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.DeleteServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified service account."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse]
    """access

    Lists access bindings for the specified service account.
    """

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Sets access bindings for the service account."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates access bindings for the specified service account."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsRequest,
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsResponse]
    """Lists operations for the specified service account."""


class ServiceAccountServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing ServiceAccount resources."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.GetServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iam.v1.service_account_pb2.ServiceAccount:
        """Returns the specified ServiceAccount resource.

        To get the list of available ServiceAccount resources, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsResponse:
        """Retrieves the list of ServiceAccount resources in the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.CreateServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a service account in the specified folder."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.UpdateServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified service account."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.DeleteServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified service account."""
        pass

    @abc.abstractmethod
    def ListAccessBindings(self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.access.access_pb2.ListAccessBindingsResponse:
        """access

        Lists access bindings for the specified service account.
        """
        pass

    @abc.abstractmethod
    def SetAccessBindings(self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Sets access bindings for the service account."""
        pass

    @abc.abstractmethod
    def UpdateAccessBindings(self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates access bindings for the specified service account."""
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsResponse:
        """Lists operations for the specified service account."""
        pass


def add_ServiceAccountServiceServicer_to_server(servicer: ServiceAccountServiceServicer, server: grpc.Server) -> None: ...
