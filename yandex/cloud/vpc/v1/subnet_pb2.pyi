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
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _IpVersion:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _IpVersionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IpVersion.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    IP_VERSION_UNSPECIFIED: _IpVersion.ValueType  # 0
    IPV4: _IpVersion.ValueType  # 1
    IPV6: _IpVersion.ValueType  # 2

class IpVersion(_IpVersion, metaclass=_IpVersionEnumTypeWrapper): ...

IP_VERSION_UNSPECIFIED: IpVersion.ValueType  # 0
IPV4: IpVersion.ValueType  # 1
IPV6: IpVersion.ValueType  # 2
global___IpVersion = IpVersion

@typing_extensions.final
class Subnet(google.protobuf.message.Message):
    """A Subnet resource. For more information, see [Subnets](/docs/vpc/concepts/subnets)."""

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

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    V4_CIDR_BLOCKS_FIELD_NUMBER: builtins.int
    V6_CIDR_BLOCKS_FIELD_NUMBER: builtins.int
    ROUTE_TABLE_ID_FIELD_NUMBER: builtins.int
    DHCP_OPTIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the subnet."""
    folder_id: builtins.str
    """ID of the folder that the subnet belongs to."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""
    name: builtins.str
    """Name of the subnet. The name is unique within the project. 3-63 characters long."""
    description: builtins.str
    """Optional description of the subnet. 0-256 characters long."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs. Maximum of 64 per resource."""
    network_id: builtins.str
    """ID of the network the subnet belongs to."""
    zone_id: builtins.str
    """ID of the availability zone where the subnet resides.
    if subnet will be zonal
    """
    @property
    def v4_cidr_blocks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """CIDR block.
        The range of internal addresses that are defined for this subnet.
        This field can be set only at Subnet resource creation time and cannot be changed.
        For example, 10.0.0.0/22 or 192.168.0.0/24.
        Minimum subnet size is /28, maximum subnet size is /16.
        """
    @property
    def v6_cidr_blocks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IPv6 not available yet."""
    route_table_id: builtins.str
    """ID of route table the subnet is linked to."""
    @property
    def dhcp_options(self) -> global___DhcpOptions: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        network_id: builtins.str = ...,
        zone_id: builtins.str = ...,
        v4_cidr_blocks: collections.abc.Iterable[builtins.str] | None = ...,
        v6_cidr_blocks: collections.abc.Iterable[builtins.str] | None = ...,
        route_table_id: builtins.str = ...,
        dhcp_options: global___DhcpOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "dhcp_options", b"dhcp_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "description", b"description", "dhcp_options", b"dhcp_options", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "network_id", b"network_id", "route_table_id", b"route_table_id", "v4_cidr_blocks", b"v4_cidr_blocks", "v6_cidr_blocks", b"v6_cidr_blocks", "zone_id", b"zone_id"]) -> None: ...

global___Subnet = Subnet

@typing_extensions.final
class DhcpOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_NAME_SERVERS_FIELD_NUMBER: builtins.int
    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    NTP_SERVERS_FIELD_NUMBER: builtins.int
    @property
    def domain_name_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    domain_name: builtins.str
    @property
    def ntp_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        domain_name_servers: collections.abc.Iterable[builtins.str] | None = ...,
        domain_name: builtins.str = ...,
        ntp_servers: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain_name", b"domain_name", "domain_name_servers", b"domain_name_servers", "ntp_servers", b"ntp_servers"]) -> None: ...

global___DhcpOptions = DhcpOptions
