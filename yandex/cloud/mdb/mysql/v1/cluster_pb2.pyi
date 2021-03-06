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
import google.type.timeofday_pb2
import typing
import typing_extensions
import yandex.cloud.mdb.mysql.v1.config.mysql5_7_pb2
import yandex.cloud.mdb.mysql.v1.config.mysql8_0_pb2
import yandex.cloud.mdb.mysql.v1.maintenance_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Cluster(google.protobuf.message.Message):
    """An object that represents MySQL cluster.

    See [the documentation](/docs/managed-mysql/concepts) for details.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Environment:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _EnvironmentEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Environment.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ENVIRONMENT_UNSPECIFIED: Cluster._Environment.ValueType  # 0
        PRODUCTION: Cluster._Environment.ValueType  # 1
        """Environment for stable versions of your apps.
        A conservative update policy is in effect: only bug fixes are applied during regular maintenance.
        """

        PRESTABLE: Cluster._Environment.ValueType  # 2
        """Environment for testing, including the Managed Service for MySQL itself.
        This environment gets new features, improvements, and bug fixes in the first place, compared to the production environment.
        However, not every update ensures backward compatibility.
        """

    class Environment(_Environment, metaclass=_EnvironmentEnumTypeWrapper):
        pass

    ENVIRONMENT_UNSPECIFIED: Cluster.Environment.ValueType  # 0
    PRODUCTION: Cluster.Environment.ValueType  # 1
    """Environment for stable versions of your apps.
    A conservative update policy is in effect: only bug fixes are applied during regular maintenance.
    """

    PRESTABLE: Cluster.Environment.ValueType  # 2
    """Environment for testing, including the Managed Service for MySQL itself.
    This environment gets new features, improvements, and bug fixes in the first place, compared to the production environment.
    However, not every update ensures backward compatibility.
    """


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Cluster._Health.ValueType  # 0
        """Health of the cluster is unknown ([Host.health] for every host in the cluster is `UNKNOWN`)."""

        ALIVE: Cluster._Health.ValueType  # 1
        """Cluster is alive and well ([Host.health] for every host in the cluster is `ALIVE`)."""

        DEAD: Cluster._Health.ValueType  # 2
        """Cluster is inoperable ([Host.health] for every host in the cluster is `DEAD`)."""

        DEGRADED: Cluster._Health.ValueType  # 3
        """Cluster is degraded ([Host.health] for at least one host in the cluster is not `ALIVE`)."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    HEALTH_UNKNOWN: Cluster.Health.ValueType  # 0
    """Health of the cluster is unknown ([Host.health] for every host in the cluster is `UNKNOWN`)."""

    ALIVE: Cluster.Health.ValueType  # 1
    """Cluster is alive and well ([Host.health] for every host in the cluster is `ALIVE`)."""

    DEAD: Cluster.Health.ValueType  # 2
    """Cluster is inoperable ([Host.health] for every host in the cluster is `DEAD`)."""

    DEGRADED: Cluster.Health.ValueType  # 3
    """Cluster is degraded ([Host.health] for at least one host in the cluster is not `ALIVE`)."""


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
        """Cluster is stopped."""

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
    """Cluster is stopped."""

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
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    PLANNED_OPERATION_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    HOST_GROUP_IDS_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the cluster.

    This ID is assigned by the platform at the time of creation.
    """

    folder_id: typing.Text
    """ID of the folder that the cluster belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp of the cluster."""
        pass
    name: typing.Text
    """Name of the cluster."""

    description: typing.Text
    """Description of the cluster."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Custom labels for the cluster as `key:value` pairs."""
        pass
    environment: global___Cluster.Environment.ValueType
    """Deployment environment of the cluster."""

    @property
    def monitoring(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Monitoring]:
        """Monitoring systems data that is relevant to the cluster."""
        pass
    @property
    def config(self) -> global___ClusterConfig:
        """Configuration of the cluster."""
        pass
    network_id: typing.Text
    """ID of the network that the cluster belongs to."""

    health: global___Cluster.Health.ValueType
    """Aggregated health of the cluster."""

    status: global___Cluster.Status.ValueType
    """Current state of the cluster."""

    @property
    def maintenance_window(self) -> yandex.cloud.mdb.mysql.v1.maintenance_pb2.MaintenanceWindow:
        """Maintenance window settings for the cluster."""
        pass
    @property
    def planned_operation(self) -> yandex.cloud.mdb.mysql.v1.maintenance_pb2.MaintenanceOperation:
        """Planned maintenance operation to be started for the cluster within the nearest [maintenance_window]."""
        pass
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Effective list of security group IDs applied to the cluster."""
        pass
    deletion_protection: builtins.bool
    """This option prevents unintended deletion of the cluster."""

    @property
    def host_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Host groups hosting VMs of the cluster."""
        pass
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
        maintenance_window: typing.Optional[yandex.cloud.mdb.mysql.v1.maintenance_pb2.MaintenanceWindow] = ...,
        planned_operation: typing.Optional[yandex.cloud.mdb.mysql.v1.maintenance_pb2.MaintenanceOperation] = ...,
        security_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        deletion_protection: builtins.bool = ...,
        host_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config","created_at",b"created_at","maintenance_window",b"maintenance_window","planned_operation",b"planned_operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","created_at",b"created_at","deletion_protection",b"deletion_protection","description",b"description","environment",b"environment","folder_id",b"folder_id","health",b"health","host_group_ids",b"host_group_ids","id",b"id","labels",b"labels","maintenance_window",b"maintenance_window","monitoring",b"monitoring","name",b"name","network_id",b"network_id","planned_operation",b"planned_operation","security_group_ids",b"security_group_ids","status",b"status"]) -> None: ...
