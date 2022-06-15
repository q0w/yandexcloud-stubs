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
import yandex.cloud.mdb.sqlserver.v1.config.sqlserver2016sp2_pb2
import yandex.cloud.mdb.sqlserver.v1.config.sqlserver2017_pb2
import yandex.cloud.mdb.sqlserver.v1.config.sqlserver2019_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Cluster(google.protobuf.message.Message):
    """An SQL Server cluster.

    For more information, see the [Concepts](/docs/managed-sqlserver/concepts) section of the documentation.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Environment:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _EnvironmentEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Environment.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ENVIRONMENT_UNSPECIFIED: Cluster._Environment.ValueType  # 0
        PRODUCTION: Cluster._Environment.ValueType  # 1
        """Stable environment with a conservative update policy: only hotfixes are applied during regular maintenance."""

        PRESTABLE: Cluster._Environment.ValueType  # 2
        """Environment with more aggressive update policy: new versions are rolled out irrespective of backward compatibility."""

    class Environment(_Environment, metaclass=_EnvironmentEnumTypeWrapper):
        pass

    ENVIRONMENT_UNSPECIFIED: Cluster.Environment.ValueType  # 0
    PRODUCTION: Cluster.Environment.ValueType  # 1
    """Stable environment with a conservative update policy: only hotfixes are applied during regular maintenance."""

    PRESTABLE: Cluster.Environment.ValueType  # 2
    """Environment with more aggressive update policy: new versions are rolled out irrespective of backward compatibility."""


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Cluster._Health.ValueType  # 0
        """State of the cluster is unknown ([Host.health] of all hosts in the cluster is `UNKNOWN`)."""

        ALIVE: Cluster._Health.ValueType  # 1
        """Cluster is alive and works well ([Host.health] of all hosts in the cluster is `ALIVE`)."""

        DEAD: Cluster._Health.ValueType  # 2
        """Cluster is inoperable ([Host.health] of all hosts in the cluster is `DEAD`)."""

        DEGRADED: Cluster._Health.ValueType  # 3
        """Cluster is in degraded state ([Host.health] of at least one of the hosts in the cluster is not `ALIVE`)."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    HEALTH_UNKNOWN: Cluster.Health.ValueType  # 0
    """State of the cluster is unknown ([Host.health] of all hosts in the cluster is `UNKNOWN`)."""

    ALIVE: Cluster.Health.ValueType  # 1
    """Cluster is alive and works well ([Host.health] of all hosts in the cluster is `ALIVE`)."""

    DEAD: Cluster.Health.ValueType  # 2
    """Cluster is inoperable ([Host.health] of all hosts in the cluster is `DEAD`)."""

    DEGRADED: Cluster.Health.ValueType  # 3
    """Cluster is in degraded state ([Host.health] of at least one of the hosts in the cluster is not `ALIVE`)."""


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
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    SQLCOLLATION_FIELD_NUMBER: builtins.int
    HOST_GROUP_IDS_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the SQL Server cluster.

    This ID is assigned by Managed Service for SQL Server at the moment of creation.
    """

    folder_id: typing.Text
    """ID of the folder the SQL Server cluster belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when SQL Server cluster was created."""
        pass
    name: typing.Text
    """Name of the SQL Server cluster.

    The name must be unique within the folder, comply with [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt) and be 1-63 characters long.
    """

    description: typing.Text
    """Description of the SQL Server cluster.

    Must be 0-256 characters long.
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Custom labels for the SQL Server cluster as `key:value` pairs.

        Maximum 64 per resource.
        """
        pass
    environment: global___Cluster.Environment.ValueType
    """Deployment environment of the SQL Server cluster."""

    @property
    def monitoring(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Monitoring]:
        """Description of monitoring systems relevant to the SQL Server cluster."""
        pass
    @property
    def config(self) -> global___ClusterConfig:
        """Configuration of the SQL Server cluster."""
        pass
    network_id: typing.Text
    """ID of the network that the cluster belongs to."""

    health: global___Cluster.Health.ValueType
    """Aggregated cluster health."""

    status: global___Cluster.Status.ValueType
    """Current state of the cluster."""

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """User security groups."""
        pass
    deletion_protection: builtins.bool
    """Determines whether the cluster is protected from being deleted."""

    sqlcollation: typing.Text
    """SQL Server Collation."""

    @property
    def host_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Host groups hosting VMs of the cluster."""
        pass
    service_account_id: typing.Text
    """ID of the service account which is used for access to Yandex Object Storage."""

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
        security_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        deletion_protection: builtins.bool = ...,
        sqlcollation: typing.Text = ...,
        host_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        service_account_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config","created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","created_at",b"created_at","deletion_protection",b"deletion_protection","description",b"description","environment",b"environment","folder_id",b"folder_id","health",b"health","host_group_ids",b"host_group_ids","id",b"id","labels",b"labels","monitoring",b"monitoring","name",b"name","network_id",b"network_id","security_group_ids",b"security_group_ids","service_account_id",b"service_account_id","sqlcollation",b"sqlcollation","status",b"status"]) -> None: ...
