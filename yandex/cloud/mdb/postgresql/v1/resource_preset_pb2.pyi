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

class ResourcePreset(google.protobuf.message.Message):
    """A ResourcePreset resource for describing hardware configuration presets."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ZONE_IDS_FIELD_NUMBER: builtins.int
    CORES_FIELD_NUMBER: builtins.int
    MEMORY_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the ResourcePreset resource."""
    @property
    def zone_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IDs of availability zones where the resource preset is available."""
    cores: builtins.int
    """Number of CPU cores for a PostgreSQL host created with the preset."""
    memory: builtins.int
    """RAM volume for a PostgreSQL host created with the preset, in bytes."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        zone_ids: collections.abc.Iterable[builtins.str] | None = ...,
        cores: builtins.int = ...,
        memory: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cores", b"cores", "id", b"id", "memory", b"memory", "zone_ids", b"zone_ids"]) -> None: ...

global___ResourcePreset = ResourcePreset
