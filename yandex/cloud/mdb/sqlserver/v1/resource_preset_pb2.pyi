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

class ResourcePreset(google.protobuf.message.Message):
    """A preset of resources for hardware configuration of SQL Server hosts."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    ZONE_IDS_FIELD_NUMBER: builtins.int
    CORES_FIELD_NUMBER: builtins.int
    MEMORY_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the resource preset."""

    @property
    def zone_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of availability zones where the resource preset is available."""
        pass
    cores: builtins.int
    """Number of CPU cores for an SQL Server host created with the preset."""

    memory: builtins.int
    """RAM volume for an SQL Server host created with the preset, in bytes."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        zone_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        cores: builtins.int = ...,
        memory: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cores",b"cores","id",b"id","memory",b"memory","zone_ids",b"zone_ids"]) -> None: ...
global___ResourcePreset = ResourcePreset