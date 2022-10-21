"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Service(google.protobuf.message.Message):
    """A Service resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the service."""
    name: builtins.str
    """Name of the service, e.g. `Compute Cloud`, `VPC`."""
    description: builtins.str
    """Description of the service."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "id", b"id", "name", b"name"]) -> None: ...

global___Service = Service
