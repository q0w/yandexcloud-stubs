"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _IpVersion:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _IpVersionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IpVersion.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    IP_VERSION_UNSPECIFIED: _IpVersion.ValueType  # 0
    IPV4: _IpVersion.ValueType  # 1
    IPV6: _IpVersion.ValueType  # 2
class IpVersion(_IpVersion, metaclass=_IpVersionEnumTypeWrapper):
    pass

IP_VERSION_UNSPECIFIED: IpVersion.ValueType  # 0
IPV4: IpVersion.ValueType  # 1
IPV6: IpVersion.ValueType  # 2
global___IpVersion = IpVersion


class Subnet(google.protobuf.message.Message):
    """A Subnet resource. For more information, see [Subnets](/docs/vpc/concepts/subnets)."""
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
    id: typing.Text
    """ID of the subnet."""

    folder_id: typing.Text
    """ID of the folder that the subnet belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""
        pass
    name: typing.Text
    """Name of the subnet. The name is unique within the project. 3-63 characters long."""

    description: typing.Text
    """Optional description of the subnet. 0-256 characters long."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `` key:value `` pairs. Maximum of 64 per resource."""
        pass
    network_id: typing.Text
    """ID of the network the subnet belongs to."""

    zone_id: typing.Text
    """ID of the availability zone where the subnet resides.
    if subnet will be zonal
    """

    @property
    def v4_cidr_blocks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """CIDR block.
        The range of internal addresses that are defined for this subnet.
        This field can be set only at Subnet resource creation time and cannot be changed.
        For example, 10.0.0.0/22 or 192.168.0.0/24.
        Minimum subnet size is /28, maximum subnet size is /16.
        """
        pass
    @property
    def v6_cidr_blocks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IPv6 not available yet."""
        pass
    route_table_id: typing.Text
    """ID of route table the subnet is linked to."""

    @property
    def dhcp_options(self) -> global___DhcpOptions: ...
    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        network_id: typing.Text = ...,
        zone_id: typing.Text = ...,
        v4_cidr_blocks: typing.Optional[typing.Iterable[typing.Text]] = ...,
        v6_cidr_blocks: typing.Optional[typing.Iterable[typing.Text]] = ...,
        route_table_id: typing.Text = ...,
        dhcp_options: typing.Optional[global___DhcpOptions] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","dhcp_options",b"dhcp_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","description",b"description","dhcp_options",b"dhcp_options","folder_id",b"folder_id","id",b"id","labels",b"labels","name",b"name","network_id",b"network_id","route_table_id",b"route_table_id","v4_cidr_blocks",b"v4_cidr_blocks","v6_cidr_blocks",b"v6_cidr_blocks","zone_id",b"zone_id"]) -> None: ...
global___Subnet = Subnet

class DhcpOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOMAIN_NAME_SERVERS_FIELD_NUMBER: builtins.int
    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    NTP_SERVERS_FIELD_NUMBER: builtins.int
    @property
    def domain_name_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    domain_name: typing.Text
    @property
    def ntp_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        domain_name_servers: typing.Optional[typing.Iterable[typing.Text]] = ...,
        domain_name: typing.Text = ...,
        ntp_servers: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain_name",b"domain_name","domain_name_servers",b"domain_name_servers","ntp_servers",b"ntp_servers"]) -> None: ...
global___DhcpOptions = DhcpOptions