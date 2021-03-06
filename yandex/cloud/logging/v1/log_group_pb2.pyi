"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class LogGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LogGroup._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: LogGroup._Status.ValueType  # 0
        """Unknown status.

        Should never occur.
        """

        CREATING: LogGroup._Status.ValueType  # 1
        """Log group is creating."""

        ACTIVE: LogGroup._Status.ValueType  # 2
        """Log group is ready to accept messages,"""

        DELETING: LogGroup._Status.ValueType  # 3
        """Log group is being deleted.

        No messages will be accepted.
        """

        ERROR: LogGroup._Status.ValueType  # 4
        """Log group is in failed state."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Possible log group statuses."""
        pass

    STATUS_UNSPECIFIED: LogGroup.Status.ValueType  # 0
    """Unknown status.

    Should never occur.
    """

    CREATING: LogGroup.Status.ValueType  # 1
    """Log group is creating."""

    ACTIVE: LogGroup.Status.ValueType  # 2
    """Log group is ready to accept messages,"""

    DELETING: LogGroup.Status.ValueType  # 3
    """Log group is being deleted.

    No messages will be accepted.
    """

    ERROR: LogGroup.Status.ValueType  # 4
    """Log group is in failed state."""


    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CLOUD_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    RETENTION_PERIOD_FIELD_NUMBER: builtins.int
    DATA_STREAM_FIELD_NUMBER: builtins.int
    id: typing.Text
    """Log group ID."""

    folder_id: typing.Text
    """Log group folder ID."""

    cloud_id: typing.Text
    """Log group cloud ID."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Log group creation time."""
        pass
    name: typing.Text
    """Log group name."""

    description: typing.Text
    """Log group description."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Log group labels."""
        pass
    status: global___LogGroup.Status.ValueType
    """Status of the log group."""

    @property
    def retention_period(self) -> google.protobuf.duration_pb2.Duration:
        """Log group entry retention period.

        Entries will be present in group during this period.
        """
        pass
    data_stream: typing.Text
    """Data stream name"""

    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        cloud_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        status: global___LogGroup.Status.ValueType = ...,
        retention_period: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        data_stream: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","retention_period",b"retention_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_id",b"cloud_id","created_at",b"created_at","data_stream",b"data_stream","description",b"description","folder_id",b"folder_id","id",b"id","labels",b"labels","name",b"name","retention_period",b"retention_period","status",b"status"]) -> None: ...
global___LogGroup = LogGroup
