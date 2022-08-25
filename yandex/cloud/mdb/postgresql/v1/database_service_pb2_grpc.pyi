"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.postgresql.v1.database_pb2
import yandex.cloud.mdb.postgresql.v1.database_service_pb2
import yandex.cloud.operation.operation_pb2

class DatabaseServiceStub:
    """A set of methods for managing PostgreSQL Database resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.postgresql.v1.database_service_pb2.GetDatabaseRequest,
        yandex.cloud.mdb.postgresql.v1.database_pb2.Database,
    ]
    """Returns the specified PostgreSQL Database resource.

    To get the list of available PostgreSQL Database resources, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.postgresql.v1.database_service_pb2.ListDatabasesRequest,
        yandex.cloud.mdb.postgresql.v1.database_service_pb2.ListDatabasesResponse,
    ]
    """Retrieves the list of PostgreSQL Database resources in the specified cluster."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.postgresql.v1.database_service_pb2.CreateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new PostgreSQL database in the specified cluster."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.postgresql.v1.database_service_pb2.UpdateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified PostgreSQL database."""
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.postgresql.v1.database_service_pb2.DeleteDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified PostgreSQL database."""

class DatabaseServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing PostgreSQL Database resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.postgresql.v1.database_service_pb2.GetDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.postgresql.v1.database_pb2.Database:
        """Returns the specified PostgreSQL Database resource.

        To get the list of available PostgreSQL Database resources, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.postgresql.v1.database_service_pb2.ListDatabasesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.postgresql.v1.database_service_pb2.ListDatabasesResponse:
        """Retrieves the list of PostgreSQL Database resources in the specified cluster."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.postgresql.v1.database_service_pb2.CreateDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a new PostgreSQL database in the specified cluster."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.postgresql.v1.database_service_pb2.UpdateDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified PostgreSQL database."""
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.postgresql.v1.database_service_pb2.DeleteDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified PostgreSQL database."""

def add_DatabaseServiceServicer_to_server(servicer: DatabaseServiceServicer, server: grpc.Server) -> None: ...
