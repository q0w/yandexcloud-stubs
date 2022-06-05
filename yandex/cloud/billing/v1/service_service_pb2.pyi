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
import yandex.cloud.billing.v1.service_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetServiceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the service to return.
    To get the service ID, use [ServiceService.List] request.
    """

    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___GetServiceRequest = GetServiceRequest

class ListServicesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    filter: typing.Text
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [yandex.cloud.billing.v1.Service.id] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListServicesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results,
    set [page_token] to the [ListServicesResponse.next_page_token]
    returned by a previous list request.
    """

    def __init__(self,
        *,
        filter: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListServicesRequest = ListServicesRequest

class ListServicesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVICES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.billing.v1.service_pb2.Service]:
        """List of services."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListServicesRequest.page_size], use
    [next_page_token] as the value
    for the [ListServicesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        services: typing.Optional[typing.Iterable[yandex.cloud.billing.v1.service_pb2.Service]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","services",b"services"]) -> None: ...
global___ListServicesResponse = ListServicesResponse
