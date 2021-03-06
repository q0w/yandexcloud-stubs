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
import google.protobuf.wrappers_pb2
import google.type.timeofday_pb2
import typing
import typing_extensions
import yandex.cloud.mdb.clickhouse.v1.config.clickhouse_pb2
import yandex.cloud.mdb.clickhouse.v1.maintenance_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Cluster(google.protobuf.message.Message):
    """A ClickHouse Cluster resource. For more information, see the
    [Cluster](/docs/managed-clickhouse/concepts) section in the Developer's Guide.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Environment:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _EnvironmentEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Environment.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ENVIRONMENT_UNSPECIFIED: Cluster._Environment.ValueType  # 0
        PRODUCTION: Cluster._Environment.ValueType  # 1
        """Stable environment with a conservative update policy:
        only hotfixes are applied during regular maintenance.
        """

        PRESTABLE: Cluster._Environment.ValueType  # 2
        """Environment with more aggressive update policy: new versions
        are rolled out irrespective of backward compatibility.
        """

    class Environment(_Environment, metaclass=_EnvironmentEnumTypeWrapper):
        pass

    ENVIRONMENT_UNSPECIFIED: Cluster.Environment.ValueType  # 0
    PRODUCTION: Cluster.Environment.ValueType  # 1
    """Stable environment with a conservative update policy:
    only hotfixes are applied during regular maintenance.
    """

    PRESTABLE: Cluster.Environment.ValueType  # 2
    """Environment with more aggressive update policy: new versions
    are rolled out irrespective of backward compatibility.
    """


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Cluster._Health.ValueType  # 0
        """State of the cluster is unknown ([Host.health] for every host in the cluster is UNKNOWN)."""

        ALIVE: Cluster._Health.ValueType  # 1
        """Cluster is alive and well ([Host.health] for every host in the cluster is ALIVE)."""

        DEAD: Cluster._Health.ValueType  # 2
        """Cluster is inoperable ([Host.health] for every host in the cluster is DEAD)."""

        DEGRADED: Cluster._Health.ValueType  # 3
        """Cluster is working below capacity ([Host.health] for at least one host in the cluster is not ALIVE)."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    HEALTH_UNKNOWN: Cluster.Health.ValueType  # 0
    """State of the cluster is unknown ([Host.health] for every host in the cluster is UNKNOWN)."""

    ALIVE: Cluster.Health.ValueType  # 1
    """Cluster is alive and well ([Host.health] for every host in the cluster is ALIVE)."""

    DEAD: Cluster.Health.ValueType  # 2
    """Cluster is inoperable ([Host.health] for every host in the cluster is DEAD)."""

    DEGRADED: Cluster.Health.ValueType  # 3
    """Cluster is working below capacity ([Host.health] for at least one host in the cluster is not ALIVE)."""


    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: Cluster._Status.ValueType  # 0
        """Cluster state is unknown."""

        CREATING: Cluster._Status.ValueType  # 1
        """Cluster is being created."""

        RUNNING: Cluster._Status.ValueType  # 2
        """Cluster is running normally."""

        ERROR: Cluster._Status.ValueType  # 3
        """Cluster encountered a problem and cannot operate."""

        UPDATING: Cluster._Status.ValueType  # 4
        """Cluster is being updated."""

        STOPPING: Cluster._Status.ValueType  # 5
        """Cluster is stopping."""

        STOPPED: Cluster._Status.ValueType  # 6
        """Cluster stopped."""

        STARTING: Cluster._Status.ValueType  # 7
        """Cluster is starting."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: Cluster.Status.ValueType  # 0
    """Cluster state is unknown."""

    CREATING: Cluster.Status.ValueType  # 1
    """Cluster is being created."""

    RUNNING: Cluster.Status.ValueType  # 2
    """Cluster is running normally."""

    ERROR: Cluster.Status.ValueType  # 3
    """Cluster encountered a problem and cannot operate."""

    UPDATING: Cluster.Status.ValueType  # 4
    """Cluster is being updated."""

    STOPPING: Cluster.Status.ValueType  # 5
    """Cluster is stopping."""

    STOPPED: Cluster.Status.ValueType  # 6
    """Cluster stopped."""

    STARTING: Cluster.Status.ValueType  # 7
    """Cluster is starting."""


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
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    MONITORING_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    PLANNED_OPERATION_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the ClickHouse cluster.
    This ID is assigned by MDB at creation time.
    """

    folder_id: typing.Text
    """ID of the folder that the ClickHouse cluster belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""
        pass
    name: typing.Text
    """Name of the ClickHouse cluster.
    The name is unique within the folder. 1-63 characters long.
    """

    description: typing.Text
    """Description of the ClickHouse cluster. 0-256 characters long."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Custom labels for the ClickHouse cluster as `key:value` pairs. Maximum 64 per resource."""
        pass
    environment: global___Cluster.Environment.ValueType
    """Deployment environment of the ClickHouse cluster."""

    @property
    def monitoring(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Monitoring]:
        """Description of monitoring systems relevant to the ClickHouse cluster."""
        pass
    @property
    def config(self) -> global___ClusterConfig:
        """Configuration of the ClickHouse cluster."""
        pass
    network_id: typing.Text
    """ID of the network that the cluster belongs to."""

    health: global___Cluster.Health.ValueType
    """Aggregated cluster health."""

    status: global___Cluster.Status.ValueType
    """Current state of the cluster."""

    service_account_id: typing.Text
    """ID of the service account used for access to Object Storage."""

    @property
    def maintenance_window(self) -> yandex.cloud.mdb.clickhouse.v1.maintenance_pb2.MaintenanceWindow:
        """Maintenance window for the cluster."""
        pass
    @property
    def planned_operation(self) -> yandex.cloud.mdb.clickhouse.v1.maintenance_pb2.MaintenanceOperation:
        """Planned maintenance operation to be started for the cluster within the nearest [maintenance_window]."""
        pass
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """User security groups"""
        pass
    deletion_protection: builtins.bool
    """Deletion Protection inhibits deletion of the cluster"""

    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        environment: global___Cluster.Environment.ValueType = ...,
        monitoring: typing.Optional[typing.Iterable[global___Monitoring]] = ...,
        config: typing.Optional[global___ClusterConfig] = ...,
        network_id: typing.Text = ...,
        health: global___Cluster.Health.ValueType = ...,
        status: global___Cluster.Status.ValueType = ...,
        service_account_id: typing.Text = ...,
        maintenance_window: typing.Optional[yandex.cloud.mdb.clickhouse.v1.maintenance_pb2.MaintenanceWindow] = ...,
        planned_operation: typing.Optional[yandex.cloud.mdb.clickhouse.v1.maintenance_pb2.MaintenanceOperation] = ...,
        security_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        deletion_protection: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config","created_at",b"created_at","maintenance_window",b"maintenance_window","planned_operation",b"planned_operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","created_at",b"created_at","deletion_protection",b"deletion_protection","description",b"description","environment",b"environment","folder_id",b"folder_id","health",b"health","id",b"id","labels",b"labels","maintenance_window",b"maintenance_window","monitoring",b"monitoring","name",b"name","network_id",b"network_id","planned_operation",b"planned_operation","security_group_ids",b"security_group_ids","service_account_id",b"service_account_id","status",b"status"]) -> None: ...
