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
import yandex.cloud.operation.operation_pb2
import yandex.cloud.vpc.v1.address_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetAddressRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    """ID of the Address resource to return.

    To get Address resource ID make a [AddressService.List] request.
    """

    def __init__(self,
        *,
        address_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id"]) -> None: ...
global___GetAddressRequest = GetAddressRequest

class GetAddressByValueRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXTERNAL_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    external_ipv4_address: typing.Text
    def __init__(self,
        *,
        external_ipv4_address: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address",b"address","external_ipv4_address",b"external_ipv4_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","external_ipv4_address",b"external_ipv4_address"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["address",b"address"]) -> typing.Optional[typing_extensions.Literal["external_ipv4_address"]]: ...
global___GetAddressByValueRequest = GetAddressByValueRequest

class ListAddressesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list addresses in.

    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListAddressesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set `page_token` to the
    [ListAddressesResponse.next_page_token] returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters Address listed in the response.

    The expression must specify:
    1. The field name. Currently you can use filtering only on [Address.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    Example of a filter: `name=my-address`.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListAddressesRequest = ListAddressesRequest

class ListAddressesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESSES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def addresses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.address_pb2.Address]:
        """List of addresses."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListAddressesRequest.page_size], use `next_page_token` as the value
    for the [ListAddressesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        addresses: typing.Optional[typing.Iterable[yandex.cloud.vpc.v1.address_pb2.Address]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["addresses",b"addresses","next_page_token",b"next_page_token"]) -> None: ...
global___ListAddressesResponse = ListAddressesResponse

class CreateAddressRequest(google.protobuf.message.Message):
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
    EXTERNAL_IPV4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to create a address in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    name: typing.Text
    """Name of the address.
    The name must be unique within the folder.
    """

    description: typing.Text
    """Description of the address."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Address labels as `key:value` pairs."""
        pass
    @property
    def external_ipv4_address_spec(self) -> global___ExternalIpv4AddressSpec: ...
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        external_ipv4_address_spec: typing.Optional[global___ExternalIpv4AddressSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address_spec",b"address_spec","external_ipv4_address_spec",b"external_ipv4_address_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_spec",b"address_spec","description",b"description","external_ipv4_address_spec",b"external_ipv4_address_spec","folder_id",b"folder_id","labels",b"labels","name",b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["address_spec",b"address_spec"]) -> typing.Optional[typing_extensions.Literal["external_ipv4_address_spec"]]: ...
global___CreateAddressRequest = CreateAddressRequest

class ExternalIpv4AddressSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    REQUIREMENTS_FIELD_NUMBER: builtins.int
    address: typing.Text
    """Value of address.
    if unspecified, one will be automatically allocated from other params
    """

    zone_id: typing.Text
    """Availability zone from which the address will be allocated.
    only if address unspecified
    """

    @property
    def requirements(self) -> yandex.cloud.vpc.v1.address_pb2.AddressRequirements:
        """Parameters of the allocated address, for example DDoS Protection."""
        pass
    def __init__(self,
        *,
        address: typing.Text = ...,
        zone_id: typing.Text = ...,
        requirements: typing.Optional[yandex.cloud.vpc.v1.address_pb2.AddressRequirements] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["requirements",b"requirements"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","requirements",b"requirements","zone_id",b"zone_id"]) -> None: ...
global___ExternalIpv4AddressSpec = ExternalIpv4AddressSpec

class CreateAddressMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    """ID of the address that is being created."""

    def __init__(self,
        *,
        address_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id"]) -> None: ...
global___CreateAddressMetadata = CreateAddressMetadata

class UpdateAddressRequest(google.protobuf.message.Message):
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

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    RESERVED_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    """ID of the address to update.

    To get the address ID make a [AddressService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the Address should be updated."""
        pass
    name: typing.Text
    """New name for the address.
    The name must be unique within the folder.
    """

    description: typing.Text
    """New description of the address."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Address labels as `key:value` pairs.

        Existing set of labels is completely replaced by the provided set, so if you just want
        to add or remove a label:
        1. Get the current set of labels with a [AddressService.Get] request.
        2. Add or remove a label in this set.
        3. Send the new set in this field.
        """
        pass
    reserved: builtins.bool
    """Specifies if address is reserved or not."""

    def __init__(self,
        *,
        address_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        reserved: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id","description",b"description","labels",b"labels","name",b"name","reserved",b"reserved","update_mask",b"update_mask"]) -> None: ...
global___UpdateAddressRequest = UpdateAddressRequest

class UpdateAddressMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    """ID of the Address that is being updated."""

    def __init__(self,
        *,
        address_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id"]) -> None: ...
global___UpdateAddressMetadata = UpdateAddressMetadata

class DeleteAddressRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    """ID of the address to delete.

    To get a address ID make a [AddressService.List] request.
    """

    def __init__(self,
        *,
        address_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id"]) -> None: ...
global___DeleteAddressRequest = DeleteAddressRequest

class DeleteAddressMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    """ID of the address that is being deleted."""

    def __init__(self,
        *,
        address_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id"]) -> None: ...
global___DeleteAddressMetadata = DeleteAddressMetadata

class ListAddressOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    """ID of the address to list operations for.

    To get a address ID make a [AddressService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListAddressOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListAddressOperationsResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        address_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListAddressOperationsRequest = ListAddressOperationsRequest

class ListAddressOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified address."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListAddressOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListAddressOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListAddressOperationsResponse = ListAddressOperationsResponse

class MoveAddressRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    destination_folder_id: typing.Text
    def __init__(self,
        *,
        address_id: typing.Text = ...,
        destination_folder_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id","destination_folder_id",b"destination_folder_id"]) -> None: ...
global___MoveAddressRequest = MoveAddressRequest

class MoveAddressMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: typing.Text
    def __init__(self,
        *,
        address_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_id",b"address_id"]) -> None: ...
global___MoveAddressMetadata = MoveAddressMetadata
