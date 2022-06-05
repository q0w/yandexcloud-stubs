"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions
import yandex.cloud.kms.v1.symmetric_key_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CreateSymmetricKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DEFAULT_ALGORITHM_FIELD_NUMBER: builtins.int
    ROTATION_PERIOD_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to create a symmetric KMS key in."""

    name: typing.Text
    """Name of the key."""

    description: typing.Text
    """Description of the key."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Custom labels for the symmetric KMS key as `key:value` pairs. Maximum 64 per key.
        For example, `"project": "mvp"` or `"source": "dictionary"`.
        """
        pass
    default_algorithm: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricAlgorithm.ValueType
    """Encryption algorithm to be used with a new key version, generated with the next rotation."""

    @property
    def rotation_period(self) -> google.protobuf.duration_pb2.Duration:
        """Interval between automatic rotations. To disable automatic rotation, don't include
        this field in the creation request.
        """
        pass
    deletion_protection: builtins.bool
    """Flag that inhibits deletion of the symmetric KMS key"""

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        default_algorithm: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricAlgorithm.ValueType = ...,
        rotation_period: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        deletion_protection: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rotation_period",b"rotation_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_algorithm",b"default_algorithm","deletion_protection",b"deletion_protection","description",b"description","folder_id",b"folder_id","labels",b"labels","name",b"name","rotation_period",b"rotation_period"]) -> None: ...
global___CreateSymmetricKeyRequest = CreateSymmetricKeyRequest

class CreateSymmetricKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    PRIMARY_VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key being created."""

    primary_version_id: typing.Text
    """ID of the primary version of the key being created."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        primary_version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","primary_version_id",b"primary_version_id"]) -> None: ...
global___CreateSymmetricKeyMetadata = CreateSymmetricKeyMetadata

class GetSymmetricKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the symmetric KMS key to return.
    To get the ID of a symmetric KMS key use a [SymmetricKeyService.List] request.
    """

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id"]) -> None: ...
global___GetSymmetricKeyRequest = GetSymmetricKeyRequest

class ListSymmetricKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list symmetric KMS keys in."""

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListSymmetricKeysResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListSymmetricKeysResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListSymmetricKeysRequest = ListSymmetricKeysRequest

class ListSymmetricKeysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEYS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKey]:
        """List of symmetric KMS keys in the specified folder."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number
    of results is greater than the specified [ListSymmetricKeysRequest.page_size], use
    the [next_page_token] as the value for the [ListSymmetricKeysRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        keys: typing.Optional[typing.Iterable[yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKey]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keys",b"keys","next_page_token",b"next_page_token"]) -> None: ...
global___ListSymmetricKeysResponse = ListSymmetricKeysResponse

class ListSymmetricKeyVersionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the symmetric KMS key to list versions for."""

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListSymmetricKeyVersionsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListSymmetricKeyVersionsResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListSymmetricKeyVersionsRequest = ListSymmetricKeyVersionsRequest

class ListSymmetricKeyVersionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_VERSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def key_versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKeyVersion]:
        """List of versions for the specified symmetric KMS key."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number
    of results is greater than the specified [ListSymmetricKeyVersionsRequest.page_size], use
    the [next_page_token] as the value for the [ListSymmetricKeyVersionsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        key_versions: typing.Optional[typing.Iterable[yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKeyVersion]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_versions",b"key_versions","next_page_token",b"next_page_token"]) -> None: ...
global___ListSymmetricKeyVersionsResponse = ListSymmetricKeyVersionsResponse

class UpdateSymmetricKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    KEY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DEFAULT_ALGORITHM_FIELD_NUMBER: builtins.int
    ROTATION_PERIOD_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the symmetric KMS key to update.
    To get the ID of a symmetric KMS key use a [SymmetricKeyService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the symmetric KMS key are going to be updated."""
        pass
    name: typing.Text
    """New name for the symmetric KMS key."""

    description: typing.Text
    """New description for the symmetric KMS key."""

    status: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKey.Status.ValueType
    """New status for the symmetric KMS key.
    Using the [SymmetricKeyService.Update] method you can only set ACTIVE or INACTIVE status.
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Custom labels for the symmetric KMS key as `key:value` pairs. Maximum 64 per key."""
        pass
    default_algorithm: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricAlgorithm.ValueType
    """Default encryption algorithm to be used with new versions of the symmetric KMS key."""

    @property
    def rotation_period(self) -> google.protobuf.duration_pb2.Duration:
        """Time period between automatic symmetric KMS key rotations.
        period between two automatic rotations
        """
        pass
    deletion_protection: builtins.bool
    """Flag that inhibits deletion of the symmetric KMS key"""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        status: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKey.Status.ValueType = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        default_algorithm: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricAlgorithm.ValueType = ...,
        rotation_period: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        deletion_protection: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rotation_period",b"rotation_period","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_algorithm",b"default_algorithm","deletion_protection",b"deletion_protection","description",b"description","key_id",b"key_id","labels",b"labels","name",b"name","rotation_period",b"rotation_period","status",b"status","update_mask",b"update_mask"]) -> None: ...
global___UpdateSymmetricKeyRequest = UpdateSymmetricKeyRequest

class UpdateSymmetricKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key being updated."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id"]) -> None: ...
global___UpdateSymmetricKeyMetadata = UpdateSymmetricKeyMetadata

class DeleteSymmetricKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key to be deleted."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id"]) -> None: ...
global___DeleteSymmetricKeyRequest = DeleteSymmetricKeyRequest

class DeleteSymmetricKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key being deleted."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id"]) -> None: ...
global___DeleteSymmetricKeyMetadata = DeleteSymmetricKeyMetadata

class SetPrimarySymmetricKeyVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key to set a primary version for."""

    version_id: typing.Text
    """ID of the version that should become primary for the specified key."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","version_id",b"version_id"]) -> None: ...
global___SetPrimarySymmetricKeyVersionRequest = SetPrimarySymmetricKeyVersionRequest

class SetPrimarySymmetricKeyVersionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key that the primary version if being changed for."""

    version_id: typing.Text
    """ID of the version that is being made primary for the key."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","version_id",b"version_id"]) -> None: ...
global___SetPrimarySymmetricKeyVersionMetadata = SetPrimarySymmetricKeyVersionMetadata

class RotateSymmetricKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key to be rotated."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id"]) -> None: ...
global___RotateSymmetricKeyRequest = RotateSymmetricKeyRequest

class RotateSymmetricKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    NEW_PRIMARY_VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key being rotated."""

    new_primary_version_id: typing.Text
    """ID of the version generated as a result of key rotation."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        new_primary_version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","new_primary_version_id",b"new_primary_version_id"]) -> None: ...
global___RotateSymmetricKeyMetadata = RotateSymmetricKeyMetadata

class ScheduleSymmetricKeyVersionDestructionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    PENDING_PERIOD_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key whose version should be scheduled for destruction."""

    version_id: typing.Text
    """ID of the version to be destroyed."""

    @property
    def pending_period(self) -> google.protobuf.duration_pb2.Duration:
        """Time interval between the version destruction request and actual destruction.
        Default value: 7 days.
        """
        pass
    def __init__(self,
        *,
        key_id: typing.Text = ...,
        version_id: typing.Text = ...,
        pending_period: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pending_period",b"pending_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","pending_period",b"pending_period","version_id",b"version_id"]) -> None: ...
global___ScheduleSymmetricKeyVersionDestructionRequest = ScheduleSymmetricKeyVersionDestructionRequest

class ScheduleSymmetricKeyVersionDestructionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    DESTROY_AT_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key whose version is being scheduled for destruction."""

    version_id: typing.Text
    """ID of the version that is being scheduled for destruction."""

    @property
    def destroy_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the version is scheduled to be destroyed."""
        pass
    def __init__(self,
        *,
        key_id: typing.Text = ...,
        version_id: typing.Text = ...,
        destroy_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["destroy_at",b"destroy_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["destroy_at",b"destroy_at","key_id",b"key_id","version_id",b"version_id"]) -> None: ...
global___ScheduleSymmetricKeyVersionDestructionMetadata = ScheduleSymmetricKeyVersionDestructionMetadata

class CancelSymmetricKeyVersionDestructionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key to cancel a version's destruction for."""

    version_id: typing.Text
    """ID of the version whose scheduled destruction should be cancelled."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","version_id",b"version_id"]) -> None: ...
global___CancelSymmetricKeyVersionDestructionRequest = CancelSymmetricKeyVersionDestructionRequest

class CancelSymmetricKeyVersionDestructionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the key whose version's destruction is being cancelled."""

    version_id: typing.Text
    """ID of the version whose scheduled destruction is being cancelled."""

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","version_id",b"version_id"]) -> None: ...
global___CancelSymmetricKeyVersionDestructionMetadata = CancelSymmetricKeyVersionDestructionMetadata

class ListSymmetricKeyOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    key_id: typing.Text
    """ID of the symmetric KMS key to get operations for.

    To get the key ID, use a [SymmetricKeyService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size], the service returns a [ListSymmetricKeyOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListSymmetricKeyOperationsResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        key_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_id",b"key_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListSymmetricKeyOperationsRequest = ListSymmetricKeyOperationsRequest

class ListSymmetricKeyOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified key."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListSymmetricKeyOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListSymmetricKeyOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListSymmetricKeyOperationsResponse = ListSymmetricKeyOperationsResponse
