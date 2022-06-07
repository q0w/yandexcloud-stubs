"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Repository(google.protobuf.message.Message):
    """A Repository resource. For more information, see [Repository](/docs/cloud/container-registry/repository)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the repository.
    The name is unique within the registry.
    """

    id: typing.Text
    """Output only. ID of the repository."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","name",b"name"]) -> None: ...
global___Repository = Repository