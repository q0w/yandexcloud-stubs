"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AccessBindingAction:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AccessBindingActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AccessBindingAction.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ACCESS_BINDING_ACTION_UNSPECIFIED: _AccessBindingAction.ValueType  # 0
    ADD: _AccessBindingAction.ValueType  # 1
    """Addition of an access binding."""
    REMOVE: _AccessBindingAction.ValueType  # 2
    """Removal of an access binding."""

class AccessBindingAction(_AccessBindingAction, metaclass=_AccessBindingActionEnumTypeWrapper): ...

ACCESS_BINDING_ACTION_UNSPECIFIED: AccessBindingAction.ValueType  # 0
ADD: AccessBindingAction.ValueType  # 1
"""Addition of an access binding."""
REMOVE: AccessBindingAction.ValueType  # 2
"""Removal of an access binding."""
global___AccessBindingAction = AccessBindingAction

class Subject(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the subject.

    It can contain one of the following values:
    * `allAuthenticatedUsers`: A special system identifier that represents anyone
       who is authenticated. It can be used only if the [type] is `system`.
    * `allUsers`: A special system identifier that represents anyone. No authentication is required.
       For example, you don't need to specify the IAM token in an API query.
    * `<cloud generated id>`: An identifier that represents a user account.
       It can be used only if the [type] is `userAccount`, `federatedUser` or `serviceAccount`.
    """
    type: builtins.str
    """Type of the subject.

    It can contain one of the following values:
    * `userAccount`: An account on Yandex or Yandex Connect, added to Yandex Cloud.
    * `serviceAccount`: A service account. This type represents the [yandex.cloud.iam.v1.ServiceAccount] resource.
    * `federatedUser`: A federated account. This type represents a user from an identity federation, like Active Directory.
    * `system`: System group. This type represents several accounts with a common system identifier.

    For more information, see [Subject to which the role is assigned](/docs/iam/concepts/access-control/#subject).
    """
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "type", b"type"]) -> None: ...

global___Subject = Subject

class AccessBinding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_ID_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    role_id: builtins.str
    """ID of the [yandex.cloud.iam.v1.Role] that is assigned to the [subject]."""
    @property
    def subject(self) -> global___Subject:
        """Identity for which access binding is being created.
        It can represent an account with a unique ID or several accounts with a system identifier.
        """
    def __init__(
        self,
        *,
        role_id: builtins.str = ...,
        subject: global___Subject | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["subject", b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["role_id", b"role_id", "subject", b"subject"]) -> None: ...

global___AccessBinding = AccessBinding

class ListAccessBindingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of the resource to list access bindings for.

    To get the resource ID, use a corresponding List request.
    For example, use the [yandex.cloud.resourcemanager.v1.CloudService.List] request to get the Cloud resource ID.
    """
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size],
    the service returns a [ListAccessBindingsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set [page_token]
    to the [ListAccessBindingsResponse.next_page_token]
    returned by a previous list request to get the next page of results.
    """
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size", b"page_size", "page_token", b"page_token", "resource_id", b"resource_id"]) -> None: ...

global___ListAccessBindingsRequest = ListAccessBindingsRequest

class ListAccessBindingsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_BINDINGS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def access_bindings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AccessBinding]:
        """List of access bindings for the specified resource."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListAccessBindingsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListAccessBindingsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        access_bindings: collections.abc.Iterable[global___AccessBinding] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_bindings", b"access_bindings", "next_page_token", b"next_page_token"]) -> None: ...

global___ListAccessBindingsResponse = ListAccessBindingsResponse

class SetAccessBindingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    ACCESS_BINDINGS_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of the resource for which access bindings are being set.

    To get the resource ID, use a corresponding List request.
    """
    @property
    def access_bindings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AccessBinding]:
        """Access bindings to be set. For more information, see [Access Bindings](/docs/iam/concepts/access-control/#access-bindings)."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        access_bindings: collections.abc.Iterable[global___AccessBinding] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_bindings", b"access_bindings", "resource_id", b"resource_id"]) -> None: ...

global___SetAccessBindingsRequest = SetAccessBindingsRequest

class SetAccessBindingsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of the resource for which access bindings are being set."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_id", b"resource_id"]) -> None: ...

global___SetAccessBindingsMetadata = SetAccessBindingsMetadata

class UpdateAccessBindingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    ACCESS_BINDING_DELTAS_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of the resource for which access bindings are being updated."""
    @property
    def access_binding_deltas(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AccessBindingDelta]:
        """Updates to access bindings."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        access_binding_deltas: collections.abc.Iterable[global___AccessBindingDelta] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_binding_deltas", b"access_binding_deltas", "resource_id", b"resource_id"]) -> None: ...

global___UpdateAccessBindingsRequest = UpdateAccessBindingsRequest

class UpdateAccessBindingsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of the resource for which access bindings are being updated."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_id", b"resource_id"]) -> None: ...

global___UpdateAccessBindingsMetadata = UpdateAccessBindingsMetadata

class AccessBindingDelta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTION_FIELD_NUMBER: builtins.int
    ACCESS_BINDING_FIELD_NUMBER: builtins.int
    action: global___AccessBindingAction.ValueType
    """The action that is being performed on an access binding."""
    @property
    def access_binding(self) -> global___AccessBinding:
        """Access binding. For more information, see [Access Bindings](/docs/iam/concepts/access-control/#access-bindings)."""
    def __init__(
        self,
        *,
        action: global___AccessBindingAction.ValueType = ...,
        access_binding: global___AccessBinding | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["access_binding", b"access_binding"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_binding", b"access_binding", "action", b"action"]) -> None: ...

global___AccessBindingDelta = AccessBindingDelta

class AccessBindingsOperationResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_DELTAS_FIELD_NUMBER: builtins.int
    @property
    def effective_deltas(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AccessBindingDelta]:
        """Result access binding deltas."""
    def __init__(
        self,
        *,
        effective_deltas: collections.abc.Iterable[global___AccessBindingDelta] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["effective_deltas", b"effective_deltas"]) -> None: ...

global___AccessBindingsOperationResult = AccessBindingsOperationResult
