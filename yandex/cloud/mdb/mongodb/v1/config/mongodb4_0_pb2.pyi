"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MongodConfig4_0(google.protobuf.message.Message):
    """Configuration of a mongod daemon. Supported options are a limited subset of all
    options described in [MongoDB documentation](https://docs.mongodb.com/v4.0/reference/configuration-options/).
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
                    pass
                def __init__(self,
                    *,
                    cache_size_gb: typing.Optional[google.protobuf.wrappers_pb2.DoubleValue] = ...,
                    ) -> None: ...
                def HasField(self, field_name: typing_extensions.Literal["cache_size_gb",b"cache_size_gb"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing_extensions.Literal["cache_size_gb",b"cache_size_gb"]) -> None: ...

            class CollectionConfig(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor
                class _Compressor:
                    ValueType = typing.NewType('ValueType', builtins.int)
                    V: typing_extensions.TypeAlias = ValueType
                class _CompressorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongodConfig4_0.Storage.WiredTiger.CollectionConfig._Compressor.ValueType], builtins.type):
                    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
                    COMPRESSOR_UNSPECIFIED: MongodConfig4_0.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 0
                    NONE: MongodConfig4_0.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 1
                    """No compression."""

                    SNAPPY: MongodConfig4_0.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 2
                    """The [Snappy](https://docs.mongodb.com/v4.0/reference/glossary/#term-snappy) compression."""

                    ZLIB: MongodConfig4_0.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 3
                    """The [zlib](https://docs.mongodb.com/v4.0/reference/glossary/#term-zlib) compression."""

                class Compressor(_Compressor, metaclass=_CompressorEnumTypeWrapper):
                    pass

                COMPRESSOR_UNSPECIFIED: MongodConfig4_0.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 0
                NONE: MongodConfig4_0.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 1
                """No compression."""

                SNAPPY: MongodConfig4_0.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 2
                """The [Snappy](https://docs.mongodb.com/v4.0/reference/glossary/#term-snappy) compression."""

                ZLIB: MongodConfig4_0.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 3
                """The [zlib](https://docs.mongodb.com/v4.0/reference/glossary/#term-zlib) compression."""


                BLOCK_COMPRESSOR_FIELD_NUMBER: builtins.int
                block_compressor: global___MongodConfig4_0.Storage.WiredTiger.CollectionConfig.Compressor.ValueType
                """Default type of compression to use for collection data."""

                def __init__(self,
                    *,
                    block_compressor: global___MongodConfig4_0.Storage.WiredTiger.CollectionConfig.Compressor.ValueType = ...,
                    ) -> None: ...
                def ClearField(self, field_name: typing_extensions.Literal["block_compressor",b"block_compressor"]) -> None: ...

            ENGINE_CONFIG_FIELD_NUMBER: builtins.int
            COLLECTION_CONFIG_FIELD_NUMBER: builtins.int
            @property
            def engine_config(self) -> global___MongodConfig4_0.Storage.WiredTiger.EngineConfig:
                """Engine configuration for WiredTiger."""
                pass
            @property
            def collection_config(self) -> global___MongodConfig4_0.Storage.WiredTiger.CollectionConfig:
                """Collection configuration for WiredTiger."""
                pass
            def __init__(self,
                *,
                engine_config: typing.Optional[global___MongodConfig4_0.Storage.WiredTiger.EngineConfig] = ...,
                collection_config: typing.Optional[global___MongodConfig4_0.Storage.WiredTiger.CollectionConfig] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["collection_config",b"collection_config","engine_config",b"engine_config"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["collection_config",b"collection_config","engine_config",b"engine_config"]) -> None: ...

        class Journal(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            COMMIT_INTERVAL_FIELD_NUMBER: builtins.int
            @property
            def commit_interval(self) -> google.protobuf.wrappers_pb2.Int64Value:
                """Commit interval between journal operations, in milliseconds.
                Default: 100.
                """
                pass
            def __init__(self,
                *,
                commit_interval: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["commit_interval",b"commit_interval"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["commit_interval",b"commit_interval"]) -> None: ...

        WIRED_TIGER_FIELD_NUMBER: builtins.int
        JOURNAL_FIELD_NUMBER: builtins.int
        @property
        def wired_tiger(self) -> global___MongodConfig4_0.Storage.WiredTiger:
            """Configuration of the WiredTiger storage engine."""
            pass
        @property
        def journal(self) -> global___MongodConfig4_0.Storage.Journal:
            """Configuration of the MongoDB [journal](https://docs.mongodb.com/v4.0/reference/glossary/#term-journal)."""
            pass
        def __init__(self,
            *,
            wired_tiger: typing.Optional[global___MongodConfig4_0.Storage.WiredTiger] = ...,
            journal: typing.Optional[global___MongodConfig4_0.Storage.Journal] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["journal",b"journal","wired_tiger",b"wired_tiger"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["journal",b"journal","wired_tiger",b"wired_tiger"]) -> None: ...

    class OperationProfiling(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _Mode:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongodConfig4_0.OperationProfiling._Mode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            MODE_UNSPECIFIED: MongodConfig4_0.OperationProfiling._Mode.ValueType  # 0
            OFF: MongodConfig4_0.OperationProfiling._Mode.ValueType  # 1
            """The profiler is off and does not collect any data."""

            SLOW_OP: MongodConfig4_0.OperationProfiling._Mode.ValueType  # 2
            """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""

            ALL: MongodConfig4_0.OperationProfiling._Mode.ValueType  # 3
            """The profiler collects data for all operations."""

        class Mode(_Mode, metaclass=_ModeEnumTypeWrapper):
            pass

        MODE_UNSPECIFIED: MongodConfig4_0.OperationProfiling.Mode.ValueType  # 0
        OFF: MongodConfig4_0.OperationProfiling.Mode.ValueType  # 1
        """The profiler is off and does not collect any data."""

        SLOW_OP: MongodConfig4_0.OperationProfiling.Mode.ValueType  # 2
        """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""

        ALL: MongodConfig4_0.OperationProfiling.Mode.ValueType  # 3
        """The profiler collects data for all operations."""


        MODE_FIELD_NUMBER: builtins.int
        SLOW_OP_THRESHOLD_FIELD_NUMBER: builtins.int
        mode: global___MongodConfig4_0.OperationProfiling.Mode.ValueType
        """Mode which specifies operations that should be profiled."""

        @property
        def slow_op_threshold(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The slow operation time threshold, in milliseconds. Operations that run
            for longer than this threshold are considered slow, and are processed by the profiler
            running in the SLOW_OP mode.
            """
            pass
        def __init__(self,
            *,
            mode: global___MongodConfig4_0.OperationProfiling.Mode.ValueType = ...,
            slow_op_threshold: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["slow_op_threshold",b"slow_op_threshold"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["mode",b"mode","slow_op_threshold",b"slow_op_threshold"]) -> None: ...

    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of simultaneous connections that mongod will accept."""
            pass
        def __init__(self,
            *,
            max_incoming_connections: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["max_incoming_connections",b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["max_incoming_connections",b"max_incoming_connections"]) -> None: ...

    STORAGE_FIELD_NUMBER: builtins.int
    OPERATION_PROFILING_FIELD_NUMBER: builtins.int
    NET_FIELD_NUMBER: builtins.int
    @property
    def storage(self) -> global___MongodConfig4_0.Storage:
        """`storage` section of mongod configuration."""
        pass
    @property
    def operation_profiling(self) -> global___MongodConfig4_0.OperationProfiling:
        """`operationProfiling` section of mongod configuration."""
        pass
    @property
    def net(self) -> global___MongodConfig4_0.Network:
        """`net` section of mongod configuration."""
        pass
    def __init__(self,
        *,
        storage: typing.Optional[global___MongodConfig4_0.Storage] = ...,
        operation_profiling: typing.Optional[global___MongodConfig4_0.OperationProfiling] = ...,
        net: typing.Optional[global___MongodConfig4_0.Network] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["net",b"net","operation_profiling",b"operation_profiling","storage",b"storage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["net",b"net","operation_profiling",b"operation_profiling","storage",b"storage"]) -> None: ...
global___MongodConfig4_0 = MongodConfig4_0

class MongoCfgConfig4_0(google.protobuf.message.Message):
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
                    pass
                def __init__(self,
                    *,
                    cache_size_gb: typing.Optional[google.protobuf.wrappers_pb2.DoubleValue] = ...,
                    ) -> None: ...
                def HasField(self, field_name: typing_extensions.Literal["cache_size_gb",b"cache_size_gb"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing_extensions.Literal["cache_size_gb",b"cache_size_gb"]) -> None: ...

            ENGINE_CONFIG_FIELD_NUMBER: builtins.int
            @property
            def engine_config(self) -> global___MongoCfgConfig4_0.Storage.WiredTiger.EngineConfig:
                """Engine configuration for WiredTiger."""
                pass
            def __init__(self,
                *,
                engine_config: typing.Optional[global___MongoCfgConfig4_0.Storage.WiredTiger.EngineConfig] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["engine_config",b"engine_config"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["engine_config",b"engine_config"]) -> None: ...

        WIRED_TIGER_FIELD_NUMBER: builtins.int
        @property
        def wired_tiger(self) -> global___MongoCfgConfig4_0.Storage.WiredTiger:
            """Configuration of the WiredTiger storage engine."""
            pass
        def __init__(self,
            *,
            wired_tiger: typing.Optional[global___MongoCfgConfig4_0.Storage.WiredTiger] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["wired_tiger",b"wired_tiger"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["wired_tiger",b"wired_tiger"]) -> None: ...

    class OperationProfiling(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _Mode:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongoCfgConfig4_0.OperationProfiling._Mode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            MODE_UNSPECIFIED: MongoCfgConfig4_0.OperationProfiling._Mode.ValueType  # 0
            OFF: MongoCfgConfig4_0.OperationProfiling._Mode.ValueType  # 1
            """The profiler is off and does not collect any data."""

            SLOW_OP: MongoCfgConfig4_0.OperationProfiling._Mode.ValueType  # 2
            """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""

            ALL: MongoCfgConfig4_0.OperationProfiling._Mode.ValueType  # 3
            """The profiler collects data for all operations."""

        class Mode(_Mode, metaclass=_ModeEnumTypeWrapper):
            pass

        MODE_UNSPECIFIED: MongoCfgConfig4_0.OperationProfiling.Mode.ValueType  # 0
        OFF: MongoCfgConfig4_0.OperationProfiling.Mode.ValueType  # 1
        """The profiler is off and does not collect any data."""

        SLOW_OP: MongoCfgConfig4_0.OperationProfiling.Mode.ValueType  # 2
        """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""

        ALL: MongoCfgConfig4_0.OperationProfiling.Mode.ValueType  # 3
        """The profiler collects data for all operations."""


        MODE_FIELD_NUMBER: builtins.int
        SLOW_OP_THRESHOLD_FIELD_NUMBER: builtins.int
        mode: global___MongoCfgConfig4_0.OperationProfiling.Mode.ValueType
        """Mode which specifies operations that should be profiled."""

        @property
        def slow_op_threshold(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The slow operation time threshold, in milliseconds. Operations that run
            for longer than this threshold are considered slow, and are processed by the profiler
            running in the SLOW_OP mode. For details see [MongoDB documentation](https://docs.mongodb.com/v4.0/reference/configuration-options/#operationProfiling.slowOpThresholdMs).
            """
            pass
        def __init__(self,
            *,
            mode: global___MongoCfgConfig4_0.OperationProfiling.Mode.ValueType = ...,
            slow_op_threshold: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["slow_op_threshold",b"slow_op_threshold"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["mode",b"mode","slow_op_threshold",b"slow_op_threshold"]) -> None: ...

    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of simultaneous connections that mongocfg will accept."""
            pass
        def __init__(self,
            *,
            max_incoming_connections: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["max_incoming_connections",b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["max_incoming_connections",b"max_incoming_connections"]) -> None: ...

    STORAGE_FIELD_NUMBER: builtins.int
    OPERATION_PROFILING_FIELD_NUMBER: builtins.int
    NET_FIELD_NUMBER: builtins.int
    @property
    def storage(self) -> global___MongoCfgConfig4_0.Storage:
        """`storage` section of mongocfg configuration."""
        pass
    @property
    def operation_profiling(self) -> global___MongoCfgConfig4_0.OperationProfiling:
        """`operationProfiling` section of mongocfg configuration."""
        pass
    @property
    def net(self) -> global___MongoCfgConfig4_0.Network:
        """`net` section of mongocfg configuration."""
        pass
    def __init__(self,
        *,
        storage: typing.Optional[global___MongoCfgConfig4_0.Storage] = ...,
        operation_profiling: typing.Optional[global___MongoCfgConfig4_0.OperationProfiling] = ...,
        net: typing.Optional[global___MongoCfgConfig4_0.Network] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["net",b"net","operation_profiling",b"operation_profiling","storage",b"storage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["net",b"net","operation_profiling",b"operation_profiling","storage",b"storage"]) -> None: ...
global___MongoCfgConfig4_0 = MongoCfgConfig4_0

class MongosConfig4_0(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of simultaneous connections that mongos will accept."""
            pass
        def __init__(self,
            *,
            max_incoming_connections: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["max_incoming_connections",b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["max_incoming_connections",b"max_incoming_connections"]) -> None: ...

    NET_FIELD_NUMBER: builtins.int
    @property
    def net(self) -> global___MongosConfig4_0.Network:
        """Network settings for mongos."""
        pass
    def __init__(self,
        *,
        net: typing.Optional[global___MongosConfig4_0.Network] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["net",b"net"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["net",b"net"]) -> None: ...
global___MongosConfig4_0 = MongosConfig4_0

class MongodConfigSet4_0(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongodConfig4_0:
        """Effective mongod settings for a MongoDB 4.0 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """
        pass
    @property
    def user_config(self) -> global___MongodConfig4_0:
        """User-defined mongod settings for a MongoDB 4.0 cluster."""
        pass
    @property
    def default_config(self) -> global___MongodConfig4_0:
        """Default mongod configuration for a MongoDB 4.0 cluster."""
        pass
    def __init__(self,
        *,
        effective_config: typing.Optional[global___MongodConfig4_0] = ...,
        user_config: typing.Optional[global___MongodConfig4_0] = ...,
        default_config: typing.Optional[global___MongodConfig4_0] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config",b"default_config","effective_config",b"effective_config","user_config",b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config",b"default_config","effective_config",b"effective_config","user_config",b"user_config"]) -> None: ...
global___MongodConfigSet4_0 = MongodConfigSet4_0

class MongoCfgConfigSet4_0(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongoCfgConfig4_0:
        """Effective mongocfg settings for a MongoDB 4.0 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """
        pass
    @property
    def user_config(self) -> global___MongoCfgConfig4_0:
        """User-defined mongocfg settings for a MongoDB 4.0 cluster."""
        pass
    @property
    def default_config(self) -> global___MongoCfgConfig4_0:
        """Default mongocfg configuration for a MongoDB 4.0 cluster."""
        pass
    def __init__(self,
        *,
        effective_config: typing.Optional[global___MongoCfgConfig4_0] = ...,
        user_config: typing.Optional[global___MongoCfgConfig4_0] = ...,
        default_config: typing.Optional[global___MongoCfgConfig4_0] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config",b"default_config","effective_config",b"effective_config","user_config",b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config",b"default_config","effective_config",b"effective_config","user_config",b"user_config"]) -> None: ...
global___MongoCfgConfigSet4_0 = MongoCfgConfigSet4_0

class MongosConfigSet4_0(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongosConfig4_0:
        """Effective mongos settings for a MongoDB 4.0 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """
        pass
    @property
    def user_config(self) -> global___MongosConfig4_0:
        """User-defined mongos settings for a MongoDB 4.0 cluster."""
        pass
    @property
    def default_config(self) -> global___MongosConfig4_0:
        """Default mongos configuration for a MongoDB 4.0 cluster."""
        pass
    def __init__(self,
        *,
        effective_config: typing.Optional[global___MongosConfig4_0] = ...,
        user_config: typing.Optional[global___MongosConfig4_0] = ...,
        default_config: typing.Optional[global___MongosConfig4_0] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_config",b"default_config","effective_config",b"effective_config","user_config",b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_config",b"default_config","effective_config",b"effective_config","user_config",b"user_config"]) -> None: ...
global___MongosConfigSet4_0 = MongosConfigSet4_0