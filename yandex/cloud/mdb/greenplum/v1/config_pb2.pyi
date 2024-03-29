"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _LogStatement:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LogStatementEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LogStatement.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LOG_STATEMENT_UNSPECIFIED: _LogStatement.ValueType  # 0
    NONE: _LogStatement.ValueType  # 1
    """None statements are logged."""
    DDL: _LogStatement.ValueType  # 2
    """Logs all data definition commands like `CREATE`, `ALTER`, and `DROP`. Default value."""
    MOD: _LogStatement.ValueType  # 3
    """Logs all `DDL` statements, plus `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, and `COPY FROM`."""
    ALL: _LogStatement.ValueType  # 4
    """Logs all statements."""

class LogStatement(_LogStatement, metaclass=_LogStatementEnumTypeWrapper): ...

LOG_STATEMENT_UNSPECIFIED: LogStatement.ValueType  # 0
NONE: LogStatement.ValueType  # 1
"""None statements are logged."""
DDL: LogStatement.ValueType  # 2
"""Logs all data definition commands like `CREATE`, `ALTER`, and `DROP`. Default value."""
MOD: LogStatement.ValueType  # 3
"""Logs all `DDL` statements, plus `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, and `COPY FROM`."""
ALL: LogStatement.ValueType  # 4
"""Logs all statements."""
global___LogStatement = LogStatement

