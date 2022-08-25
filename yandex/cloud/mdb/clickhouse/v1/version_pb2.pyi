"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Version(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DEPRECATED_FIELD_NUMBER: builtins.int
    UPDATABLE_TO_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the version."""
    name: builtins.str
    """Name of the version."""
    deprecated: builtins.bool
    """Whether version is deprecated."""
    @property
    def updatable_to(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of versions that can be updated from current."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        deprecated: builtins.bool = ...,
        updatable_to: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["deprecated", b"deprecated", "id", b"id", "name", b"name", "updatable_to", b"updatable_to"]) -> None: ...

global___Version = Version
