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

class Certificate(google.protobuf.message.Message):
    """A certificate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    FEDERATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the certificate."""

    federation_id: typing.Text
    """ID of the federation that the certificate belongs to."""

    name: typing.Text
    """Name of the certificate."""

    description: typing.Text
    """Description of the certificate."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    data: typing.Text
    """Certificate data in PEM format."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        federation_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        data: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","data",b"data","description",b"description","federation_id",b"federation_id","id",b"id","name",b"name"]) -> None: ...
global___Certificate = Certificate
