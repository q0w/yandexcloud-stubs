"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Backup(google.protobuf.message.Message):
    """A MongoDB Backup resource. For more information, see the 
    [Developer's Guide](/docs/managed-mongodb/concepts).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _BackupType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _BackupTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Backup._BackupType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        BACKUP_TYPE_UNSPECIFIED: Backup._BackupType.ValueType  # 0
        AUTOMATED: Backup._BackupType.ValueType  # 1
        """Backup created by automated daily schedule"""

        MANUAL: Backup._BackupType.ValueType  # 2
        """Backup created by user request"""

    class BackupType(_BackupType, metaclass=_BackupTypeEnumTypeWrapper):
        pass

    BACKUP_TYPE_UNSPECIFIED: Backup.BackupType.ValueType  # 0
    AUTOMATED: Backup.BackupType.ValueType  # 1
    """Backup created by automated daily schedule"""

    MANUAL: Backup.BackupType.ValueType  # 2
    """Backup created by user request"""


    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    SOURCE_CLUSTER_ID_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    SOURCE_SHARD_NAMES_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the backup."""

    folder_id: typing.Text
    """ID of the folder that the backup belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format
        (i.e. when the backup operation was completed).
        """
        pass
    source_cluster_id: typing.Text
    """ID of the MongoDB cluster that the backup was created for."""

    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the backup operation was started."""
        pass
    @property
    def source_shard_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Shard names used as a source for backup."""
        pass
    size: builtins.int
    """Size of backup in bytes"""

    type: global___Backup.BackupType.ValueType
    """How this backup was created (manual/automatic/etc...)"""

    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        source_cluster_id: typing.Text = ...,
        started_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        source_shard_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        size: builtins.int = ...,
        type: global___Backup.BackupType.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","started_at",b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","folder_id",b"folder_id","id",b"id","size",b"size","source_cluster_id",b"source_cluster_id","source_shard_names",b"source_shard_names","started_at",b"started_at","type",b"type"]) -> None: ...
global___Backup = Backup
