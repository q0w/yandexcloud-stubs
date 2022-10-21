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

@typing_extensions.final
class Blob(google.protobuf.message.Message):
    """A Blob resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    DIGEST_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    URLS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Output only. ID of the blob."""
    digest: builtins.str
    """Content-addressable identifier of the blob."""
    size: builtins.int
    """Size of the blob, specified in bytes."""
    @property
    def urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of blob urls."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        digest: builtins.str = ...,
        size: builtins.int = ...,
        urls: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["digest", b"digest", "id", b"id", "size", b"size", "urls", b"urls"]) -> None: ...

global___Blob = Blob
