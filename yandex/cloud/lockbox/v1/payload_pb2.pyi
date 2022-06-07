"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Payload(google.protobuf.message.Message):
    """A payload."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Entry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        TEXT_VALUE_FIELD_NUMBER: builtins.int
        BINARY_VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        """Non-confidential key of the entry."""

        text_value: typing.Text
        """Text value."""

        binary_value: builtins.bytes
        """Binary value."""

        def __init__(self,
            *,
            key: typing.Text = ...,
            text_value: typing.Text = ...,
            binary_value: builtins.bytes = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["binary_value",b"binary_value","text_value",b"text_value","value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["binary_value",b"binary_value","key",b"key","text_value",b"text_value","value",b"value"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["text_value","binary_value"]]: ...

    VERSION_ID_FIELD_NUMBER: builtins.int
    ENTRIES_FIELD_NUMBER: builtins.int
    version_id: typing.Text
    """ID of the version that the payload belongs to."""

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Payload.Entry]:
        """Payload entries."""
        pass
    def __init__(self,
        *,
        version_id: typing.Text = ...,
        entries: typing.Optional[typing.Iterable[global___Payload.Entry]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entries",b"entries","version_id",b"version_id"]) -> None: ...
global___Payload = Payload