global___Cluster = Cluster

class Monitoring(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the monitoring system."""

    description: typing.Text
    """Description of the monitoring system."""

    link: typing.Text
    """Link to the monitoring system charts for the SQL Server cluster."""

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
    class _SecondaryConnections:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SecondaryConnectionsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ClusterConfig._SecondaryConnections.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SECONDARY_CONNECTIONS_UNSPECIFIED: ClusterConfig._SecondaryConnections.ValueType  # 0
        SECONDARY_CONNECTIONS_OFF: ClusterConfig._SecondaryConnections.ValueType  # 1
        """Connections to secondary replicas are prohibited"""

        SECONDARY_CONNECTIONS_READ_ONLY: ClusterConfig._SecondaryConnections.ValueType  # 2
        """Secondary replicas are read-only"""

    class SecondaryConnections(_SecondaryConnections, metaclass=_SecondaryConnectionsEnumTypeWrapper):
        pass

    SECONDARY_CONNECTIONS_UNSPECIFIED: ClusterConfig.SecondaryConnections.ValueType  # 0
    SECONDARY_CONNECTIONS_OFF: ClusterConfig.SecondaryConnections.ValueType  # 1
    """Connections to secondary replicas are prohibited"""

    SECONDARY_CONNECTIONS_READ_ONLY: ClusterConfig.SecondaryConnections.ValueType  # 2
    """Secondary replicas are read-only"""


    VERSION_FIELD_NUMBER: builtins.int
    SQLSERVER_CONFIG_2016SP2STD_FIELD_NUMBER: builtins.int
    SQLSERVER_CONFIG_2016SP2ENT_FIELD_NUMBER: builtins.int
    SQLSERVER_CONFIG_2017STD_FIELD_NUMBER: builtins.int
    SQLSERVER_CONFIG_2017ENT_FIELD_NUMBER: builtins.int
    SQLSERVER_CONFIG_2019STD_FIELD_NUMBER: builtins.int
    SQLSERVER_CONFIG_2019ENT_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    BACKUP_WINDOW_START_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    SECONDARY_CONNECTIONS_FIELD_NUMBER: builtins.int
    version: typing.Text
    """Version of the SQL Server."""

    @property
    def sqlserver_config_2016sp2std(self) -> yandex.cloud.mdb.sqlserver.v1.config.sqlserver2016sp2_pb2.SQLServerConfigSet2016sp2std:
        """Configuration of the SQL Server 2016sp2 standard edition instance."""
        pass
    @property
    def sqlserver_config_2016sp2ent(self) -> yandex.cloud.mdb.sqlserver.v1.config.sqlserver2016sp2_pb2.SQLServerConfigSet2016sp2ent:
        """Configuration of the SQL Server 2016sp2 enterprise edition instance."""
        pass
    @property
    def sqlserver_config_2017std(self) -> yandex.cloud.mdb.sqlserver.v1.config.sqlserver2017_pb2.SQLServerConfigSet2017std:
        """Configuration of the SQL Server 2017 standard edition instance."""
        pass
    @property
    def sqlserver_config_2017ent(self) -> yandex.cloud.mdb.sqlserver.v1.config.sqlserver2017_pb2.SQLServerConfigSet2017ent:
        """Configuration of the SQL Server 2017 enterprise edition instance."""
        pass
    @property
    def sqlserver_config_2019std(self) -> yandex.cloud.mdb.sqlserver.v1.config.sqlserver2019_pb2.SQLServerConfigSet2019std:
        """Configuration of the SQL Server 2019 standard edition instance."""
        pass
    @property
    def sqlserver_config_2019ent(self) -> yandex.cloud.mdb.sqlserver.v1.config.sqlserver2019_pb2.SQLServerConfigSet2019ent:
        """Configuration of the SQL Server 2019 enterprise edition instance."""
        pass
    @property
    def resources(self) -> global___Resources:
        """Resources allocated to SQL Server hosts."""
        pass
    @property
    def backup_window_start(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Start time for the daily backup in UTC timezone."""
        pass
    @property
    def access(self) -> global___Access:
        """Database access policy."""
        pass
    secondary_connections: global___ClusterConfig.SecondaryConnections.ValueType
    """Secondary replicas connection mode"""

    def __init__(self,
        *,
        version: typing.Text = ...,
        sqlserver_config_2016sp2std: typing.Optional[yandex.cloud.mdb.sqlserver.v1.config.sqlserver2016sp2_pb2.SQLServerConfigSet2016sp2std] = ...,
        sqlserver_config_2016sp2ent: typing.Optional[yandex.cloud.mdb.sqlserver.v1.config.sqlserver2016sp2_pb2.SQLServerConfigSet2016sp2ent] = ...,
        sqlserver_config_2017std: typing.Optional[yandex.cloud.mdb.sqlserver.v1.config.sqlserver2017_pb2.SQLServerConfigSet2017std] = ...,
        sqlserver_config_2017ent: typing.Optional[yandex.cloud.mdb.sqlserver.v1.config.sqlserver2017_pb2.SQLServerConfigSet2017ent] = ...,
        sqlserver_config_2019std: typing.Optional[yandex.cloud.mdb.sqlserver.v1.config.sqlserver2019_pb2.SQLServerConfigSet2019std] = ...,
        sqlserver_config_2019ent: typing.Optional[yandex.cloud.mdb.sqlserver.v1.config.sqlserver2019_pb2.SQLServerConfigSet2019ent] = ...,
        resources: typing.Optional[global___Resources] = ...,
        backup_window_start: typing.Optional[google.type.timeofday_pb2.TimeOfDay] = ...,
        access: typing.Optional[global___Access] = ...,
        secondary_connections: global___ClusterConfig.SecondaryConnections.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["access",b"access","backup_window_start",b"backup_window_start","resources",b"resources","sqlserver_config",b"sqlserver_config","sqlserver_config_2016sp2ent",b"sqlserver_config_2016sp2ent","sqlserver_config_2016sp2std",b"sqlserver_config_2016sp2std","sqlserver_config_2017ent",b"sqlserver_config_2017ent","sqlserver_config_2017std",b"sqlserver_config_2017std","sqlserver_config_2019ent",b"sqlserver_config_2019ent","sqlserver_config_2019std",b"sqlserver_config_2019std"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access",b"access","backup_window_start",b"backup_window_start","resources",b"resources","secondary_connections",b"secondary_connections","sqlserver_config",b"sqlserver_config","sqlserver_config_2016sp2ent",b"sqlserver_config_2016sp2ent","sqlserver_config_2016sp2std",b"sqlserver_config_2016sp2std","sqlserver_config_2017ent",b"sqlserver_config_2017ent","sqlserver_config_2017std",b"sqlserver_config_2017std","sqlserver_config_2019ent",b"sqlserver_config_2019ent","sqlserver_config_2019std",b"sqlserver_config_2019std","version",b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["sqlserver_config",b"sqlserver_config"]) -> typing.Optional[typing_extensions.Literal["sqlserver_config_2016sp2std","sqlserver_config_2016sp2ent","sqlserver_config_2017std","sqlserver_config_2017ent","sqlserver_config_2019std","sqlserver_config_2019ent"]]: ...
global___ClusterConfig = ClusterConfig

class Host(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Role:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _RoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Role.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ROLE_UNKNOWN: Host._Role.ValueType  # 0
        """Role of the host in the cluster is unknown."""

        MASTER: Host._Role.ValueType  # 1
        """Host is the master SQL Server instance in the cluster."""

        REPLICA: Host._Role.ValueType  # 2
        """Host is a replica SQL Server instance in the cluster."""

    class Role(_Role, metaclass=_RoleEnumTypeWrapper):
        pass

    ROLE_UNKNOWN: Host.Role.ValueType  # 0
    """Role of the host in the cluster is unknown."""

    MASTER: Host.Role.ValueType  # 1
    """Host is the master SQL Server instance in the cluster."""

    REPLICA: Host.Role.ValueType  # 2
    """Host is a replica SQL Server instance in the cluster."""


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Host._Health.ValueType  # 0
        """Health of the host is unknown."""

        ALIVE: Host._Health.ValueType  # 1
        """The host is performing all its functions normally."""

        DEAD: Host._Health.ValueType  # 2
        """The host is inoperable and cannot perform any of its essential functions."""

        DEGRADED: Host._Health.ValueType  # 3
        """The host is degraded and can perform only some of its essential functions."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    HEALTH_UNKNOWN: Host.Health.ValueType  # 0
    """Health of the host is unknown."""

    ALIVE: Host.Health.ValueType  # 1
    """The host is performing all its functions normally."""

    DEAD: Host.Health.ValueType  # 2
    """The host is inoperable and cannot perform any of its essential functions."""

    DEGRADED: Host.Health.ValueType  # 3
    """The host is degraded and can perform only some of its essential functions."""


    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the SQL Server host.

    The host name is assigned by Managed Service for SQL Server at the moment of creation and cannot be changed. 1-63 characters long.

    The name is unique across all existing database hosts in Yandex Cloud as it defines the FQDN of the host.
    """

    cluster_id: typing.Text
    """ID of the SQL Server host.

    The ID is assigned by Managed Service for SQL Server at the moment of creation.
    """

    zone_id: typing.Text
    """ID of the availability zone where the SQL Server host resides."""

    @property
    def resources(self) -> global___Resources:
        """Resources allocated to the host."""
        pass
    role: global___Host.Role.ValueType
    """Role of the host in the cluster."""

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
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resources",b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_public_ip",b"assign_public_ip","cluster_id",b"cluster_id","health",b"health","name",b"name","resources",b"resources","role",b"role","services",b"services","subnet_id",b"subnet_id","zone_id",b"zone_id"]) -> None: ...
global___Host = Host

class Service(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Service._Type.ValueType  # 0
        SQLSERVER: Service._Type.ValueType  # 1
        """SQL Server service."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    TYPE_UNSPECIFIED: Service.Type.ValueType  # 0
    SQLSERVER: Service.Type.ValueType  # 1
    """SQL Server service."""


    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Service._Health.ValueType  # 0
        """Health of the server is unknown."""

        ALIVE: Service._Health.ValueType  # 1
        """The server is working normally."""

        DEAD: Service._Health.ValueType  # 2
        """The server is dead or unresponsive."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    HEALTH_UNKNOWN: Service.Health.ValueType  # 0
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
    """ID of the preset for computational resources available to a host (CPU, memory, etc.).

    All available presets are listed in the [documentation](/docs/managed-sqlserver/concepts/instance-types).
    """

    disk_size: builtins.int
    """Volume of the storage available to a host."""

    disk_type_id: typing.Text
    """Type of the storage environment for the host.

    Possible values:
    * `network-hdd` - network HDD drive;
    * `network-ssd` - network SSD drive;
    * `local-ssd` - local SSD storage.
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
    data_lens: builtins.bool
    """Allows access for DataLens."""

    web_sql: builtins.bool
    """Allows access for Web SQL."""

    def __init__(self,
        *,
        data_lens: builtins.bool = ...,
        web_sql: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_lens",b"data_lens","web_sql",b"web_sql"]) -> None: ...
global___Access = Access
