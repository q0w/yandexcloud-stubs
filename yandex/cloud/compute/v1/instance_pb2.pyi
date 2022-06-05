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
    """IPv4 address, for example 192.0.2.235."""

    IPV6: _IpVersion.ValueType  # 2
    """IPv6 address. Not available yet."""

class IpVersion(_IpVersion, metaclass=_IpVersionEnumTypeWrapper):
    pass

IP_VERSION_UNSPECIFIED: IpVersion.ValueType  # 0
IPV4: IpVersion.ValueType  # 1
"""IPv4 address, for example 192.0.2.235."""

IPV6: IpVersion.ValueType  # 2
"""IPv6 address. Not available yet."""

global___IpVersion = IpVersion


class Instance(google.protobuf.message.Message):
    """An Instance resource. For more information, see [Instances](/docs/compute/concepts/vm)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Instance._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Instance._Status.ValueType  # 0
        PROVISIONING: Instance._Status.ValueType  # 1
        """Instance is waiting for resources to be allocated."""

        RUNNING: Instance._Status.ValueType  # 2
        """Instance is running normally."""

        STOPPING: Instance._Status.ValueType  # 3
        """Instance is being stopped."""

        STOPPED: Instance._Status.ValueType  # 4
        """Instance stopped."""

        STARTING: Instance._Status.ValueType  # 5
        """Instance is being started."""

        RESTARTING: Instance._Status.ValueType  # 6
        """Instance is being restarted."""

        UPDATING: Instance._Status.ValueType  # 7
        """Instance is being updated."""

        ERROR: Instance._Status.ValueType  # 8
        """Instance encountered a problem and cannot operate."""

        CRASHED: Instance._Status.ValueType  # 9
        """Instance crashed and will be restarted automatically."""

        DELETING: Instance._Status.ValueType  # 10
        """Instance is being deleted."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNSPECIFIED: Instance.Status.ValueType  # 0
    PROVISIONING: Instance.Status.ValueType  # 1
    """Instance is waiting for resources to be allocated."""

    RUNNING: Instance.Status.ValueType  # 2
    """Instance is running normally."""

    STOPPING: Instance.Status.ValueType  # 3
    """Instance is being stopped."""

    STOPPED: Instance.Status.ValueType  # 4
    """Instance stopped."""

    STARTING: Instance.Status.ValueType  # 5
    """Instance is being started."""

    RESTARTING: Instance.Status.ValueType  # 6
    """Instance is being restarted."""

    UPDATING: Instance.Status.ValueType  # 7
    """Instance is being updated."""

    ERROR: Instance.Status.ValueType  # 8
    """Instance encountered a problem and cannot operate."""

    CRASHED: Instance.Status.ValueType  # 9
    """Instance crashed and will be restarted automatically."""

    DELETING: Instance.Status.ValueType  # 10
    """Instance is being deleted."""


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

    class MetadataEntry(google.protobuf.message.Message):
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
    ZONE_ID_FIELD_NUMBER: builtins.int
    PLATFORM_ID_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    BOOT_DISK_FIELD_NUMBER: builtins.int
    SECONDARY_DISKS_FIELD_NUMBER: builtins.int
    LOCAL_DISKS_FIELD_NUMBER: builtins.int
    FILESYSTEMS_FIELD_NUMBER: builtins.int
    NETWORK_INTERFACES_FIELD_NUMBER: builtins.int
    FQDN_FIELD_NUMBER: builtins.int
    SCHEDULING_POLICY_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    NETWORK_SETTINGS_FIELD_NUMBER: builtins.int
    PLACEMENT_POLICY_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the instance."""

    folder_id: typing.Text
    """ID of the folder that the instance belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    name: typing.Text
    """Name of the instance. 1-63 characters long."""

    description: typing.Text
    """Description of the instance. 0-256 characters long."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs. Maximum of 64 per resource."""
        pass
    zone_id: typing.Text
    """ID of the availability zone where the instance resides."""

    platform_id: typing.Text
    """ID of the hardware platform configuration for the instance."""

    @property
    def resources(self) -> global___Resources:
        """Computing resources of the instance such as the amount of memory and number of cores."""
        pass
    status: global___Instance.Status.ValueType
    """Status of the instance."""

    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """The metadata `key:value` pairs assigned to this instance. This includes custom metadata and predefined keys.

        For example, you may use the metadata in order to provide your public SSH key to the instance.
        For more information, see [Metadata](/docs/compute/concepts/vm-metadata).
        """
        pass
    @property
    def boot_disk(self) -> global___AttachedDisk:
        """Boot disk that is attached to the instance."""
        pass
    @property
    def secondary_disks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AttachedDisk]:
        """Array of secondary disks that are attached to the instance."""
        pass
    @property
    def local_disks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AttachedLocalDisk]:
        """Array of local disks that are attached to the instance."""
        pass
    @property
    def filesystems(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AttachedFilesystem]:
        """Array of filesystems that are attached to the instance."""
        pass
    @property
    def network_interfaces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetworkInterface]:
        """Array of network interfaces that are attached to the instance."""
        pass
    fqdn: typing.Text
    """A domain name of the instance. FQDN is defined by the server
    in the format `<hostname>.<region_id>.internal` when the instance is created.
    If the hostname were not specified when the instance was created, FQDN would be `<id>.auto.internal`.
    output only
    """

    @property
    def scheduling_policy(self) -> global___SchedulingPolicy:
        """Scheduling policy configuration."""
        pass
    service_account_id: typing.Text
    """ID of the service account to use for [authentication inside the instance](/docs/compute/operations/vm-connect/auth-inside-vm).
    To get the service account ID, use a [yandex.cloud.iam.v1.ServiceAccountService.List] request.
    """

    @property
    def network_settings(self) -> global___NetworkSettings:
        """Network Settings"""
        pass
    @property
    def placement_policy(self) -> global___PlacementPolicy:
        """Placement policy configuration."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        zone_id: typing.Text = ...,
        platform_id: typing.Text = ...,
        resources: typing.Optional[global___Resources] = ...,
        status: global___Instance.Status.ValueType = ...,
        metadata: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        boot_disk: typing.Optional[global___AttachedDisk] = ...,
        secondary_disks: typing.Optional[typing.Iterable[global___AttachedDisk]] = ...,
        local_disks: typing.Optional[typing.Iterable[global___AttachedLocalDisk]] = ...,
        filesystems: typing.Optional[typing.Iterable[global___AttachedFilesystem]] = ...,
        network_interfaces: typing.Optional[typing.Iterable[global___NetworkInterface]] = ...,
        fqdn: typing.Text = ...,
        scheduling_policy: typing.Optional[global___SchedulingPolicy] = ...,
        service_account_id: typing.Text = ...,
        network_settings: typing.Optional[global___NetworkSettings] = ...,
        placement_policy: typing.Optional[global___PlacementPolicy] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["boot_disk",b"boot_disk","created_at",b"created_at","network_settings",b"network_settings","placement_policy",b"placement_policy","resources",b"resources","scheduling_policy",b"scheduling_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["boot_disk",b"boot_disk","created_at",b"created_at","description",b"description","filesystems",b"filesystems","folder_id",b"folder_id","fqdn",b"fqdn","id",b"id","labels",b"labels","local_disks",b"local_disks","metadata",b"metadata","name",b"name","network_interfaces",b"network_interfaces","network_settings",b"network_settings","placement_policy",b"placement_policy","platform_id",b"platform_id","resources",b"resources","scheduling_policy",b"scheduling_policy","secondary_disks",b"secondary_disks","service_account_id",b"service_account_id","status",b"status","zone_id",b"zone_id"]) -> None: ...
global___Instance = Instance

class Resources(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MEMORY_FIELD_NUMBER: builtins.int
    CORES_FIELD_NUMBER: builtins.int
    CORE_FRACTION_FIELD_NUMBER: builtins.int
    GPUS_FIELD_NUMBER: builtins.int
    memory: builtins.int
    """The amount of memory available to the instance, specified in bytes."""

    cores: builtins.int
    """The number of cores available to the instance."""

    core_fraction: builtins.int
    """Baseline level of CPU performance with the ability to burst performance above that baseline level.
    This field sets baseline performance for each core.
    """

    gpus: builtins.int
    """The number of GPUs available to the instance."""

    def __init__(self,
        *,
        memory: builtins.int = ...,
        cores: builtins.int = ...,
        core_fraction: builtins.int = ...,
        gpus: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["core_fraction",b"core_fraction","cores",b"cores","gpus",b"gpus","memory",b"memory"]) -> None: ...
global___Resources = Resources

class AttachedDisk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Mode:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AttachedDisk._Mode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        MODE_UNSPECIFIED: AttachedDisk._Mode.ValueType  # 0
        READ_ONLY: AttachedDisk._Mode.ValueType  # 1
        """Read-only access."""

        READ_WRITE: AttachedDisk._Mode.ValueType  # 2
        """Read/Write access."""

    class Mode(_Mode, metaclass=_ModeEnumTypeWrapper):
        pass

    MODE_UNSPECIFIED: AttachedDisk.Mode.ValueType  # 0
    READ_ONLY: AttachedDisk.Mode.ValueType  # 1
    """Read-only access."""

    READ_WRITE: AttachedDisk.Mode.ValueType  # 2
    """Read/Write access."""


    MODE_FIELD_NUMBER: builtins.int
    DEVICE_NAME_FIELD_NUMBER: builtins.int
    AUTO_DELETE_FIELD_NUMBER: builtins.int
    DISK_ID_FIELD_NUMBER: builtins.int
    mode: global___AttachedDisk.Mode.ValueType
    """Access mode to the Disk resource."""

    device_name: typing.Text
    """Serial number that is reflected into the /dev/disk/by-id/ tree
    of a Linux operating system running within the instance.

    This value can be used to reference the device for mounting, resizing, and so on, from within the instance.
    """

    auto_delete: builtins.bool
    """Specifies whether the disk will be auto-deleted when the instance is deleted."""

    disk_id: typing.Text
    """ID of the disk that is attached to the instance."""

    def __init__(self,
        *,
        mode: global___AttachedDisk.Mode.ValueType = ...,
        device_name: typing.Text = ...,
        auto_delete: builtins.bool = ...,
        disk_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_delete",b"auto_delete","device_name",b"device_name","disk_id",b"disk_id","mode",b"mode"]) -> None: ...
global___AttachedDisk = AttachedDisk

class AttachedLocalDisk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SIZE_FIELD_NUMBER: builtins.int
    DEVICE_NAME_FIELD_NUMBER: builtins.int
    size: builtins.int
    """Size of the disk, specified in bytes."""

    device_name: typing.Text
    """Serial number that is reflected into the /dev/disk/by-id/ tree
    of a Linux operating system running within the instance.

    This value can be used to reference the device for mounting, resizing, and so on, from within the instance.
    """

    def __init__(self,
        *,
        size: builtins.int = ...,
        device_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["device_name",b"device_name","size",b"size"]) -> None: ...
global___AttachedLocalDisk = AttachedLocalDisk

class AttachedFilesystem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Mode:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AttachedFilesystem._Mode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        MODE_UNSPECIFIED: AttachedFilesystem._Mode.ValueType  # 0
        READ_ONLY: AttachedFilesystem._Mode.ValueType  # 1
        """Read-only access."""

        READ_WRITE: AttachedFilesystem._Mode.ValueType  # 2
        """Read/Write access."""

    class Mode(_Mode, metaclass=_ModeEnumTypeWrapper):
        pass

    MODE_UNSPECIFIED: AttachedFilesystem.Mode.ValueType  # 0
    READ_ONLY: AttachedFilesystem.Mode.ValueType  # 1
    """Read-only access."""

    READ_WRITE: AttachedFilesystem.Mode.ValueType  # 2
    """Read/Write access."""


    MODE_FIELD_NUMBER: builtins.int
    DEVICE_NAME_FIELD_NUMBER: builtins.int
    FILESYSTEM_ID_FIELD_NUMBER: builtins.int
    mode: global___AttachedFilesystem.Mode.ValueType
    """Access mode to the filesystem."""

    device_name: typing.Text
    """Name of the device representing the filesystem on the instance.

    The name should be used for referencing the filesystem from within the instance
    when it's being mounted, resized etc.
    """

    filesystem_id: typing.Text
    """ID of the filesystem that is attached to the instance."""

    def __init__(self,
        *,
        mode: global___AttachedFilesystem.Mode.ValueType = ...,
        device_name: typing.Text = ...,
        filesystem_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["device_name",b"device_name","filesystem_id",b"filesystem_id","mode",b"mode"]) -> None: ...
global___AttachedFilesystem = AttachedFilesystem

class NetworkInterface(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_FIELD_NUMBER: builtins.int
    MAC_ADDRESS_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    PRIMARY_V4_ADDRESS_FIELD_NUMBER: builtins.int
    PRIMARY_V6_ADDRESS_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    index: typing.Text
    """The index of the network interface, generated by the server, 0,1,2... etc.
    Currently only one network interface is supported per instance.
    """

    mac_address: typing.Text
    """MAC address that is assigned to the network interface."""

    subnet_id: typing.Text
    """ID of the subnet."""

    @property
    def primary_v4_address(self) -> global___PrimaryAddress:
        """Primary IPv4 address that is assigned to the instance for this network interface."""
        pass
    @property
    def primary_v6_address(self) -> global___PrimaryAddress:
        """Primary IPv6 address that is assigned to the instance for this network interface. IPv6 not available yet."""
        pass
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """ID's of security groups attached to the interface"""
        pass
    def __init__(self,
        *,
        index: typing.Text = ...,
        mac_address: typing.Text = ...,
        subnet_id: typing.Text = ...,
        primary_v4_address: typing.Optional[global___PrimaryAddress] = ...,
        primary_v6_address: typing.Optional[global___PrimaryAddress] = ...,
        security_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["primary_v4_address",b"primary_v4_address","primary_v6_address",b"primary_v6_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["index",b"index","mac_address",b"mac_address","primary_v4_address",b"primary_v4_address","primary_v6_address",b"primary_v6_address","security_group_ids",b"security_group_ids","subnet_id",b"subnet_id"]) -> None: ...
global___NetworkInterface = NetworkInterface

class PrimaryAddress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    ONE_TO_ONE_NAT_FIELD_NUMBER: builtins.int
    DNS_RECORDS_FIELD_NUMBER: builtins.int
    address: typing.Text
    """An IPv4 internal network address that is assigned to the instance for this network interface."""

    @property
    def one_to_one_nat(self) -> global___OneToOneNat:
        """One-to-one NAT configuration. If missing, NAT has not been set up."""
        pass
    @property
    def dns_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DnsRecord]:
        """Internal DNS configuration"""
        pass
    def __init__(self,
        *,
        address: typing.Text = ...,
        one_to_one_nat: typing.Optional[global___OneToOneNat] = ...,
        dns_records: typing.Optional[typing.Iterable[global___DnsRecord]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["one_to_one_nat",b"one_to_one_nat"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","dns_records",b"dns_records","one_to_one_nat",b"one_to_one_nat"]) -> None: ...
global___PrimaryAddress = PrimaryAddress

class OneToOneNat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    IP_VERSION_FIELD_NUMBER: builtins.int
    DNS_RECORDS_FIELD_NUMBER: builtins.int
    address: typing.Text
    """An external IP address associated with this instance."""

    ip_version: global___IpVersion.ValueType
    """IP version for the external IP address."""

    @property
    def dns_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DnsRecord]:
        """External DNS configuration"""
        pass
    def __init__(self,
        *,
        address: typing.Text = ...,
        ip_version: global___IpVersion.ValueType = ...,
        dns_records: typing.Optional[typing.Iterable[global___DnsRecord]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","dns_records",b"dns_records","ip_version",b"ip_version"]) -> None: ...
global___OneToOneNat = OneToOneNat

class DnsRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FQDN_FIELD_NUMBER: builtins.int
    DNS_ZONE_ID_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    PTR_FIELD_NUMBER: builtins.int
    fqdn: typing.Text
    """Name of the A/AAAA record as specified when creating the instance.
    Note that if `fqdn' has no trailing '.', it is specified relative to the zone (@see dns_zone_id).
    """

    dns_zone_id: typing.Text
    """DNS zone id for the record (optional, if not set, some private zone is used)."""

    ttl: builtins.int
    """DNS record ttl (optional, if not set, a reasonable default is used.)"""

    ptr: builtins.bool
    """When true, indicates there is a corresponding auto-created PTR DNS record."""

    def __init__(self,
        *,
        fqdn: typing.Text = ...,
        dns_zone_id: typing.Text = ...,
        ttl: builtins.int = ...,
        ptr: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dns_zone_id",b"dns_zone_id","fqdn",b"fqdn","ptr",b"ptr","ttl",b"ttl"]) -> None: ...
global___DnsRecord = DnsRecord

class SchedulingPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PREEMPTIBLE_FIELD_NUMBER: builtins.int
    preemptible: builtins.bool
    """True for short-lived compute instances. For more information, see [Preemptible VMs](/docs/compute/concepts/preemptible-vm)."""

    def __init__(self,
        *,
        preemptible: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["preemptible",b"preemptible"]) -> None: ...
global___SchedulingPolicy = SchedulingPolicy

class NetworkSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NetworkSettings._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: NetworkSettings._Type.ValueType  # 0
        STANDARD: NetworkSettings._Type.ValueType  # 1
        """Standard network."""

        SOFTWARE_ACCELERATED: NetworkSettings._Type.ValueType  # 2
        """Software accelerated network."""

        HARDWARE_ACCELERATED: NetworkSettings._Type.ValueType  # 3
        """Hardware accelerated network (not available yet, reserved for future use)."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    TYPE_UNSPECIFIED: NetworkSettings.Type.ValueType  # 0
    STANDARD: NetworkSettings.Type.ValueType  # 1
    """Standard network."""

    SOFTWARE_ACCELERATED: NetworkSettings.Type.ValueType  # 2
    """Software accelerated network."""

    HARDWARE_ACCELERATED: NetworkSettings.Type.ValueType  # 3
    """Hardware accelerated network (not available yet, reserved for future use)."""


    TYPE_FIELD_NUMBER: builtins.int
    type: global___NetworkSettings.Type.ValueType
    """Network Type"""

    def __init__(self,
        *,
        type: global___NetworkSettings.Type.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["type",b"type"]) -> None: ...
global___NetworkSettings = NetworkSettings

class PlacementPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class HostAffinityRule(google.protobuf.message.Message):
        """Affinitity definition"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _Operator:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _OperatorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PlacementPolicy.HostAffinityRule._Operator.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            OPERATOR_UNSPECIFIED: PlacementPolicy.HostAffinityRule._Operator.ValueType  # 0
            IN: PlacementPolicy.HostAffinityRule._Operator.ValueType  # 1
            NOT_IN: PlacementPolicy.HostAffinityRule._Operator.ValueType  # 2
        class Operator(_Operator, metaclass=_OperatorEnumTypeWrapper):
            pass

        OPERATOR_UNSPECIFIED: PlacementPolicy.HostAffinityRule.Operator.ValueType  # 0
        IN: PlacementPolicy.HostAffinityRule.Operator.ValueType  # 1
        NOT_IN: PlacementPolicy.HostAffinityRule.Operator.ValueType  # 2

        KEY_FIELD_NUMBER: builtins.int
        OP_FIELD_NUMBER: builtins.int
        VALUES_FIELD_NUMBER: builtins.int
        key: typing.Text
        """Affinity label or one of reserved values - 'yc.hostId', 'yc.hostGroupId'"""

        op: global___PlacementPolicy.HostAffinityRule.Operator.ValueType
        """Include or exclude action"""

        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """Affinity value or host ID or host group ID"""
            pass
        def __init__(self,
            *,
            key: typing.Text = ...,
            op: global___PlacementPolicy.HostAffinityRule.Operator.ValueType = ...,
            values: typing.Optional[typing.Iterable[typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","op",b"op","values",b"values"]) -> None: ...

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    HOST_AFFINITY_RULES_FIELD_NUMBER: builtins.int
    placement_group_id: typing.Text
    """Placement group ID."""

    @property
    def host_affinity_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PlacementPolicy.HostAffinityRule]:
        """List of affinity rules. Scheduler will attempt to allocate instances according to order of rules."""
        pass
    def __init__(self,
        *,
        placement_group_id: typing.Text = ...,
        host_affinity_rules: typing.Optional[typing.Iterable[global___PlacementPolicy.HostAffinityRule]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_affinity_rules",b"host_affinity_rules","placement_group_id",b"placement_group_id"]) -> None: ...
global___PlacementPolicy = PlacementPolicy
