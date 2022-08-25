"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Backup(google.protobuf.message.Message):
    """A ClickHouse Backup resource. See the [Developer's Guide](/docs/managed-clickhouse/concepts)
    for more information.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    SOURCE_CLUSTER_ID_FIELD_NUMBER: builtins.int
    SOURCE_SHARD_NAMES_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the backup."""
    folder_id: builtins.str
    """ID of the folder that the backup belongs to."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format
        (i.e. when the backup operation was completed).
        """
    source_cluster_id: builtins.str
    """ID of the ClickHouse cluster that the backup was created for."""
    @property
    def source_shard_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of the shards included in the backup."""
    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the backup operation was started."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        source_cluster_id: builtins.str = ...,
        source_shard_names: collections.abc.Iterable[builtins.str] | None = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "started_at", b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "folder_id", b"folder_id", "id", b"id", "source_cluster_id", b"source_cluster_id", "source_shard_names", b"source_shard_names", "started_at", b"started_at"]) -> None: ...

global___Backup = Backup
