"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.clickhouse.v1.format_schema_pb2
import yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2
import yandex.cloud.operation.operation_pb2

class FormatSchemaServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.GetFormatSchemaRequest,
        yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchema]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.ListFormatSchemasRequest,
        yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.ListFormatSchemasResponse]

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.CreateFormatSchemaRequest,
        yandex.cloud.operation.operation_pb2.Operation]

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.UpdateFormatSchemaRequest,
        yandex.cloud.operation.operation_pb2.Operation]

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.DeleteFormatSchemaRequest,
        yandex.cloud.operation.operation_pb2.Operation]


class FormatSchemaServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.GetFormatSchemaRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchema: ...

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.ListFormatSchemasRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.ListFormatSchemasResponse: ...

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.CreateFormatSchemaRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation: ...

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.UpdateFormatSchemaRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation: ...

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2.DeleteFormatSchemaRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation: ...


def add_FormatSchemaServiceServicer_to_server(servicer: FormatSchemaServiceServicer, server: grpc.Server) -> None: ...