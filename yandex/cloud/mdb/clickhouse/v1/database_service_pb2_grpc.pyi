"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.clickhouse.v1.database_pb2
import yandex.cloud.mdb.clickhouse.v1.database_service_pb2
import yandex.cloud.operation.operation_pb2

class DatabaseServiceStub:
    """A set of methods for managing ClickHouse Database resources.
    NOTE: these methods are available only if database management through SQL is disabled.
    """
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.database_service_pb2.GetDatabaseRequest,
        yandex.cloud.mdb.clickhouse.v1.database_pb2.Database]
    """Returns the specified ClickHouse Database resource.

    To get the list of available ClickHouse Database resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.database_service_pb2.ListDatabasesRequest,
        yandex.cloud.mdb.clickhouse.v1.database_service_pb2.ListDatabasesResponse]
    """Retrieves the list of ClickHouse Database resources in the specified cluster."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.database_service_pb2.CreateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a new ClickHouse database in the specified cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.database_service_pb2.DeleteDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified ClickHouse database."""


class DatabaseServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing ClickHouse Database resources.
    NOTE: these methods are available only if database management through SQL is disabled.
    """
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.mdb.clickhouse.v1.database_service_pb2.GetDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.clickhouse.v1.database_pb2.Database:
        """Returns the specified ClickHouse Database resource.

        To get the list of available ClickHouse Database resources, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.mdb.clickhouse.v1.database_service_pb2.ListDatabasesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.clickhouse.v1.database_service_pb2.ListDatabasesResponse:
        """Retrieves the list of ClickHouse Database resources in the specified cluster."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.mdb.clickhouse.v1.database_service_pb2.CreateDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a new ClickHouse database in the specified cluster."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.mdb.clickhouse.v1.database_service_pb2.DeleteDatabaseRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified ClickHouse database."""
        pass


def add_DatabaseServiceServicer_to_server(servicer: DatabaseServiceServicer, server: grpc.Server) -> None: ...