"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Backup(google.protobuf.message.Message):
    """An object that represents MySQL backup.

    See [the documentation](/docs/managed-mysql/concepts/backup) for details.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    SOURCE_CLUSTER_ID_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the backup."""

    folder_id: typing.Text
    """ID of the folder that the backup belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp (the time when the backup operation was completed)."""
        pass
    source_cluster_id: typing.Text
    """ID of the cluster that the backup was created for."""

    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Start timestamp (the time when the backup operation was started)."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        source_cluster_id: typing.Text = ...,
        started_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","started_at",b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","folder_id",b"folder_id","id",b"id","source_cluster_id",b"source_cluster_id","started_at",b"started_at"]) -> None: ...
global___Backup = Backup