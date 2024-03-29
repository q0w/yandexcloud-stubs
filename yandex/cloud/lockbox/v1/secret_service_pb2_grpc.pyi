"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.access.access_pb2
import yandex.cloud.lockbox.v1.secret_pb2
import yandex.cloud.lockbox.v1.secret_service_pb2
import yandex.cloud.operation.operation_pb2

class SecretServiceStub:
    """A set of methods for managing secrets."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.GetSecretRequest,
        yandex.cloud.lockbox.v1.secret_pb2.Secret,
    ]
    """Returns the specified secret.

    To get the list of all available secrets, make a [List] request.
    Use [PayloadService.Get] to get the payload (confidential data themselves) of the secret.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.ListSecretsRequest,
        yandex.cloud.lockbox.v1.secret_service_pb2.ListSecretsResponse,
    ]
    """Retrieves the list of secrets in the specified folder."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.CreateSecretRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a secret in the specified folder."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.UpdateSecretRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified secret."""
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.DeleteSecretRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified secret."""
    Activate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.ActivateSecretRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Activates the specified secret."""
    Deactivate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.DeactivateSecretRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deactivates the specified secret."""
    ListVersions: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.ListVersionsRequest,
        yandex.cloud.lockbox.v1.secret_service_pb2.ListVersionsResponse,
    ]
    """Retrieves the list of versions of the specified secret."""
    AddVersion: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.AddVersionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds new version based on a previous one."""
    ScheduleVersionDestruction: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.ScheduleVersionDestructionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Schedules the specified version for destruction.

    Scheduled destruction can be cancelled with the [SecretService.CancelVersionDestruction] method.
    """
    CancelVersionDestruction: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.CancelVersionDestructionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Cancels previously scheduled version destruction, if the version hasn't been destroyed yet."""
    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.lockbox.v1.secret_service_pb2.ListSecretOperationsRequest,
        yandex.cloud.lockbox.v1.secret_service_pb2.ListSecretOperationsResponse,
    ]
    """Lists operations for the specified secret."""
    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified secret."""
    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the secret."""
    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the secret."""

class SecretServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing secrets."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.GetSecretRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.lockbox.v1.secret_pb2.Secret:
        """Returns the specified secret.

        To get the list of all available secrets, make a [List] request.
        Use [PayloadService.Get] to get the payload (confidential data themselves) of the secret.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.ListSecretsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.lockbox.v1.secret_service_pb2.ListSecretsResponse:
        """Retrieves the list of secrets in the specified folder."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.CreateSecretRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a secret in the specified folder."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.UpdateSecretRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified secret."""
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.DeleteSecretRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified secret."""
    @abc.abstractmethod
    def Activate(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.ActivateSecretRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Activates the specified secret."""
    @abc.abstractmethod
    def Deactivate(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.DeactivateSecretRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deactivates the specified secret."""
    @abc.abstractmethod
    def ListVersions(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.ListVersionsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.lockbox.v1.secret_service_pb2.ListVersionsResponse:
        """Retrieves the list of versions of the specified secret."""
    @abc.abstractmethod
    def AddVersion(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.AddVersionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Adds new version based on a previous one."""
    @abc.abstractmethod
    def ScheduleVersionDestruction(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.ScheduleVersionDestructionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Schedules the specified version for destruction.

        Scheduled destruction can be cancelled with the [SecretService.CancelVersionDestruction] method.
        """
    @abc.abstractmethod
    def CancelVersionDestruction(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.CancelVersionDestructionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Cancels previously scheduled version destruction, if the version hasn't been destroyed yet."""
    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.lockbox.v1.secret_service_pb2.ListSecretOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.lockbox.v1.secret_service_pb2.ListSecretOperationsResponse:
        """Lists operations for the specified secret."""
    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.access.access_pb2.ListAccessBindingsResponse:
        """Lists existing access bindings for the specified secret."""
    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Sets access bindings for the secret."""
    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates access bindings for the secret."""

def add_SecretServiceServicer_to_server(servicer: SecretServiceServicer, server: grpc.Server) -> None: ...
