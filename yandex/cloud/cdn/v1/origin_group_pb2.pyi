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
import yandex.cloud.cdn.v1.origin_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class OriginGroup(google.protobuf.message.Message):
    """Origin group parameters. For details about the concept, see [documentation](/docs/cdn/concepts/origins#groups)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    USE_NEXT_FIELD_NUMBER: builtins.int
    ORIGINS_FIELD_NUMBER: builtins.int
    id: builtins.int
    """ID of the origin group. Generated at creation time."""
    folder_id: builtins.str
    """ID of the folder that the origin group belongs to."""
    name: builtins.str
    """Name of the origin group."""
    use_next: builtins.bool
    """This option have two possible conditions:
    true - the option is active. In case the origin responds with 4XX or 5XX codes,
           use the next origin from the list.
    false - the option is disabled.
    """
    @property
    def origins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.cdn.v1.origin_pb2.Origin]:
        """List of origins."""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        use_next: builtins.bool = ...,
        origins: collections.abc.Iterable[yandex.cloud.cdn.v1.origin_pb2.Origin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id", b"folder_id", "id", b"id", "name", b"name", "origins", b"origins", "use_next", b"use_next"]) -> None: ...

global___OriginGroup = OriginGroup
