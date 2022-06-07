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
import yandex.cloud.containerregistry.v1.ip_permission_pb2
import yandex.cloud.containerregistry.v1.registry_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetRegistryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the Registry resource to return.

    To get the registry ID use a [RegistryService.List] request.
    """

    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id",b"registry_id"]) -> None: ...
global___GetRegistryRequest = GetRegistryRequest

class ListRegistriesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list registries in.

    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListRegistriesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListRegistriesResponse.next_page_token] returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [Registry.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListRegistriesRequest = ListRegistriesRequest

class ListRegistriesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def registries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.registry_pb2.Registry]:
        """List of Registry resources."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListRegistriesRequest.page_size], use
    the [next_page_token] as the value
    for the [ListRegistriesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        registries: typing.Optional[typing.Iterable[yandex.cloud.containerregistry.v1.registry_pb2.Registry]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","registries",b"registries"]) -> None: ...
global___ListRegistriesResponse = ListRegistriesResponse

class CreateRegistryRequest(google.protobuf.message.Message):
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
    LABELS_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to create a registry in.

    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    name: typing.Text
    """Name of the registry.

    There may be only one registry per folder.
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs."""
        pass
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id","labels",b"labels","name",b"name"]) -> None: ...
global___CreateRegistryRequest = CreateRegistryRequest

class CreateRegistryMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry that is being created."""

    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id",b"registry_id"]) -> None: ...
global___CreateRegistryMetadata = CreateRegistryMetadata

class UpdateRegistryRequest(google.protobuf.message.Message):
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

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the Registry resource to update.

    To get the registry ID use a [RegistryService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Registry resource are going to be updated."""
        pass
    name: typing.Text
    """Name of the registry.

    There may be only one registry per folder.
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """
        pass
    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["labels",b"labels","name",b"name","registry_id",b"registry_id","update_mask",b"update_mask"]) -> None: ...
global___UpdateRegistryRequest = UpdateRegistryRequest

class UpdateRegistryMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the Registry resource that is being updated."""

    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id",b"registry_id"]) -> None: ...
global___UpdateRegistryMetadata = UpdateRegistryMetadata

class DeleteRegistryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry to delete."""

    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id",b"registry_id"]) -> None: ...
global___DeleteRegistryRequest = DeleteRegistryRequest

class DeleteRegistryMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry that is being deleted."""

    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id",b"registry_id"]) -> None: ...
global___DeleteRegistryMetadata = DeleteRegistryMetadata

class SetIpPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    IP_PERMISSION_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry for which ip permissions are being set."""

    @property
    def ip_permission(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.ip_permission_pb2.IpPermission]:
        """IP permission to be set."""
        pass
    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ip_permission: typing.Optional[typing.Iterable[yandex.cloud.containerregistry.v1.ip_permission_pb2.IpPermission]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ip_permission",b"ip_permission","registry_id",b"registry_id"]) -> None: ...
global___SetIpPermissionRequest = SetIpPermissionRequest

class UpdateIpPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    IP_PERMISSION_DELTAS_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry for which ip permissions are being updated."""

    @property
    def ip_permission_deltas(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.ip_permission_pb2.IpPermissionDelta]:
        """Updates to IP permissions."""
        pass
    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ip_permission_deltas: typing.Optional[typing.Iterable[yandex.cloud.containerregistry.v1.ip_permission_pb2.IpPermissionDelta]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ip_permission_deltas",b"ip_permission_deltas","registry_id",b"registry_id"]) -> None: ...
global___UpdateIpPermissionRequest = UpdateIpPermissionRequest

class ListIpPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the Registry to return ip permission list."""

    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id",b"registry_id"]) -> None: ...
global___ListIpPermissionRequest = ListIpPermissionRequest

class ListIpPermissionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PERMISSIONS_FIELD_NUMBER: builtins.int
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.ip_permission_pb2.IpPermission]:
        """List of ip permissions for registry"""
        pass
    def __init__(self,
        *,
        permissions: typing.Optional[typing.Iterable[yandex.cloud.containerregistry.v1.ip_permission_pb2.IpPermission]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["permissions",b"permissions"]) -> None: ...
global___ListIpPermissionsResponse = ListIpPermissionsResponse

class SetIpPermissionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry that ip permission is being set."""

    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id",b"registry_id"]) -> None: ...
global___SetIpPermissionMetadata = SetIpPermissionMetadata

class UpdateIpPermissionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry that ip permission is being updated."""

    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id",b"registry_id"]) -> None: ...
global___UpdateIpPermissionMetadata = UpdateIpPermissionMetadata