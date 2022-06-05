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

class _DeviceView:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _DeviceViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DeviceView.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    BASIC: _DeviceView.ValueType  # 0
    """Server responses without monitoring data.
    The default value.
    """

    FULL: _DeviceView.ValueType  # 1
    """Server responses with monitoring data."""

class DeviceView(_DeviceView, metaclass=_DeviceViewEnumTypeWrapper):
    pass

BASIC: DeviceView.ValueType  # 0
"""Server responses without monitoring data.
The default value.
"""

FULL: DeviceView.ValueType  # 1
"""Server responses with monitoring data."""

global___DeviceView = DeviceView


class Device(google.protobuf.message.Message):
    """A device. For more information, see [Device](/docs/iot-core/concepts/index#device)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Device._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Device._Status.ValueType  # 0
        CREATING: Device._Status.ValueType  # 1
        """Device is being created."""

        ACTIVE: Device._Status.ValueType  # 2
        """Device is ready to use."""

        DELETING: Device._Status.ValueType  # 3
        """Device is being deleted."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNSPECIFIED: Device.Status.ValueType  # 0
    CREATING: Device.Status.ValueType  # 1
    """Device is being created."""

    ACTIVE: Device.Status.ValueType  # 2
    """Device is ready to use."""

    DELETING: Device.Status.ValueType  # 3
    """Device is being deleted."""


    class TopicAliasesEntry(google.protobuf.message.Message):
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
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TOPIC_ALIASES_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MONITORING_DATA_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the device."""

    registry_id: typing.Text
    """ID of the registry that the device belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    name: typing.Text
    """Name of the device. The name is unique within the registry."""

    description: typing.Text
    """Description of the device. 0-256 characters long."""

    @property
    def topic_aliases(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Alias of a device topic.

        Alias is an alternate name of a device topic assigned by the user. Map alias to canonical topic name prefix, e.g. `my/custom/alias` match to `$device/abcdef/events`.
        """
        pass
    status: global___Device.Status.ValueType
    """Status of the device."""

    @property
    def monitoring_data(self) -> global___DeviceMonitoringData:
        """Device monitoring data, returns if FULL view specified."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        registry_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        topic_aliases: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        status: global___Device.Status.ValueType = ...,
        monitoring_data: typing.Optional[global___DeviceMonitoringData] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","monitoring_data",b"monitoring_data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","description",b"description","id",b"id","monitoring_data",b"monitoring_data","name",b"name","registry_id",b"registry_id","status",b"status","topic_aliases",b"topic_aliases"]) -> None: ...
global___Device = Device

class DeviceCertificate(google.protobuf.message.Message):
    """A device certificate. For more information, see [Managing device certificates](/docs/iot-core/operations/certificates/device-certificates)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEVICE_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    device_id: typing.Text
    """ID of the device that the certificate belongs to."""

    fingerprint: typing.Text
    """SHA256 hash of the certificate."""

    certificate_data: typing.Text
    """Public part of the certificate."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    def __init__(self,
        *,
        device_id: typing.Text = ...,
        fingerprint: typing.Text = ...,
        certificate_data: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_data",b"certificate_data","created_at",b"created_at","device_id",b"device_id","fingerprint",b"fingerprint"]) -> None: ...
global___DeviceCertificate = DeviceCertificate

class DevicePassword(google.protobuf.message.Message):
    """A device password."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEVICE_ID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    device_id: typing.Text
    """ID of the device that the password belongs to."""

    id: typing.Text
    """ID of the password."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    def __init__(self,
        *,
        device_id: typing.Text = ...,
        id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","device_id",b"device_id","id",b"id"]) -> None: ...
global___DevicePassword = DevicePassword

class DeviceMonitoringData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LAST_AUTH_IP_FIELD_NUMBER: builtins.int
    LAST_AUTH_TIME_FIELD_NUMBER: builtins.int
    LAST_PUB_ACTIVITY_TIME_FIELD_NUMBER: builtins.int
    LAST_SUB_ACTIVITY_TIME_FIELD_NUMBER: builtins.int
    LAST_ONLINE_TIME_FIELD_NUMBER: builtins.int
    last_auth_ip: typing.Text
    @property
    def last_auth_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def last_pub_activity_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def last_sub_activity_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def last_online_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        last_auth_ip: typing.Text = ...,
        last_auth_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_pub_activity_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_sub_activity_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_online_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["last_auth_time",b"last_auth_time","last_online_time",b"last_online_time","last_pub_activity_time",b"last_pub_activity_time","last_sub_activity_time",b"last_sub_activity_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["last_auth_ip",b"last_auth_ip","last_auth_time",b"last_auth_time","last_online_time",b"last_online_time","last_pub_activity_time",b"last_pub_activity_time","last_sub_activity_time",b"last_sub_activity_time"]) -> None: ...
global___DeviceMonitoringData = DeviceMonitoringData
