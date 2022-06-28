"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.kafka.v1.connector_pb2
import yandex.cloud.mdb.kafka.v1.connector_service_pb2
import yandex.cloud.operation.operation_pb2

class ConnectorServiceStub:
    """A set of methods for managing Apache Kafka® connectors."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.GetConnectorRequest,
        yandex.cloud.mdb.kafka.v1.connector_pb2.Connector]
    """Returns information about an Apache Kafka® connector."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsRequest,
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsResponse]
    """Retrieves the list of Apache Kafka® connectors in a cluster."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.CreateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a new Apache Kafka® connector in a cluster."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.UpdateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates an Apache Kafka® connector."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.DeleteConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes an Apache Kafka® connector."""

    Resume: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ResumeConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Resumes an Apache Kafka® connector."""

    Pause: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.PauseConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Pauses an Apache Kafka® connector."""


class ConnectorServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Apache Kafka® connectors."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.GetConnectorRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.kafka.v1.connector_pb2.Connector:
        """Returns information about an Apache Kafka® connector."""
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsResponse:
        """Retrieves the list of Apache Kafka® connectors in a cluster."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.CreateConnectorRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a new Apache Kafka® connector in a cluster."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.UpdateConnectorRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates an Apache Kafka® connector."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.DeleteConnectorRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes an Apache Kafka® connector."""
        pass

    @abc.abstractmethod
    def Resume(self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.ResumeConnectorRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Resumes an Apache Kafka® connector."""
        pass

    @abc.abstractmethod
    def Pause(self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.PauseConnectorRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Pauses an Apache Kafka® connector."""
        pass


def add_ConnectorServiceServicer_to_server(servicer: ConnectorServiceServicer, server: grpc.Server) -> None: ...
