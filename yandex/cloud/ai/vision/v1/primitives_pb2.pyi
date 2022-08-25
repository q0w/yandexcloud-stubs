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

class Polygon(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERTICES_FIELD_NUMBER: builtins.int
    @property
    def vertices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Vertex]:
        """The bounding polygon vertices."""
    def __init__(
        self,
        *,
        vertices: collections.abc.Iterable[global___Vertex] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["vertices", b"vertices"]) -> None: ...

global___Polygon = Polygon

class Vertex(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    x: builtins.int
    """X coordinate in pixels."""
    y: builtins.int
    """Y coordinate in pixels."""
    def __init__(
        self,
        *,
        x: builtins.int = ...,
        y: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["x", b"x", "y", b"y"]) -> None: ...

global___Vertex = Vertex
