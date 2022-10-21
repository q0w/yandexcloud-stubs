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

@typing_extensions.final
class Address(google.protobuf.message.Message):
    """An Address resource. For more information, see [Address](/docs/vpc/concepts/address)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Address._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Address._Type.ValueType  # 0
        INTERNAL: Address._Type.ValueType  # 1
        """Internal IP address."""
        EXTERNAL: Address._Type.ValueType  # 2
        """Public IP address."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: Address.Type.ValueType  # 0
    INTERNAL: Address.Type.ValueType  # 1
    """Internal IP address."""
    EXTERNAL: Address.Type.ValueType  # 2
    """Public IP address."""

    class _IpVersion:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _IpVersionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Address._IpVersion.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        IP_VERSION_UNSPECIFIED: Address._IpVersion.ValueType  # 0
        IPV4: Address._IpVersion.ValueType  # 1
        """IPv4 address."""
        IPV6: Address._IpVersion.ValueType  # 2
        """IPv6 address."""

    class IpVersion(_IpVersion, metaclass=_IpVersionEnumTypeWrapper): ...
    IP_VERSION_UNSPECIFIED: Address.IpVersion.ValueType  # 0
    IPV4: Address.IpVersion.ValueType  # 1
    """IPv4 address."""
    IPV6: Address.IpVersion.ValueType  # 2
    """IPv6 address."""

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
    EXTERNAL_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    RESERVED_FIELD_NUMBER: builtins.int
    USED_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    IP_VERSION_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the address. Generated at creation time."""
    folder_id: builtins.str
    """ID of the folder that the address belongs to."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
    name: builtins.str
    """Name of the address.
    The name is unique within the folder.
    """
    description: builtins.str
    """Description of the address."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""
    @property
    def external_ipv4_address(self) -> global___ExternalIpv4Address: ...
    reserved: builtins.bool
    """Specifies if address is reserved or not."""
    used: builtins.bool
    """Specifies if address is used or not."""
    type: global___Address.Type.ValueType
    """Type of the IP address."""
    ip_version: global___Address.IpVersion.ValueType
    """Vervion of the IP address."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        external_ipv4_address: global___ExternalIpv4Address | None = ...,
        reserved: builtins.bool = ...,
        used: builtins.bool = ...,
        type: global___Address.Type.ValueType = ...,
        ip_version: global___Address.IpVersion.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address", b"address", "created_at", b"created_at", "external_ipv4_address", b"external_ipv4_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "created_at", b"created_at", "description", b"description", "external_ipv4_address", b"external_ipv4_address", "folder_id", b"folder_id", "id", b"id", "ip_version", b"ip_version", "labels", b"labels", "name", b"name", "reserved", b"reserved", "type", b"type", "used", b"used"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["address", b"address"]) -> typing_extensions.Literal["external_ipv4_address"] | None: ...

global___Address = Address

@typing_extensions.final
class ExternalIpv4Address(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    REQUIREMENTS_FIELD_NUMBER: builtins.int
    address: builtins.str
    """Value of address."""
    zone_id: builtins.str
    """Availability zone from which the address will be allocated."""
    @property
    def requirements(self) -> global___AddressRequirements:
        """Parameters of the allocated address, for example DDoS Protection."""
    def __init__(
        self,
        *,
        address: builtins.str = ...,
        zone_id: builtins.str = ...,
        requirements: global___AddressRequirements | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["requirements", b"requirements"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "requirements", b"requirements", "zone_id", b"zone_id"]) -> None: ...

global___ExternalIpv4Address = ExternalIpv4Address

@typing_extensions.final
class AddressRequirements(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DDOS_PROTECTION_PROVIDER_FIELD_NUMBER: builtins.int
    OUTGOING_SMTP_CAPABILITY_FIELD_NUMBER: builtins.int
    ddos_protection_provider: builtins.str
    """DDoS protection provider ID."""
    outgoing_smtp_capability: builtins.str
    """Capability to send SMTP traffic."""
    def __init__(
        self,
        *,
        ddos_protection_provider: builtins.str = ...,
        outgoing_smtp_capability: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ddos_protection_provider", b"ddos_protection_provider", "outgoing_smtp_capability", b"outgoing_smtp_capability"]) -> None: ...

global___AddressRequirements = AddressRequirements
