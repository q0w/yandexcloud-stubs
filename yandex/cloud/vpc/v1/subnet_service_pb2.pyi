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
import yandex.cloud.operation.operation_pb2
import yandex.cloud.reference.reference_pb2
import yandex.cloud.vpc.v1.subnet_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetSubnetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource to return.
    To get the subnet ID use a [SubnetService.List] request.
    """
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___GetSubnetRequest = GetSubnetRequest

@typing_extensions.final
class ListSubnetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list subnets in.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListSubnetsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListSubnetsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [Subnet.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListSubnetsRequest = ListSubnetsRequest

@typing_extensions.final
class ListSubnetsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def subnets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.subnet_pb2.Subnet]:
        """List of Subnet resources."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListSubnetsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListSubnetsRequest.page_token] query parameter
    in the next list request. Subsequent list requests will have their own
    [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        subnets: collections.abc.Iterable[yandex.cloud.vpc.v1.subnet_pb2.Subnet] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "subnets", b"subnets"]) -> None: ...

global___ListSubnetsResponse = ListSubnetsResponse

@typing_extensions.final
class CreateSubnetRequest(google.protobuf.message.Message):
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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    V4_CIDR_BLOCKS_FIELD_NUMBER: builtins.int
    ROUTE_TABLE_ID_FIELD_NUMBER: builtins.int
    DHCP_OPTIONS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a subnet in.
    To get folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the subnet.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the subnet."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels, `` key:value `` pairs."""
    network_id: builtins.str
    """ID of the network to create subnet in."""
    zone_id: builtins.str
    """ID of the availability zone where the subnet resides.
    To get a list of available zones, use the [yandex.cloud.compute.v1.ZoneService.List] request.
    """
    @property
    def v4_cidr_blocks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """CIDR block.
        The range of internal addresses that are defined for this subnet.
        This field can be set only at Subnet resource creation time and cannot be changed.
        For example, 10.0.0.0/22 or 192.168.0.0/24.
        Minimum subnet size is /28, maximum subnet size is /16.
        """
    route_table_id: builtins.str
    """IPv6 not available yet.
     repeated string v6_cidr_blocks = 8;

    ID of route table the subnet is linked to.
    """
    @property
    def dhcp_options(self) -> yandex.cloud.vpc.v1.subnet_pb2.DhcpOptions: ...
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        network_id: builtins.str = ...,
        zone_id: builtins.str = ...,
        v4_cidr_blocks: collections.abc.Iterable[builtins.str] | None = ...,
        route_table_id: builtins.str = ...,
        dhcp_options: yandex.cloud.vpc.v1.subnet_pb2.DhcpOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dhcp_options", b"dhcp_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "dhcp_options", b"dhcp_options", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "network_id", b"network_id", "route_table_id", b"route_table_id", "v4_cidr_blocks", b"v4_cidr_blocks", "zone_id", b"zone_id"]) -> None: ...

global___CreateSubnetRequest = CreateSubnetRequest

@typing_extensions.final
class CreateSubnetMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the subnet that is being created."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___CreateSubnetMetadata = CreateSubnetMetadata

@typing_extensions.final
class UpdateSubnetRequest(google.protobuf.message.Message):
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

    SUBNET_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ROUTE_TABLE_ID_FIELD_NUMBER: builtins.int
    DHCP_OPTIONS_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource to update."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Subnet resource are going to be updated."""
    name: builtins.str
    """Name of the subnet.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the subnet."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs."""
    route_table_id: builtins.str
    """ID of route table the subnet is linked to."""
    @property
    def dhcp_options(self) -> yandex.cloud.vpc.v1.subnet_pb2.DhcpOptions: ...
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        route_table_id: builtins.str = ...,
        dhcp_options: yandex.cloud.vpc.v1.subnet_pb2.DhcpOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dhcp_options", b"dhcp_options", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "dhcp_options", b"dhcp_options", "labels", b"labels", "name", b"name", "route_table_id", b"route_table_id", "subnet_id", b"subnet_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateSubnetRequest = UpdateSubnetRequest

@typing_extensions.final
class UpdateSubnetMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource that is being updated."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___UpdateSubnetMetadata = UpdateSubnetMetadata

