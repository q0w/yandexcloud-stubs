"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.kafka.v1.topic_pb2
import yandex.cloud.mdb.kafka.v1.topic_service_pb2
import yandex.cloud.operation.operation_pb2

class TopicServiceStub:
    """A set of methods for managing Kafka topics."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.topic_service_pb2.GetTopicRequest,
        yandex.cloud.mdb.kafka.v1.topic_pb2.Topic]
    """Returns the specified Kafka topic.

    To get the list of available Kafka topics, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.topic_service_pb2.ListTopicsRequest,
        yandex.cloud.mdb.kafka.v1.topic_service_pb2.ListTopicsResponse]
    """Retrieves the list of Kafka topics in the specified cluster."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.topic_service_pb2.CreateTopicRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a new Kafka topic in the specified cluster."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.topic_service_pb2.UpdateTopicRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified Kafka topic."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.topic_service_pb2.DeleteTopicRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified Kafka topic."""


class TopicServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Kafka topics."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.mdb.kafka.v1.topic_service_pb2.GetTopicRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.kafka.v1.topic_pb2.Topic:
        """Returns the specified Kafka topic.

        To get the list of available Kafka topics, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.mdb.kafka.v1.topic_service_pb2.ListTopicsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.kafka.v1.topic_service_pb2.ListTopicsResponse:
        """Retrieves the list of Kafka topics in the specified cluster."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.mdb.kafka.v1.topic_service_pb2.CreateTopicRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a new Kafka topic in the specified cluster."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.mdb.kafka.v1.topic_service_pb2.UpdateTopicRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified Kafka topic."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.mdb.kafka.v1.topic_service_pb2.DeleteTopicRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified Kafka topic."""
        pass


def add_TopicServiceServicer_to_server(servicer: TopicServiceServicer, server: grpc.Server) -> None: ...
