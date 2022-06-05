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

class _MaintenancePolicy:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _MaintenancePolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MaintenancePolicy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MAINTENANCE_POLICY_UNSPECIFIED: _MaintenancePolicy.ValueType  # 0
    RESTART: _MaintenancePolicy.ValueType  # 1
    """Restart instances on the same host after maintenance event."""

    MIGRATE: _MaintenancePolicy.ValueType  # 2
    """Migrate instances to another host before maintenance event."""

class MaintenancePolicy(_MaintenancePolicy, metaclass=_MaintenancePolicyEnumTypeWrapper):
    pass

MAINTENANCE_POLICY_UNSPECIFIED: MaintenancePolicy.ValueType  # 0
RESTART: MaintenancePolicy.ValueType  # 1
"""Restart instances on the same host after maintenance event."""

MIGRATE: MaintenancePolicy.ValueType  # 2
"""Migrate instances to another host before maintenance event."""

global___MaintenancePolicy = MaintenancePolicy


class HostGroup(google.protobuf.message.Message):
    """Represents group of dedicated hosts"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[HostGroup._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: HostGroup._Status.ValueType  # 0
        CREATING: HostGroup._Status.ValueType  # 1
        READY: HostGroup._Status.ValueType  # 2
        UPDATING: HostGroup._Status.ValueType  # 3
        DELETING: HostGroup._Status.ValueType  # 4
    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNSPECIFIED: HostGroup.Status.ValueType  # 0
    CREATING: HostGroup.Status.ValueType  # 1
    READY: HostGroup.Status.ValueType  # 2
    UPDATING: HostGroup.Status.ValueType  # 3
    DELETING: HostGroup.Status.ValueType  # 4

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
    ZONE_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TYPE_ID_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the group."""

    folder_id: typing.Text
    """ID of the folder that the group belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""
        pass
    name: typing.Text
    """Name of the group. The name is unique within the folder."""

    description: typing.Text
    """Description of the group."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs."""
        pass
    zone_id: typing.Text
    """Availability zone where all dedicated hosts are allocated."""

    status: global___HostGroup.Status.ValueType
    """Status of the group."""

    type_id: typing.Text
    """ID of host type. Resources provided by each host of the group."""

    maintenance_policy: global___MaintenancePolicy.ValueType
    """Behaviour on maintenance events."""

    @property
    def scale_policy(self) -> global___ScalePolicy:
        """Scale policy. Only fixed number of hosts are supported at this moment."""
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
        status: global___HostGroup.Status.ValueType = ...,
        type_id: typing.Text = ...,
        maintenance_policy: global___MaintenancePolicy.ValueType = ...,
        scale_policy: typing.Optional[global___ScalePolicy] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","scale_policy",b"scale_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","description",b"description","folder_id",b"folder_id","id",b"id","labels",b"labels","maintenance_policy",b"maintenance_policy","name",b"name","scale_policy",b"scale_policy","status",b"status","type_id",b"type_id","zone_id",b"zone_id"]) -> None: ...
global___HostGroup = HostGroup

class Host(google.protobuf.message.Message):
    """Represents a dedicated host"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Host._Status.ValueType  # 0
        UP: Host._Status.ValueType  # 1
        DOWN: Host._Status.ValueType  # 2
    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNSPECIFIED: Host.Status.ValueType  # 0
    UP: Host.Status.ValueType  # 1
    DOWN: Host.Status.ValueType  # 2

    ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    SERVER_ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the host."""

    status: global___Host.Status.ValueType
    """Current status of the host. New instances are unable to start on host in DOWN status."""

    server_id: typing.Text
    """ID of the physical server that the host belongs to."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        status: global___Host.Status.ValueType = ...,
        server_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","server_id",b"server_id","status",b"status"]) -> None: ...
global___Host = Host

class ScalePolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class FixedScale(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        SIZE_FIELD_NUMBER: builtins.int
        size: builtins.int
        def __init__(self,
            *,
            size: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["size",b"size"]) -> None: ...

    FIXED_SCALE_FIELD_NUMBER: builtins.int
    @property
    def fixed_scale(self) -> global___ScalePolicy.FixedScale: ...
    def __init__(self,
        *,
        fixed_scale: typing.Optional[global___ScalePolicy.FixedScale] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fixed_scale",b"fixed_scale","scale_type",b"scale_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fixed_scale",b"fixed_scale","scale_type",b"scale_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["scale_type",b"scale_type"]) -> typing.Optional[typing_extensions.Literal["fixed_scale"]]: ...
global___ScalePolicy = ScalePolicy
