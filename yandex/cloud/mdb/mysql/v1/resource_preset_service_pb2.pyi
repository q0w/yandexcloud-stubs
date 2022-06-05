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
import yandex.cloud.mdb.mysql.v1.resource_preset_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetResourcePresetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    resource_preset_id: typing.Text
    """ID of the resource preset to return information about.

    To get this ID, make a [ResourcePresetService.List] request.
    """

    def __init__(self,
        *,
        resource_preset_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_preset_id",b"resource_preset_id"]) -> None: ...
global___GetResourcePresetRequest = GetResourcePresetRequest

class ListResourcePresetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the API returns a [ListResourcePresetsResponse.next_page_token] that can be used to get the next page of results in the subsequent [ResourcePresetService.List] requests.
    """

    page_token: typing.Text
    """Page token that can be used to iterate through multiple pages of results.

    To get the next page of results, set [page_token] to the [ListResourcePresetsResponse.next_page_token] returned by the previous [ResourcePresetService.List] request.
    """

    def __init__(self,
        *,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListResourcePresetsRequest = ListResourcePresetsRequest

class ListResourcePresetsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_PRESETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def resource_presets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.mysql.v1.resource_preset_pb2.ResourcePreset]:
        """List of resource presets."""
        pass
    next_page_token: typing.Text
    """The token that can be used to get the next page of results.

    If the number of results is larger than [ListResourcePresetsRequest.page_size], use the [next_page_token] as the value for the [ListResourcePresetsRequest.page_token] in the subsequent [ResourcePresetService.List] request to iterate through multiple pages of results.

    Each of the subsequent [ResourcePresetService.List] requests should use the [next_page_token] value returned by the previous request to continue paging through the results.
    """

    def __init__(self,
        *,
        resource_presets: typing.Optional[typing.Iterable[yandex.cloud.mdb.mysql.v1.resource_preset_pb2.ResourcePreset]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","resource_presets",b"resource_presets"]) -> None: ...
global___ListResourcePresetsResponse = ListResourcePresetsResponse