global___Cluster = Cluster

class Monitoring(google.protobuf.message.Message):
    """Monitoring system metadata."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the monitoring system."""

    description: typing.Text
    """Description of the monitoring system."""

    link: typing.Text
    """Link to the monitoring system charts for the ClickHouse cluster."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        description: typing.Text = ...,
        link: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","link",b"link","name",b"name"]) -> None: ...
global___Monitoring = Monitoring

class ClusterConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Clickhouse(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CONFIG_FIELD_NUMBER: builtins.int
        RESOURCES_FIELD_NUMBER: builtins.int
        @property
        def config(self) -> yandex.cloud.mdb.clickhouse.v1.config.clickhouse_pb2.ClickhouseConfigSet:
            """Configuration settings of a ClickHouse server."""
            pass
        @property
        def resources(self) -> global___Resources:
            """Resources allocated to ClickHouse hosts."""
            pass
        def __init__(self,
            *,
            config: typing.Optional[yandex.cloud.mdb.clickhouse.v1.config.clickhouse_pb2.ClickhouseConfigSet] = ...,
            resources: typing.Optional[global___Resources] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["config",b"config","resources",b"resources"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config","resources",b"resources"]) -> None: ...

    class Zookeeper(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        RESOURCES_FIELD_NUMBER: builtins.int
        @property
        def resources(self) -> global___Resources:
            """Resources allocated to ZooKeeper hosts."""
            pass
        def __init__(self,
            *,
            resources: typing.Optional[global___Resources] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["resources",b"resources"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["resources",b"resources"]) -> None: ...

    VERSION_FIELD_NUMBER: builtins.int
    CLICKHOUSE_FIELD_NUMBER: builtins.int
    ZOOKEEPER_FIELD_NUMBER: builtins.int
    BACKUP_WINDOW_START_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    CLOUD_STORAGE_FIELD_NUMBER: builtins.int
    SQL_DATABASE_MANAGEMENT_FIELD_NUMBER: builtins.int
    SQL_USER_MANAGEMENT_FIELD_NUMBER: builtins.int
    EMBEDDED_KEEPER_FIELD_NUMBER: builtins.int
    version: typing.Text
    """Version of the ClickHouse server software."""

    @property
    def clickhouse(self) -> global___ClusterConfig.Clickhouse:
        """Configuration and resource allocation for ClickHouse hosts."""
        pass
    @property
    def zookeeper(self) -> global___ClusterConfig.Zookeeper:
        """Configuration and resource allocation for ZooKeeper hosts."""
        pass
    @property
    def backup_window_start(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Time to start the daily backup, in the UTC timezone."""
        pass
    @property
    def access(self) -> global___Access:
        """Access policy for external services."""
        pass
    @property
    def cloud_storage(self) -> global___CloudStorage: ...
    @property
    def sql_database_management(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Whether database management through SQL commands is enabled."""
        pass
    @property
    def sql_user_management(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Whether user management through SQL commands is enabled."""
        pass
    @property
    def embedded_keeper(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Whether cluster should use embedded Keeper instead of Zookeeper."""
        pass
    def __init__(self,
        *,
        version: typing.Text = ...,
        clickhouse: typing.Optional[global___ClusterConfig.Clickhouse] = ...,
        zookeeper: typing.Optional[global___ClusterConfig.Zookeeper] = ...,
        backup_window_start: typing.Optional[google.type.timeofday_pb2.TimeOfDay] = ...,
        access: typing.Optional[global___Access] = ...,
        cloud_storage: typing.Optional[global___CloudStorage] = ...,
        sql_database_management: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        sql_user_management: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        embedded_keeper: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["access",b"access","backup_window_start",b"backup_window_start","clickhouse",b"clickhouse","cloud_storage",b"cloud_storage","embedded_keeper",b"embedded_keeper","sql_database_management",b"sql_database_management","sql_user_management",b"sql_user_management","zookeeper",b"zookeeper"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access",b"access","backup_window_start",b"backup_window_start","clickhouse",b"clickhouse","cloud_storage",b"cloud_storage","embedded_keeper",b"embedded_keeper","sql_database_management",b"sql_database_management","sql_user_management",b"sql_user_management","version",b"version","zookeeper",b"zookeeper"]) -> None: ...
global___ClusterConfig = ClusterConfig

class Shard(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the shard."""

    cluster_id: typing.Text
    """ID of the cluster that the shard belongs to."""

    @property
    def config(self) -> global___ShardConfig:
        """Configuration of the shard."""
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        cluster_id: typing.Text = ...,
        config: typing.Optional[global___ShardConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","config",b"config","name",b"name"]) -> None: ...
global___Shard = Shard

class ShardGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SHARD_NAMES_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the shard group."""

    cluster_id: typing.Text
    """ID of the ClickHouse cluster that the shard group belongs to."""

    description: typing.Text
    """Description of the shard group. 0-256 characters long."""

    @property
    def shard_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List of shard names contained in the shard group."""
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        cluster_id: typing.Text = ...,
        description: typing.Text = ...,
        shard_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","description",b"description","name",b"name","shard_names",b"shard_names"]) -> None: ...
global___ShardGroup = ShardGroup

class ShardConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Clickhouse(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CONFIG_FIELD_NUMBER: builtins.int
        RESOURCES_FIELD_NUMBER: builtins.int
        WEIGHT_FIELD_NUMBER: builtins.int
        @property
        def config(self) -> yandex.cloud.mdb.clickhouse.v1.config.clickhouse_pb2.ClickhouseConfigSet:
            """ClickHouse settings for a shard."""
            pass
        @property
        def resources(self) -> global___Resources:
            """Computational resources for a shard."""
            pass
        @property
        def weight(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """Relative weight of a shard considered when writing data to the cluster.
            For details, see [ClickHouse documentation](https://clickhouse.com/docs/en/operations/table_engines/distributed/).
            """
            pass
        def __init__(self,
            *,
            config: typing.Optional[yandex.cloud.mdb.clickhouse.v1.config.clickhouse_pb2.ClickhouseConfigSet] = ...,
            resources: typing.Optional[global___Resources] = ...,
            weight: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["config",b"config","resources",b"resources","weight",b"weight"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config","resources",b"resources","weight",b"weight"]) -> None: ...

    CLICKHOUSE_FIELD_NUMBER: builtins.int
    @property
    def clickhouse(self) -> global___ShardConfig.Clickhouse:
        """ClickHouse configuration for a shard."""
        pass
    def __init__(self,
        *,
        clickhouse: typing.Optional[global___ShardConfig.Clickhouse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["clickhouse",b"clickhouse"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["clickhouse",b"clickhouse"]) -> None: ...
global___ShardConfig = ShardConfig

class Host(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Host._Type.ValueType  # 0
        CLICKHOUSE: Host._Type.ValueType  # 1
        """ClickHouse host."""

        ZOOKEEPER: Host._Type.ValueType  # 2
        """ZooKeeper host."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    TYPE_UNSPECIFIED: Host.Type.ValueType  # 0
    CLICKHOUSE: Host.Type.ValueType  # 1
    """ClickHouse host."""

    ZOOKEEPER: Host.Type.ValueType  # 2
    """ZooKeeper host."""


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: Host._Health.ValueType  # 0
        """Health of the host is unknown."""

        ALIVE: Host._Health.ValueType  # 1
        """The host is performing all its functions normally."""

        DEAD: Host._Health.ValueType  # 2
        """The host is inoperable, and cannot perform any of its essential functions."""

        DEGRADED: Host._Health.ValueType  # 3
        """The host is degraded, and can perform only some of its essential functions."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    UNKNOWN: Host.Health.ValueType  # 0
    """Health of the host is unknown."""

    ALIVE: Host.Health.ValueType  # 1
    """The host is performing all its functions normally."""

    DEAD: Host.Health.ValueType  # 2
    """The host is inoperable, and cannot perform any of its essential functions."""

    DEGRADED: Host.Health.ValueType  # 3
    """The host is degraded, and can perform only some of its essential functions."""


    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    SHARD_NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the ClickHouse host. The host name is assigned by MDB at creation time, and cannot be changed.
    1-63 characters long.

    The name is unique across all MDB hosts that exist on the platform, as it defines the FQDN of the host.
    """

    cluster_id: typing.Text
    """ID of the ClickHouse host. The ID is assigned by MDB at creation time."""

    zone_id: typing.Text
    """ID of the availability zone where the ClickHouse host resides."""

    type: global___Host.Type.ValueType
    """Type of the host."""

    @property
    def resources(self) -> global___Resources:
        """Resources allocated to the ClickHouse host."""
        pass
    health: global___Host.Health.ValueType
    """Status code of the aggregated health of the host."""

    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Service]:
        """Services provided by the host."""
        pass
    subnet_id: typing.Text
    """ID of the subnet that the host belongs to."""

    assign_public_ip: builtins.bool
    """Flag showing public IP assignment status to this host."""

    shard_name: typing.Text
    def __init__(self,
        *,
        name: typing.Text = ...,
        cluster_id: typing.Text = ...,
        zone_id: typing.Text = ...,
        type: global___Host.Type.ValueType = ...,
        resources: typing.Optional[global___Resources] = ...,
        health: global___Host.Health.ValueType = ...,
        services: typing.Optional[typing.Iterable[global___Service]] = ...,
        subnet_id: typing.Text = ...,
        assign_public_ip: builtins.bool = ...,
        shard_name: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resources",b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_public_ip",b"assign_public_ip","cluster_id",b"cluster_id","health",b"health","name",b"name","resources",b"resources","services",b"services","shard_name",b"shard_name","subnet_id",b"subnet_id","type",b"type","zone_id",b"zone_id"]) -> None: ...
global___Host = Host

class Service(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Service._Type.ValueType  # 0
        CLICKHOUSE: Service._Type.ValueType  # 1
        """The host is a ClickHouse server."""

        ZOOKEEPER: Service._Type.ValueType  # 2
        """The host is a ZooKeeper server."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    TYPE_UNSPECIFIED: Service.Type.ValueType  # 0
    CLICKHOUSE: Service.Type.ValueType  # 1
    """The host is a ClickHouse server."""

    ZOOKEEPER: Service.Type.ValueType  # 2
    """The host is a ZooKeeper server."""


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: Service._Health.ValueType  # 0
        """Health of the server is unknown."""

        ALIVE: Service._Health.ValueType  # 1
        """The server is working normally."""

        DEAD: Service._Health.ValueType  # 2
        """The server is dead or unresponsive."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    UNKNOWN: Service.Health.ValueType  # 0
    """Health of the server is unknown."""

    ALIVE: Service.Health.ValueType  # 1
    """The server is working normally."""

    DEAD: Service.Health.ValueType  # 2
    """The server is dead or unresponsive."""


    TYPE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    type: global___Service.Type.ValueType
    """Type of the service provided by the host."""

    health: global___Service.Health.ValueType
    """Status code of server availability."""

    def __init__(self,
        *,
        type: global___Service.Type.ValueType = ...,
        health: global___Service.Health.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["health",b"health","type",b"type"]) -> None: ...
global___Service = Service

class Resources(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    DISK_TYPE_ID_FIELD_NUMBER: builtins.int
    resource_preset_id: typing.Text
    """ID of the preset for computational resources available to a host (CPU, memory etc.).
    All available presets are listed in the [documentation](/docs/managed-clickhouse/concepts/instance-types)
    """

    disk_size: builtins.int
    """Volume of the storage available to a host, in bytes."""

    disk_type_id: typing.Text
    """Type of the storage environment for the host.
    Possible values:
    * network-hdd - network HDD drive,
    * network-ssd - network SSD drive,
    * local-ssd - local SSD storage.
    """

    def __init__(self,
        *,
        resource_preset_id: typing.Text = ...,
        disk_size: builtins.int = ...,
        disk_type_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_size",b"disk_size","disk_type_id",b"disk_type_id","resource_preset_id",b"resource_preset_id"]) -> None: ...
global___Resources = Resources

class Access(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_LENS_FIELD_NUMBER: builtins.int
    WEB_SQL_FIELD_NUMBER: builtins.int
    METRIKA_FIELD_NUMBER: builtins.int
    SERVERLESS_FIELD_NUMBER: builtins.int
    DATA_TRANSFER_FIELD_NUMBER: builtins.int
    YANDEX_QUERY_FIELD_NUMBER: builtins.int
    data_lens: builtins.bool
    """Allow to export data from the cluster to DataLens."""

    web_sql: builtins.bool
    """Allow SQL queries to the cluster databases from the management console.

    See [SQL queries in the management console](/docs/managed-clickhouse/operations/web-sql-query) for more details.
    """

    metrika: builtins.bool
    """Allow to import data from Yandex Metrica and AppMetrica to the cluster.

    See [AppMetrica documentation](https://appmetrica.yandex.com/docs/cloud/index.html) for more details.
    """

    serverless: builtins.bool
    """Allow access to cluster for Serverless."""

    data_transfer: builtins.bool
    """Allow access for DataTransfer"""

    yandex_query: builtins.bool
    """Allow access for Query"""

    def __init__(self,
        *,
        data_lens: builtins.bool = ...,
        web_sql: builtins.bool = ...,
        metrika: builtins.bool = ...,
        serverless: builtins.bool = ...,
        data_transfer: builtins.bool = ...,
        yandex_query: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_lens",b"data_lens","data_transfer",b"data_transfer","metrika",b"metrika","serverless",b"serverless","web_sql",b"web_sql","yandex_query",b"yandex_query"]) -> None: ...
global___Access = Access

class CloudStorage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENABLED_FIELD_NUMBER: builtins.int
    MOVE_FACTOR_FIELD_NUMBER: builtins.int
    DATA_CACHE_ENABLED_FIELD_NUMBER: builtins.int
    DATA_CACHE_MAX_SIZE_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    """Whether to use Object Storage for storing ClickHouse data."""

    @property
    def move_factor(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def data_cache_enabled(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def data_cache_max_size(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    def __init__(self,
        *,
        enabled: builtins.bool = ...,
        move_factor: typing.Optional[google.protobuf.wrappers_pb2.DoubleValue] = ...,
        data_cache_enabled: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        data_cache_max_size: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data_cache_enabled",b"data_cache_enabled","data_cache_max_size",b"data_cache_max_size","move_factor",b"move_factor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_cache_enabled",b"data_cache_enabled","data_cache_max_size",b"data_cache_max_size","enabled",b"enabled","move_factor",b"move_factor"]) -> None: ...
global___CloudStorage = CloudStorage
