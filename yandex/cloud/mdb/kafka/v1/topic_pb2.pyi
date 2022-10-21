"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing
import yandex.cloud.mdb.kafka.v1.common_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Topic(google.protobuf.message.Message):
    """An Kafka topic.
    For more information, see the [Concepts -> Topics and partitions](/docs/managed-kafka/concepts/topics) section of the documentation.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PARTITIONS_FIELD_NUMBER: builtins.int
    REPLICATION_FACTOR_FIELD_NUMBER: builtins.int
    TOPIC_CONFIG_2_1_FIELD_NUMBER: builtins.int
    TOPIC_CONFIG_2_6_FIELD_NUMBER: builtins.int
    TOPIC_CONFIG_2_8_FIELD_NUMBER: builtins.int
    TOPIC_CONFIG_3_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the topic."""
    cluster_id: builtins.str
    """ID of an Apache Kafka® cluster that the topic belongs to.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    @property
    def partitions(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of the topic's partitions."""
    @property
    def replication_factor(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Amount of data copies (replicas) for the topic in the cluster."""
    @property
    def topic_config_2_1(self) -> global___TopicConfig2_1: ...
    @property
    def topic_config_2_6(self) -> global___TopicConfig2_6: ...
    @property
    def topic_config_2_8(self) -> global___TopicConfig2_8: ...
    @property
    def topic_config_3(self) -> global___TopicConfig3: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
        partitions: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        replication_factor: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        topic_config_2_1: global___TopicConfig2_1 | None = ...,
        topic_config_2_6: global___TopicConfig2_6 | None = ...,
        topic_config_2_8: global___TopicConfig2_8 | None = ...,
        topic_config_3: global___TopicConfig3 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partitions", b"partitions", "replication_factor", b"replication_factor", "topic_config", b"topic_config", "topic_config_2_1", b"topic_config_2_1", "topic_config_2_6", b"topic_config_2_6", "topic_config_2_8", b"topic_config_2_8", "topic_config_3", b"topic_config_3"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "name", b"name", "partitions", b"partitions", "replication_factor", b"replication_factor", "topic_config", b"topic_config", "topic_config_2_1", b"topic_config_2_1", "topic_config_2_6", b"topic_config_2_6", "topic_config_2_8", b"topic_config_2_8", "topic_config_3", b"topic_config_3"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["topic_config", b"topic_config"]) -> typing_extensions.Literal["topic_config_2_1", "topic_config_2_6", "topic_config_2_8", "topic_config_3"] | None: ...

global___Topic = Topic

@typing_extensions.final
class TopicSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    PARTITIONS_FIELD_NUMBER: builtins.int
    REPLICATION_FACTOR_FIELD_NUMBER: builtins.int
    TOPIC_CONFIG_2_1_FIELD_NUMBER: builtins.int
    TOPIC_CONFIG_2_6_FIELD_NUMBER: builtins.int
    TOPIC_CONFIG_2_8_FIELD_NUMBER: builtins.int
    TOPIC_CONFIG_3_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the topic."""
    @property
    def partitions(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of the topic's partitions."""
    @property
    def replication_factor(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Amount of copies of a topic data kept in the cluster."""
    @property
    def topic_config_2_1(self) -> global___TopicConfig2_1: ...
    @property
    def topic_config_2_6(self) -> global___TopicConfig2_6: ...
    @property
    def topic_config_2_8(self) -> global___TopicConfig2_8: ...
    @property
    def topic_config_3(self) -> global___TopicConfig3: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        partitions: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        replication_factor: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        topic_config_2_1: global___TopicConfig2_1 | None = ...,
        topic_config_2_6: global___TopicConfig2_6 | None = ...,
        topic_config_2_8: global___TopicConfig2_8 | None = ...,
        topic_config_3: global___TopicConfig3 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partitions", b"partitions", "replication_factor", b"replication_factor", "topic_config", b"topic_config", "topic_config_2_1", b"topic_config_2_1", "topic_config_2_6", b"topic_config_2_6", "topic_config_2_8", b"topic_config_2_8", "topic_config_3", b"topic_config_3"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "partitions", b"partitions", "replication_factor", b"replication_factor", "topic_config", b"topic_config", "topic_config_2_1", b"topic_config_2_1", "topic_config_2_6", b"topic_config_2_6", "topic_config_2_8", b"topic_config_2_8", "topic_config_3", b"topic_config_3"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["topic_config", b"topic_config"]) -> typing_extensions.Literal["topic_config_2_1", "topic_config_2_6", "topic_config_2_8", "topic_config_3"] | None: ...

global___TopicSpec = TopicSpec

@typing_extensions.final
class TopicConfig2_1(google.protobuf.message.Message):
    """Deprecated. Version `2.1` of Kafka not supported in Yandex Cloud."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _CleanupPolicy:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CleanupPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TopicConfig2_1._CleanupPolicy.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CLEANUP_POLICY_UNSPECIFIED: TopicConfig2_1._CleanupPolicy.ValueType  # 0
        CLEANUP_POLICY_DELETE: TopicConfig2_1._CleanupPolicy.ValueType  # 1
        """this policy discards log segments when either their retention time or log size limit is reached. See also: [KafkaConfig2_1.log_retention_ms] and other similar parameters."""
        CLEANUP_POLICY_COMPACT: TopicConfig2_1._CleanupPolicy.ValueType  # 2
        """this policy compacts messages in log."""
        CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig2_1._CleanupPolicy.ValueType  # 3
        """this policy use both compaction and deletion for messages and log segments."""

    class CleanupPolicy(_CleanupPolicy, metaclass=_CleanupPolicyEnumTypeWrapper): ...
    CLEANUP_POLICY_UNSPECIFIED: TopicConfig2_1.CleanupPolicy.ValueType  # 0
    CLEANUP_POLICY_DELETE: TopicConfig2_1.CleanupPolicy.ValueType  # 1
    """this policy discards log segments when either their retention time or log size limit is reached. See also: [KafkaConfig2_1.log_retention_ms] and other similar parameters."""
    CLEANUP_POLICY_COMPACT: TopicConfig2_1.CleanupPolicy.ValueType  # 2
    """this policy compacts messages in log."""
    CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig2_1.CleanupPolicy.ValueType  # 3
    """this policy use both compaction and deletion for messages and log segments."""

    CLEANUP_POLICY_FIELD_NUMBER: builtins.int
    COMPRESSION_TYPE_FIELD_NUMBER: builtins.int
    DELETE_RETENTION_MS_FIELD_NUMBER: builtins.int
    FILE_DELETE_DELAY_MS_FIELD_NUMBER: builtins.int
    FLUSH_MESSAGES_FIELD_NUMBER: builtins.int
    FLUSH_MS_FIELD_NUMBER: builtins.int
    MIN_COMPACTION_LAG_MS_FIELD_NUMBER: builtins.int
    RETENTION_BYTES_FIELD_NUMBER: builtins.int
    RETENTION_MS_FIELD_NUMBER: builtins.int
    MAX_MESSAGE_BYTES_FIELD_NUMBER: builtins.int
    MIN_INSYNC_REPLICAS_FIELD_NUMBER: builtins.int
    SEGMENT_BYTES_FIELD_NUMBER: builtins.int
    PREALLOCATE_FIELD_NUMBER: builtins.int
    cleanup_policy: global___TopicConfig2_1.CleanupPolicy.ValueType
    """Retention policy to use on old log messages."""
    compression_type: yandex.cloud.mdb.kafka.v1.common_pb2.CompressionType.ValueType
    """The compression type for a given topic."""
    @property
    def delete_retention_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The amount of time in milliseconds to retain delete tombstone markers for log compacted topics."""
    @property
    def file_delete_delay_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The time to wait before deleting a file from the filesystem."""
    @property
    def flush_messages(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of messages accumulated on a log partition before messages are flushed to disk.

        This setting overrides the cluster-level [KafkaConfig2_1.log_flush_interval_messages] setting on the topic level.
        """
    @property
    def flush_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum time in milliseconds that a message in the topic is kept in memory before flushed to disk.

        This setting overrides the cluster-level [KafkaConfig2_1.log_flush_interval_ms] setting on the topic level.
        """
    @property
    def min_compaction_lag_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The minimum time in milliseconds a message will remain uncompacted in the log."""
    @property
    def retention_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum size a partition can grow to before Kafka will discard old log segments to free up space if the `delete` [cleanup_policy] is in effect.
        It is helpful if you need to control the size of log due to limited disk space.

        This setting overrides the cluster-level [KafkaConfig2_1.log_retention_bytes] setting on the topic level.
        """
    @property
    def retention_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of milliseconds to keep a log segment's file before deleting it.

        This setting overrides the cluster-level [KafkaConfig2_1.log_retention_ms] setting on the topic level.
        """
    @property
    def max_message_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The largest record batch size allowed in topic."""
    @property
    def min_insync_replicas(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This configuration specifies the minimum number of replicas that must acknowledge a write to topic for the write
        to be considered successful (when a producer sets acks to "all").
        """
    @property
    def segment_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This configuration controls the segment file size for the log. Retention and cleaning is always done a file
        at a time so a larger segment size means fewer files but less granular control over retention.

        This setting overrides the cluster-level [KafkaConfig2_1.log_segment_bytes] setting on the topic level.
        """
    @property
    def preallocate(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """True if we should preallocate the file on disk when creating a new log segment.

        This setting overrides the cluster-level [KafkaConfig2_1.log_preallocate] setting on the topic level.
        """
    def __init__(
        self,
        *,
        cleanup_policy: global___TopicConfig2_1.CleanupPolicy.ValueType = ...,
        compression_type: yandex.cloud.mdb.kafka.v1.common_pb2.CompressionType.ValueType = ...,
        delete_retention_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        file_delete_delay_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        flush_messages: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        flush_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        min_compaction_lag_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        retention_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        retention_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_message_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        min_insync_replicas: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        segment_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        preallocate: google.protobuf.wrappers_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delete_retention_ms", b"delete_retention_ms", "file_delete_delay_ms", b"file_delete_delay_ms", "flush_messages", b"flush_messages", "flush_ms", b"flush_ms", "max_message_bytes", b"max_message_bytes", "min_compaction_lag_ms", b"min_compaction_lag_ms", "min_insync_replicas", b"min_insync_replicas", "preallocate", b"preallocate", "retention_bytes", b"retention_bytes", "retention_ms", b"retention_ms", "segment_bytes", b"segment_bytes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cleanup_policy", b"cleanup_policy", "compression_type", b"compression_type", "delete_retention_ms", b"delete_retention_ms", "file_delete_delay_ms", b"file_delete_delay_ms", "flush_messages", b"flush_messages", "flush_ms", b"flush_ms", "max_message_bytes", b"max_message_bytes", "min_compaction_lag_ms", b"min_compaction_lag_ms", "min_insync_replicas", b"min_insync_replicas", "preallocate", b"preallocate", "retention_bytes", b"retention_bytes", "retention_ms", b"retention_ms", "segment_bytes", b"segment_bytes"]) -> None: ...

global___TopicConfig2_1 = TopicConfig2_1

@typing_extensions.final
class TopicConfig2_6(google.protobuf.message.Message):
    """Deprecated. Version `2.6` of Kafka not supported in Yandex Cloud."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _CleanupPolicy:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CleanupPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TopicConfig2_6._CleanupPolicy.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CLEANUP_POLICY_UNSPECIFIED: TopicConfig2_6._CleanupPolicy.ValueType  # 0
        CLEANUP_POLICY_DELETE: TopicConfig2_6._CleanupPolicy.ValueType  # 1
        """this policy discards log segments when either their retention time or log size limit is reached. See also: [KafkaConfig2_1.log_retention_ms] and other similar parameters."""
        CLEANUP_POLICY_COMPACT: TopicConfig2_6._CleanupPolicy.ValueType  # 2
        """this policy compacts messages in log."""
        CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig2_6._CleanupPolicy.ValueType  # 3
        """this policy use both compaction and deletion for messages and log segments."""

    class CleanupPolicy(_CleanupPolicy, metaclass=_CleanupPolicyEnumTypeWrapper): ...
    CLEANUP_POLICY_UNSPECIFIED: TopicConfig2_6.CleanupPolicy.ValueType  # 0
    CLEANUP_POLICY_DELETE: TopicConfig2_6.CleanupPolicy.ValueType  # 1
    """this policy discards log segments when either their retention time or log size limit is reached. See also: [KafkaConfig2_1.log_retention_ms] and other similar parameters."""
    CLEANUP_POLICY_COMPACT: TopicConfig2_6.CleanupPolicy.ValueType  # 2
    """this policy compacts messages in log."""
    CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig2_6.CleanupPolicy.ValueType  # 3
    """this policy use both compaction and deletion for messages and log segments."""

    CLEANUP_POLICY_FIELD_NUMBER: builtins.int
    COMPRESSION_TYPE_FIELD_NUMBER: builtins.int
    DELETE_RETENTION_MS_FIELD_NUMBER: builtins.int
    FILE_DELETE_DELAY_MS_FIELD_NUMBER: builtins.int
    FLUSH_MESSAGES_FIELD_NUMBER: builtins.int
    FLUSH_MS_FIELD_NUMBER: builtins.int
    MIN_COMPACTION_LAG_MS_FIELD_NUMBER: builtins.int
    RETENTION_BYTES_FIELD_NUMBER: builtins.int
    RETENTION_MS_FIELD_NUMBER: builtins.int
    MAX_MESSAGE_BYTES_FIELD_NUMBER: builtins.int
    MIN_INSYNC_REPLICAS_FIELD_NUMBER: builtins.int
    SEGMENT_BYTES_FIELD_NUMBER: builtins.int
    PREALLOCATE_FIELD_NUMBER: builtins.int
    cleanup_policy: global___TopicConfig2_6.CleanupPolicy.ValueType
    """Retention policy to use on old log messages."""
    compression_type: yandex.cloud.mdb.kafka.v1.common_pb2.CompressionType.ValueType
    """The compression type for a given topic."""
    @property
    def delete_retention_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The amount of time in milliseconds to retain delete tombstone markers for log compacted topics."""
    @property
    def file_delete_delay_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The time to wait before deleting a file from the filesystem."""
    @property
    def flush_messages(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of messages accumulated on a log partition before messages are flushed to disk.

        This setting overrides the cluster-level [KafkaConfig2_6.log_flush_interval_messages] setting on the topic level.
        """
    @property
    def flush_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum time in milliseconds that a message in the topic is kept in memory before flushed to disk.

        This setting overrides the cluster-level [KafkaConfig2_6.log_flush_interval_ms] setting on the topic level.
        """
    @property
    def min_compaction_lag_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The minimum time in milliseconds a message will remain uncompacted in the log."""
    @property
    def retention_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum size a partition can grow to before Kafka will discard old log segments to free up space if the `delete` [cleanup_policy] is in effect.
        It is helpful if you need to control the size of log due to limited disk space.

        This setting overrides the cluster-level [KafkaConfig2_6.log_retention_bytes] setting on the topic level.
        """
    @property
    def retention_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of milliseconds to keep a log segment's file before deleting it.

        This setting overrides the cluster-level [KafkaConfig2_6.log_retention_ms] setting on the topic level.
        """
    @property
    def max_message_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The largest record batch size allowed in topic."""
    @property
    def min_insync_replicas(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This configuration specifies the minimum number of replicas that must acknowledge a write to topic for the write
        to be considered successful (when a producer sets acks to "all").
        """
    @property
    def segment_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This configuration controls the segment file size for the log. Retention and cleaning is always done a file
        at a time so a larger segment size means fewer files but less granular control over retention.

        This setting overrides the cluster-level [KafkaConfig2_6.log_segment_bytes] setting on the topic level.
        """
    @property
    def preallocate(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """True if we should preallocate the file on disk when creating a new log segment.

        This setting overrides the cluster-level [KafkaConfig2_6.log_preallocate] setting on the topic level.
        """
    def __init__(
        self,
        *,
        cleanup_policy: global___TopicConfig2_6.CleanupPolicy.ValueType = ...,
        compression_type: yandex.cloud.mdb.kafka.v1.common_pb2.CompressionType.ValueType = ...,
        delete_retention_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        file_delete_delay_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        flush_messages: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        flush_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        min_compaction_lag_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        retention_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        retention_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_message_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        min_insync_replicas: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        segment_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        preallocate: google.protobuf.wrappers_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delete_retention_ms", b"delete_retention_ms", "file_delete_delay_ms", b"file_delete_delay_ms", "flush_messages", b"flush_messages", "flush_ms", b"flush_ms", "max_message_bytes", b"max_message_bytes", "min_compaction_lag_ms", b"min_compaction_lag_ms", "min_insync_replicas", b"min_insync_replicas", "preallocate", b"preallocate", "retention_bytes", b"retention_bytes", "retention_ms", b"retention_ms", "segment_bytes", b"segment_bytes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cleanup_policy", b"cleanup_policy", "compression_type", b"compression_type", "delete_retention_ms", b"delete_retention_ms", "file_delete_delay_ms", b"file_delete_delay_ms", "flush_messages", b"flush_messages", "flush_ms", b"flush_ms", "max_message_bytes", b"max_message_bytes", "min_compaction_lag_ms", b"min_compaction_lag_ms", "min_insync_replicas", b"min_insync_replicas", "preallocate", b"preallocate", "retention_bytes", b"retention_bytes", "retention_ms", b"retention_ms", "segment_bytes", b"segment_bytes"]) -> None: ...

global___TopicConfig2_6 = TopicConfig2_6

@typing_extensions.final
class TopicConfig2_8(google.protobuf.message.Message):
    """A topic settings for 2.8"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _CleanupPolicy:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CleanupPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TopicConfig2_8._CleanupPolicy.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CLEANUP_POLICY_UNSPECIFIED: TopicConfig2_8._CleanupPolicy.ValueType  # 0
        CLEANUP_POLICY_DELETE: TopicConfig2_8._CleanupPolicy.ValueType  # 1
        """this policy discards log segments when either their retention time or log size limit is reached. See also: [KafkaConfig2_1.log_retention_ms] and other similar parameters."""
        CLEANUP_POLICY_COMPACT: TopicConfig2_8._CleanupPolicy.ValueType  # 2
        """this policy compacts messages in log."""
        CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig2_8._CleanupPolicy.ValueType  # 3
        """this policy use both compaction and deletion for messages and log segments."""

    class CleanupPolicy(_CleanupPolicy, metaclass=_CleanupPolicyEnumTypeWrapper): ...
    CLEANUP_POLICY_UNSPECIFIED: TopicConfig2_8.CleanupPolicy.ValueType  # 0
    CLEANUP_POLICY_DELETE: TopicConfig2_8.CleanupPolicy.ValueType  # 1
    """this policy discards log segments when either their retention time or log size limit is reached. See also: [KafkaConfig2_1.log_retention_ms] and other similar parameters."""
    CLEANUP_POLICY_COMPACT: TopicConfig2_8.CleanupPolicy.ValueType  # 2
    """this policy compacts messages in log."""
    CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig2_8.CleanupPolicy.ValueType  # 3
    """this policy use both compaction and deletion for messages and log segments."""

    CLEANUP_POLICY_FIELD_NUMBER: builtins.int
    COMPRESSION_TYPE_FIELD_NUMBER: builtins.int
    DELETE_RETENTION_MS_FIELD_NUMBER: builtins.int
    FILE_DELETE_DELAY_MS_FIELD_NUMBER: builtins.int
    FLUSH_MESSAGES_FIELD_NUMBER: builtins.int
    FLUSH_MS_FIELD_NUMBER: builtins.int
    MIN_COMPACTION_LAG_MS_FIELD_NUMBER: builtins.int
    RETENTION_BYTES_FIELD_NUMBER: builtins.int
    RETENTION_MS_FIELD_NUMBER: builtins.int
    MAX_MESSAGE_BYTES_FIELD_NUMBER: builtins.int
    MIN_INSYNC_REPLICAS_FIELD_NUMBER: builtins.int
    SEGMENT_BYTES_FIELD_NUMBER: builtins.int
    PREALLOCATE_FIELD_NUMBER: builtins.int
    cleanup_policy: global___TopicConfig2_8.CleanupPolicy.ValueType
    """Retention policy to use on old log messages."""
    compression_type: yandex.cloud.mdb.kafka.v1.common_pb2.CompressionType.ValueType
    """The compression type for a given topic."""
    @property
    def delete_retention_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The amount of time in milliseconds to retain delete tombstone markers for log compacted topics."""
    @property
    def file_delete_delay_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The time to wait before deleting a file from the filesystem."""
    @property
    def flush_messages(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of messages accumulated on a log partition before messages are flushed to disk.

        This setting overrides the cluster-level [KafkaConfig2_8.log_flush_interval_messages] setting on the topic level.
        """
    @property
    def flush_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum time in milliseconds that a message in the topic is kept in memory before flushed to disk.

        This setting overrides the cluster-level [KafkaConfig2_8.log_flush_interval_ms] setting on the topic level.
        """
    @property
    def min_compaction_lag_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The minimum time in milliseconds a message will remain uncompacted in the log."""
    @property
    def retention_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum size a partition can grow to before Kafka will discard old log segments to free up space if the `delete` [cleanup_policy] is in effect.
        It is helpful if you need to control the size of log due to limited disk space.

        This setting overrides the cluster-level [KafkaConfig2_8.log_retention_bytes] setting on the topic level.
        """
    @property
    def retention_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of milliseconds to keep a log segment's file before deleting it.

        This setting overrides the cluster-level [KafkaConfig2_8.log_retention_ms] setting on the topic level.
        """
    @property
    def max_message_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The largest record batch size allowed in topic."""
    @property
    def min_insync_replicas(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This configuration specifies the minimum number of replicas that must acknowledge a write to topic for the write
        to be considered successful (when a producer sets acks to "all").
        """
    @property
    def segment_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This configuration controls the segment file size for the log. Retention and cleaning is always done a file
        at a time so a larger segment size means fewer files but less granular control over retention.

        This setting overrides the cluster-level [KafkaConfig2_8.log_segment_bytes] setting on the topic level.
        """
    @property
    def preallocate(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """True if we should preallocate the file on disk when creating a new log segment.

        This setting overrides the cluster-level [KafkaConfig2_8.log_preallocate] setting on the topic level.
        """
    def __init__(
        self,
        *,
        cleanup_policy: global___TopicConfig2_8.CleanupPolicy.ValueType = ...,
        compression_type: yandex.cloud.mdb.kafka.v1.common_pb2.CompressionType.ValueType = ...,
        delete_retention_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        file_delete_delay_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        flush_messages: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        flush_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        min_compaction_lag_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        retention_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        retention_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_message_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        min_insync_replicas: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        segment_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        preallocate: google.protobuf.wrappers_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delete_retention_ms", b"delete_retention_ms", "file_delete_delay_ms", b"file_delete_delay_ms", "flush_messages", b"flush_messages", "flush_ms", b"flush_ms", "max_message_bytes", b"max_message_bytes", "min_compaction_lag_ms", b"min_compaction_lag_ms", "min_insync_replicas", b"min_insync_replicas", "preallocate", b"preallocate", "retention_bytes", b"retention_bytes", "retention_ms", b"retention_ms", "segment_bytes", b"segment_bytes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cleanup_policy", b"cleanup_policy", "compression_type", b"compression_type", "delete_retention_ms", b"delete_retention_ms", "file_delete_delay_ms", b"file_delete_delay_ms", "flush_messages", b"flush_messages", "flush_ms", b"flush_ms", "max_message_bytes", b"max_message_bytes", "min_compaction_lag_ms", b"min_compaction_lag_ms", "min_insync_replicas", b"min_insync_replicas", "preallocate", b"preallocate", "retention_bytes", b"retention_bytes", "retention_ms", b"retention_ms", "segment_bytes", b"segment_bytes"]) -> None: ...

global___TopicConfig2_8 = TopicConfig2_8

@typing_extensions.final
class TopicConfig3(google.protobuf.message.Message):
    """A topic settings for 3.x"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _CleanupPolicy:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CleanupPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TopicConfig3._CleanupPolicy.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CLEANUP_POLICY_UNSPECIFIED: TopicConfig3._CleanupPolicy.ValueType  # 0
        CLEANUP_POLICY_DELETE: TopicConfig3._CleanupPolicy.ValueType  # 1
        """this policy discards log segments when either their retention time or log size limit is reached. See also: [KafkaConfig3.log_retention_ms] and other similar parameters."""
        CLEANUP_POLICY_COMPACT: TopicConfig3._CleanupPolicy.ValueType  # 2
        """this policy compacts messages in log."""
        CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig3._CleanupPolicy.ValueType  # 3
        """this policy use both compaction and deletion for messages and log segments."""

    class CleanupPolicy(_CleanupPolicy, metaclass=_CleanupPolicyEnumTypeWrapper): ...
    CLEANUP_POLICY_UNSPECIFIED: TopicConfig3.CleanupPolicy.ValueType  # 0
    CLEANUP_POLICY_DELETE: TopicConfig3.CleanupPolicy.ValueType  # 1
    """this policy discards log segments when either their retention time or log size limit is reached. See also: [KafkaConfig3.log_retention_ms] and other similar parameters."""
    CLEANUP_POLICY_COMPACT: TopicConfig3.CleanupPolicy.ValueType  # 2
    """this policy compacts messages in log."""
    CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig3.CleanupPolicy.ValueType  # 3
    """this policy use both compaction and deletion for messages and log segments."""

    CLEANUP_POLICY_FIELD_NUMBER: builtins.int
    COMPRESSION_TYPE_FIELD_NUMBER: builtins.int
    DELETE_RETENTION_MS_FIELD_NUMBER: builtins.int
    FILE_DELETE_DELAY_MS_FIELD_NUMBER: builtins.int
    FLUSH_MESSAGES_FIELD_NUMBER: builtins.int
    FLUSH_MS_FIELD_NUMBER: builtins.int
    MIN_COMPACTION_LAG_MS_FIELD_NUMBER: builtins.int
    RETENTION_BYTES_FIELD_NUMBER: builtins.int
    RETENTION_MS_FIELD_NUMBER: builtins.int
    MAX_MESSAGE_BYTES_FIELD_NUMBER: builtins.int
    MIN_INSYNC_REPLICAS_FIELD_NUMBER: builtins.int
    SEGMENT_BYTES_FIELD_NUMBER: builtins.int
    PREALLOCATE_FIELD_NUMBER: builtins.int
    cleanup_policy: global___TopicConfig3.CleanupPolicy.ValueType
    """Retention policy to use on old log messages."""
    compression_type: yandex.cloud.mdb.kafka.v1.common_pb2.CompressionType.ValueType
    """The compression type for a given topic."""
    @property
    def delete_retention_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The amount of time in milliseconds to retain delete tombstone markers for log compacted topics."""
    @property
    def file_delete_delay_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The time to wait before deleting a file from the filesystem."""
    @property
    def flush_messages(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of messages accumulated on a log partition before messages are flushed to disk.

        This setting overrides the cluster-level [KafkaConfig3.log_flush_interval_messages] setting on the topic level.
        """
    @property
    def flush_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum time in milliseconds that a message in the topic is kept in memory before flushed to disk.

        This setting overrides the cluster-level [KafkaConfig3.log_flush_interval_ms] setting on the topic level.
        """
    @property
    def min_compaction_lag_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The minimum time in milliseconds a message will remain uncompacted in the log."""
    @property
    def retention_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum size a partition can grow to before Kafka will discard old log segments to free up space if the `delete` [cleanup_policy] is in effect.
        It is helpful if you need to control the size of log due to limited disk space.

        This setting overrides the cluster-level [KafkaConfig3.log_retention_bytes] setting on the topic level.
        """
    @property
    def retention_ms(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of milliseconds to keep a log segment's file before deleting it.

        This setting overrides the cluster-level [KafkaConfig3.log_retention_ms] setting on the topic level.
        """
    @property
    def max_message_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The largest record batch size allowed in topic."""
    @property
    def min_insync_replicas(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This configuration specifies the minimum number of replicas that must acknowledge a write to topic for the write
        to be considered successful (when a producer sets acks to "all").
        """
    @property
    def segment_bytes(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This configuration controls the segment file size for the log. Retention and cleaning is always done a file
        at a time so a larger segment size means fewer files but less granular control over retention.

        This setting overrides the cluster-level [KafkaConfig3.log_segment_bytes] setting on the topic level.
        """
    @property
    def preallocate(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """True if we should preallocate the file on disk when creating a new log segment.

        This setting overrides the cluster-level [KafkaConfig3.log_preallocate] setting on the topic level.
        """
    def __init__(
        self,
        *,
        cleanup_policy: global___TopicConfig3.CleanupPolicy.ValueType = ...,
        compression_type: yandex.cloud.mdb.kafka.v1.common_pb2.CompressionType.ValueType = ...,
        delete_retention_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        file_delete_delay_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        flush_messages: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        flush_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        min_compaction_lag_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        retention_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        retention_ms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_message_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        min_insync_replicas: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        segment_bytes: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        preallocate: google.protobuf.wrappers_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delete_retention_ms", b"delete_retention_ms", "file_delete_delay_ms", b"file_delete_delay_ms", "flush_messages", b"flush_messages", "flush_ms", b"flush_ms", "max_message_bytes", b"max_message_bytes", "min_compaction_lag_ms", b"min_compaction_lag_ms", "min_insync_replicas", b"min_insync_replicas", "preallocate", b"preallocate", "retention_bytes", b"retention_bytes", "retention_ms", b"retention_ms", "segment_bytes", b"segment_bytes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cleanup_policy", b"cleanup_policy", "compression_type", b"compression_type", "delete_retention_ms", b"delete_retention_ms", "file_delete_delay_ms", b"file_delete_delay_ms", "flush_messages", b"flush_messages", "flush_ms", b"flush_ms", "max_message_bytes", b"max_message_bytes", "min_compaction_lag_ms", b"min_compaction_lag_ms", "min_insync_replicas", b"min_insync_replicas", "preallocate", b"preallocate", "retention_bytes", b"retention_bytes", "retention_ms", b"retention_ms", "segment_bytes", b"segment_bytes"]) -> None: ...

global___TopicConfig3 = TopicConfig3
