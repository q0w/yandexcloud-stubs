"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.clickhouse.v1.user_pb2
import yandex.cloud.mdb.clickhouse.v1.user_service_pb2
import yandex.cloud.operation.operation_pb2

class UserServiceStub:
    """A set of methods for managing ClickHouse User resources.
    NOTE: these methods are available only if user management through SQL is disabled.
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.user_service_pb2.GetUserRequest,
        yandex.cloud.mdb.clickhouse.v1.user_pb2.User,
    ]
    """Returns the specified ClickHouse User resource.

    To get the list of available ClickHouse User resources, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.user_service_pb2.ListUsersRequest,
        yandex.cloud.mdb.clickhouse.v1.user_service_pb2.ListUsersResponse,
    ]
    """Retrieves the list of ClickHouse User resources in the specified cluster."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.user_service_pb2.CreateUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a ClickHouse user in the specified cluster."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.user_service_pb2.UpdateUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified ClickHouse user."""
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.user_service_pb2.DeleteUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified ClickHouse user."""
    GrantPermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.user_service_pb2.GrantUserPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Grants a permission to the specified ClickHouse user."""
    RevokePermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.user_service_pb2.RevokeUserPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Revokes a permission from the specified ClickHouse user."""

class UserServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing ClickHouse User resources.
    NOTE: these methods are available only if user management through SQL is disabled.
    """

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.clickhouse.v1.user_service_pb2.GetUserRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.clickhouse.v1.user_pb2.User:
        """Returns the specified ClickHouse User resource.

        To get the list of available ClickHouse User resources, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.clickhouse.v1.user_service_pb2.ListUsersRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.clickhouse.v1.user_service_pb2.ListUsersResponse:
        """Retrieves the list of ClickHouse User resources in the specified cluster."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.clickhouse.v1.user_service_pb2.CreateUserRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a ClickHouse user in the specified cluster."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.clickhouse.v1.user_service_pb2.UpdateUserRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified ClickHouse user."""
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.clickhouse.v1.user_service_pb2.DeleteUserRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified ClickHouse user."""
    @abc.abstractmethod
    def GrantPermission(
        self,
        request: yandex.cloud.mdb.clickhouse.v1.user_service_pb2.GrantUserPermissionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Grants a permission to the specified ClickHouse user."""
    @abc.abstractmethod
    def RevokePermission(
        self,
        request: yandex.cloud.mdb.clickhouse.v1.user_service_pb2.RevokeUserPermissionRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Revokes a permission from the specified ClickHouse user."""

def add_UserServiceServicer_to_server(servicer: UserServiceServicer, server: grpc.Server) -> None: ...
