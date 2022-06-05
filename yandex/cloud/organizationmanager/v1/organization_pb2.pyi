"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Organization(google.protobuf.message.Message):
    """An Organization resource. For more information, see [Organization](/docs/organization/enable-org)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
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
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the organization."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    name: typing.Text
    """Name of the organization. 3-63 characters long."""

    description: typing.Text
    """Description of the organization. 0-256 characters long."""

    title: typing.Text
    """Display name of the organization. 0-256 characters long."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `` key:value `` pairs. Maximum of 64 per resource."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        title: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","description",b"description","id",b"id","labels",b"labels","name",b"name","title",b"title"]) -> None: ...
global___Organization = Organization