@typing_extensions.final
class Resources(google.protobuf.message.Message):
    """A list of computational resources allocated to a host."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    DISK_TYPE_ID_FIELD_NUMBER: builtins.int
    resource_preset_id: builtins.str
    """ID of the preset for computational resources allocated to a host.

    Available presets are listed in the [documentation](/docs/managed-greenplum/concepts/instance-types).
    """
    disk_size: builtins.int
    """Volume of the storage used by the host, in bytes."""
    disk_type_id: builtins.str
    """Type of the storage used by the host: `network-hdd`, `network-ssd` or `local-ssd`."""
    def __init__(
        self,
        *,
        resource_preset_id: builtins.str = ...,
        disk_size: builtins.int = ...,
        disk_type_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_size", b"disk_size", "disk_type_id", b"disk_type_id", "resource_preset_id", b"resource_preset_id"]) -> None: ...

global___Resources = Resources

@typing_extensions.final
class ConnectionPoolerConfig(google.protobuf.message.Message):
    """Route server configuration."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _PoolMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PoolModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ConnectionPoolerConfig._PoolMode.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        POOL_MODE_UNSPECIFIED: ConnectionPoolerConfig._PoolMode.ValueType  # 0
        SESSION: ConnectionPoolerConfig._PoolMode.ValueType  # 1
        """Assign server connection to a client until it disconnects. Default value."""
        TRANSACTION: ConnectionPoolerConfig._PoolMode.ValueType  # 2
        """Assign server connection to a client for a transaction processing."""

    class PoolMode(_PoolMode, metaclass=_PoolModeEnumTypeWrapper):
        """Route server pool mode."""

    POOL_MODE_UNSPECIFIED: ConnectionPoolerConfig.PoolMode.ValueType  # 0
    SESSION: ConnectionPoolerConfig.PoolMode.ValueType  # 1
    """Assign server connection to a client until it disconnects. Default value."""
    TRANSACTION: ConnectionPoolerConfig.PoolMode.ValueType  # 2
    """Assign server connection to a client for a transaction processing."""

    MODE_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    CLIENT_IDLE_TIMEOUT_FIELD_NUMBER: builtins.int
    mode: global___ConnectionPoolerConfig.PoolMode.ValueType
    """Route server pool mode."""
    @property
    def size(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of servers in the server pool. Clients are placed in a wait queue when all servers are busy.

        Set to zero to disable the limit.
        """
    @property
    def client_idle_timeout(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Server pool idle timeout, in seconds.

        A server connection closes after being idle for the specified time.

        Set to zero to disable the limit.
        """
    def __init__(
        self,
        *,
        mode: global___ConnectionPoolerConfig.PoolMode.ValueType = ...,
        size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        client_idle_timeout: google.protobuf.wrappers_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["client_idle_timeout", b"client_idle_timeout", "size", b"size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_idle_timeout", b"client_idle_timeout", "mode", b"mode", "size", b"size"]) -> None: ...

global___ConnectionPoolerConfig = ConnectionPoolerConfig

@typing_extensions.final
class MasterSubclusterConfig(google.protobuf.message.Message):
    """Configuration of the master subcluster."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCES_FIELD_NUMBER: builtins.int
    @property
    def resources(self) -> global___Resources:
        """Computational resources allocated to Greenplum® master subcluster hosts."""
    def __init__(
        self,
        *,
        resources: global___Resources | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resources", b"resources"]) -> None: ...

global___MasterSubclusterConfig = MasterSubclusterConfig

@typing_extensions.final
class SegmentSubclusterConfig(google.protobuf.message.Message):
    """Configuration of the segment subcluster."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCES_FIELD_NUMBER: builtins.int
    @property
    def resources(self) -> global___Resources:
        """Computational resources allocated to Greenplum® segment subcluster hosts."""
    def __init__(
        self,
        *,
        resources: global___Resources | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resources", b"resources"]) -> None: ...

global___SegmentSubclusterConfig = SegmentSubclusterConfig

@typing_extensions.final
class GreenplumConfig6_17(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_CONNECTIONS_FIELD_NUMBER: builtins.int
    MAX_SLOT_WAL_KEEP_SIZE_FIELD_NUMBER: builtins.int
    GP_WORKFILE_LIMIT_PER_SEGMENT_FIELD_NUMBER: builtins.int
    GP_WORKFILE_LIMIT_PER_QUERY_FIELD_NUMBER: builtins.int
    GP_WORKFILE_LIMIT_FILES_PER_QUERY_FIELD_NUMBER: builtins.int
    MAX_PREPARED_TRANSACTIONS_FIELD_NUMBER: builtins.int
    GP_WORKFILE_COMPRESSION_FIELD_NUMBER: builtins.int
    @property
    def max_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Maximum number of inbound connections on master segment."""
    @property
    def max_slot_wal_keep_size(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum size of WAL files that replication slots are allowed to retain in the `pg_wal` directory at checkpoint time.

        More info in [PostgreSQL® documentation](https://www.postgresql.org/docs/current/runtime-config-replication.html).
        """
    @property
    def gp_workfile_limit_per_segment(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum total disk size that all running queries are allowed to use for creating temporary spill files at each segment.

        The default value is 0 (no limit).

        More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#gp_workfile_limit_per_segment).
        """
    @property
    def gp_workfile_limit_per_query(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum disk size that an individual query is allowed to use for creating temporary spill files at each segment.

        The default value is 0 (no limit).

        More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#gp_workfile_limit_per_query).
        """
    @property
    def gp_workfile_limit_files_per_query(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum number of temporary spill files allowed per query at each segment.

        Spill files, also known as workfiles, are created when a query requires more memory than there is allocated.

        The current query is terminated if the limit is exceeded.

        Set to zero to disable the limit.

        Master session reloads if the parameter changes.

        Default value is 10000.

        More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#gp_workfile_limit_files_per_query).
        """
    @property
    def max_prepared_transactions(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum number of transactions that can be in the `prepared` state simultaneously.

        More info in [PostgreSQL® documentation](https://www.postgresql.org/docs/9.6/runtime-config-resource.html).
        """
    @property
    def gp_workfile_compression(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Whether the spill files are compressed or not.

        More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#gp_workfile_compression).
        """
    def __init__(
        self,
        *,
        max_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_slot_wal_keep_size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        gp_workfile_limit_per_segment: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        gp_workfile_limit_per_query: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        gp_workfile_limit_files_per_query: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_prepared_transactions: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        gp_workfile_compression: google.protobuf.wrappers_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gp_workfile_compression", b"gp_workfile_compression", "gp_workfile_limit_files_per_query", b"gp_workfile_limit_files_per_query", "gp_workfile_limit_per_query", b"gp_workfile_limit_per_query", "gp_workfile_limit_per_segment", b"gp_workfile_limit_per_segment", "max_connections", b"max_connections", "max_prepared_transactions", b"max_prepared_transactions", "max_slot_wal_keep_size", b"max_slot_wal_keep_size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gp_workfile_compression", b"gp_workfile_compression", "gp_workfile_limit_files_per_query", b"gp_workfile_limit_files_per_query", "gp_workfile_limit_per_query", b"gp_workfile_limit_per_query", "gp_workfile_limit_per_segment", b"gp_workfile_limit_per_segment", "max_connections", b"max_connections", "max_prepared_transactions", b"max_prepared_transactions", "max_slot_wal_keep_size", b"max_slot_wal_keep_size"]) -> None: ...

global___GreenplumConfig6_17 = GreenplumConfig6_17

@typing_extensions.final
class GreenplumConfig6_19(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_CONNECTIONS_FIELD_NUMBER: builtins.int
    MAX_SLOT_WAL_KEEP_SIZE_FIELD_NUMBER: builtins.int
    GP_WORKFILE_LIMIT_PER_SEGMENT_FIELD_NUMBER: builtins.int
    GP_WORKFILE_LIMIT_PER_QUERY_FIELD_NUMBER: builtins.int
    GP_WORKFILE_LIMIT_FILES_PER_QUERY_FIELD_NUMBER: builtins.int
    MAX_PREPARED_TRANSACTIONS_FIELD_NUMBER: builtins.int
    GP_WORKFILE_COMPRESSION_FIELD_NUMBER: builtins.int
    MAX_STATEMENT_MEM_FIELD_NUMBER: builtins.int
    LOG_STATEMENT_FIELD_NUMBER: builtins.int
    @property
    def max_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Maximum number of inbound connections on master segment."""
    @property
    def max_slot_wal_keep_size(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum size of WAL files that replication slots are allowed to retain in the `pg_wal` directory at checkpoint time.

        More info in [PostgreSQL® documentation](https://www.postgresql.org/docs/current/runtime-config-replication.html).
        """
    @property
    def gp_workfile_limit_per_segment(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum total disk size that all running queries are allowed to use for creating temporary spill files at each segment.

        The default value is 0 (no limit).

        More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#gp_workfile_limit_per_segment).
        """
    @property
    def gp_workfile_limit_per_query(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum disk size that an individual query is allowed to use for creating temporary spill files at each segment.

        The default value is 0 (no limit).

        More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#gp_workfile_limit_per_query).
        """
    @property
    def gp_workfile_limit_files_per_query(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum number of temporary spill files allowed per query at each segment.

        Spill files, also known as workfiles, are created when a query requires more memory than there is allocated.

        The current query is terminated if the limit is exceeded.

        Set to zero to disable the limit.

        Master session reloads if the parameter changes.

        Default value is 10000.

        More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#gp_workfile_limit_files_per_query).
        """
    @property
    def max_prepared_transactions(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum number of transactions that can be in the `prepared` state simultaneously.

        More info in [PostgreSQL® documentation](https://www.postgresql.org/docs/9.6/runtime-config-resource.html).
        """
    @property
    def gp_workfile_compression(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Whether the spill files are compressed or not.

        More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#gp_workfile_compression).
        """
    @property
    def max_statement_mem(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum memory limit for a query, in bytes.

        Helps to avoid out-of-memory errors on a segment host during query processing as a result of setting `statement_mem` too high.

        Taking into account the configuration of a single segment host, calculate [max_statement_mem] as follows: `seghost_physical_memory` / `average_number_concurrent_queries`.

        When changing both [max_statement_mem] and `statement_mem`, [max_statement_mem] must be changed first, or listed first in the `postgresql.conf` file.

        Default value is 2097152000 (2000 MB).

        More info in [Greenplum® documentation](https://greenplum.docs.pivotal.io/6-19/ref_guide/config_params/guc-list.html#max_statement_mem).
        in bytes
        """
    log_statement: global___LogStatement.ValueType
    """Logged SQL statements.

    `PREPARE` and `EXPLAIN ANALYZE` statements are also logged if their contained command belongs to an appropriate type.

    More info in [Greenplum® documentation](https://docs.greenplum.org/6-5/ref_guide/config_params/guc-list.html#log_statement).
    """
    def __init__(
        self,
        *,
        max_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_slot_wal_keep_size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        gp_workfile_limit_per_segment: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        gp_workfile_limit_per_query: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        gp_workfile_limit_files_per_query: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_prepared_transactions: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        gp_workfile_compression: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        max_statement_mem: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        log_statement: global___LogStatement.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gp_workfile_compression", b"gp_workfile_compression", "gp_workfile_limit_files_per_query", b"gp_workfile_limit_files_per_query", "gp_workfile_limit_per_query", b"gp_workfile_limit_per_query", "gp_workfile_limit_per_segment", b"gp_workfile_limit_per_segment", "max_connections", b"max_connections", "max_prepared_transactions", b"max_prepared_transactions", "max_slot_wal_keep_size", b"max_slot_wal_keep_size", "max_statement_mem", b"max_statement_mem"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gp_workfile_compression", b"gp_workfile_compression", "gp_workfile_limit_files_per_query", b"gp_workfile_limit_files_per_query", "gp_workfile_limit_per_query", b"gp_workfile_limit_per_query", "gp_workfile_limit_per_segment", b"gp_workfile_limit_per_segment", "log_statement", b"log_statement", "max_connections", b"max_connections", "max_prepared_transactions", b"max_prepared_transactions", "max_slot_wal_keep_size", b"max_slot_wal_keep_size", "max_statement_mem", b"max_statement_mem"]) -> None: ...

global___GreenplumConfig6_19 = GreenplumConfig6_19

@typing_extensions.final
class GreenplumConfigSet6_17(google.protobuf.message.Message):
    """Configuration settings version 6.17"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___GreenplumConfig6_17:
        """Effective settings for a Greenplum® cluster (a combination of settings defined in [GreenplumConfigSet6_17.user_config] and [GreenplumConfigSet6_17.default_config])."""
    @property
    def user_config(self) -> global___GreenplumConfig6_17:
        """User-defined settings for a Greenplum® cluster."""
    @property
    def default_config(self) -> global___GreenplumConfig6_17:
        """Default configuration for a Greenplum® cluster."""
    def __init__(
        self,
        *,
        effective_config: global___GreenplumConfig6_17 | None = ...,
        user_config: global___GreenplumConfig6_17 | None = ...,
        default_config: global___GreenplumConfig6_17 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___GreenplumConfigSet6_17 = GreenplumConfigSet6_17

@typing_extensions.final
class GreenplumConfigSet6_19(google.protobuf.message.Message):
    """Configuration settings version 6.19"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___GreenplumConfig6_19:
        """Effective settings for a Greenplum® cluster (a combination of settings defined in [GreenplumConfigSet6_19.user_config] and [GreenplumConfigSet6_19.default_config])."""
    @property
    def user_config(self) -> global___GreenplumConfig6_19:
        """User-defined settings for a Greenplum® cluster."""
    @property
    def default_config(self) -> global___GreenplumConfig6_19:
        """Default configuration for a Greenplum® cluster."""
    def __init__(
        self,
        *,
        effective_config: global___GreenplumConfig6_19 | None = ...,
        user_config: global___GreenplumConfig6_19 | None = ...,
        default_config: global___GreenplumConfig6_19 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___GreenplumConfigSet6_19 = GreenplumConfigSet6_19

@typing_extensions.final
class ConnectionPoolerConfigSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___ConnectionPoolerConfig:
        """Effective settings for an Odyssey® pooler (a combination of settings defined in [ConnectionPoolerConfigSet.user_config] and [ConnectionPoolerConfigSet.default_config])."""
    @property
    def user_config(self) -> global___ConnectionPoolerConfig:
        """User-defined settings for an Odyssey® pooler."""
    @property
    def default_config(self) -> global___ConnectionPoolerConfig:
        """Default configuration for an Odyssey® pooler."""
    def __init__(
        self,
        *,
        effective_config: global___ConnectionPoolerConfig | None = ...,
        user_config: global___ConnectionPoolerConfig | None = ...,
        default_config: global___ConnectionPoolerConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___ConnectionPoolerConfigSet = ConnectionPoolerConfigSet
