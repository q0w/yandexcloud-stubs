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
import yandex.cloud.mdb.elasticsearch.v1.extension_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetExtensionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    EXTENSION_ID_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster."""

    extension_id: typing.Text
    """ID of the extension to return."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        extension_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","extension_id",b"extension_id"]) -> None: ...
global___GetExtensionRequest = GetExtensionRequest

class ListExtensionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster to list extensions in."""

    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the API returns a [ListExtensionsResponse.next_page_token] that can be used to get the next page of results in subsequent [ExtensionService.List] requests.
    """

    page_token: typing.Text
    """Page token that can be used to iterate through multiple pages of results.

    To get the next page of results, set [page_token] to the [ListExtensionsResponse.next_page_token] returned by the previous [ExtensionService.List] request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListExtensionsRequest = ListExtensionsRequest

class ListExtensionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXTENSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def extensions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.elasticsearch.v1.extension_pb2.Extension]:
        """Requested list of extensions."""
        pass
    next_page_token: typing.Text
    """The token that can be used to get the next page of results.

    If the number of results is larger than [ListExtensionsRequest.page_size], use the [next_page_token] as the value for the [ListExtensionsRequest.page_token] in the subsequent [ExtensionService.List] request to iterate through multiple pages of results.

    Each of the subsequent [ExtensionService.List] requests should use the [next_page_token] value returned in the previous request to continue paging through the results.
    """

    def __init__(self,
        *,
        extensions: typing.Optional[typing.Iterable[yandex.cloud.mdb.elasticsearch.v1.extension_pb2.Extension]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["extensions",b"extensions","next_page_token",b"next_page_token"]) -> None: ...
global___ListExtensionsResponse = ListExtensionsResponse

class DeleteExtensionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    EXTENSION_ID_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster."""

    extension_id: typing.Text
    """ID of the extension to delete."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        extension_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","extension_id",b"extension_id"]) -> None: ...
global___DeleteExtensionRequest = DeleteExtensionRequest

class DeleteExtensionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    EXTENSION_ID_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster."""

    extension_id: typing.Text
    """ID of the extension to delete."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        extension_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","extension_id",b"extension_id"]) -> None: ...
global___DeleteExtensionMetadata = DeleteExtensionMetadata

class UpdateExtensionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    EXTENSION_ID_FIELD_NUMBER: builtins.int
    ACTIVE_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster."""

    extension_id: typing.Text
    """ID of the extension to update."""

    active: builtins.bool
    """The flag shows whether to make the extension active."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        extension_id: typing.Text = ...,
        active: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["active",b"active","cluster_id",b"cluster_id","extension_id",b"extension_id"]) -> None: ...
global___UpdateExtensionRequest = UpdateExtensionRequest

class UpdateExtensionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    EXTENSION_ID_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster."""

    extension_id: typing.Text
    """ID of the extension."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        extension_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","extension_id",b"extension_id"]) -> None: ...
global___UpdateExtensionMetadata = UpdateExtensionMetadata

class CreateExtensionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster."""

    name: typing.Text
    """Name of the extension."""

    uri: typing.Text
    """URI of the zip archive to create the new extension from. Currently only supports links that are stored in Object Storage."""

    disabled: builtins.bool
    """The flag that disables the extension."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        name: typing.Text = ...,
        uri: typing.Text = ...,
        disabled: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","disabled",b"disabled","name",b"name","uri",b"uri"]) -> None: ...
global___CreateExtensionRequest = CreateExtensionRequest

class CreateExtensionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    EXTENSION_ID_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster."""

    extension_id: typing.Text
    """ID of the extension."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        extension_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","extension_id",b"extension_id"]) -> None: ...
global___CreateExtensionMetadata = CreateExtensionMetadata
