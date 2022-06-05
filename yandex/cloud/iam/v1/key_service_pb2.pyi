"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.iam.v1.key_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _KeyFormat:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _KeyFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KeyFormat.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PEM_FILE: _KeyFormat.ValueType  # 0
    """Privacy-Enhanced Mail (PEM) format. Default value."""

class KeyFormat(_KeyFormat, metaclass=_KeyFormatEnumTypeWrapper):
    pass

PEM_FILE: KeyFormat.ValueType  # 0
"""Privacy-Enhanced Mail (PEM) format. Default value."""

global___KeyFormat = KeyFormat


class GetKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the Key resource to return.
    To get the ID use a [KeyService.List] request.
    """

    format: global___KeyFormat.ValueType
    """Output format of the key."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        format: global___KeyFormat.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["format",b"format","key_id",b"key_id"]) -> None: ...
global___GetKeyRequest = GetKeyRequest

class ListKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FORMAT_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    format: global___KeyFormat.ValueType
    """Output format of the key."""

    service_account_id: typing.Text
    """ID of the service account to list key pairs for.
    To get the service account ID, use a [yandex.cloud.iam.v1.ServiceAccountService.List] request.
    If not specified, it defaults to the subject that made the request.
    use userAccount identity if this not set
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListKeysResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListKeysResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        format: global___KeyFormat.ValueType = ...,
        service_account_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["format",b"format","page_size",b"page_size","page_token",b"page_token","service_account_id",b"service_account_id"]) -> None: ...
global___ListKeysRequest = ListKeysRequest

class ListKeysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEYS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iam.v1.key_pb2.Key]:
        """List of Key resources."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListKeysRequest.page_size], use
    the [next_page_token] as the value
    for the [ListKeysRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        keys: typing.Optional[typing.Iterable[yandex.cloud.iam.v1.key_pb2.Key]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keys",b"keys","next_page_token",b"next_page_token"]) -> None: ...
global___ListKeysResponse = ListKeysResponse

class CreateKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    KEY_ALGORITHM_FIELD_NUMBER: builtins.int
    service_account_id: typing.Text
    """ID of the service account to create a key pair for.
    To get the service account ID, use a [yandex.cloud.iam.v1.ServiceAccountService.List] request.
    If not specified, it defaults to the subject that made the request.
    use userAccount identity if this not set
    """

    description: typing.Text
    """Description of the key pair."""

    format: global___KeyFormat.ValueType
    """Output format of the key."""

    key_algorithm: yandex.cloud.iam.v1.key_pb2.Key.Algorithm.ValueType
    """An algorithm used to generate a key pair of the Key resource."""

    def __init__(self,
        *,
        service_account_id: typing.Text = ...,
        description: typing.Text = ...,
        format: global___KeyFormat.ValueType = ...,
        key_algorithm: yandex.cloud.iam.v1.key_pb2.Key.Algorithm.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","format",b"format","key_algorithm",b"key_algorithm","service_account_id",b"service_account_id"]) -> None: ...
global___CreateKeyRequest = CreateKeyRequest

class CreateKeyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    PRIVATE_KEY_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> yandex.cloud.iam.v1.key_pb2.Key:
        """Key resource."""
        pass
    private_key: typing.Text
    """A private key of the Key resource.
    This key must be stored securely.
    """

    def __init__(self,
        *,
        key: typing.Optional[yandex.cloud.iam.v1.key_pb2.Key] = ...,
        private_key: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["key",b"key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","private_key",b"private_key"]) -> None: ...
global___CreateKeyResponse = CreateKeyResponse

class UpdateKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the Key resource to update.
    To get key pair ID, use a [KeyService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Key resource are going to be updated."""
        pass
    description: typing.Text
    """Description of the key pair."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        description: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","key_id",b"key_id","update_mask",b"update_mask"]) -> None: ...
global___UpdateKeyRequest = UpdateKeyRequest

class UpdateKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the Key resource that is being updated."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id"]) -> None: ...
global___UpdateKeyMetadata = UpdateKeyMetadata

class DeleteKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key to delete.
    To get key ID use a [KeyService.List] request.
    """

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id"]) -> None: ...
global___DeleteKeyRequest = DeleteKeyRequest

class DeleteKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key that is being deleted."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id"]) -> None: ...
global___DeleteKeyMetadata = DeleteKeyMetadata

class ListKeyOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key to list operations for."""

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListKeyOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListKeyOperationsResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListKeyOperationsRequest = ListKeyOperationsRequest

class ListKeyOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified key."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListKeyOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListKeyOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListKeyOperationsResponse = ListKeyOperationsResponse
