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
import yandex.cloud.iot.devices.v1.registry_pb2
import yandex.cloud.operation.operation_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetRegistryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to return.

    To get a registry ID make a [RegistryService.List] request.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id", b"registry_id"]) -> None: ...

global___GetRegistryRequest = GetRegistryRequest

@typing_extensions.final
class GetByNameRegistryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    REGISTRY_NAME_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list registries in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    registry_name: builtins.str
    """Name of the registry to return.

    To get a registry Name make a [RegistryService.List] request.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        registry_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id", b"folder_id", "registry_name", b"registry_name"]) -> None: ...

global___GetByNameRegistryRequest = GetByNameRegistryRequest

@typing_extensions.final
class ListRegistriesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list registries in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a [ListRegistriesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListRegistriesResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListRegistriesRequest = ListRegistriesRequest

@typing_extensions.final
class ListRegistriesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def registries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.devices.v1.registry_pb2.Registry]:
        """List of registries."""
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListRegistriesRequest.page_size], use `next_page_token` as the value
    for the [ListRegistriesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        registries: collections.abc.Iterable[yandex.cloud.iot.devices.v1.registry_pb2.Registry] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "registries", b"registries"]) -> None: ...

global___ListRegistriesResponse = ListRegistriesResponse

@typing_extensions.final
class CreateRegistryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class Certificate(google.protobuf.message.Message):
        """Specification of a registry certificate."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
        certificate_data: builtins.str
        """Public part of the registry certificate."""
        def __init__(
            self,
            *,
            certificate_data: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["certificate_data", b"certificate_data"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CERTIFICATES_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a registry in.

    To get a folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the registry. The name must be unique within the folder."""
    description: builtins.str
    """Description of the registry."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CreateRegistryRequest.Certificate]:
        """Registry certificates."""
    password: builtins.str
    """Registry passwords.

    The password must contain at least three character categories among the following: upper case latin, lower case latin, numbers and special symbols.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        certificates: collections.abc.Iterable[global___CreateRegistryRequest.Certificate] | None = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificates", b"certificates", "description", b"description", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "password", b"password"]) -> None: ...

global___CreateRegistryRequest = CreateRegistryRequest

@typing_extensions.final
class CreateRegistryMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry that is being created."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id", b"registry_id"]) -> None: ...

global___CreateRegistryMetadata = CreateRegistryMetadata

@typing_extensions.final
class UpdateRegistryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to update.

    To get a registry ID make a [RegistryService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the registry are going to be updated."""
    name: builtins.str
    """Name of the registry. The name must be unique within the folder."""
    description: builtins.str
    """Description of the registry."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "labels", b"labels", "name", b"name", "registry_id", b"registry_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateRegistryRequest = UpdateRegistryRequest

@typing_extensions.final
class UpdateRegistryMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry that is being updated."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id", b"registry_id"]) -> None: ...

global___UpdateRegistryMetadata = UpdateRegistryMetadata

@typing_extensions.final
class DeleteRegistryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to delete.

    To get a registry ID make a [RegistryService.List] request.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id", b"registry_id"]) -> None: ...

global___DeleteRegistryRequest = DeleteRegistryRequest

@typing_extensions.final
class DeleteRegistryMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry that is being deleted."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id", b"registry_id"]) -> None: ...

global___DeleteRegistryMetadata = DeleteRegistryMetadata

@typing_extensions.final
class ListRegistryCertificatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to list certificates for."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id", b"registry_id"]) -> None: ...

global___ListRegistryCertificatesRequest = ListRegistryCertificatesRequest

@typing_extensions.final
class ListRegistryCertificatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATES_FIELD_NUMBER: builtins.int
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.devices.v1.registry_pb2.RegistryCertificate]:
        """List of certificates for the specified registry."""
    def __init__(
        self,
        *,
        certificates: collections.abc.Iterable[yandex.cloud.iot.devices.v1.registry_pb2.RegistryCertificate] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificates", b"certificates"]) -> None: ...

global___ListRegistryCertificatesResponse = ListRegistryCertificatesResponse

@typing_extensions.final
class AddRegistryCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry for which the certificate is being added.

    To get a registry ID make a [RegistryService.List] request.
    """
    certificate_data: builtins.str
    """Public part of the certificate that is being added."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        certificate_data: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_data", b"certificate_data", "registry_id", b"registry_id"]) -> None: ...

global___AddRegistryCertificateRequest = AddRegistryCertificateRequest

@typing_extensions.final
class AddRegistryCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry certificate that is being added."""
    fingerprint: builtins.str
    """Fingerprint of the certificate that is being added."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fingerprint", b"fingerprint", "registry_id", b"registry_id"]) -> None: ...

global___AddRegistryCertificateMetadata = AddRegistryCertificateMetadata

@typing_extensions.final
class DeleteRegistryCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to delete a certificate for.

    To get a registry ID make a [RegistryService.List] request.
    """
    fingerprint: builtins.str
    """Fingerprint of the certificate that is being deleted."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fingerprint", b"fingerprint", "registry_id", b"registry_id"]) -> None: ...

global___DeleteRegistryCertificateRequest = DeleteRegistryCertificateRequest

@typing_extensions.final
class DeleteRegistryCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of a registry for which the certificate is being delete."""
    fingerprint: builtins.str
    """Fingerprint of the certificate to deleted."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fingerprint", b"fingerprint", "registry_id", b"registry_id"]) -> None: ...

global___DeleteRegistryCertificateMetadata = DeleteRegistryCertificateMetadata

@typing_extensions.final
class ListRegistryPasswordsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to list passwords in.

    To get a registry ID make a [RegistryService.List] request.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registry_id", b"registry_id"]) -> None: ...

global___ListRegistryPasswordsRequest = ListRegistryPasswordsRequest

@typing_extensions.final
class ListRegistryPasswordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PASSWORDS_FIELD_NUMBER: builtins.int
    @property
    def passwords(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.devices.v1.registry_pb2.RegistryPassword]:
        """List of passwords for the specified registry."""
    def __init__(
        self,
        *,
        passwords: collections.abc.Iterable[yandex.cloud.iot.devices.v1.registry_pb2.RegistryPassword] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["passwords", b"passwords"]) -> None: ...

global___ListRegistryPasswordsResponse = ListRegistryPasswordsResponse

@typing_extensions.final
class AddRegistryPasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to add a password for.

    To get a registry ID make a [RegistryService.List] request.
    """
    password: builtins.str
    """Passwords for the registry.

    The password must contain at least three character categories among the following: upper case latin, lower case latin, numbers and special symbols.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password", b"password", "registry_id", b"registry_id"]) -> None: ...

global___AddRegistryPasswordRequest = AddRegistryPasswordRequest

@typing_extensions.final
class AddRegistryPasswordMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry for which the password is being added."""
    password_id: builtins.str
    """ID of a password that is being added."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password_id", b"password_id", "registry_id", b"registry_id"]) -> None: ...

global___AddRegistryPasswordMetadata = AddRegistryPasswordMetadata

@typing_extensions.final
class DeleteRegistryPasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to delete a password for.

    To get a registry ID make a [DeviceService.List] request.
    """
    password_id: builtins.str
    """ID of the password to delete.

    To get a password ID make a [RegistryService.ListPasswords] request.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password_id", b"password_id", "registry_id", b"registry_id"]) -> None: ...

global___DeleteRegistryPasswordRequest = DeleteRegistryPasswordRequest

@typing_extensions.final
class DeleteRegistryPasswordMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of a registry for which the password is being delete."""
    password_id: builtins.str
    """ID of the password to delete.

    To get a password ID make a [RegistryService.ListPasswords] request.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password_id", b"password_id", "registry_id", b"registry_id"]) -> None: ...

global___DeleteRegistryPasswordMetadata = DeleteRegistryPasswordMetadata

@typing_extensions.final
class ListDeviceTopicAliasesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to list aliases for device topic.

    To get a registry ID make a [RegistryService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a [ListDeviceTopicAliasesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListDeviceTopicAliasesResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size", b"page_size", "page_token", b"page_token", "registry_id", b"registry_id"]) -> None: ...

global___ListDeviceTopicAliasesRequest = ListDeviceTopicAliasesRequest

@typing_extensions.final
class ListDeviceTopicAliasesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALIASES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def aliases(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.devices.v1.registry_pb2.DeviceAlias]:
        """List of device aliases for the specified registry."""
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListDeviceTopicAliasesRequest.page_size], use `next_page_token` as the value
    for the [ListDeviceTopicAliasesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        aliases: collections.abc.Iterable[yandex.cloud.iot.devices.v1.registry_pb2.DeviceAlias] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aliases", b"aliases", "next_page_token", b"next_page_token"]) -> None: ...

global___ListDeviceTopicAliasesResponse = ListDeviceTopicAliasesResponse

@typing_extensions.final
class ListRegistryOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a [ListRegistryOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListRegistryOperationsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on [Registry.name] field.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "page_size", b"page_size", "page_token", b"page_token", "registry_id", b"registry_id"]) -> None: ...

global___ListRegistryOperationsRequest = ListRegistryOperationsRequest

@typing_extensions.final
class ListRegistryOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified registry."""
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListRegistryOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListRegistryOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListRegistryOperationsResponse = ListRegistryOperationsResponse
