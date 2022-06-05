"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.datatransfer.v1.endpoint.common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PostgresObjectTransferSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SEQUENCE_FIELD_NUMBER: builtins.int
    SEQUENCE_OWNED_BY_FIELD_NUMBER: builtins.int
    TABLE_FIELD_NUMBER: builtins.int
    PRIMARY_KEY_FIELD_NUMBER: builtins.int
    FK_CONSTRAINT_FIELD_NUMBER: builtins.int
    DEFAULT_VALUES_FIELD_NUMBER: builtins.int
    CONSTRAINT_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    FUNCTION_FIELD_NUMBER: builtins.int
    TRIGGER_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    RULE_FIELD_NUMBER: builtins.int
    COLLATION_FIELD_NUMBER: builtins.int
    POLICY_FIELD_NUMBER: builtins.int
    CAST_FIELD_NUMBER: builtins.int
    MATERIALIZED_VIEW_FIELD_NUMBER: builtins.int
    sequence: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Sequences

    CREATE SEQUENCE ...
    """

    sequence_owned_by: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Owned sequences

    CREATE SEQUENCE ... OWNED BY ...
    """

    table: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Tables

    CREATE TABLE ...
    """

    primary_key: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Primary keys

    ALTER TABLE ... ADD PRIMARY KEY ...
    """

    fk_constraint: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Foreign keys

    ALTER TABLE ... ADD FOREIGN KEY ...
    """

    default_values: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Default values

    ALTER TABLE ... ALTER COLUMN ... SET DEFAULT ...
    """

    constraint: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Constraints

    ALTER TABLE ... ADD CONSTRAINT ...
    """

    index: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Indexes

    CREATE INDEX ...
    """

    view: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Views

    CREATE VIEW ...
    """

    function: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Functions

    CREATE FUNCTION ...
    """

    trigger: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Triggers

    CREATE TRIGGER ...
    """

    type: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Types

    CREATE TYPE ...
    """

    rule: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Rules

    CREATE RULE ...
    """

    collation: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Collations

    CREATE COLLATION ...
    """

    policy: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Policies

    CREATE POLICY ...
    """

    cast: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Casts

    CREATE CAST ...
    """

    materialized_view: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType
    """Materialized views

    CREATE MATERIALIZED VIEW ...
    """

    def __init__(self,
        *,
        sequence: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        sequence_owned_by: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        table: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        primary_key: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        fk_constraint: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        default_values: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        constraint: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        index: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        view: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        function: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        trigger: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        type: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        rule: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        collation: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        policy: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        cast: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        materialized_view: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ObjectTransferStage.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cast",b"cast","collation",b"collation","constraint",b"constraint","default_values",b"default_values","fk_constraint",b"fk_constraint","function",b"function","index",b"index","materialized_view",b"materialized_view","policy",b"policy","primary_key",b"primary_key","rule",b"rule","sequence",b"sequence","sequence_owned_by",b"sequence_owned_by","table",b"table","trigger",b"trigger","type",b"type","view",b"view"]) -> None: ...
global___PostgresObjectTransferSettings = PostgresObjectTransferSettings

class OnPremisePostgres(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HOSTS_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    TLS_MODE_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    @property
    def hosts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    port: builtins.int
    """Database port

    Will be used if the cluster ID is not specified. Default: 6432.
    """

    @property
    def tls_mode(self) -> yandex.cloud.datatransfer.v1.endpoint.common_pb2.TLSMode:
        """TLS mode

        TLS settings for server connection. Disabled by default.
        """
        pass
    subnet_id: typing.Text
    """Network interface for endpoint

    Default: public IPv4.
    """

    def __init__(self,
        *,
        hosts: typing.Optional[typing.Iterable[typing.Text]] = ...,
        port: builtins.int = ...,
        tls_mode: typing.Optional[yandex.cloud.datatransfer.v1.endpoint.common_pb2.TLSMode] = ...,
        subnet_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tls_mode",b"tls_mode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hosts",b"hosts","port",b"port","subnet_id",b"subnet_id","tls_mode",b"tls_mode"]) -> None: ...
global___OnPremisePostgres = OnPremisePostgres

class PostgresConnection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MDB_CLUSTER_ID_FIELD_NUMBER: builtins.int
    ON_PREMISE_FIELD_NUMBER: builtins.int
    mdb_cluster_id: typing.Text
    """Managed cluster

    Yandex.Cloud Managed PostgreSQL cluster ID
    """

    @property
    def on_premise(self) -> global___OnPremisePostgres:
        """On-premise

        Connection options for on-premise PostgreSQL
        """
        pass
    def __init__(self,
        *,
        mdb_cluster_id: typing.Text = ...,
        on_premise: typing.Optional[global___OnPremisePostgres] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connection",b"connection","mdb_cluster_id",b"mdb_cluster_id","on_premise",b"on_premise"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connection",b"connection","mdb_cluster_id",b"mdb_cluster_id","on_premise",b"on_premise"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["connection",b"connection"]) -> typing.Optional[typing_extensions.Literal["mdb_cluster_id","on_premise"]]: ...
global___PostgresConnection = PostgresConnection

class PostgresSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONNECTION_FIELD_NUMBER: builtins.int
    SECURITY_GROUPS_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    INCLUDE_TABLES_FIELD_NUMBER: builtins.int
    EXCLUDE_TABLES_FIELD_NUMBER: builtins.int
    SLOT_BYTE_LAG_LIMIT_FIELD_NUMBER: builtins.int
    SERVICE_SCHEMA_FIELD_NUMBER: builtins.int
    OBJECT_TRANSFER_SETTINGS_FIELD_NUMBER: builtins.int
    @property
    def connection(self) -> global___PostgresConnection:
        """Connection settings

        Database connection settings
        """
        pass
    @property
    def security_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Security groups"""
        pass
    database: typing.Text
    """Database name"""

    user: typing.Text
    """Username

    User for database access.
    """

    @property
    def password(self) -> yandex.cloud.datatransfer.v1.endpoint.common_pb2.Secret:
        """Password

        Password for database access.
        """
        pass
    @property
    def include_tables(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Included tables

        If none or empty list is presented, all tables are replicated. Full table name
        with schema. Can contain schema_name.* patterns.
        """
        pass
    @property
    def exclude_tables(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Excluded tables

        If none or empty list is presented, all tables are replicated. Full table name
        with schema. Can contain schema_name.* patterns.
        """
        pass
    slot_byte_lag_limit: builtins.int
    """Maximum WAL size for the replication slot

    Maximum WAL size held by the replication slot. Exceeding this limit will result
    in a replication failure and deletion of the replication slot. Unlimited by
    default.
    """

    service_schema: typing.Text
    """Database schema for service tables

    Default: public. Here created technical tables (__consumer_keeper,
    __data_transfer_mole_finder).
    """

    @property
    def object_transfer_settings(self) -> global___PostgresObjectTransferSettings:
        """Schema migration

        Select database objects to be transferred during activation or deactivation.
        """
        pass
    def __init__(self,
        *,
        connection: typing.Optional[global___PostgresConnection] = ...,
        security_groups: typing.Optional[typing.Iterable[typing.Text]] = ...,
        database: typing.Text = ...,
        user: typing.Text = ...,
        password: typing.Optional[yandex.cloud.datatransfer.v1.endpoint.common_pb2.Secret] = ...,
        include_tables: typing.Optional[typing.Iterable[typing.Text]] = ...,
        exclude_tables: typing.Optional[typing.Iterable[typing.Text]] = ...,
        slot_byte_lag_limit: builtins.int = ...,
        service_schema: typing.Text = ...,
        object_transfer_settings: typing.Optional[global___PostgresObjectTransferSettings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connection",b"connection","object_transfer_settings",b"object_transfer_settings","password",b"password"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connection",b"connection","database",b"database","exclude_tables",b"exclude_tables","include_tables",b"include_tables","object_transfer_settings",b"object_transfer_settings","password",b"password","security_groups",b"security_groups","service_schema",b"service_schema","slot_byte_lag_limit",b"slot_byte_lag_limit","user",b"user"]) -> None: ...
global___PostgresSource = PostgresSource

class PostgresTarget(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONNECTION_FIELD_NUMBER: builtins.int
    SECURITY_GROUPS_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    CLEANUP_POLICY_FIELD_NUMBER: builtins.int
    @property
    def connection(self) -> global___PostgresConnection:
        """Connection settings

        Database connection settings
        """
        pass
    @property
    def security_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Security groups"""
        pass
    database: typing.Text
    """Database name"""

    user: typing.Text
    """Username

    User for database access.
    """

    @property
    def password(self) -> yandex.cloud.datatransfer.v1.endpoint.common_pb2.Secret:
        """Password

        Password for database access.
        """
        pass
    cleanup_policy: yandex.cloud.datatransfer.v1.endpoint.common_pb2.CleanupPolicy.ValueType
    """Cleanup policy

    Cleanup policy for activate, reactivate and reupload processes. Default is
    DISABLED.
    """

    def __init__(self,
        *,
        connection: typing.Optional[global___PostgresConnection] = ...,
        security_groups: typing.Optional[typing.Iterable[typing.Text]] = ...,
        database: typing.Text = ...,
        user: typing.Text = ...,
        password: typing.Optional[yandex.cloud.datatransfer.v1.endpoint.common_pb2.Secret] = ...,
        cleanup_policy: yandex.cloud.datatransfer.v1.endpoint.common_pb2.CleanupPolicy.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connection",b"connection","password",b"password"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cleanup_policy",b"cleanup_policy","connection",b"connection","database",b"database","password",b"password","security_groups",b"security_groups","user",b"user"]) -> None: ...
global___PostgresTarget = PostgresTarget
