"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ConnectorSpec(google.protobuf.message.Message):
    """An Apache Kafka® connector specification"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class PropertiesEntry(google.protobuf.message.Message):
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

    NAME_FIELD_NUMBER: builtins.int
    TASKS_MAX_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    CONNECTOR_CONFIG_MIRRORMAKER_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the connector."""

    @property
    def tasks_max(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Maximum number of connector tasks.
        Default is the number of brokers.
        """
        pass
    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Properties passed with connector config to Connect service.
        Example: 'sync.topics.config.enabled: true'.
        """
        pass
    @property
    def connector_config_mirrormaker(self) -> global___ConnectorConfigMirrorMakerSpec:
        """Configuration of MirrorMaker connector"""
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        tasks_max: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        properties: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        connector_config_mirrormaker: typing.Optional[global___ConnectorConfigMirrorMakerSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector_config",b"connector_config","connector_config_mirrormaker",b"connector_config_mirrormaker","tasks_max",b"tasks_max"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_config",b"connector_config","connector_config_mirrormaker",b"connector_config_mirrormaker","name",b"name","properties",b"properties","tasks_max",b"tasks_max"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["connector_config",b"connector_config"]) -> typing.Optional[typing_extensions.Literal["connector_config_mirrormaker"]]: ...
global___ConnectorSpec = ConnectorSpec

class UpdateConnectorSpec(google.protobuf.message.Message):
    """An Apache Kafka® connector's update specification."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class PropertiesEntry(google.protobuf.message.Message):
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

    TASKS_MAX_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    CONNECTOR_CONFIG_MIRRORMAKER_FIELD_NUMBER: builtins.int
    @property
    def tasks_max(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Maximum number of tasks to update."""
        pass
    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Properties passed with connector config to Connect service, that
        we should change or add in existing Properties-set of connector.
        Example: 'sync.topics.config.enabled: false'
        """
        pass
    @property
    def connector_config_mirrormaker(self) -> global___ConnectorConfigMirrorMakerSpec:
        """Update specification for MirrorMaker."""
        pass
    def __init__(self,
        *,
        tasks_max: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        properties: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        connector_config_mirrormaker: typing.Optional[global___ConnectorConfigMirrorMakerSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector_config",b"connector_config","connector_config_mirrormaker",b"connector_config_mirrormaker","tasks_max",b"tasks_max"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_config",b"connector_config","connector_config_mirrormaker",b"connector_config_mirrormaker","properties",b"properties","tasks_max",b"tasks_max"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["connector_config",b"connector_config"]) -> typing.Optional[typing_extensions.Literal["connector_config_mirrormaker"]]: ...
global___UpdateConnectorSpec = UpdateConnectorSpec

class ConnectorConfigMirrorMakerSpec(google.protobuf.message.Message):
    """An An Apache Kafka® MirrorMaker
    connector specification.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SOURCE_CLUSTER_FIELD_NUMBER: builtins.int
    TARGET_CLUSTER_FIELD_NUMBER: builtins.int
    TOPICS_FIELD_NUMBER: builtins.int
    REPLICATION_FACTOR_FIELD_NUMBER: builtins.int
    @property
    def source_cluster(self) -> global___ClusterConnectionSpec:
        """Source cluster configuration."""
        pass
    @property
    def target_cluster(self) -> global___ClusterConnectionSpec:
        """Target cluster configuration."""
        pass
    topics: typing.Text
    """List of Kafka topics, separated by ','"""

    @property
    def replication_factor(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Replication factor for automatically created topics."""
        pass
    def __init__(self,
        *,
        source_cluster: typing.Optional[global___ClusterConnectionSpec] = ...,
        target_cluster: typing.Optional[global___ClusterConnectionSpec] = ...,
        topics: typing.Text = ...,
        replication_factor: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["replication_factor",b"replication_factor","source_cluster",b"source_cluster","target_cluster",b"target_cluster"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["replication_factor",b"replication_factor","source_cluster",b"source_cluster","target_cluster",b"target_cluster","topics",b"topics"]) -> None: ...
global___ConnectorConfigMirrorMakerSpec = ConnectorConfigMirrorMakerSpec

class ClusterConnectionSpec(google.protobuf.message.Message):
    """Specification of ClusterConnection -
    connection to clusters, that
    are source or target of MirrorMaker
    clusters.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ALIAS_FIELD_NUMBER: builtins.int
    THIS_CLUSTER_FIELD_NUMBER: builtins.int
    EXTERNAL_CLUSTER_FIELD_NUMBER: builtins.int
    alias: typing.Text
    """Alias of ClusterConnection.
    For example: 'source', 'target', ...
    """

    @property
    def this_cluster(self) -> global___ThisClusterSpec:
        """If type is 'this_cluster' - we connect to
        cluster that is handle Kafka Connect Worker,
        on which we try to register connector.
        """
        pass
    @property
    def external_cluster(self) -> global___ExternalClusterConnectionSpec:
        """If type is 'external_cluster' - we connect
        to cluster that is not handle Kafka Connect Worker,
        on which we try to register connector.
        """
        pass
    def __init__(self,
        *,
        alias: typing.Text = ...,
        this_cluster: typing.Optional[global___ThisClusterSpec] = ...,
        external_cluster: typing.Optional[global___ExternalClusterConnectionSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cluster_connection",b"cluster_connection","external_cluster",b"external_cluster","this_cluster",b"this_cluster"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alias",b"alias","cluster_connection",b"cluster_connection","external_cluster",b"external_cluster","this_cluster",b"this_cluster"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["cluster_connection",b"cluster_connection"]) -> typing.Optional[typing_extensions.Literal["this_cluster","external_cluster"]]: ...
global___ClusterConnectionSpec = ClusterConnectionSpec

class ThisClusterSpec(google.protobuf.message.Message):
    """Specification of cluster_connection
    type 'this_cluster'. This means
    that we already have all credentials,
    so this spec is empty.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ThisClusterSpec = ThisClusterSpec

class ExternalClusterConnectionSpec(google.protobuf.message.Message):
    """Specification of connection to
    external cluster. It contains
    all necessary credentials to
    connect to external cluster.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BOOTSTRAP_SERVERS_FIELD_NUMBER: builtins.int
    SASL_USERNAME_FIELD_NUMBER: builtins.int
    SASL_PASSWORD_FIELD_NUMBER: builtins.int
    SASL_MECHANISM_FIELD_NUMBER: builtins.int
    SECURITY_PROTOCOL_FIELD_NUMBER: builtins.int
    SSL_TRUSTSTORE_CERTIFICATES_FIELD_NUMBER: builtins.int
    bootstrap_servers: typing.Text
    """List bootstrap servers of cluster,
    separated by ','.
    """

    sasl_username: typing.Text
    """Sasl username which
    we use to connect to cluster.
    """

    sasl_password: typing.Text
    """Sasl password which we use
    to connect to cluster.
    """

    sasl_mechanism: typing.Text
    """Sasl mechanism, which we
    should use to connect to cluster.
    """

    security_protocol: typing.Text
    """Security protocol, which
    we should use to connect
    to cluster.
    """

    ssl_truststore_certificates: typing.Text
    """CA in PEM format to connect to external cluster.
    Lines of certificate separated by '\\n' symbol.
    """

    def __init__(self,
        *,
        bootstrap_servers: typing.Text = ...,
        sasl_username: typing.Text = ...,
        sasl_password: typing.Text = ...,
        sasl_mechanism: typing.Text = ...,
        security_protocol: typing.Text = ...,
        ssl_truststore_certificates: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bootstrap_servers",b"bootstrap_servers","sasl_mechanism",b"sasl_mechanism","sasl_password",b"sasl_password","sasl_username",b"sasl_username","security_protocol",b"security_protocol","ssl_truststore_certificates",b"ssl_truststore_certificates"]) -> None: ...
global___ExternalClusterConnectionSpec = ExternalClusterConnectionSpec

class Connector(google.protobuf.message.Message):
    """An Apache Kafka® connector resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Health:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Connector._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Connector._Health.ValueType  # 0
        """State of the connector is unknown."""

        ALIVE: Connector._Health.ValueType  # 1
        """Connector is running."""

        DEAD: Connector._Health.ValueType  # 2
        """Connector is failed to start."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper):
        pass

    HEALTH_UNKNOWN: Connector.Health.ValueType  # 0
    """State of the connector is unknown."""

    ALIVE: Connector.Health.ValueType  # 1
    """Connector is running."""

    DEAD: Connector.Health.ValueType  # 2
    """Connector is failed to start."""


    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Connector._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: Connector._Status.ValueType  # 0
        """Connector state is unknown."""

        RUNNING: Connector._Status.ValueType  # 1
        """Connector is running normally."""

        ERROR: Connector._Status.ValueType  # 2
        """Connector encountered a problem and cannot operate."""

        PAUSED: Connector._Status.ValueType  # 3
        """Connector paused."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: Connector.Status.ValueType  # 0
    """Connector state is unknown."""

    RUNNING: Connector.Status.ValueType  # 1
    """Connector is running normally."""

    ERROR: Connector.Status.ValueType  # 2
    """Connector encountered a problem and cannot operate."""

    PAUSED: Connector.Status.ValueType  # 3
    """Connector paused."""


    class PropertiesEntry(google.protobuf.message.Message):
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

    NAME_FIELD_NUMBER: builtins.int
    TASKS_MAX_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_CONFIG_MIRRORMAKER_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the connector."""

    @property
    def tasks_max(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Maximum number of tasks. Default is the number of brokers"""
        pass
    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Properties passed with connector config to Connect service
        Example: 'sync.topics.config.enabled: true'
        """
        pass
    health: global___Connector.Health.ValueType
    """Connector health."""

    status: global___Connector.Status.ValueType
    """Current status of the connector."""

    cluster_id: typing.Text
    """ID of the Apache Kafka cluster that the connector belongs to."""

    @property
    def connector_config_mirrormaker(self) -> global___ConnectorConfigMirrorMaker: ...
    def __init__(self,
        *,
        name: typing.Text = ...,
        tasks_max: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        properties: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        health: global___Connector.Health.ValueType = ...,
        status: global___Connector.Status.ValueType = ...,
        cluster_id: typing.Text = ...,
        connector_config_mirrormaker: typing.Optional[global___ConnectorConfigMirrorMaker] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector_config",b"connector_config","connector_config_mirrormaker",b"connector_config_mirrormaker","tasks_max",b"tasks_max"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","connector_config",b"connector_config","connector_config_mirrormaker",b"connector_config_mirrormaker","health",b"health","name",b"name","properties",b"properties","status",b"status","tasks_max",b"tasks_max"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["connector_config",b"connector_config"]) -> typing.Optional[typing_extensions.Literal["connector_config_mirrormaker"]]: ...
global___Connector = Connector

class ConnectorConfigMirrorMaker(google.protobuf.message.Message):
    """An An Apache Kafka® MirrorMaker
    connector resource.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SOURCE_CLUSTER_FIELD_NUMBER: builtins.int
    TARGET_CLUSTER_FIELD_NUMBER: builtins.int
    TOPICS_FIELD_NUMBER: builtins.int
    REPLICATION_FACTOR_FIELD_NUMBER: builtins.int
    @property
    def source_cluster(self) -> global___ClusterConnection:
        """Source cluster resource
        settings.
        """
        pass
    @property
    def target_cluster(self) -> global___ClusterConnection:
        """Target cluster resource
        settings.
        """
        pass
    topics: typing.Text
    """List of Kafka topics, separated by ','"""

    @property
    def replication_factor(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Replication factor for automatically created topics."""
        pass
    def __init__(self,
        *,
        source_cluster: typing.Optional[global___ClusterConnection] = ...,
        target_cluster: typing.Optional[global___ClusterConnection] = ...,
        topics: typing.Text = ...,
        replication_factor: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["replication_factor",b"replication_factor","source_cluster",b"source_cluster","target_cluster",b"target_cluster"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["replication_factor",b"replication_factor","source_cluster",b"source_cluster","target_cluster",b"target_cluster","topics",b"topics"]) -> None: ...
global___ConnectorConfigMirrorMaker = ConnectorConfigMirrorMaker

class ClusterConnection(google.protobuf.message.Message):
    """Resource ClusterConnection -
    settings of
    connection to clusters, that
    are source or target of MirrorMaker
    clusters.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ALIAS_FIELD_NUMBER: builtins.int
    THIS_CLUSTER_FIELD_NUMBER: builtins.int
    EXTERNAL_CLUSTER_FIELD_NUMBER: builtins.int
    alias: typing.Text
    """Alias of ClusterConnection resource.
    For example: 'source', 'target', ...
    """

    @property
    def this_cluster(self) -> global___ThisCluster:
        """If type is 'this_cluster' - we connect to
        cluster that is handle Kafka Connect Worker,
        on which we try to register connector.
        """
        pass
    @property
    def external_cluster(self) -> global___ExternalClusterConnection:
        """If type is 'external_cluster' - we connect
        to cluster that is not handle Kafka Connect Worker,
        on which we try to register connector.
        """
        pass
    def __init__(self,
        *,
        alias: typing.Text = ...,
        this_cluster: typing.Optional[global___ThisCluster] = ...,
        external_cluster: typing.Optional[global___ExternalClusterConnection] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cluster_connection",b"cluster_connection","external_cluster",b"external_cluster","this_cluster",b"this_cluster"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alias",b"alias","cluster_connection",b"cluster_connection","external_cluster",b"external_cluster","this_cluster",b"this_cluster"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["cluster_connection",b"cluster_connection"]) -> typing.Optional[typing_extensions.Literal["this_cluster","external_cluster"]]: ...
global___ClusterConnection = ClusterConnection

class ThisCluster(google.protobuf.message.Message):
    """Resource of cluster_connection
    type 'this_cluster'.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ThisCluster = ThisCluster

class ExternalClusterConnection(google.protobuf.message.Message):
    """Resource of connection to
    external cluster. It contains
    all settings of connection
    to external cluster.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BOOTSTRAP_SERVERS_FIELD_NUMBER: builtins.int
    SASL_USERNAME_FIELD_NUMBER: builtins.int
    SASL_MECHANISM_FIELD_NUMBER: builtins.int
    SECURITY_PROTOCOL_FIELD_NUMBER: builtins.int
    bootstrap_servers: typing.Text
    """List bootstrap servers of cluster,
    separated by ','
    """

    sasl_username: typing.Text
    """Sasl username which
    we use to connect to cluster.
    """

    sasl_mechanism: typing.Text
    """Sasl mechanism, which we
    should use to connect to cluster.
    """

    security_protocol: typing.Text
    """Security protocol, which
    we should use to connect
    to cluster.
    """

    def __init__(self,
        *,
        bootstrap_servers: typing.Text = ...,
        sasl_username: typing.Text = ...,
        sasl_mechanism: typing.Text = ...,
        security_protocol: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bootstrap_servers",b"bootstrap_servers","sasl_mechanism",b"sasl_mechanism","sasl_username",b"sasl_username","security_protocol",b"security_protocol"]) -> None: ...
global___ExternalClusterConnection = ExternalClusterConnection