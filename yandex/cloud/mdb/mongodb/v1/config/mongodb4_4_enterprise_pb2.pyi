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

class MongodConfig4_4_enterprise(google.protobuf.message.Message):
    """Configuration of a mongod daemon. Supported options are a limited subset of all
    options described in [MongoDB documentation](https://docs.mongodb.com/v4.4/reference/configuration-options/).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Storage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class WiredTiger(google.protobuf.message.Message):
            """Configuration of WiredTiger storage engine."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            class EngineConfig(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                CACHE_SIZE_GB_FIELD_NUMBER: builtins.int
                @property
                def cache_size_gb(self) -> google.protobuf.wrappers_pb2.DoubleValue:
                    """The maximum size of the internal cache that WiredTiger will use for all data."""
                def __init__(
                    self,
                    *,
                    cache_size_gb: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
                ) -> None: ...
                def HasField(self, field_name: typing_extensions.Literal["cache_size_gb", b"cache_size_gb"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing_extensions.Literal["cache_size_gb", b"cache_size_gb"]) -> None: ...

            class CollectionConfig(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                class _Compressor:
                    ValueType = typing.NewType("ValueType", builtins.int)
                    V: typing_extensions.TypeAlias = ValueType

                class _CompressorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig._Compressor.ValueType], builtins.type):  # noqa: F821
                    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
                    COMPRESSOR_UNSPECIFIED: MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 0
                    NONE: MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 1
                    """No compression."""
                    SNAPPY: MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 2
                    """The [Snappy](https://docs.mongodb.com/v4.4/reference/glossary/#term-snappy) compression."""
                    ZLIB: MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 3
                    """The [zlib](https://docs.mongodb.com/v4.4/reference/glossary/#term-zlib) compression."""

                class Compressor(_Compressor, metaclass=_CompressorEnumTypeWrapper): ...
                COMPRESSOR_UNSPECIFIED: MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 0
                NONE: MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 1
                """No compression."""
                SNAPPY: MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 2
                """The [Snappy](https://docs.mongodb.com/v4.4/reference/glossary/#term-snappy) compression."""
                ZLIB: MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 3
                """The [zlib](https://docs.mongodb.com/v4.4/reference/glossary/#term-zlib) compression."""

                BLOCK_COMPRESSOR_FIELD_NUMBER: builtins.int
                block_compressor: global___MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig.Compressor.ValueType
                """Default type of compression to use for collection data."""
                def __init__(
                    self,
                    *,
                    block_compressor: global___MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig.Compressor.ValueType = ...,
                ) -> None: ...
                def ClearField(self, field_name: typing_extensions.Literal["block_compressor", b"block_compressor"]) -> None: ...

            ENGINE_CONFIG_FIELD_NUMBER: builtins.int
            COLLECTION_CONFIG_FIELD_NUMBER: builtins.int
            @property
            def engine_config(self) -> global___MongodConfig4_4_enterprise.Storage.WiredTiger.EngineConfig:
                """Engine configuration for WiredTiger."""
            @property
            def collection_config(self) -> global___MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig:
                """Collection configuration for WiredTiger."""
            def __init__(
                self,
                *,
                engine_config: global___MongodConfig4_4_enterprise.Storage.WiredTiger.EngineConfig | None = ...,
                collection_config: global___MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["collection_config", b"collection_config", "engine_config", b"engine_config"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["collection_config", b"collection_config", "engine_config", b"engine_config"]) -> None: ...

        class Journal(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            COMMIT_INTERVAL_FIELD_NUMBER: builtins.int
            @property
            def commit_interval(self) -> google.protobuf.wrappers_pb2.Int64Value:
                """Commit interval between journal operations, in milliseconds.
                Default: 100.
                """
            def __init__(
                self,
                *,
                commit_interval: google.protobuf.wrappers_pb2.Int64Value | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["commit_interval", b"commit_interval"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["commit_interval", b"commit_interval"]) -> None: ...

        WIRED_TIGER_FIELD_NUMBER: builtins.int
        JOURNAL_FIELD_NUMBER: builtins.int
        @property
        def wired_tiger(self) -> global___MongodConfig4_4_enterprise.Storage.WiredTiger:
            """Configuration of the WiredTiger storage engine."""
        @property
        def journal(self) -> global___MongodConfig4_4_enterprise.Storage.Journal:
            """Configuration of the MongoDB [journal](https://docs.mongodb.com/v4.4/reference/glossary/#term-journal)."""
        def __init__(
            self,
            *,
            wired_tiger: global___MongodConfig4_4_enterprise.Storage.WiredTiger | None = ...,
            journal: global___MongodConfig4_4_enterprise.Storage.Journal | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["journal", b"journal", "wired_tiger", b"wired_tiger"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["journal", b"journal", "wired_tiger", b"wired_tiger"]) -> None: ...

    class OperationProfiling(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Mode:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongodConfig4_4_enterprise.OperationProfiling._Mode.ValueType], builtins.type):  # noqa: F821
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            MODE_UNSPECIFIED: MongodConfig4_4_enterprise.OperationProfiling._Mode.ValueType  # 0
            OFF: MongodConfig4_4_enterprise.OperationProfiling._Mode.ValueType  # 1
            """The profiler is off and does not collect any data."""
            SLOW_OP: MongodConfig4_4_enterprise.OperationProfiling._Mode.ValueType  # 2
            """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""
            ALL: MongodConfig4_4_enterprise.OperationProfiling._Mode.ValueType  # 3
            """The profiler collects data for all operations."""

        class Mode(_Mode, metaclass=_ModeEnumTypeWrapper): ...
        MODE_UNSPECIFIED: MongodConfig4_4_enterprise.OperationProfiling.Mode.ValueType  # 0
        OFF: MongodConfig4_4_enterprise.OperationProfiling.Mode.ValueType  # 1
        """The profiler is off and does not collect any data."""
        SLOW_OP: MongodConfig4_4_enterprise.OperationProfiling.Mode.ValueType  # 2
        """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""
        ALL: MongodConfig4_4_enterprise.OperationProfiling.Mode.ValueType  # 3
        """The profiler collects data for all operations."""

        MODE_FIELD_NUMBER: builtins.int
        SLOW_OP_THRESHOLD_FIELD_NUMBER: builtins.int
        mode: global___MongodConfig4_4_enterprise.OperationProfiling.Mode.ValueType
        """Mode which specifies operations that should be profiled."""
        @property
        def slow_op_threshold(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The slow operation time threshold, in milliseconds. Operations that run
            for longer than this threshold are considered slow, and are processed by the profiler
            running in the SLOW_OP mode.
            """
        def __init__(
            self,
            *,
            mode: global___MongodConfig4_4_enterprise.OperationProfiling.Mode.ValueType = ...,
            slow_op_threshold: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["slow_op_threshold", b"slow_op_threshold"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["mode", b"mode", "slow_op_threshold", b"slow_op_threshold"]) -> None: ...

    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of simultaneous connections that mongod will accept."""
        def __init__(
            self,
            *,
            max_incoming_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["max_incoming_connections", b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["max_incoming_connections", b"max_incoming_connections"]) -> None: ...

    class Security(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class KMIP(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            SERVER_NAME_FIELD_NUMBER: builtins.int
            PORT_FIELD_NUMBER: builtins.int
            SERVER_CA_FIELD_NUMBER: builtins.int
            CLIENT_CERTIFICATE_FIELD_NUMBER: builtins.int
            KEY_IDENTIFIER_FIELD_NUMBER: builtins.int
            server_name: builtins.str
            """KMIP server name"""
            @property
            def port(self) -> google.protobuf.wrappers_pb2.Int64Value:
                """KMIP server port"""
            server_ca: builtins.str
            """KMIP Server CA"""
            client_certificate: builtins.str
            """KMIP client certificate + private key (unencrypted)"""
            key_identifier: builtins.str
            """KMIP Key identifier (if any)"""
            def __init__(
                self,
                *,
                server_name: builtins.str = ...,
                port: google.protobuf.wrappers_pb2.Int64Value | None = ...,
                server_ca: builtins.str = ...,
                client_certificate: builtins.str = ...,
                key_identifier: builtins.str = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["port", b"port"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["client_certificate", b"client_certificate", "key_identifier", b"key_identifier", "port", b"port", "server_ca", b"server_ca", "server_name", b"server_name"]) -> None: ...

        ENABLE_ENCRYPTION_FIELD_NUMBER: builtins.int
        KMIP_FIELD_NUMBER: builtins.int
        @property
        def enable_encryption(self) -> google.protobuf.wrappers_pb2.BoolValue:
            """If encryption at rest should be enabled or not"""
        @property
        def kmip(self) -> global___MongodConfig4_4_enterprise.Security.KMIP:
            """`kmip` section of mongod security config"""
        def __init__(
            self,
            *,
            enable_encryption: google.protobuf.wrappers_pb2.BoolValue | None = ...,
            kmip: global___MongodConfig4_4_enterprise.Security.KMIP | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["enable_encryption", b"enable_encryption", "kmip", b"kmip"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["enable_encryption", b"enable_encryption", "kmip", b"kmip"]) -> None: ...

    class AuditLog(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FILTER_FIELD_NUMBER: builtins.int
        filter: builtins.str
        """Audit filter"""
        def __init__(
            self,
            *,
            filter: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> None: ...

    class SetParameter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        AUDIT_AUTHORIZATION_SUCCESS_FIELD_NUMBER: builtins.int
        @property
        def audit_authorization_success(self) -> google.protobuf.wrappers_pb2.BoolValue:
            """Enables the auditing of authorization successes"""
        def __init__(
            self,
            *,
            audit_authorization_success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["audit_authorization_success", b"audit_authorization_success"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["audit_authorization_success", b"audit_authorization_success"]) -> None: ...

    STORAGE_FIELD_NUMBER: builtins.int
    OPERATION_PROFILING_FIELD_NUMBER: builtins.int
    NET_FIELD_NUMBER: builtins.int
    SECURITY_FIELD_NUMBER: builtins.int
    AUDIT_LOG_FIELD_NUMBER: builtins.int
    SET_PARAMETER_FIELD_NUMBER: builtins.int
    @property
    def storage(self) -> global___MongodConfig4_4_enterprise.Storage:
        """`storage` section of mongod configuration."""
    @property
    def operation_profiling(self) -> global___MongodConfig4_4_enterprise.OperationProfiling:
        """`operationProfiling` section of mongod configuration."""
    @property
    def net(self) -> global___MongodConfig4_4_enterprise.Network:
        """`net` section of mongod configuration."""
    @property
    def security(self) -> global___MongodConfig4_4_enterprise.Security:
        """`security` section of mongod configuration."""
    @property
    def audit_log(self) -> global___MongodConfig4_4_enterprise.AuditLog:
        """`AuditLog` section of mongod configuration."""
    @property
    def set_parameter(self) -> global___MongodConfig4_4_enterprise.SetParameter:
        """`SetParameter` section of mongod configuration."""
    def __init__(
        self,
        *,
        storage: global___MongodConfig4_4_enterprise.Storage | None = ...,
        operation_profiling: global___MongodConfig4_4_enterprise.OperationProfiling | None = ...,
        net: global___MongodConfig4_4_enterprise.Network | None = ...,
        security: global___MongodConfig4_4_enterprise.Security | None = ...,
        audit_log: global___MongodConfig4_4_enterprise.AuditLog | None = ...,
        set_parameter: global___MongodConfig4_4_enterprise.SetParameter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["audit_log", b"audit_log", "net", b"net", "operation_profiling", b"operation_profiling", "security", b"security", "set_parameter", b"set_parameter", "storage", b"storage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["audit_log", b"audit_log", "net", b"net", "operation_profiling", b"operation_profiling", "security", b"security", "set_parameter", b"set_parameter", "storage", b"storage"]) -> None: ...

global___MongodConfig4_4_enterprise = MongodConfig4_4_enterprise

class MongoCfgConfig4_4_enterprise(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Storage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class WiredTiger(google.protobuf.message.Message):
            """Configuration of WiredTiger storage engine."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            class EngineConfig(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                CACHE_SIZE_GB_FIELD_NUMBER: builtins.int
                @property
                def cache_size_gb(self) -> google.protobuf.wrappers_pb2.DoubleValue:
                    """The maximum size of the internal cache that WiredTiger will use for all data."""
                def __init__(
                    self,
                    *,
                    cache_size_gb: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
                ) -> None: ...
                def HasField(self, field_name: typing_extensions.Literal["cache_size_gb", b"cache_size_gb"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing_extensions.Literal["cache_size_gb", b"cache_size_gb"]) -> None: ...

            ENGINE_CONFIG_FIELD_NUMBER: builtins.int
            @property
            def engine_config(self) -> global___MongoCfgConfig4_4_enterprise.Storage.WiredTiger.EngineConfig:
                """Engine configuration for WiredTiger."""
            def __init__(
                self,
                *,
                engine_config: global___MongoCfgConfig4_4_enterprise.Storage.WiredTiger.EngineConfig | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["engine_config", b"engine_config"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["engine_config", b"engine_config"]) -> None: ...

        WIRED_TIGER_FIELD_NUMBER: builtins.int
        @property
        def wired_tiger(self) -> global___MongoCfgConfig4_4_enterprise.Storage.WiredTiger:
            """Configuration of the WiredTiger storage engine."""
        def __init__(
            self,
            *,
            wired_tiger: global___MongoCfgConfig4_4_enterprise.Storage.WiredTiger | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["wired_tiger", b"wired_tiger"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["wired_tiger", b"wired_tiger"]) -> None: ...

    class OperationProfiling(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Mode:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongoCfgConfig4_4_enterprise.OperationProfiling._Mode.ValueType], builtins.type):  # noqa: F821
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            MODE_UNSPECIFIED: MongoCfgConfig4_4_enterprise.OperationProfiling._Mode.ValueType  # 0
            OFF: MongoCfgConfig4_4_enterprise.OperationProfiling._Mode.ValueType  # 1
            """The profiler is off and does not collect any data."""
            SLOW_OP: MongoCfgConfig4_4_enterprise.OperationProfiling._Mode.ValueType  # 2
            """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""
            ALL: MongoCfgConfig4_4_enterprise.OperationProfiling._Mode.ValueType  # 3
            """The profiler collects data for all operations."""

        class Mode(_Mode, metaclass=_ModeEnumTypeWrapper): ...
        MODE_UNSPECIFIED: MongoCfgConfig4_4_enterprise.OperationProfiling.Mode.ValueType  # 0
        OFF: MongoCfgConfig4_4_enterprise.OperationProfiling.Mode.ValueType  # 1
        """The profiler is off and does not collect any data."""
        SLOW_OP: MongoCfgConfig4_4_enterprise.OperationProfiling.Mode.ValueType  # 2
        """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""
        ALL: MongoCfgConfig4_4_enterprise.OperationProfiling.Mode.ValueType  # 3
        """The profiler collects data for all operations."""

        MODE_FIELD_NUMBER: builtins.int
        SLOW_OP_THRESHOLD_FIELD_NUMBER: builtins.int
        mode: global___MongoCfgConfig4_4_enterprise.OperationProfiling.Mode.ValueType
        """Mode which specifies operations that should be profiled."""
        @property
        def slow_op_threshold(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The slow operation time threshold, in milliseconds. Operations that run
            for longer than this threshold are considered slow, and are processed by the profiler
            running in the SLOW_OP mode. For details see [MongoDB documentation](https://docs.mongodb.com/v4.4/reference/configuration-options/#operationProfiling.slowOpThresholdMs).
            """
        def __init__(
            self,
            *,
            mode: global___MongoCfgConfig4_4_enterprise.OperationProfiling.Mode.ValueType = ...,
            slow_op_threshold: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["slow_op_threshold", b"slow_op_threshold"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["mode", b"mode", "slow_op_threshold", b"slow_op_threshold"]) -> None: ...

    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of simultaneous connections that mongocfg will accept."""
        def __init__(
            self,
            *,
            max_incoming_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["max_incoming_connections", b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["max_incoming_connections", b"max_incoming_connections"]) -> None: ...

    STORAGE_FIELD_NUMBER: builtins.int
    OPERATION_PROFILING_FIELD_NUMBER: builtins.int
    NET_FIELD_NUMBER: builtins.int
    @property
    def storage(self) -> global___MongoCfgConfig4_4_enterprise.Storage:
        """`storage` section of mongocfg configuration."""
    @property
    def operation_profiling(self) -> global___MongoCfgConfig4_4_enterprise.OperationProfiling:
        """`operationProfiling` section of mongocfg configuration."""
    @property
    def net(self) -> global___MongoCfgConfig4_4_enterprise.Network:
        """`net` section of mongocfg configuration."""
    def __init__(
        self,
        *,
        storage: global___MongoCfgConfig4_4_enterprise.Storage | None = ...,
        operation_profiling: global___MongoCfgConfig4_4_enterprise.OperationProfiling | None = ...,
        net: global___MongoCfgConfig4_4_enterprise.Network | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["net", b"net", "operation_profiling", b"operation_profiling", "storage", b"storage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["net", b"net", "operation_profiling", b"operation_profiling", "storage", b"storage"]) -> None: ...

global___MongoCfgConfig4_4_enterprise = MongoCfgConfig4_4_enterprise

class MongosConfig4_4_enterprise(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of simultaneous connections that mongos will accept."""
        def __init__(
            self,
            *,
            max_incoming_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["max_incoming_connections", b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["max_incoming_connections", b"max_incoming_connections"]) -> None: ...

    NET_FIELD_NUMBER: builtins.int
    @property
    def net(self) -> global___MongosConfig4_4_enterprise.Network:
        """Network settings for mongos."""
    def __init__(
        self,
        *,
        net: global___MongosConfig4_4_enterprise.Network | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["net", b"net"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["net", b"net"]) -> None: ...

global___MongosConfig4_4_enterprise = MongosConfig4_4_enterprise

class MongodConfigSet4_4_enterprise(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongodConfig4_4_enterprise:
        """Effective mongod settings for a MongoDB 4.4 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """
    @property
    def user_config(self) -> global___MongodConfig4_4_enterprise:
        """User-defined mongod settings for a MongoDB 4.4 cluster."""
    @property
    def default_config(self) -> global___MongodConfig4_4_enterprise:
        """Default mongod configuration for a MongoDB 4.4 cluster."""
    def __init__(
        self,
        *,
        effective_config: global___MongodConfig4_4_enterprise | None = ...,
        user_config: global___MongodConfig4_4_enterprise | None = ...,
        default_config: global___MongodConfig4_4_enterprise | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___MongodConfigSet4_4_enterprise = MongodConfigSet4_4_enterprise

class MongoCfgConfigSet4_4_enterprise(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongoCfgConfig4_4_enterprise:
        """Effective mongocfg settings for a MongoDB 4.4 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """
    @property
    def user_config(self) -> global___MongoCfgConfig4_4_enterprise:
        """User-defined mongocfg settings for a MongoDB 4.4 cluster."""
    @property
    def default_config(self) -> global___MongoCfgConfig4_4_enterprise:
        """Default mongocfg configuration for a MongoDB 4.4 cluster."""
    def __init__(
        self,
        *,
        effective_config: global___MongoCfgConfig4_4_enterprise | None = ...,
        user_config: global___MongoCfgConfig4_4_enterprise | None = ...,
        default_config: global___MongoCfgConfig4_4_enterprise | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___MongoCfgConfigSet4_4_enterprise = MongoCfgConfigSet4_4_enterprise

class MongosConfigSet4_4_enterprise(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongosConfig4_4_enterprise:
        """Effective mongos settings for a MongoDB 4.4 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """
    @property
    def user_config(self) -> global___MongosConfig4_4_enterprise:
        """User-defined mongos settings for a MongoDB 4.4 cluster."""
    @property
    def default_config(self) -> global___MongosConfig4_4_enterprise:
        """Default mongos configuration for a MongoDB 4.4 cluster."""
    def __init__(
        self,
        *,
        effective_config: global___MongosConfig4_4_enterprise | None = ...,
        user_config: global___MongosConfig4_4_enterprise | None = ...,
        default_config: global___MongosConfig4_4_enterprise | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___MongosConfigSet4_4_enterprise = MongosConfigSet4_4_enterprise
