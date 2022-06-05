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
import yandex.cloud.iam.v1.role_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROLE_ID_FIELD_NUMBER: builtins.int
    role_id: typing.Text
    """ID of the Role resource to return.
    To get the role ID, use a [RoleService.List] request.
    """

    def __init__(self,
        *,
        role_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["role_id",b"role_id"]) -> None: ...
global___GetRoleRequest = GetRoleRequest

class ListRolesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListRolesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token]
    to the [ListRolesResponse.next_page_token]
    returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters resources listed in the response."""

    def __init__(self,
        *,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListRolesRequest = ListRolesRequest

class ListRolesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROLES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def roles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iam.v1.role_pb2.Role]:
        """List of Role resources."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListRolesRequest.page_size], use
    the [next_page_token] as the value
    for the [ListRolesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        roles: typing.Optional[typing.Iterable[yandex.cloud.iam.v1.role_pb2.Role]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","roles",b"roles"]) -> None: ...
global___ListRolesResponse = ListRolesResponse
