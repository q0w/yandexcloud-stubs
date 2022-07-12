"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.mdb.mongodb.v1.user_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    user_name: typing.Text
    """Name of the MongoDB User resource to return.
    To get the name of the user, use a [UserService.List] request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","user_name",b"user_name"]) -> None: ...
global___GetUserRequest = GetUserRequest

class ListUsersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the cluster to list MongoDB users in.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListUsersResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the 
    [ListUsersResponse.next_page_token] returned by the previous list request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListUsersRequest = ListUsersRequest

class ListUsersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.mongodb.v1.user_pb2.User]:
        """List of MongoDB User resources."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListUsersRequest.page_size], use the [next_page_token] as the value
    for the [ListUsersRequest.page_token] parameter in the next list request. Each subsequent
    list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        users: typing.Optional[typing.Iterable[yandex.cloud.mdb.mongodb.v1.user_pb2.User]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","users",b"users"]) -> None: ...
global___ListUsersResponse = ListUsersResponse

class CreateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster to create a user in.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    @property
    def user_spec(self) -> yandex.cloud.mdb.mongodb.v1.user_pb2.UserSpec:
        """Properties of the user to be created."""
        pass
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_spec: typing.Optional[yandex.cloud.mdb.mongodb.v1.user_pb2.UserSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user_spec",b"user_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","user_spec",b"user_spec"]) -> None: ...
global___CreateUserRequest = CreateUserRequest

class CreateUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user is being created in."""

    user_name: typing.Text
    """Name of the user that is being created."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","user_name",b"user_name"]) -> None: ...
global___CreateUserMetadata = CreateUserMetadata

class UpdateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    user_name: typing.Text
    """Name of the user to be updated.
    To get the name of the user, use a [UserService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the MongoDB User resource should be updated."""
        pass
    password: typing.Text
    """New password for the user."""

    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.mongodb.v1.user_pb2.Permission]:
        """New set of permissions for the user."""
        pass
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        password: typing.Text = ...,
        permissions: typing.Optional[typing.Iterable[yandex.cloud.mdb.mongodb.v1.user_pb2.Permission]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","password",b"password","permissions",b"permissions","update_mask",b"update_mask","user_name",b"user_name"]) -> None: ...
global___UpdateUserRequest = UpdateUserRequest

class UpdateUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to."""

    user_name: typing.Text
    """Name of the user that is being updated."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","user_name",b"user_name"]) -> None: ...
global___UpdateUserMetadata = UpdateUserMetadata

class DeleteUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    user_name: typing.Text
    """Name of the user to delete.
    To get the name of the user use a [UserService.List] request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","user_name",b"user_name"]) -> None: ...
global___DeleteUserRequest = DeleteUserRequest

class DeleteUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to."""

    user_name: typing.Text
    """Name of the user that is being deleted."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","user_name",b"user_name"]) -> None: ...
global___DeleteUserMetadata = DeleteUserMetadata

class GrantUserPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    user_name: typing.Text
    """Name of the user to grant the permission to.
    To get the name of the user, use a [UserService.List] request.
    """

    @property
    def permission(self) -> yandex.cloud.mdb.mongodb.v1.user_pb2.Permission:
        """Permission that should be granted to the specified user."""
        pass
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        permission: typing.Optional[yandex.cloud.mdb.mongodb.v1.user_pb2.Permission] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["permission",b"permission"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","permission",b"permission","user_name",b"user_name"]) -> None: ...
global___GrantUserPermissionRequest = GrantUserPermissionRequest

class GrantUserPermissionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    user_name: typing.Text
    """Name of the user that is being granted a permission."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","user_name",b"user_name"]) -> None: ...
global___GrantUserPermissionMetadata = GrantUserPermissionMetadata

class RevokeUserPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    user_name: typing.Text
    """Name of the user to revoke a permission from.
    To get the name of the user, use a [UserService.List] request.
    """

    database_name: typing.Text
    """Name of the database that the user should lose access to."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","database_name",b"database_name","user_name",b"user_name"]) -> None: ...
global___RevokeUserPermissionRequest = RevokeUserPermissionRequest

class RevokeUserPermissionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MongoDB cluster the user belongs to."""

    user_name: typing.Text
    """Name of the user whose permission is being revoked."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        user_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","user_name",b"user_name"]) -> None: ...
global___RevokeUserPermissionMetadata = RevokeUserPermissionMetadata