@typing_extensions.final
class AddSubnetCidrBlocksRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    V4_CIDR_BLOCKS_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource that is being updated."""
    @property
    def v4_cidr_blocks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """CIDR block.
        The range of internal addresses that should be added to this subnet.
        For example, 10.0.0.0/22 or 192.168.0.0/24.
        Minimum subnet size is /28, maximum subnet size is /16.
        """
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
        v4_cidr_blocks: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id", "v4_cidr_blocks", b"v4_cidr_blocks"]) -> None: ...

global___AddSubnetCidrBlocksRequest = AddSubnetCidrBlocksRequest

@typing_extensions.final
class AddSubnetCidrBlocksMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource that is being updated."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___AddSubnetCidrBlocksMetadata = AddSubnetCidrBlocksMetadata

@typing_extensions.final
class RemoveSubnetCidrBlocksRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    V4_CIDR_BLOCKS_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource that is being updated."""
    @property
    def v4_cidr_blocks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """CIDR block.
        The range of internal addresses that are removed from this subnet.
        """
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
        v4_cidr_blocks: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id", "v4_cidr_blocks", b"v4_cidr_blocks"]) -> None: ...

global___RemoveSubnetCidrBlocksRequest = RemoveSubnetCidrBlocksRequest

@typing_extensions.final
class RemoveSubnetCidrBlocksMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource that is being updated."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___RemoveSubnetCidrBlocksMetadata = RemoveSubnetCidrBlocksMetadata

@typing_extensions.final
class DeleteSubnetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the subnet to delete.
    To get the subnet ID use a [SubnetService.List] request.
    """
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___DeleteSubnetRequest = DeleteSubnetRequest

@typing_extensions.final
class DeleteSubnetMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource that is being deleted."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___DeleteSubnetMetadata = DeleteSubnetMetadata

@typing_extensions.final
class ListSubnetOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size], the service returns a [ListSubnetOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListSubnetOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size", b"page_size", "page_token", b"page_token", "subnet_id", b"subnet_id"]) -> None: ...

global___ListSubnetOperationsRequest = ListSubnetOperationsRequest

@typing_extensions.final
class ListSubnetOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified Subnet resource."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListSubnetOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListSubnetOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListSubnetOperationsResponse = ListSubnetOperationsResponse

@typing_extensions.final
class MoveSubnetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource to move."""
    destination_folder_id: builtins.str
    """ID of the destination folder."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
        destination_folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["destination_folder_id", b"destination_folder_id", "subnet_id", b"subnet_id"]) -> None: ...

global___MoveSubnetRequest = MoveSubnetRequest

@typing_extensions.final
class MoveSubnetMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the Subnet resource that is being moved."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___MoveSubnetMetadata = MoveSubnetMetadata

@typing_extensions.final
class ListUsedAddressesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    page_size: builtins.int
    page_token: builtins.str
    filter: builtins.str
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "page_size", b"page_size", "page_token", b"page_token", "subnet_id", b"subnet_id"]) -> None: ...

global___ListUsedAddressesRequest = ListUsedAddressesRequest

@typing_extensions.final
class ListUsedAddressesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESSES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def addresses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UsedAddress]: ...
    next_page_token: builtins.str
    def __init__(
        self,
        *,
        addresses: collections.abc.Iterable[global___UsedAddress] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["addresses", b"addresses", "next_page_token", b"next_page_token"]) -> None: ...

global___ListUsedAddressesResponse = ListUsedAddressesResponse

@typing_extensions.final
class UsedAddress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    IP_VERSION_FIELD_NUMBER: builtins.int
    REFERENCES_FIELD_NUMBER: builtins.int
    address: builtins.str
    ip_version: yandex.cloud.vpc.v1.subnet_pb2.IpVersion.ValueType
    @property
    def references(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.reference.reference_pb2.Reference]: ...
    def __init__(
        self,
        *,
        address: builtins.str = ...,
        ip_version: yandex.cloud.vpc.v1.subnet_pb2.IpVersion.ValueType = ...,
        references: collections.abc.Iterable[yandex.cloud.reference.reference_pb2.Reference] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "ip_version", b"ip_version", "references", b"references"]) -> None: ...

global___UsedAddress = UsedAddress
