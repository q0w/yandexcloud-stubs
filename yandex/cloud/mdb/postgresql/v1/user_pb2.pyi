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

class User(google.protobuf.message.Message):
    """A PostgreSQL User resource. For more information, see
    the [Developer's Guide](/docs/managed-postgresql/concepts).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    CONN_LIMIT_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    LOGIN_FIELD_NUMBER: builtins.int
    GRANTS_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the PostgreSQL user."""

    cluster_id: typing.Text
    """ID of the PostgreSQL cluster the user belongs to."""

    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Permission]:
        """Set of permissions granted to the user to access specific databases."""
        pass
    conn_limit: builtins.int
    """Maximum number of database connections available to the user.

    When used in session pooling, this setting limits the number of connections to every single host in PostgreSQL cluster. In this case, the setting's value must be greater than the total number of connections that backend services can open to access the PostgreSQL cluster. The setting's value should not exceed the value of the [Cluster.config.postgresql_config_12.effective_config.max_connections] setting.

    When used in transaction pooling, this setting limits the number of user's active transactions; therefore, in this mode user can open thousands of connections, but only `N` concurrent connections will be opened, where `N` is the value of the setting.

    Minimum value: `10` (default: `50`), when used in session pooling.
    """

    @property
    def settings(self) -> global___UserSettings: ...
    @property
    def login(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """This flag defines whether the user can login to a PostgreSQL database.

        Default value: `true` (login is allowed).
        """
        pass
    @property
    def grants(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Roles and privileges that are granted to the user (`GRANT <role> TO <user>`).

        For more information, see [the documentation](/docs/managed-postgresql/operations/grant).
        """
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        cluster_id: typing.Text = ...,
        permissions: typing.Optional[typing.Iterable[global___Permission]] = ...,
        conn_limit: builtins.int = ...,
        settings: typing.Optional[global___UserSettings] = ...,
        login: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        grants: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["login",b"login","settings",b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","conn_limit",b"conn_limit","grants",b"grants","login",b"login","name",b"name","permissions",b"permissions","settings",b"settings"]) -> None: ...
global___User = User

class Permission(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_name: typing.Text
    """Name of the database that the permission grants access to."""

    def __init__(self,
        *,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_name",b"database_name"]) -> None: ...
global___Permission = Permission

class UserSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    CONN_LIMIT_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    LOGIN_FIELD_NUMBER: builtins.int
    GRANTS_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the PostgreSQL user."""

    password: typing.Text
    """Password of the PostgreSQL user."""

    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Permission]:
        """Set of permissions to grant to the user to access specific databases."""
        pass
    @property
    def conn_limit(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Maximum number of database connections that should be available to the user.

        When used in session pooling, this setting limits the number of connections to every single host in PostgreSQL cluster. In this case, the setting's value must be greater than the total number of connections that backend services can open to access the PostgreSQL cluster. The setting's value should not exceed the value of the [Cluster.config.postgresql_config_12.effective_config.max_connections] setting.

        When used in transaction pooling, this setting limits the number of user's active transactions; therefore, in this mode user can open thousands of connections, but only `N` concurrent connections will be opened, where `N` is the value of the setting.

        Minimum value: `10` (default: `50`), when used in session pooling.
        """
        pass
    @property
    def settings(self) -> global___UserSettings:
        """PostgreSQL settings for the user."""
        pass
    @property
    def login(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """This flag defines whether the user can login to a PostgreSQL database.

        Default value: `true` (login is allowed).
        """
        pass
    @property
    def grants(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Roles and privileges that are granted to the user (`GRANT <role> TO <user>`).

        For more information, see [the documentation](/docs/managed-postgresql/operations/grant).
        """
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        password: typing.Text = ...,
        permissions: typing.Optional[typing.Iterable[global___Permission]] = ...,
        conn_limit: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        settings: typing.Optional[global___UserSettings] = ...,
        login: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        grants: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["conn_limit",b"conn_limit","login",b"login","settings",b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["conn_limit",b"conn_limit","grants",b"grants","login",b"login","name",b"name","password",b"password","permissions",b"permissions","settings",b"settings"]) -> None: ...
global___UserSpec = UserSpec

class UserSettings(google.protobuf.message.Message):
    """PostgreSQL user settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _SynchronousCommit:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SynchronousCommitEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[UserSettings._SynchronousCommit.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SYNCHRONOUS_COMMIT_UNSPECIFIED: UserSettings._SynchronousCommit.ValueType  # 0
        SYNCHRONOUS_COMMIT_ON: UserSettings._SynchronousCommit.ValueType  # 1
        """(default value) success is reported to the client if the data is in WAL (Write-Ahead Log), and WAL is written to the storage of both the master and its synchronous standby server."""

        SYNCHRONOUS_COMMIT_OFF: UserSettings._SynchronousCommit.ValueType  # 2
        """success is reported to the client even if the data is not in WAL.
        There is no synchronous write operation, data may be loss in case of storage subsystem failure.
        """

        SYNCHRONOUS_COMMIT_LOCAL: UserSettings._SynchronousCommit.ValueType  # 3
        """success is reported to the client if the data is in WAL, and WAL is written to the storage of the master server.
        The transaction may be lost due to storage subsystem failure on the master server.
        """

        SYNCHRONOUS_COMMIT_REMOTE_WRITE: UserSettings._SynchronousCommit.ValueType  # 4
        """success is reported to the client if the data is in WAL, WAL is written to the storage of the master server, and the server's synchronous standby indicates that it has received WAL and written it out to its operating system.
        The transaction may be lost due to simultaneous storage subsystem failure on the master and operating system's failure on the synchronous standby.
        """

        SYNCHRONOUS_COMMIT_REMOTE_APPLY: UserSettings._SynchronousCommit.ValueType  # 5
        """success is reported to the client if the data is in WAL (Write-Ahead Log), WAL is written to the storage of the master server, and its synchronous standby indicates that it has received WAL and applied it.
        The transaction may be lost due to irrecoverably failure of both the master and its synchronous standby.
        """

    class SynchronousCommit(_SynchronousCommit, metaclass=_SynchronousCommitEnumTypeWrapper):
        pass

    SYNCHRONOUS_COMMIT_UNSPECIFIED: UserSettings.SynchronousCommit.ValueType  # 0
    SYNCHRONOUS_COMMIT_ON: UserSettings.SynchronousCommit.ValueType  # 1
    """(default value) success is reported to the client if the data is in WAL (Write-Ahead Log), and WAL is written to the storage of both the master and its synchronous standby server."""

    SYNCHRONOUS_COMMIT_OFF: UserSettings.SynchronousCommit.ValueType  # 2
    """success is reported to the client even if the data is not in WAL.
    There is no synchronous write operation, data may be loss in case of storage subsystem failure.
    """

    SYNCHRONOUS_COMMIT_LOCAL: UserSettings.SynchronousCommit.ValueType  # 3
    """success is reported to the client if the data is in WAL, and WAL is written to the storage of the master server.
    The transaction may be lost due to storage subsystem failure on the master server.
    """

    SYNCHRONOUS_COMMIT_REMOTE_WRITE: UserSettings.SynchronousCommit.ValueType  # 4
    """success is reported to the client if the data is in WAL, WAL is written to the storage of the master server, and the server's synchronous standby indicates that it has received WAL and written it out to its operating system.
    The transaction may be lost due to simultaneous storage subsystem failure on the master and operating system's failure on the synchronous standby.
    """

    SYNCHRONOUS_COMMIT_REMOTE_APPLY: UserSettings.SynchronousCommit.ValueType  # 5
    """success is reported to the client if the data is in WAL (Write-Ahead Log), WAL is written to the storage of the master server, and its synchronous standby indicates that it has received WAL and applied it.
    The transaction may be lost due to irrecoverably failure of both the master and its synchronous standby.
    """


    class _LogStatement:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _LogStatementEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[UserSettings._LogStatement.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        LOG_STATEMENT_UNSPECIFIED: UserSettings._LogStatement.ValueType  # 0
        LOG_STATEMENT_NONE: UserSettings._LogStatement.ValueType  # 1
        """(default) logs none of SQL statements."""

        LOG_STATEMENT_DDL: UserSettings._LogStatement.ValueType  # 2
        """logs all data definition statements (such as `CREATE`, `ALTER`, `DROP` and others)."""

        LOG_STATEMENT_MOD: UserSettings._LogStatement.ValueType  # 3
        """logs all statements that fall in the `LOG_STATEMENT_DDL` category plus data-modifying statements (such as `INSERT`, `UPDATE` and others)."""

        LOG_STATEMENT_ALL: UserSettings._LogStatement.ValueType  # 4
        """logs all SQL statements."""

    class LogStatement(_LogStatement, metaclass=_LogStatementEnumTypeWrapper):
        pass

    LOG_STATEMENT_UNSPECIFIED: UserSettings.LogStatement.ValueType  # 0
    LOG_STATEMENT_NONE: UserSettings.LogStatement.ValueType  # 1
    """(default) logs none of SQL statements."""

    LOG_STATEMENT_DDL: UserSettings.LogStatement.ValueType  # 2
    """logs all data definition statements (such as `CREATE`, `ALTER`, `DROP` and others)."""

    LOG_STATEMENT_MOD: UserSettings.LogStatement.ValueType  # 3
    """logs all statements that fall in the `LOG_STATEMENT_DDL` category plus data-modifying statements (such as `INSERT`, `UPDATE` and others)."""

    LOG_STATEMENT_ALL: UserSettings.LogStatement.ValueType  # 4
    """logs all SQL statements."""


    class _TransactionIsolation:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TransactionIsolationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[UserSettings._TransactionIsolation.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TRANSACTION_ISOLATION_UNSPECIFIED: UserSettings._TransactionIsolation.ValueType  # 0
        TRANSACTION_ISOLATION_READ_UNCOMMITTED: UserSettings._TransactionIsolation.ValueType  # 1
        """this level behaves like `TRANSACTION_ISOLATION_READ_COMMITTED` in PostgreSQL."""

        TRANSACTION_ISOLATION_READ_COMMITTED: UserSettings._TransactionIsolation.ValueType  # 2
        """(default) on this level query sees only data committed before the query began."""

        TRANSACTION_ISOLATION_REPEATABLE_READ: UserSettings._TransactionIsolation.ValueType  # 3
        """on this level all subsequent queries in a transaction will see the same rows, that were read by the first `SELECT` or `INSERT` query in this transaction, unchanged (these rows are locked during the first query)."""

        TRANSACTION_ISOLATION_SERIALIZABLE: UserSettings._TransactionIsolation.ValueType  # 4
        """this level provides the strictest transaction isolation.
        All queries in the current transaction see only the rows that were fixed prior to execution of the first `SELECT` or `INSERT` query in this transaction.
        If read and write operations in a concurrent set of serializable transactions overlap and this may cause an inconsistency that is not possible during the serial transaction execution, then one of the transaction will be rolled back, triggering a serialization failure.
        """

    class TransactionIsolation(_TransactionIsolation, metaclass=_TransactionIsolationEnumTypeWrapper):
        pass

    TRANSACTION_ISOLATION_UNSPECIFIED: UserSettings.TransactionIsolation.ValueType  # 0
    TRANSACTION_ISOLATION_READ_UNCOMMITTED: UserSettings.TransactionIsolation.ValueType  # 1
    """this level behaves like `TRANSACTION_ISOLATION_READ_COMMITTED` in PostgreSQL."""

    TRANSACTION_ISOLATION_READ_COMMITTED: UserSettings.TransactionIsolation.ValueType  # 2
    """(default) on this level query sees only data committed before the query began."""

    TRANSACTION_ISOLATION_REPEATABLE_READ: UserSettings.TransactionIsolation.ValueType  # 3
    """on this level all subsequent queries in a transaction will see the same rows, that were read by the first `SELECT` or `INSERT` query in this transaction, unchanged (these rows are locked during the first query)."""

    TRANSACTION_ISOLATION_SERIALIZABLE: UserSettings.TransactionIsolation.ValueType  # 4
    """this level provides the strictest transaction isolation.
    All queries in the current transaction see only the rows that were fixed prior to execution of the first `SELECT` or `INSERT` query in this transaction.
    If read and write operations in a concurrent set of serializable transactions overlap and this may cause an inconsistency that is not possible during the serial transaction execution, then one of the transaction will be rolled back, triggering a serialization failure.
    """


    DEFAULT_TRANSACTION_ISOLATION_FIELD_NUMBER: builtins.int
    LOCK_TIMEOUT_FIELD_NUMBER: builtins.int
    LOG_MIN_DURATION_STATEMENT_FIELD_NUMBER: builtins.int
    SYNCHRONOUS_COMMIT_FIELD_NUMBER: builtins.int
    TEMP_FILE_LIMIT_FIELD_NUMBER: builtins.int
    LOG_STATEMENT_FIELD_NUMBER: builtins.int
    default_transaction_isolation: global___UserSettings.TransactionIsolation.ValueType
    """SQL sets an isolation level for each transaction.
    This setting defines the default isolation level to be set for all new SQL transactions.

    See in-depth description in [PostgreSQL documentation](https://www.postgresql.org/docs/current/transaction-iso.html).
    """

    @property
    def lock_timeout(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum time (in milliseconds) for any statement to wait for acquiring a lock on an table, index, row or other database object.
        If the wait time is longer than the specified amount, then this statement is aborted.

        Default value: `0` (no control is enforced, a statement waiting time is unlimited).
        """
        pass
    @property
    def log_min_duration_statement(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """This setting controls logging of the duration of statements.

        The duration of each completed statement will be logged if the statement ran for at least the specified amount of time (in milliseconds).
        E.g., if this setting's value is set to `500`, a statement that took 300 milliseconds to complete will not be logged; on the other hand, the one that took 2000 milliseconds to complete, will be logged.

        Value of `0` forces PostgreSQL to log the duration of all statements.

        Value of `-1` (default) disables logging of the duration of statements.

        See in-depth description in [PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-logging.html).
        """
        pass
    synchronous_commit: global___UserSettings.SynchronousCommit.ValueType
    """This setting defines whether DBMS will commit transaction in a synchronous way.

    When synchronization is enabled, cluster waits for the synchronous operations to be completed prior to reporting `success` to the client.
    These operations guarantee different levels of the data safety and visibility in the cluster.

    See in-depth description in [PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-SYNCHRONOUS-COMMIT).
    """

    @property
    def temp_file_limit(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum storage space size (in kilobytes) that a single process can use to create temporary files.
        If a transaction exceeds this limit during execution, it will be aborted.

        A huge query may not fit into a server's RAM, therefore PostgreSQL will use some storage to store and execute such a query. Too big queries can make excessive use of the storage system, effectively making other quieries to run slow. This setting prevents execution of a big queries that can influence other queries by limiting size of temporary files.
        """
        pass
    log_statement: global___UserSettings.LogStatement.ValueType
    """This setting specifies which SQL statements should be logged (on the user level).

    See in-depth description in [PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-logging.html).
    """

    def __init__(self,
        *,
        default_transaction_isolation: global___UserSettings.TransactionIsolation.ValueType = ...,
        lock_timeout: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        log_min_duration_statement: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        synchronous_commit: global___UserSettings.SynchronousCommit.ValueType = ...,
        temp_file_limit: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        log_statement: global___UserSettings.LogStatement.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["lock_timeout",b"lock_timeout","log_min_duration_statement",b"log_min_duration_statement","temp_file_limit",b"temp_file_limit"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_transaction_isolation",b"default_transaction_isolation","lock_timeout",b"lock_timeout","log_min_duration_statement",b"log_min_duration_statement","log_statement",b"log_statement","synchronous_commit",b"synchronous_commit","temp_file_limit",b"temp_file_limit"]) -> None: ...
global___UserSettings = UserSettings
