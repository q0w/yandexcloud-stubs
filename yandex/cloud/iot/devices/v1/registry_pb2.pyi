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

class Registry(google.protobuf.message.Message):
    """A registry. For more information, see [Registry](/docs/iot-core/concepts/index#registry)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Registry._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Registry._Status.ValueType  # 0
        CREATING: Registry._Status.ValueType  # 1
        """Registry is being created."""

        ACTIVE: Registry._Status.ValueType  # 2
        """Registry is ready to use."""

        DELETING: Registry._Status.ValueType  # 3
        """Registry is being deleted."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNSPECIFIED: Registry.Status.ValueType  # 0
    CREATING: Registry.Status.ValueType  # 1
    """Registry is being created."""

    ACTIVE: Registry.Status.ValueType  # 2
    """Registry is ready to use."""

    DELETING: Registry.Status.ValueType  # 3
    """Registry is being deleted."""


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
    STATUS_FIELD_NUMBER: builtins.int
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the registry."""

    folder_id: typing.Text
    """ID of the folder that the registry belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    name: typing.Text
    """Name of the registry. The name is unique within the folder."""

    description: typing.Text
    """Description of the registry. 0-256 characters long."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs. Maximum of 64 per resource."""
        pass
    status: global___Registry.Status.ValueType
    """Status of the registry."""

    log_group_id: typing.Text
    """ID of the logs group for the specified registry."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        status: global___Registry.Status.ValueType = ...,
        log_group_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","description",b"description","folder_id",b"folder_id","id",b"id","labels",b"labels","log_group_id",b"log_group_id","name",b"name","status",b"status"]) -> None: ...
global___Registry = Registry

class RegistryCertificate(google.protobuf.message.Message):
    """A registry certificate. For more information, see [Managing registry certificates](/docs/iot-core/operations/certificates/registry-certificates)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry that the certificate belongs to."""

    fingerprint: typing.Text
    """SHA256 hash of the certificates."""

    certificate_data: typing.Text
    """Public part of the certificate."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        fingerprint: typing.Text = ...,
        certificate_data: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_data",b"certificate_data","created_at",b"created_at","fingerprint",b"fingerprint","registry_id",b"registry_id"]) -> None: ...
global___RegistryCertificate = RegistryCertificate

class DeviceAlias(google.protobuf.message.Message):
    """A device topic alias.

    Alias is an alternate name of a device topic assigned by the user. Map alias to canonical topic name prefix, e.g. `my/custom/alias` match to `$device/abcdef/events`. For more information, see [Using topic aliases](/docs/iot-core/concepts/topic#aliases).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEVICE_ID_FIELD_NUMBER: builtins.int
    TOPIC_PREFIX_FIELD_NUMBER: builtins.int
    ALIAS_FIELD_NUMBER: builtins.int
    device_id: typing.Text
    """ID of the device that the alias belongs to."""

    topic_prefix: typing.Text
    """Prefix of a canonical topic name to be aliased, e.g. `$devices/abcdef`."""

    alias: typing.Text
    """Alias of a device topic."""

    def __init__(self,
        *,
        device_id: typing.Text = ...,
        topic_prefix: typing.Text = ...,
        alias: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alias",b"alias","device_id",b"device_id","topic_prefix",b"topic_prefix"]) -> None: ...
global___DeviceAlias = DeviceAlias

class RegistryPassword(google.protobuf.message.Message):
    """A registry password."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    registry_id: typing.Text
    """ID of the registry that the password belongs to."""

    id: typing.Text
    """ID of the password."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    def __init__(self,
        *,
        registry_id: typing.Text = ...,
        id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","id",b"id","registry_id",b"registry_id"]) -> None: ...
global___RegistryPassword = RegistryPassword
