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
    """IPv4 address, for example 192.168.0.0."""

    IPV6: _IpVersion.ValueType  # 2
    """IPv6 address, not available yet."""

class IpVersion(_IpVersion, metaclass=_IpVersionEnumTypeWrapper):
    pass

IP_VERSION_UNSPECIFIED: IpVersion.ValueType  # 0
IPV4: IpVersion.ValueType  # 1
"""IPv4 address, for example 192.168.0.0."""

IPV6: IpVersion.ValueType  # 2
"""IPv6 address, not available yet."""

global___IpVersion = IpVersion


class Node(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Node._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Node._Status.ValueType  # 0
        PROVISIONING: Node._Status.ValueType  # 1
        """Node instance is not yet created (e.g. in progress)."""

        NOT_CONNECTED: Node._Status.ValueType  # 2
        """Node instance is created but not registered
        (e.g. is still initializing).
        """

        NOT_READY: Node._Status.ValueType  # 3
        """Node has connected but is not ready for
        workload (see conditions for details).
        """

        READY: Node._Status.ValueType  # 4
        """Node has connected and ready for workload."""

        MISSING: Node._Status.ValueType  # 5
        """Node is still registered but its instance
        is deleted (this is our bug).
        """

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Computed node status."""
        pass

    STATUS_UNSPECIFIED: Node.Status.ValueType  # 0
    PROVISIONING: Node.Status.ValueType  # 1
    """Node instance is not yet created (e.g. in progress)."""

    NOT_CONNECTED: Node.Status.ValueType  # 2
    """Node instance is created but not registered
    (e.g. is still initializing).
    """

    NOT_READY: Node.Status.ValueType  # 3
    """Node has connected but is not ready for
    workload (see conditions for details).
    """

    READY: Node.Status.ValueType  # 4
    """Node has connected and ready for workload."""

    MISSING: Node.Status.ValueType  # 5
    """Node is still registered but its instance
    is deleted (this is our bug).
    """


    class KubernetesStatus(google.protobuf.message.Message):
        """Kubernetes node info"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ID_FIELD_NUMBER: builtins.int
        CONDITIONS_FIELD_NUMBER: builtins.int
        TAINTS_FIELD_NUMBER: builtins.int
        ATTACHED_VOLUMES_FIELD_NUMBER: builtins.int
        id: typing.Text
        """Node id (and instance name)"""

        @property
        def conditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Condition]:
            """Conditions is an array of current observed node conditions.
            More info: https://kubernetes.io/docs/concepts/nodes/node/#condition
            """
            pass
        @property
        def taints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Taint]:
            """If specified, the node's taints."""
            pass
        @property
        def attached_volumes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AttachedVolume]:
            """List of volumes that are attached to the node."""
            pass
        def __init__(self,
            *,
            id: typing.Text = ...,
            conditions: typing.Optional[typing.Iterable[global___Condition]] = ...,
            taints: typing.Optional[typing.Iterable[global___Taint]] = ...,
            attached_volumes: typing.Optional[typing.Iterable[global___AttachedVolume]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["attached_volumes",b"attached_volumes","conditions",b"conditions","id",b"id","taints",b"taints"]) -> None: ...

    class CloudStatus(google.protobuf.message.Message):
        """Cloud instance info"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ID_FIELD_NUMBER: builtins.int
        STATUS_FIELD_NUMBER: builtins.int
        STATUS_MESSAGE_FIELD_NUMBER: builtins.int
        id: typing.Text
        """Compute instance id"""

        status: typing.Text
        """IG instance status"""

        status_message: typing.Text
        """IG instance status message"""

        def __init__(self,
            *,
            id: typing.Text = ...,
            status: typing.Text = ...,
            status_message: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["id",b"id","status",b"status","status_message",b"status_message"]) -> None: ...

    class Spec(google.protobuf.message.Message):
        """Node specification."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        RESOURCES_FIELD_NUMBER: builtins.int
        DISK_FIELD_NUMBER: builtins.int
        @property
        def resources(self) -> global___ResourcesSpec:
            """Node group specified resources."""
            pass
        @property
        def disk(self) -> global___DiskSpec:
            """Node group specified disk."""
            pass
        def __init__(self,
            *,
            resources: typing.Optional[global___ResourcesSpec] = ...,
            disk: typing.Optional[global___DiskSpec] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["disk",b"disk","resources",b"resources"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["disk",b"disk","resources",b"resources"]) -> None: ...

    STATUS_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    CLOUD_STATUS_FIELD_NUMBER: builtins.int
    KUBERNETES_STATUS_FIELD_NUMBER: builtins.int
    status: global___Node.Status.ValueType
    """Computed node status."""

    @property
    def spec(self) -> global___Node.Spec:
        """Node specificaion."""
        pass
    @property
    def cloud_status(self) -> global___Node.CloudStatus:
        """Cloud instance status.
        Not available in `MISSING` status.
        """
        pass
    @property
    def kubernetes_status(self) -> global___Node.KubernetesStatus:
        """Kubernetes node status.
        Not available in `PROVISIONING` and `NOT_CONNECTED` states.
        """
        pass
    def __init__(self,
        *,
        status: global___Node.Status.ValueType = ...,
        spec: typing.Optional[global___Node.Spec] = ...,
        cloud_status: typing.Optional[global___Node.CloudStatus] = ...,
        kubernetes_status: typing.Optional[global___Node.KubernetesStatus] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cloud_status",b"cloud_status","kubernetes_status",b"kubernetes_status","spec",b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_status",b"cloud_status","kubernetes_status",b"kubernetes_status","spec",b"spec","status",b"status"]) -> None: ...
global___Node = Node

class Condition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    LAST_HEARTBEAT_TIME_FIELD_NUMBER: builtins.int
    LAST_TRANSITION_TIME_FIELD_NUMBER: builtins.int
    type: typing.Text
    """Type of node condition."""

    status: typing.Text
    """Status is the status of the condition."""

    message: typing.Text
    """Human-readable message indicating details about last transition."""

    @property
    def last_heartbeat_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Last time we got an update on a given condition."""
        pass
    @property
    def last_transition_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Last time the condition transit from one status to another."""
        pass
    def __init__(self,
        *,
        type: typing.Text = ...,
        status: typing.Text = ...,
        message: typing.Text = ...,
        last_heartbeat_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_transition_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["last_heartbeat_time",b"last_heartbeat_time","last_transition_time",b"last_transition_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["last_heartbeat_time",b"last_heartbeat_time","last_transition_time",b"last_transition_time","message",b"message","status",b"status","type",b"type"]) -> None: ...
global___Condition = Condition

class Taint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Effect:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _EffectEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Taint._Effect.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        EFFECT_UNSPECIFIED: Taint._Effect.ValueType  # 0
        NO_SCHEDULE: Taint._Effect.ValueType  # 1
        """Do not allow new pods to schedule onto the node unless they tolerate the taint,
        but allow all pods submitted to Kubelet without going through the scheduler
        to start, and allow all already-running pods to continue running.
        """

        PREFER_NO_SCHEDULE: Taint._Effect.ValueType  # 2
        """Like NO_SCHEDULE, but the scheduler tries not to schedule
        new pods onto the node, rather than prohibiting new pods from scheduling
        onto the node entirely. Enforced by the scheduler.
        """

        NO_EXECUTE: Taint._Effect.ValueType  # 3
        """Evict any already-running pods that do not tolerate the taint."""

    class Effect(_Effect, metaclass=_EffectEnumTypeWrapper):
        pass

    EFFECT_UNSPECIFIED: Taint.Effect.ValueType  # 0
    NO_SCHEDULE: Taint.Effect.ValueType  # 1
    """Do not allow new pods to schedule onto the node unless they tolerate the taint,
    but allow all pods submitted to Kubelet without going through the scheduler
    to start, and allow all already-running pods to continue running.
    """

    PREFER_NO_SCHEDULE: Taint.Effect.ValueType  # 2
    """Like NO_SCHEDULE, but the scheduler tries not to schedule
    new pods onto the node, rather than prohibiting new pods from scheduling
    onto the node entirely. Enforced by the scheduler.
    """

    NO_EXECUTE: Taint.Effect.ValueType  # 3
    """Evict any already-running pods that do not tolerate the taint."""


    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    EFFECT_FIELD_NUMBER: builtins.int
    key: typing.Text
    """The taint key to be applied to a node."""

    value: typing.Text
    """The taint value corresponding to the taint key."""

    effect: global___Taint.Effect.ValueType
    """The effect of the taint on pods that do not tolerate the taint."""

    def __init__(self,
        *,
        key: typing.Text = ...,
        value: typing.Text = ...,
        effect: global___Taint.Effect.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["effect",b"effect","key",b"key","value",b"value"]) -> None: ...
global___Taint = Taint

class AttachedVolume(google.protobuf.message.Message):
    """AttachedVolume describes a volume attached to a node"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DRIVER_NAME_FIELD_NUMBER: builtins.int
    VOLUME_HANDLE_FIELD_NUMBER: builtins.int
    driver_name: typing.Text
    """Name of the driver which has attached the volume"""

    volume_handle: typing.Text
    """Volume handle (cloud disk id)"""

    def __init__(self,
        *,
        driver_name: typing.Text = ...,
        volume_handle: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["driver_name",b"driver_name","volume_handle",b"volume_handle"]) -> None: ...
global___AttachedVolume = AttachedVolume

class NodeTemplate(google.protobuf.message.Message):
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

    class NetworkSettings(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _Type:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NodeTemplate.NetworkSettings._Type.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            TYPE_UNSPECIFIED: NodeTemplate.NetworkSettings._Type.ValueType  # 0
            STANDARD: NodeTemplate.NetworkSettings._Type.ValueType  # 1
            SOFTWARE_ACCELERATED: NodeTemplate.NetworkSettings._Type.ValueType  # 2
            """unsupported yet, commented for possible future utilization.
            HARDWARE_ACCELERATED = 3;
            """

        class Type(_Type, metaclass=_TypeEnumTypeWrapper):
            pass

        TYPE_UNSPECIFIED: NodeTemplate.NetworkSettings.Type.ValueType  # 0
        STANDARD: NodeTemplate.NetworkSettings.Type.ValueType  # 1
        SOFTWARE_ACCELERATED: NodeTemplate.NetworkSettings.Type.ValueType  # 2
        """unsupported yet, commented for possible future utilization.
        HARDWARE_ACCELERATED = 3;
        """


        TYPE_FIELD_NUMBER: builtins.int
        type: global___NodeTemplate.NetworkSettings.Type.ValueType
        def __init__(self,
            *,
            type: global___NodeTemplate.NetworkSettings.Type.ValueType = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["type",b"type"]) -> None: ...

    class ContainerRuntimeSettings(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _Type:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NodeTemplate.ContainerRuntimeSettings._Type.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            TYPE_UNSPECIFIED: NodeTemplate.ContainerRuntimeSettings._Type.ValueType  # 0
            DOCKER: NodeTemplate.ContainerRuntimeSettings._Type.ValueType  # 1
            CONTAINERD: NodeTemplate.ContainerRuntimeSettings._Type.ValueType  # 2
        class Type(_Type, metaclass=_TypeEnumTypeWrapper):
            pass

        TYPE_UNSPECIFIED: NodeTemplate.ContainerRuntimeSettings.Type.ValueType  # 0
        DOCKER: NodeTemplate.ContainerRuntimeSettings.Type.ValueType  # 1
        CONTAINERD: NodeTemplate.ContainerRuntimeSettings.Type.ValueType  # 2

        TYPE_FIELD_NUMBER: builtins.int
        type: global___NodeTemplate.ContainerRuntimeSettings.Type.ValueType
        def __init__(self,
            *,
            type: global___NodeTemplate.ContainerRuntimeSettings.Type.ValueType = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["type",b"type"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    PLATFORM_ID_FIELD_NUMBER: builtins.int
    RESOURCES_SPEC_FIELD_NUMBER: builtins.int
    BOOT_DISK_SPEC_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    V4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    SCHEDULING_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_INTERFACE_SPECS_FIELD_NUMBER: builtins.int
    PLACEMENT_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_SETTINGS_FIELD_NUMBER: builtins.int
    CONTAINER_RUNTIME_SETTINGS_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the instance.
    In order to be unique it must contain at least on of instance unique placeholders:
      {instance.short_id}
      {instance.index}
      combination of {instance.zone_id} and {instance.index_in_zone}
    Example: my-instance-{instance.index}
    If not set, default is used: {instance_group.id}-{instance.short_id}
    It may also contain another placeholders, see metadata doc for full list.
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """these labels will be assigned to compute nodes (instances), created by the nodegroup"""
        pass
    platform_id: typing.Text
    """ID of the hardware platform configuration for the node."""

    @property
    def resources_spec(self) -> global___ResourcesSpec:
        """Computing resources of the node such as the amount of memory and number of cores."""
        pass
    @property
    def boot_disk_spec(self) -> global___DiskSpec:
        """Specification for the boot disk that will be attached to the node."""
        pass
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """The metadata as `key:value` pairs assigned to this instance template. This includes custom metadata and predefined keys.

        For example, you may use the metadata in order to provide your public SSH key to the node.
        For more information, see [Metadata](/docs/compute/concepts/vm-metadata).
        """
        pass
    @property
    def v4_address_spec(self) -> global___NodeAddressSpec:
        """Specification for the create network interfaces for the node group compute instances.
        Deprecated, please use network_interface_specs.
        """
        pass
    @property
    def scheduling_policy(self) -> global___SchedulingPolicy:
        """Scheduling policy configuration."""
        pass
    @property
    def network_interface_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetworkInterfaceSpec]:
        """New api, to specify network interfaces for the node group compute instances.
        Can not be used together with 'v4_address_spec'
        """
        pass
    @property
    def placement_policy(self) -> global___PlacementPolicy: ...
    @property
    def network_settings(self) -> global___NodeTemplate.NetworkSettings:
        """this parameter allows to specify type of network acceleration used on nodes (instances)"""
        pass
    @property
    def container_runtime_settings(self) -> global___NodeTemplate.ContainerRuntimeSettings: ...
    def __init__(self,
        *,
        name: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        platform_id: typing.Text = ...,
        resources_spec: typing.Optional[global___ResourcesSpec] = ...,
        boot_disk_spec: typing.Optional[global___DiskSpec] = ...,
        metadata: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        v4_address_spec: typing.Optional[global___NodeAddressSpec] = ...,
        scheduling_policy: typing.Optional[global___SchedulingPolicy] = ...,
        network_interface_specs: typing.Optional[typing.Iterable[global___NetworkInterfaceSpec]] = ...,
        placement_policy: typing.Optional[global___PlacementPolicy] = ...,
        network_settings: typing.Optional[global___NodeTemplate.NetworkSettings] = ...,
        container_runtime_settings: typing.Optional[global___NodeTemplate.ContainerRuntimeSettings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["boot_disk_spec",b"boot_disk_spec","container_runtime_settings",b"container_runtime_settings","network_settings",b"network_settings","placement_policy",b"placement_policy","resources_spec",b"resources_spec","scheduling_policy",b"scheduling_policy","v4_address_spec",b"v4_address_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["boot_disk_spec",b"boot_disk_spec","container_runtime_settings",b"container_runtime_settings","labels",b"labels","metadata",b"metadata","name",b"name","network_interface_specs",b"network_interface_specs","network_settings",b"network_settings","placement_policy",b"placement_policy","platform_id",b"platform_id","resources_spec",b"resources_spec","scheduling_policy",b"scheduling_policy","v4_address_spec",b"v4_address_spec"]) -> None: ...
global___NodeTemplate = NodeTemplate

class NetworkInterfaceSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    PRIMARY_V4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    PRIMARY_V6_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of the subnets."""
        pass
    @property
    def primary_v4_address_spec(self) -> global___NodeAddressSpec:
        """Primary IPv4 address that is assigned to the instance for this network interface."""
        pass
    @property
    def primary_v6_address_spec(self) -> global___NodeAddressSpec:
        """Primary IPv6 address that is assigned to the instance for this network interface."""
        pass
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of security groups."""
        pass
    def __init__(self,
        *,
        subnet_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        primary_v4_address_spec: typing.Optional[global___NodeAddressSpec] = ...,
        primary_v6_address_spec: typing.Optional[global___NodeAddressSpec] = ...,
        security_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["primary_v4_address_spec",b"primary_v4_address_spec","primary_v6_address_spec",b"primary_v6_address_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["primary_v4_address_spec",b"primary_v4_address_spec","primary_v6_address_spec",b"primary_v6_address_spec","security_group_ids",b"security_group_ids","subnet_ids",b"subnet_ids"]) -> None: ...
global___NetworkInterfaceSpec = NetworkInterfaceSpec

class NodeAddressSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ONE_TO_ONE_NAT_SPEC_FIELD_NUMBER: builtins.int
    DNS_RECORD_SPECS_FIELD_NUMBER: builtins.int
    @property
    def one_to_one_nat_spec(self) -> global___OneToOneNatSpec:
        """One-to-one NAT configuration. Setting up one-to-one NAT ensures that public IP addresses are assigned to nodes, and therefore internet is accessible for all nodes of the node group. If the field is not set, NAT will not be set up."""
        pass
    @property
    def dns_record_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DnsRecordSpec]:
        """Internal DNS configuration."""
        pass
    def __init__(self,
        *,
        one_to_one_nat_spec: typing.Optional[global___OneToOneNatSpec] = ...,
        dns_record_specs: typing.Optional[typing.Iterable[global___DnsRecordSpec]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["one_to_one_nat_spec",b"one_to_one_nat_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dns_record_specs",b"dns_record_specs","one_to_one_nat_spec",b"one_to_one_nat_spec"]) -> None: ...
global___NodeAddressSpec = NodeAddressSpec

class DnsRecordSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FQDN_FIELD_NUMBER: builtins.int
    DNS_ZONE_ID_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    PTR_FIELD_NUMBER: builtins.int
    fqdn: typing.Text
    """FQDN (required)."""

    dns_zone_id: typing.Text
    """DNS zone id (optional, if not set, private zone is used)."""

    ttl: builtins.int
    """DNS record ttl, values in 0-86400 (optional)."""

    ptr: builtins.bool
    """When set to true, also create PTR DNS record (optional)."""

    def __init__(self,
        *,
        fqdn: typing.Text = ...,
        dns_zone_id: typing.Text = ...,
        ttl: builtins.int = ...,
        ptr: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dns_zone_id",b"dns_zone_id","fqdn",b"fqdn","ptr",b"ptr","ttl",b"ttl"]) -> None: ...
global___DnsRecordSpec = DnsRecordSpec

class OneToOneNatSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IP_VERSION_FIELD_NUMBER: builtins.int
    ip_version: global___IpVersion.ValueType
    """IP version for the public IP address."""

    def __init__(self,
        *,
        ip_version: global___IpVersion.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ip_version",b"ip_version"]) -> None: ...
global___OneToOneNatSpec = OneToOneNatSpec

class ResourcesSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MEMORY_FIELD_NUMBER: builtins.int
    CORES_FIELD_NUMBER: builtins.int
    CORE_FRACTION_FIELD_NUMBER: builtins.int
    GPUS_FIELD_NUMBER: builtins.int
    memory: builtins.int
    """Amount of memory available to the node, specified in bytes."""

    cores: builtins.int
    """Number of cores available to the node."""

    core_fraction: builtins.int
    """Baseline level of CPU performance with the possibility to burst performance above that baseline level.
    This field sets baseline performance for each core.
    """

    gpus: builtins.int
    """Number of GPUs available to the node."""

    def __init__(self,
        *,
        memory: builtins.int = ...,
        cores: builtins.int = ...,
        core_fraction: builtins.int = ...,
        gpus: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["core_fraction",b"core_fraction","cores",b"cores","gpus",b"gpus","memory",b"memory"]) -> None: ...
global___ResourcesSpec = ResourcesSpec

class DiskSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_TYPE_ID_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    disk_type_id: typing.Text
    """ID of the disk type."""

    disk_size: builtins.int
    """Size of the disk, specified in bytes."""

    def __init__(self,
        *,
        disk_type_id: typing.Text = ...,
        disk_size: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_size",b"disk_size","disk_type_id",b"disk_type_id"]) -> None: ...
global___DiskSpec = DiskSpec

class SchedulingPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PREEMPTIBLE_FIELD_NUMBER: builtins.int
    preemptible: builtins.bool
    """True for preemptible compute instances. Default value is false. Preemptible compute instances are stopped at least once every 24 hours, and can be stopped at any time
    if their resources are needed by Compute.
    For more information, see [Preemptible Virtual Machines](/docs/compute/concepts/preemptible-vm).
    """

    def __init__(self,
        *,
        preemptible: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["preemptible",b"preemptible"]) -> None: ...
global___SchedulingPolicy = SchedulingPolicy

class PlacementPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    placement_group_id: typing.Text
    """Identifier of placement group"""

    def __init__(self,
        *,
        placement_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["placement_group_id",b"placement_group_id"]) -> None: ...
global___PlacementPolicy = PlacementPolicy
