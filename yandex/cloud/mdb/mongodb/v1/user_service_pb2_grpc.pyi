"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.mongodb.v1.user_pb2
import yandex.cloud.mdb.mongodb.v1.user_service_pb2
import yandex.cloud.operation.operation_pb2

class UserServiceStub:
    """A set of methods for managing MongoDB User resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.user_service_pb2.GetUserRequest,
        yandex.cloud.mdb.mongodb.v1.user_pb2.User,
    ]
    """Returns the specified MongoDB User resource.

    To get the list of available MongoDB User resources, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.user_service_pb2.ListUsersRequest,
        yandex.cloud.mdb.mongodb.v1.user_service_pb2.ListUsersResponse,
    ]
    """Retrieves the list of MongoDB User resources in the specified cluster."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.user_service_pb2.CreateUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a MongoDB user in the specified cluster."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.user_service_pb2.UpdateUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified MongoDB user."""
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.user_service_pb2.DeleteUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified MongoDB user."""
    GrantPermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.user_service_pb2.GrantUserPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Grants permission to the specified MongoDB user."""
    RevokePermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.user_service_pb2.RevokeUserPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Revokes permission from the specified MongoDB user."""

class UserServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing MongoDB User resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.mongodb.v1.user_service_pb2.GetUserRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mongodb.v1.user_pb2.User:
        """Returns the specified MongoDB User resource.

        To get the list of available MongoDB User resources, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.mongodb.v1.user_service_pb2.ListUsersRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mongodb.v1.user_service_pb2.ListUsersResponse:
        """Retrieves the list of MongoDB User resources in the specified cluster."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.mongodb.v1.user_service_pb2.CreateUserRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a MongoDB user in the specified cluster."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.mongodb.v1.user_service_pb2.UpdateUserRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified MongoDB user."""
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.mongodb.v1.user_service_pb2.DeleteUserRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified MongoDB user."""
    @abc.abstractmethod
    def GrantPermission(
        self,
        request: yandex.cloud.mdb.mongodb.v1.user_service_pb2.GrantUserPermissionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Grants permission to the specified MongoDB user."""
    @abc.abstractmethod
    def RevokePermission(
        self,
        request: yandex.cloud.mdb.mongodb.v1.user_service_pb2.RevokeUserPermissionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Revokes permission from the specified MongoDB user."""

def add_UserServiceServicer_to_server(servicer: UserServiceServicer, server: grpc.Server) -> None: ...
