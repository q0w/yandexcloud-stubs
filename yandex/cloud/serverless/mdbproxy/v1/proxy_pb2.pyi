"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Proxy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
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
    TARGET_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the proxy."""

    folder_id: typing.Text
    """ID of the folder that the proxy belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp for the proxy."""
        pass
    name: typing.Text
    """Name of the proxy."""

    description: typing.Text
    """Description of the proxy."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs."""
        pass
    @property
    def target(self) -> global___Target:
        """MDB specific settings."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        target: typing.Optional[global___Target] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","target",b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","description",b"description","folder_id",b"folder_id","id",b"id","labels",b"labels","name",b"name","target",b"target"]) -> None: ...
global___Proxy = Proxy

class Target(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class PostgreSQL(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CLUSTER_ID_FIELD_NUMBER: builtins.int
        USER_FIELD_NUMBER: builtins.int
        PASSWORD_FIELD_NUMBER: builtins.int
        DB_FIELD_NUMBER: builtins.int
        ENDPOINT_FIELD_NUMBER: builtins.int
        cluster_id: typing.Text
        """Cluster identifier for postgresql."""

        user: typing.Text
        """PostgreSQL user."""

        password: typing.Text
        """PostgreSQL password, input only field."""

        db: typing.Text
        """PostgreSQL database name."""

        endpoint: typing.Text
        """PostgreSQL proxy-host for connection, output only field."""

        def __init__(self,
            *,
            cluster_id: typing.Text = ...,
            user: typing.Text = ...,
            password: typing.Text = ...,
            db: typing.Text = ...,
            endpoint: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","db",b"db","endpoint",b"endpoint","password",b"password","user",b"user"]) -> None: ...

    class ClickHouse(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CLUSTER_ID_FIELD_NUMBER: builtins.int
        USER_FIELD_NUMBER: builtins.int
        PASSWORD_FIELD_NUMBER: builtins.int
        DB_FIELD_NUMBER: builtins.int
        ENDPOINT_FIELD_NUMBER: builtins.int
        cluster_id: typing.Text
        """Cluster identifier for clickhouse."""

        user: typing.Text
        """Clickhouse user."""

        password: typing.Text
        """Clickhouse password, input only field."""

        db: typing.Text
        """Clickhouse database name."""

        endpoint: typing.Text
        """Clickhouse proxy-host for connection, output only field."""

        def __init__(self,
            *,
            cluster_id: typing.Text = ...,
            user: typing.Text = ...,
            password: typing.Text = ...,
            db: typing.Text = ...,
            endpoint: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","db",b"db","endpoint",b"endpoint","password",b"password","user",b"user"]) -> None: ...

    CLICKHOUSE_FIELD_NUMBER: builtins.int
    POSTGRESQL_FIELD_NUMBER: builtins.int
    @property
    def clickhouse(self) -> global___Target.ClickHouse:
        """Clickhouse settings for proxy."""
        pass
    @property
    def postgresql(self) -> global___Target.PostgreSQL:
        """PostgreSQL settings for proxy."""
        pass
    def __init__(self,
        *,
        clickhouse: typing.Optional[global___Target.ClickHouse] = ...,
        postgresql: typing.Optional[global___Target.PostgreSQL] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["clickhouse",b"clickhouse","mdb",b"mdb","postgresql",b"postgresql"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["clickhouse",b"clickhouse","mdb",b"mdb","postgresql",b"postgresql"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["mdb",b"mdb"]) -> typing.Optional[typing_extensions.Literal["clickhouse","postgresql"]]: ...
global___Target = Target