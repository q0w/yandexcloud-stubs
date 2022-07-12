"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.mdb.kafka.v1.topic_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetTopicRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TOPIC_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster that the topic belongs to.

    To get the cluster ID, make a [ClusterService.List] request.
    """

    topic_name: typing.Text
    """Name of the Kafka topic resource to return.

    To get the name of the topic, make a [TopicService.List] request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        topic_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","topic_name",b"topic_name"]) -> None: ...
global___GetTopicRequest = GetTopicRequest

class ListTopicsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster to list topics in.

    To get the cluster ID, make a [ClusterService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the service returns a [ListTopicsResponse.next_page_token] that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token.

    To get the next page of results, set [page_token] to the [ListTopicsResponse.next_page_token] returned by the previous list request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListTopicsRequest = ListTopicsRequest

class ListTopicsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOPICS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def topics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.kafka.v1.topic_pb2.Topic]:
        """List of Kafka topics."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests.

    If the number of results is larger than [ListTopicsRequest.page_size], use the [next_page_token] as the value for the [ListTopicsRequest.page_token] parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        topics: typing.Optional[typing.Iterable[yandex.cloud.mdb.kafka.v1.topic_pb2.Topic]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","topics",b"topics"]) -> None: ...
global___ListTopicsResponse = ListTopicsResponse

class CreateTopicRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TOPIC_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster to create a topic in.

    To get the cluster ID, make a [ClusterService.List] request.
    """

    @property
    def topic_spec(self) -> yandex.cloud.mdb.kafka.v1.topic_pb2.TopicSpec:
        """Configuration of the topic to create."""
        pass
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        topic_spec: typing.Optional[yandex.cloud.mdb.kafka.v1.topic_pb2.TopicSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["topic_spec",b"topic_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","topic_spec",b"topic_spec"]) -> None: ...
global___CreateTopicRequest = CreateTopicRequest

class CreateTopicMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TOPIC_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster where a topic is being created."""

    topic_name: typing.Text
    """Name of the Kafka topic that is being created."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        topic_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","topic_name",b"topic_name"]) -> None: ...
global___CreateTopicMetadata = CreateTopicMetadata

class UpdateTopicRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TOPIC_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    TOPIC_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster to update a topic in.

    To get the cluster ID, make a [ClusterService.List] request.
    """

    topic_name: typing.Text
    """Name of the topic to update.

    To get the name of the topic, make a [TopicService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def topic_spec(self) -> yandex.cloud.mdb.kafka.v1.topic_pb2.TopicSpec:
        """New configuration of the topic.

        Use [update_mask] to prevent reverting all topic settings that are not listed in [topic_spec] to their default values.
        """
        pass
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        topic_name: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        topic_spec: typing.Optional[yandex.cloud.mdb.kafka.v1.topic_pb2.TopicSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["topic_spec",b"topic_spec","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","topic_name",b"topic_name","topic_spec",b"topic_spec","update_mask",b"update_mask"]) -> None: ...
global___UpdateTopicRequest = UpdateTopicRequest

class UpdateTopicMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TOPIC_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster where a topic is being updated."""

    topic_name: typing.Text
    """Name of the Kafka topic that is being updated."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        topic_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","topic_name",b"topic_name"]) -> None: ...
global___UpdateTopicMetadata = UpdateTopicMetadata

class DeleteTopicRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TOPIC_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster to delete a topic in.

    To get the cluster ID, make a [ClusterService.List] request.
    """

    topic_name: typing.Text
    """Name of the topic to delete.

    To get the name of the topic, make a [TopicService.List] request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        topic_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","topic_name",b"topic_name"]) -> None: ...
global___DeleteTopicRequest = DeleteTopicRequest

class DeleteTopicMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TOPIC_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster where a topic is being deleted."""

    topic_name: typing.Text
    """Name of the Kafka topic that is being deleted."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        topic_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","topic_name",b"topic_name"]) -> None: ...
global___DeleteTopicMetadata = DeleteTopicMetadata
