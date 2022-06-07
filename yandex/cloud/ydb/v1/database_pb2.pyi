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
import yandex.cloud.ydb.v1.backup_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AlertEvaluationStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _AlertEvaluationStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AlertEvaluationStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ALERT_EVALUATION_STATUS_UNSPECIFIED: _AlertEvaluationStatus.ValueType  # 0
    ALERT_EVALUATION_STATUS_OK: _AlertEvaluationStatus.ValueType  # 1
    ALERT_EVALUATION_STATUS_NO_DATA: _AlertEvaluationStatus.ValueType  # 2
    ALERT_EVALUATION_STATUS_ERROR: _AlertEvaluationStatus.ValueType  # 3
    ALERT_EVALUATION_STATUS_ALARM: _AlertEvaluationStatus.ValueType  # 4
    ALERT_EVALUATION_STATUS_WARN: _AlertEvaluationStatus.ValueType  # 5
class AlertEvaluationStatus(_AlertEvaluationStatus, metaclass=_AlertEvaluationStatusEnumTypeWrapper):
    pass

ALERT_EVALUATION_STATUS_UNSPECIFIED: AlertEvaluationStatus.ValueType  # 0
ALERT_EVALUATION_STATUS_OK: AlertEvaluationStatus.ValueType  # 1
ALERT_EVALUATION_STATUS_NO_DATA: AlertEvaluationStatus.ValueType  # 2
ALERT_EVALUATION_STATUS_ERROR: AlertEvaluationStatus.ValueType  # 3
ALERT_EVALUATION_STATUS_ALARM: AlertEvaluationStatus.ValueType  # 4
ALERT_EVALUATION_STATUS_WARN: AlertEvaluationStatus.ValueType  # 5
global___AlertEvaluationStatus = AlertEvaluationStatus


