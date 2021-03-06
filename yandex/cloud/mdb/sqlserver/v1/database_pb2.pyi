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

class Database(google.protobuf.message.Message):
    """An SQL Server database.

    For more information, see the [Concepts](/docs/managed-sqlserver/concepts) section of the documentation.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the database."""

    cluster_id: typing.Text
    """ID of the SQL Server cluster that the database belongs to."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        cluster_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","name",b"name"]) -> None: ...
global___Database = Database

class DatabaseSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the database."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DatabaseSpec = DatabaseSpec
