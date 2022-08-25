"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import yandex.cloud.mdb.elasticsearch.v1.user_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Elasticsearch cluster the user belongs to.

    To get the cluster ID, make a [ClusterService.List] request.
    """
    user_name: builtins.str
    """Name of the Elasticsearch user to return.

    To get the name of the user, make a [UserService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___GetUserRequest = GetUserRequest

class ListUsersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Elasticsearch cluster to list Elasticsearch users in.

    To get the cluster ID, use a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than `page_size`, the service returns a [ListUsersResponse.next_page_token] that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token.

    To get the next page of results, set `page_token` to the [ListUsersResponse.next_page_token] returned by the previous list request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListUsersRequest = ListUsersRequest

class ListUsersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.elasticsearch.v1.user_pb2.User]:
        """List of Elasticsearch users."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests.

    If the number of results is larger than [ListUsersRequest.page_size], use the `next_page_token` as the value for the [ListUsersRequest.page_token] parameter in the next list request.
    Each subsequent list request will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        users: collections.abc.Iterable[yandex.cloud.mdb.elasticsearch.v1.user_pb2.User] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "users", b"users"]) -> None: ...

global___ListUsersResponse = ListUsersResponse

class CreateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Elasticsearch cluster to create a user in.

    To get the cluster ID, make a [ClusterService.List] request.
    """
    @property
    def user_spec(self) -> yandex.cloud.mdb.elasticsearch.v1.user_pb2.UserSpec:
        """Configuration of the user to create."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_spec: yandex.cloud.mdb.elasticsearch.v1.user_pb2.UserSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user_spec", b"user_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "user_spec", b"user_spec"]) -> None: ...

global___CreateUserRequest = CreateUserRequest

class CreateUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Elasticsearch cluster the user is being created in."""
    user_name: builtins.str
    """Name of the user that is being created."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___CreateUserMetadata = CreateUserMetadata

class UpdateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Elasticsearch cluster the user belongs to.

    To get the cluster ID, make a [ClusterService.List] request.
    """
    user_name: builtins.str
    """Name of the user to be updated.

    To get the name of the user, make a [UserService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    password: builtins.str
    """New password for the user."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "password", b"password", "update_mask", b"update_mask", "user_name", b"user_name"]) -> None: ...

global___UpdateUserRequest = UpdateUserRequest

class UpdateUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Elasticsearch cluster the user belongs to."""
    user_name: builtins.str
    """Name of the user that is being updated."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___UpdateUserMetadata = UpdateUserMetadata

class DeleteUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Elasticsearch cluster the user belongs to.

    To get the cluster ID, make a [ClusterService.List] request.
    """
    user_name: builtins.str
    """Name of the user to delete.

    To get the name of the user, make a [UserService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___DeleteUserRequest = DeleteUserRequest

class DeleteUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Elasticsearch cluster the user belongs to."""
    user_name: builtins.str
    """Name of the user that is being deleted."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___DeleteUserMetadata = DeleteUserMetadata