class Database(google.protobuf.message.Message):
    """YDB database."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Database._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Database._Status.ValueType  # 0
        PROVISIONING: Database._Status.ValueType  # 1
        RUNNING: Database._Status.ValueType  # 2
        UPDATING: Database._Status.ValueType  # 4
        ERROR: Database._Status.ValueType  # 5
        DELETING: Database._Status.ValueType  # 6
        STARTING: Database._Status.ValueType  # 7
        STOPPED: Database._Status.ValueType  # 8
    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNSPECIFIED: Database.Status.ValueType  # 0
    PROVISIONING: Database.Status.ValueType  # 1
    RUNNING: Database.Status.ValueType  # 2
    UPDATING: Database.Status.ValueType  # 4
    ERROR: Database.Status.ValueType  # 5
    DELETING: Database.Status.ValueType  # 6
    STARTING: Database.Status.ValueType  # 7
    STOPPED: Database.Status.ValueType  # 8

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
    STATUS_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    STORAGE_CONFIG_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    ZONAL_DATABASE_FIELD_NUMBER: builtins.int
    REGIONAL_DATABASE_FIELD_NUMBER: builtins.int
    DEDICATED_DATABASE_FIELD_NUMBER: builtins.int
    SERVERLESS_DATABASE_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BACKUP_CONFIG_FIELD_NUMBER: builtins.int
    DOCUMENT_API_ENDPOINT_FIELD_NUMBER: builtins.int
    KINESIS_API_ENDPOINT_FIELD_NUMBER: builtins.int
    MONITORING_CONFIG_FIELD_NUMBER: builtins.int
    id: typing.Text
    folder_id: typing.Text
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    name: typing.Text
    description: typing.Text
    status: global___Database.Status.ValueType
    endpoint: typing.Text
    resource_preset_id: typing.Text
    @property
    def storage_config(self) -> global___StorageConfig: ...
    @property
    def scale_policy(self) -> global___ScalePolicy: ...
    network_id: typing.Text
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def zonal_database(self) -> global___ZonalDatabase:
        """deprecated field"""
        pass
    @property
    def regional_database(self) -> global___RegionalDatabase:
        """deprecated field"""
        pass
    @property
    def dedicated_database(self) -> global___DedicatedDatabase: ...
    @property
    def serverless_database(self) -> global___ServerlessDatabase: ...
    assign_public_ips: builtins.bool
    location_id: typing.Text
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    @property
    def backup_config(self) -> yandex.cloud.ydb.v1.backup_pb2.BackupConfig: ...
    document_api_endpoint: typing.Text
    kinesis_api_endpoint: typing.Text
    @property
    def monitoring_config(self) -> global___MonitoringConfig: ...
    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        status: global___Database.Status.ValueType = ...,
        endpoint: typing.Text = ...,
        resource_preset_id: typing.Text = ...,
        storage_config: typing.Optional[global___StorageConfig] = ...,
        scale_policy: typing.Optional[global___ScalePolicy] = ...,
        network_id: typing.Text = ...,
        subnet_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        zonal_database: typing.Optional[global___ZonalDatabase] = ...,
        regional_database: typing.Optional[global___RegionalDatabase] = ...,
        dedicated_database: typing.Optional[global___DedicatedDatabase] = ...,
        serverless_database: typing.Optional[global___ServerlessDatabase] = ...,
        assign_public_ips: builtins.bool = ...,
        location_id: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        backup_config: typing.Optional[yandex.cloud.ydb.v1.backup_pb2.BackupConfig] = ...,
        document_api_endpoint: typing.Text = ...,
        kinesis_api_endpoint: typing.Text = ...,
        monitoring_config: typing.Optional[global___MonitoringConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["backup_config",b"backup_config","created_at",b"created_at","database_type",b"database_type","dedicated_database",b"dedicated_database","monitoring_config",b"monitoring_config","regional_database",b"regional_database","scale_policy",b"scale_policy","serverless_database",b"serverless_database","storage_config",b"storage_config","zonal_database",b"zonal_database"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_public_ips",b"assign_public_ips","backup_config",b"backup_config","created_at",b"created_at","database_type",b"database_type","dedicated_database",b"dedicated_database","description",b"description","document_api_endpoint",b"document_api_endpoint","endpoint",b"endpoint","folder_id",b"folder_id","id",b"id","kinesis_api_endpoint",b"kinesis_api_endpoint","labels",b"labels","location_id",b"location_id","monitoring_config",b"monitoring_config","name",b"name","network_id",b"network_id","regional_database",b"regional_database","resource_preset_id",b"resource_preset_id","scale_policy",b"scale_policy","serverless_database",b"serverless_database","status",b"status","storage_config",b"storage_config","subnet_ids",b"subnet_ids","zonal_database",b"zonal_database"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["database_type",b"database_type"]) -> typing.Optional[typing_extensions.Literal["zonal_database","regional_database","dedicated_database","serverless_database"]]: ...
global___Database = Database

class AlertParameter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class DoubleParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        name: typing.Text
        """Required. Parameter name"""

        value: builtins.float
        """Required. Parameter value"""

        def __init__(self,
            *,
            name: typing.Text = ...,
            value: builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["name",b"name","value",b"value"]) -> None: ...

    class IntegerParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        name: typing.Text
        """Required. Parameter name"""

        value: builtins.int
        """Required. Parameter value"""

        def __init__(self,
            *,
            name: typing.Text = ...,
            value: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["name",b"name","value",b"value"]) -> None: ...

    class TextParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        name: typing.Text
        """Required. Parameter name"""

        value: typing.Text
        """Required. Parameter value"""

        def __init__(self,
            *,
            name: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["name",b"name","value",b"value"]) -> None: ...

    class TextListParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        VALUES_FIELD_NUMBER: builtins.int
        name: typing.Text
        """Required. Parameter name"""

        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """Required. Parameter value"""
            pass
        def __init__(self,
            *,
            name: typing.Text = ...,
            values: typing.Optional[typing.Iterable[typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["name",b"name","values",b"values"]) -> None: ...

    class LabelListParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        VALUES_FIELD_NUMBER: builtins.int
        name: typing.Text
        """Required. Parameter name"""

        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """Required. Parameter value"""
            pass
        def __init__(self,
            *,
            name: typing.Text = ...,
            values: typing.Optional[typing.Iterable[typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["name",b"name","values",b"values"]) -> None: ...

    DOUBLE_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    INTEGER_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    TEXT_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    TEXT_LIST_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    LABEL_LIST_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    @property
    def double_parameter_value(self) -> global___AlertParameter.DoubleParameterValue: ...
    @property
    def integer_parameter_value(self) -> global___AlertParameter.IntegerParameterValue: ...
    @property
    def text_parameter_value(self) -> global___AlertParameter.TextParameterValue: ...
    @property
    def text_list_parameter_value(self) -> global___AlertParameter.TextListParameterValue: ...
    @property
    def label_list_parameter_value(self) -> global___AlertParameter.LabelListParameterValue: ...
    def __init__(self,
        *,
        double_parameter_value: typing.Optional[global___AlertParameter.DoubleParameterValue] = ...,
        integer_parameter_value: typing.Optional[global___AlertParameter.IntegerParameterValue] = ...,
        text_parameter_value: typing.Optional[global___AlertParameter.TextParameterValue] = ...,
        text_list_parameter_value: typing.Optional[global___AlertParameter.TextListParameterValue] = ...,
        label_list_parameter_value: typing.Optional[global___AlertParameter.LabelListParameterValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["double_parameter_value",b"double_parameter_value","integer_parameter_value",b"integer_parameter_value","label_list_parameter_value",b"label_list_parameter_value","parameter",b"parameter","text_list_parameter_value",b"text_list_parameter_value","text_parameter_value",b"text_parameter_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["double_parameter_value",b"double_parameter_value","integer_parameter_value",b"integer_parameter_value","label_list_parameter_value",b"label_list_parameter_value","parameter",b"parameter","text_list_parameter_value",b"text_list_parameter_value","text_parameter_value",b"text_parameter_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["parameter",b"parameter"]) -> typing.Optional[typing_extensions.Literal["double_parameter_value","integer_parameter_value","text_parameter_value","text_list_parameter_value","label_list_parameter_value"]]: ...
global___AlertParameter = AlertParameter

class NotificationChannel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NOTIFICATION_CHANNEL_ID_FIELD_NUMBER: builtins.int
    NOTIFY_ABOUT_STATUSES_FIELD_NUMBER: builtins.int
    REPEATE_NOTIFY_DELAY_MS_FIELD_NUMBER: builtins.int
    notification_channel_id: typing.Text
    @property
    def notify_about_statuses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___AlertEvaluationStatus.ValueType]: ...
    repeate_notify_delay_ms: builtins.int
    def __init__(self,
        *,
        notification_channel_id: typing.Text = ...,
        notify_about_statuses: typing.Optional[typing.Iterable[global___AlertEvaluationStatus.ValueType]] = ...,
        repeate_notify_delay_ms: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["notification_channel_id",b"notification_channel_id","notify_about_statuses",b"notify_about_statuses","repeate_notify_delay_ms",b"repeate_notify_delay_ms"]) -> None: ...
global___NotificationChannel = NotificationChannel

class Alert(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ALERT_ID_FIELD_NUMBER: builtins.int
    ALERT_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    NOTIFICATION_CHANNELS_FIELD_NUMBER: builtins.int
    ALERT_PARAMETERS_FIELD_NUMBER: builtins.int
    ALERT_THRESHOLDS_FIELD_NUMBER: builtins.int
    alert_id: typing.Text
    """output only field."""

    alert_template_id: typing.Text
    """template of the alert."""

    name: typing.Text
    """name of the alert."""

    description: typing.Text
    """human readable description of the alert."""

    @property
    def notification_channels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NotificationChannel]:
        """the notification channels of the alert."""
        pass
    @property
    def alert_parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AlertParameter]:
        """alert parameters to override."""
        pass
    @property
    def alert_thresholds(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AlertParameter]:
        """alert paratemers to override."""
        pass
    def __init__(self,
        *,
        alert_id: typing.Text = ...,
        alert_template_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        notification_channels: typing.Optional[typing.Iterable[global___NotificationChannel]] = ...,
        alert_parameters: typing.Optional[typing.Iterable[global___AlertParameter]] = ...,
        alert_thresholds: typing.Optional[typing.Iterable[global___AlertParameter]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","alert_parameters",b"alert_parameters","alert_template_id",b"alert_template_id","alert_thresholds",b"alert_thresholds","description",b"description","name",b"name","notification_channels",b"notification_channels"]) -> None: ...
global___Alert = Alert

class MonitoringConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ALERTS_FIELD_NUMBER: builtins.int
    @property
    def alerts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Alert]: ...
    def __init__(self,
        *,
        alerts: typing.Optional[typing.Iterable[global___Alert]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alerts",b"alerts"]) -> None: ...
global___MonitoringConfig = MonitoringConfig

class DedicatedDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    STORAGE_CONFIG_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    resource_preset_id: typing.Text
    @property
    def storage_config(self) -> global___StorageConfig: ...
    @property
    def scale_policy(self) -> global___ScalePolicy: ...
    network_id: typing.Text
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    assign_public_ips: builtins.bool
    def __init__(self,
        *,
        resource_preset_id: typing.Text = ...,
        storage_config: typing.Optional[global___StorageConfig] = ...,
        scale_policy: typing.Optional[global___ScalePolicy] = ...,
        network_id: typing.Text = ...,
        subnet_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        assign_public_ips: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["scale_policy",b"scale_policy","storage_config",b"storage_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_public_ips",b"assign_public_ips","network_id",b"network_id","resource_preset_id",b"resource_preset_id","scale_policy",b"scale_policy","storage_config",b"storage_config","subnet_ids",b"subnet_ids"]) -> None: ...
global___DedicatedDatabase = DedicatedDatabase

class ServerlessDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    THROTTLING_RCU_LIMIT_FIELD_NUMBER: builtins.int
    STORAGE_SIZE_LIMIT_FIELD_NUMBER: builtins.int
    ENABLE_THROTTLING_RCU_LIMIT_FIELD_NUMBER: builtins.int
    PROVISIONED_RCU_LIMIT_FIELD_NUMBER: builtins.int
    throttling_rcu_limit: builtins.int
    """Let's define 1 RU  - 1 request unit
    Let's define 1 RCU - 1 request capacity unit, which is 1 RU per second.
    If `enable_throttling_rcu_limit` flag is true, the database will be throttled using `throttling_rcu_limit` value.
    Otherwise, the database is throttled using the cloud quotas.
    If zero, all requests will be blocked until non zero value is set.
    """

    storage_size_limit: builtins.int
    """Specify serverless database storage size limit. If zero, default value is applied."""

    enable_throttling_rcu_limit: builtins.bool
    """If false, the database is throttled by cloud value."""

    provisioned_rcu_limit: builtins.int
    """Specify the number of provisioned RCUs to pay less if the database has predictable load.
    You will be charged for the provisioned capacity regularly even if this capacity is not fully consumed.
    You will be charged for the on-demand consumption only if provisioned capacity is consumed.
    """

    def __init__(self,
        *,
        throttling_rcu_limit: builtins.int = ...,
        storage_size_limit: builtins.int = ...,
        enable_throttling_rcu_limit: builtins.bool = ...,
        provisioned_rcu_limit: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enable_throttling_rcu_limit",b"enable_throttling_rcu_limit","provisioned_rcu_limit",b"provisioned_rcu_limit","storage_size_limit",b"storage_size_limit","throttling_rcu_limit",b"throttling_rcu_limit"]) -> None: ...
global___ServerlessDatabase = ServerlessDatabase

class ZonalDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ZONE_ID_FIELD_NUMBER: builtins.int
    zone_id: typing.Text
    def __init__(self,
        *,
        zone_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["zone_id",b"zone_id"]) -> None: ...
global___ZonalDatabase = ZonalDatabase

class RegionalDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGION_ID_FIELD_NUMBER: builtins.int
    region_id: typing.Text
    def __init__(self,
        *,
        region_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["region_id",b"region_id"]) -> None: ...
global___RegionalDatabase = RegionalDatabase

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

class StorageConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STORAGE_OPTIONS_FIELD_NUMBER: builtins.int
    STORAGE_SIZE_LIMIT_FIELD_NUMBER: builtins.int
    @property
    def storage_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StorageOption]: ...
    storage_size_limit: builtins.int
    """output only field: storage size limit of dedicated database."""

    def __init__(self,
        *,
        storage_options: typing.Optional[typing.Iterable[global___StorageOption]] = ...,
        storage_size_limit: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["storage_options",b"storage_options","storage_size_limit",b"storage_size_limit"]) -> None: ...
global___StorageConfig = StorageConfig

class StorageOption(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STORAGE_TYPE_ID_FIELD_NUMBER: builtins.int
    GROUP_COUNT_FIELD_NUMBER: builtins.int
    storage_type_id: typing.Text
    group_count: builtins.int
    def __init__(self,
        *,
        storage_type_id: typing.Text = ...,
        group_count: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["group_count",b"group_count","storage_type_id",b"storage_type_id"]) -> None: ...
global___StorageOption = StorageOption