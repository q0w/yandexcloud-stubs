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
class Database(google.protobuf.message.Message):
    """An object that represents MySQL database.

    See [the documentation](/docs/managed-mysql/operations/databases) for details.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the database."""
    cluster_id: builtins.str
    """ID of the cluster that the database belongs to."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "name", b"name"]) -> None: ...

global___Database = Database

@typing_extensions.final
class DatabaseSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the database."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___DatabaseSpec = DatabaseSpec
