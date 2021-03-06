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

class Extension(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    ACTIVE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the extension."""

    id: typing.Text
    """Unique ID of the extension."""

    cluster_id: typing.Text
    """ID of the Elasticsearch cluster the extension belongs to."""

    version: builtins.int
    """Version of the extension."""

    active: builtins.bool
    """The flag shows whether the extension is active."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        id: typing.Text = ...,
        cluster_id: typing.Text = ...,
        version: builtins.int = ...,
        active: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["active",b"active","cluster_id",b"cluster_id","id",b"id","name",b"name","version",b"version"]) -> None: ...
global___Extension = Extension

class ExtensionSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the extension."""

    uri: typing.Text
    """URI of the zip archive to create the new extension from. Currently only supports links that are stored in Object Storage."""

    disabled: builtins.bool
    """The flag shows whether to create the extension in disabled state."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        uri: typing.Text = ...,
        disabled: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disabled",b"disabled","name",b"name","uri",b"uri"]) -> None: ...
global___ExtensionSpec = ExtensionSpec
