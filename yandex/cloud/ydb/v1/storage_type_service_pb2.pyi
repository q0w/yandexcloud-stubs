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
import yandex.cloud.ydb.v1.storage_type_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetStorageTypeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STORAGE_TYPE_ID_FIELD_NUMBER: builtins.int
    storage_type_id: typing.Text
    """Required. ID of the storage type to return."""

    def __init__(self,
        *,
        storage_type_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["storage_type_id",b"storage_type_id"]) -> None: ...
global___GetStorageTypeRequest = GetStorageTypeRequest

class ListStorageTypesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a `next_page_token` that can be used
    to get the next page of results in subsequent ListStorageTypes requests.
    Acceptable values are 0 to 1000, inclusive. Default value: 100.
    """

    page_token: typing.Text
    """Page token. Set `page_token` to the `next_page_token` returned by a previous ListStorageTypes
    request to get the next page of results.
    """

    def __init__(self,
        *,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListStorageTypesRequest = ListStorageTypesRequest

class ListStorageTypesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STORAGE_TYPES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def storage_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ydb.v1.storage_type_pb2.StorageType]:
        """Requested list of storage types."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for ListStorageTypes requests,
    if the number of results is larger than `page_size` specified in the request.
    To get the next page, specify the value of `next_page_token` as a value for
    the `page_token` parameter in the next ListStorageTypes request. Subsequent ListStorageTypes
    requests will have their own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        storage_types: typing.Optional[typing.Iterable[yandex.cloud.ydb.v1.storage_type_pb2.StorageType]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","storage_types",b"storage_types"]) -> None: ...
global___ListStorageTypesResponse = ListStorageTypesResponse