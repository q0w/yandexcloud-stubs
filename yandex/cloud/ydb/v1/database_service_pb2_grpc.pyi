"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.access.access_pb2
import yandex.cloud.operation.operation_pb2
import yandex.cloud.ydb.v1.database_pb2
import yandex.cloud.ydb.v1.database_service_pb2

class DatabaseServiceStub:
    """A set of methods for managing databases."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.GetDatabaseRequest,
        yandex.cloud.ydb.v1.database_pb2.Database,
    ]
    """Returns the specified database."""
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.ListDatabasesRequest,
        yandex.cloud.ydb.v1.database_service_pb2.ListDatabasesResponse,
    ]
    """Retrieves a list of databases."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.CreateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new database."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.UpdateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Modifies the specified database."""
    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.StartDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified database."""
    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.StopDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified database."""
    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.MoveDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.DeleteDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified database."""
    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.RestoreBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Restores the specified backup"""
    Backup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.database_service_pb2.BackupDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

class DatabaseServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing databases."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.GetDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.ydb.v1.database_pb2.Database:
        """Returns the specified database."""
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.ListDatabasesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.ydb.v1.database_service_pb2.ListDatabasesResponse:
        """Retrieves a list of databases."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.CreateDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a new database."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.UpdateDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Modifies the specified database."""
    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.StartDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Starts the specified database."""
    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.StopDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Stops the specified database."""
    @abc.abstractmethod
    def Move(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.MoveDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation: ...
    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.access.access_pb2.ListAccessBindingsResponse: ...
    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation: ...
    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation: ...
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.DeleteDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified database."""
    @abc.abstractmethod
    def Restore(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.RestoreBackupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Restores the specified backup"""
    @abc.abstractmethod
    def Backup(
        self,
        request: yandex.cloud.ydb.v1.database_service_pb2.BackupDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation: ...

def add_DatabaseServiceServicer_to_server(servicer: DatabaseServiceServicer, server: grpc.Server) -> None: ...