global___Cluster = Cluster

class Monitoring(google.protobuf.message.Message):
    """Cluster-related monitoring system data."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the monitoring system."""

    description: typing.Text
    """Description of the monitoring system."""

    link: typing.Text
    """Link to the monitoring system charts for the cluster."""

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
    VERSION_FIELD_NUMBER: builtins.int
    MYSQL_CONFIG_5_7_FIELD_NUMBER: builtins.int
    MYSQL_CONFIG_8_0_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    BACKUP_WINDOW_START_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    PERFORMANCE_DIAGNOSTICS_FIELD_NUMBER: builtins.int
    version: typing.Text
    """Version of MySQL used in the cluster."""

    @property
    def mysql_config_5_7(self) -> yandex.cloud.mdb.mysql.v1.config.mysql5_7_pb2.MysqlConfigSet5_7:
        """Configuration of a MySQL 5.7 server."""
        pass
    @property
    def mysql_config_8_0(self) -> yandex.cloud.mdb.mysql.v1.config.mysql8_0_pb2.MysqlConfigSet8_0:
        """Configuration of a MySQL 8.0 server."""
        pass
    @property
    def resources(self) -> global___Resources:
        """Resource preset for the cluster hosts."""
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
    def performance_diagnostics(self) -> global___PerformanceDiagnostics:
        """Configuration of the performance diagnostics service."""
        pass
    def __init__(self,
        *,
        version: typing.Text = ...,
        mysql_config_5_7: typing.Optional[yandex.cloud.mdb.mysql.v1.config.mysql5_7_pb2.MysqlConfigSet5_7] = ...,
        mysql_config_8_0: typing.Optional[yandex.cloud.mdb.mysql.v1.config.mysql8_0_pb2.MysqlConfigSet8_0] = ...,
        resources: typing.Optional[global___Resources] = ...,
        backup_window_start: typing.Optional[google.type.timeofday_pb2.TimeOfDay] = ...,
        access: typing.Optional[global___Access] = ...,
        performance_diagnostics: typing.Optional[global___PerformanceDiagnostics] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["access",b"access","backup_window_start",b"backup_window_start","mysql_config",b"mysql_config","mysql_config_5_7",b"mysql_config_5_7","mysql_config_8_0",b"mysql_config_8_0","performance_diagnostics",b"performance_diagnostics","resources",b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access",b"access","backup_window_start",b"backup_window_start","mysql_config",b"mysql_config","mysql_config_5_7",b"mysql_config_5_7","mysql_config_8_0",b"mysql_config_8_0","performance_diagnostics",b"performance_diagnostics","resources",b"resources","version",b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["mysql_config",b"mysql_config"]) -> typing.Optional[typing_extensions.Literal["mysql_config_5_7","mysql_config_8_0"]]: ...
global___ClusterConfig = ClusterConfig

class Host(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Role:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _RoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Role.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ROLE_UNKNOWN: Host._Role.ValueType  # 0
        """Role of the host is unknown."""

        MASTER: Host._Role.ValueType  # 1
        """Host is the master."""

        REPLICA: Host._Role.ValueType  # 2
        """Host is a replica."""

    class Role(_Role, metaclass=_RoleEnumTypeWrapper):
        pass

    ROLE_UNKNOWN: Host.Role.ValueType  # 0
    """Role of the host is unknown."""

    MASTER: Host.Role.ValueType  # 1
    """Host is the master."""

    REPLICA: Host.Role.ValueType  # 2
    """Host is a replica."""


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Host._Health.ValueType  # 0
        """Health of the host is unknown."""

        ALIVE: Host._Health.ValueType  # 1
        """Host is performing all its functions normally."""

        DEAD: Host._Health.ValueType  # 2
        """Host is inoperable, and cannot perform any of its essential functions."""

        DEGRADED: Host._Health.ValueType  # 3
        """Host is degraded, and can perform only some of its essential functions."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    HEALTH_UNKNOWN: Host.Health.ValueType  # 0
    """Health of the host is unknown."""

    ALIVE: Host.Health.ValueType  # 1
    """Host is performing all its functions normally."""

    DEAD: Host.Health.ValueType  # 2
    """Host is inoperable, and cannot perform any of its essential functions."""

    DEGRADED: Host.Health.ValueType  # 3
    """Host is degraded, and can perform only some of its essential functions."""


    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    REPLICATION_SOURCE_FIELD_NUMBER: builtins.int
    BACKUP_PRIORITY_FIELD_NUMBER: builtins.int
    PRIORITY_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the host.

    This name is assigned by the platform at the time of creation.
    The name is unique across all MDB hosts that exist on the platform, as it defines the FQDN of the host.
    """

    cluster_id: typing.Text
    """ID of the cluster the host belongs to."""

    zone_id: typing.Text
    """ID of the availability zone where the host resides."""

    @property
    def resources(self) -> global___Resources:
        """Resources allocated to the host."""
        pass
    role: global___Host.Role.ValueType
    """Role of the host in the cluster."""

    health: global___Host.Health.ValueType
    """Aggregated health of the host."""

    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Service]:
        """List of services provided by the host."""
        pass
    subnet_id: typing.Text
    """ID of the subnet that the host belongs to."""

    assign_public_ip: builtins.bool
    """Flag that shows if public IP address is assigned to the host so that the host can be accessed from the internet."""

    replication_source: typing.Text
    """Name of the host to be used as the replication source for cascading replication."""

    backup_priority: builtins.int
    """Host backup priority."""

    priority: builtins.int
    """Host master promotion priority."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        cluster_id: typing.Text = ...,
        zone_id: typing.Text = ...,
        resources: typing.Optional[global___Resources] = ...,
        role: global___Host.Role.ValueType = ...,
        health: global___Host.Health.ValueType = ...,
        services: typing.Optional[typing.Iterable[global___Service]] = ...,
        subnet_id: typing.Text = ...,
        assign_public_ip: builtins.bool = ...,
        replication_source: typing.Text = ...,
        backup_priority: builtins.int = ...,
        priority: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resources",b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_public_ip",b"assign_public_ip","backup_priority",b"backup_priority","cluster_id",b"cluster_id","health",b"health","name",b"name","priority",b"priority","replication_source",b"replication_source","resources",b"resources","role",b"role","services",b"services","subnet_id",b"subnet_id","zone_id",b"zone_id"]) -> None: ...
global___Host = Host

class Service(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Service._Type.ValueType  # 0
        MYSQL: Service._Type.ValueType  # 1
        """The host is a MySQL server."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    TYPE_UNSPECIFIED: Service.Type.ValueType  # 0
    MYSQL: Service.Type.ValueType  # 1
    """The host is a MySQL server."""


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Service._Health.ValueType  # 0
        """Health of the service is unknown."""

        ALIVE: Service._Health.ValueType  # 1
        """The service is working normally."""

        DEAD: Service._Health.ValueType  # 2
        """The service is dead or unresponsive."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    HEALTH_UNKNOWN: Service.Health.ValueType  # 0
    """Health of the service is unknown."""

    ALIVE: Service.Health.ValueType  # 1
    """The service is working normally."""

    DEAD: Service.Health.ValueType  # 2
    """The service is dead or unresponsive."""


    TYPE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    type: global___Service.Type.ValueType
    """Type of the service provided by the host."""

    health: global___Service.Health.ValueType
    """Aggregated health of the service."""

    def __init__(self,
        *,
        type: global___Service.Type.ValueType = ...,
        health: global___Service.Health.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["health",b"health","type",b"type"]) -> None: ...
global___Service = Service

class Resources(google.protobuf.message.Message):
    """Cluster resource preset."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    DISK_TYPE_ID_FIELD_NUMBER: builtins.int
    resource_preset_id: typing.Text
    """ID of the resource preset that defines available computational resources (vCPU, RAM, etc.) for a cluster host.

    All available presets are listed in [the documentation](/docs/managed-mysql/concepts/instance-types).
    """

    disk_size: builtins.int
    """Volume of the storage (for each cluster host, in bytes)."""

    disk_type_id: typing.Text
    """Type of the storage.

    Possible values:
    * `network-hdd` - standard network storage
    * `network-ssd` - fast network storage
    * `network-ssd-nonreplicated` - fast network nonreplicated storage
    * `local-ssd` - fast local storage.

    See [the documentation](/docs/managed-mysql/concepts/storage) for details.
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
    DATA_TRANSFER_FIELD_NUMBER: builtins.int
    data_lens: builtins.bool
    """Allows access from DataLens.

    See [the documentation](/docs/managed-mysql/operations/datalens-connect) for details.
    """

    web_sql: builtins.bool
    """Allows SQL queries to the cluster databases from management console.

    See [the documentation](/docs/managed-mysql/operations/web-sql-query) for details.
    """

    data_transfer: builtins.bool
    """Allow access for DataTransfer."""

    def __init__(self,
        *,
        data_lens: builtins.bool = ...,
        web_sql: builtins.bool = ...,
        data_transfer: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_lens",b"data_lens","data_transfer",b"data_transfer","web_sql",b"web_sql"]) -> None: ...
global___Access = Access

class PerformanceDiagnostics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENABLED_FIELD_NUMBER: builtins.int
    SESSIONS_SAMPLING_INTERVAL_FIELD_NUMBER: builtins.int
    STATEMENTS_SAMPLING_INTERVAL_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    """Flag that shows if performance statistics gathering is enabled for the cluster."""

    sessions_sampling_interval: builtins.int
    """Interval (in seconds) for `my_session` sampling."""

    statements_sampling_interval: builtins.int
    """Interval (in seconds) for `my_statements` sampling."""

    def __init__(self,
        *,
        enabled: builtins.bool = ...,
        sessions_sampling_interval: builtins.int = ...,
        statements_sampling_interval: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled",b"enabled","sessions_sampling_interval",b"sessions_sampling_interval","statements_sampling_interval",b"statements_sampling_interval"]) -> None: ...
global___PerformanceDiagnostics = PerformanceDiagnostics
