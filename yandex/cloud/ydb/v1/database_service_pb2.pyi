"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.ydb.v1.backup_pb2
import yandex.cloud.ydb.v1.database_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RestoreBackupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BACKUP_ID_FIELD_NUMBER: builtins.int
    DATABASE_ID_FIELD_NUMBER: builtins.int
    PATHS_TO_RESTORE_FIELD_NUMBER: builtins.int
    TARGET_PATH_FIELD_NUMBER: builtins.int
    backup_id: typing.Text
    """Required. ID of the YDB backup."""

    database_id: typing.Text
    """Required. ID of the YDB database."""

    @property
    def paths_to_restore(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Specify paths to restore.
        If empty, all paths will restored by default.
        """
        pass
    target_path: typing.Text
    """Specify target path."""

    def __init__(self,
        *,
        backup_id: typing.Text = ...,
        database_id: typing.Text = ...,
        paths_to_restore: typing.Optional[typing.Iterable[typing.Text]] = ...,
        target_path: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_id",b"backup_id","database_id",b"database_id","paths_to_restore",b"paths_to_restore","target_path",b"target_path"]) -> None: ...
global___RestoreBackupRequest = RestoreBackupRequest

class RestoreBackupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BACKUP_ID_FIELD_NUMBER: builtins.int
    DATABASE_ID_FIELD_NUMBER: builtins.int
    backup_id: typing.Text
    database_id: typing.Text
    def __init__(self,
        *,
        backup_id: typing.Text = ...,
        database_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_id",b"backup_id","database_id",b"database_id"]) -> None: ...
global___RestoreBackupMetadata = RestoreBackupMetadata

class BackupDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    BACKUP_SETTINGS_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    @property
    def backup_settings(self) -> yandex.cloud.ydb.v1.backup_pb2.BackupSettings:
        """custom backup options, if required."""
        pass
    def __init__(self,
        *,
        database_id: typing.Text = ...,
        backup_settings: typing.Optional[yandex.cloud.ydb.v1.backup_pb2.BackupSettings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["backup_settings",b"backup_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_settings",b"backup_settings","database_id",b"database_id"]) -> None: ...
global___BackupDatabaseRequest = BackupDatabaseRequest

class BackupDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BACKUP_ID_FIELD_NUMBER: builtins.int
    DATABASE_ID_FIELD_NUMBER: builtins.int
    backup_id: typing.Text
    database_id: typing.Text
    def __init__(self,
        *,
        backup_id: typing.Text = ...,
        database_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_id",b"backup_id","database_id",b"database_id"]) -> None: ...
global___BackupDatabaseMetadata = BackupDatabaseMetadata

class StartDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    def __init__(self,
        *,
        database_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id"]) -> None: ...
global___StartDatabaseRequest = StartDatabaseRequest

class StartDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    database_name: typing.Text
    def __init__(self,
        *,
        database_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id","database_name",b"database_name"]) -> None: ...
global___StartDatabaseMetadata = StartDatabaseMetadata

class StopDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    def __init__(self,
        *,
        database_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id"]) -> None: ...
global___StopDatabaseRequest = StopDatabaseRequest

class StopDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    database_name: typing.Text
    def __init__(self,
        *,
        database_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id","database_name",b"database_name"]) -> None: ...
global___StopDatabaseMetadata = StopDatabaseMetadata

class GetDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    """Required. ID of the YDB cluster."""

    def __init__(self,
        *,
        database_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id"]) -> None: ...
global___GetDatabaseRequest = GetDatabaseRequest

class ListDatabasesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a `next_page_token` that can be used
    to get the next page of results in subsequent ListDatabases requests.
    Acceptable values are 0 to 1000, inclusive. Default value: 100.
    """

    page_token: typing.Text
    """Page token. Set `page_token` to the `next_page_token` returned by a previous ListDatabases
    request to get the next page of results.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListDatabasesRequest = ListDatabasesRequest

class ListDatabasesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def databases(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ydb.v1.database_pb2.Database]: ...
    next_page_token: typing.Text
    """This token allows you to get the next page of results for ListDatabases requests,
    if the number of results is larger than `page_size` specified in the request.
    To get the next page, specify the value of `next_page_token` as a value for
    the `page_token` parameter in the next ListDatabases request. Subsequent ListDatabases
    requests will have their own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        databases: typing.Optional[typing.Iterable[yandex.cloud.ydb.v1.database_pb2.Database]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["databases",b"databases","next_page_token",b"next_page_token"]) -> None: ...
global___ListDatabasesResponse = ListDatabasesResponse

class CreateDatabaseRequest(google.protobuf.message.Message):
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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    STORAGE_CONFIG_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    ZONAL_DATABASE_FIELD_NUMBER: builtins.int
    REGIONAL_DATABASE_FIELD_NUMBER: builtins.int
    DEDICATED_DATABASE_FIELD_NUMBER: builtins.int
    SERVERLESS_DATABASE_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BACKUP_CONFIG_FIELD_NUMBER: builtins.int
    MONITORING_CONFIG_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    name: typing.Text
    description: typing.Text
    resource_preset_id: typing.Text
    @property
    def storage_config(self) -> yandex.cloud.ydb.v1.database_pb2.StorageConfig: ...
    @property
    def scale_policy(self) -> yandex.cloud.ydb.v1.database_pb2.ScalePolicy: ...
    network_id: typing.Text
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def zonal_database(self) -> yandex.cloud.ydb.v1.database_pb2.ZonalDatabase:
        """deprecated field"""
        pass
    @property
    def regional_database(self) -> yandex.cloud.ydb.v1.database_pb2.RegionalDatabase:
        """deprecated field"""
        pass
    @property
    def dedicated_database(self) -> yandex.cloud.ydb.v1.database_pb2.DedicatedDatabase: ...
    @property
    def serverless_database(self) -> yandex.cloud.ydb.v1.database_pb2.ServerlessDatabase: ...
    assign_public_ips: builtins.bool
    location_id: typing.Text
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    @property
    def backup_config(self) -> yandex.cloud.ydb.v1.backup_pb2.BackupConfig: ...
    @property
    def monitoring_config(self) -> yandex.cloud.ydb.v1.database_pb2.MonitoringConfig: ...
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        resource_preset_id: typing.Text = ...,
        storage_config: typing.Optional[yandex.cloud.ydb.v1.database_pb2.StorageConfig] = ...,
        scale_policy: typing.Optional[yandex.cloud.ydb.v1.database_pb2.ScalePolicy] = ...,
        network_id: typing.Text = ...,
        subnet_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        zonal_database: typing.Optional[yandex.cloud.ydb.v1.database_pb2.ZonalDatabase] = ...,
        regional_database: typing.Optional[yandex.cloud.ydb.v1.database_pb2.RegionalDatabase] = ...,
        dedicated_database: typing.Optional[yandex.cloud.ydb.v1.database_pb2.DedicatedDatabase] = ...,
        serverless_database: typing.Optional[yandex.cloud.ydb.v1.database_pb2.ServerlessDatabase] = ...,
        assign_public_ips: builtins.bool = ...,
        location_id: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        backup_config: typing.Optional[yandex.cloud.ydb.v1.backup_pb2.BackupConfig] = ...,
        monitoring_config: typing.Optional[yandex.cloud.ydb.v1.database_pb2.MonitoringConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["backup_config",b"backup_config","database_type",b"database_type","dedicated_database",b"dedicated_database","monitoring_config",b"monitoring_config","regional_database",b"regional_database","scale_policy",b"scale_policy","serverless_database",b"serverless_database","storage_config",b"storage_config","zonal_database",b"zonal_database"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_public_ips",b"assign_public_ips","backup_config",b"backup_config","database_type",b"database_type","dedicated_database",b"dedicated_database","description",b"description","folder_id",b"folder_id","labels",b"labels","location_id",b"location_id","monitoring_config",b"monitoring_config","name",b"name","network_id",b"network_id","regional_database",b"regional_database","resource_preset_id",b"resource_preset_id","scale_policy",b"scale_policy","serverless_database",b"serverless_database","storage_config",b"storage_config","subnet_ids",b"subnet_ids","zonal_database",b"zonal_database"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["database_type",b"database_type"]) -> typing.Optional[typing_extensions.Literal["zonal_database","regional_database","dedicated_database","serverless_database"]]: ...
global___CreateDatabaseRequest = CreateDatabaseRequest

class CreateDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    """Required. ID of the YDB cluster."""

    database_name: typing.Text
    """Required. Name of the creating database."""

    def __init__(self,
        *,
        database_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id","database_name",b"database_name"]) -> None: ...
global___CreateDatabaseMetadata = CreateDatabaseMetadata

class UpdateDatabaseRequest(google.protobuf.message.Message):
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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    DATABASE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    STORAGE_CONFIG_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    ZONAL_DATABASE_FIELD_NUMBER: builtins.int
    REGIONAL_DATABASE_FIELD_NUMBER: builtins.int
    DEDICATED_DATABASE_FIELD_NUMBER: builtins.int
    SERVERLESS_DATABASE_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BACKUP_CONFIG_FIELD_NUMBER: builtins.int
    MONITORING_CONFIG_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    database_id: typing.Text
    name: typing.Text
    description: typing.Text
    resource_preset_id: typing.Text
    @property
    def storage_config(self) -> yandex.cloud.ydb.v1.database_pb2.StorageConfig: ...
    @property
    def scale_policy(self) -> yandex.cloud.ydb.v1.database_pb2.ScalePolicy: ...
    network_id: typing.Text
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def zonal_database(self) -> yandex.cloud.ydb.v1.database_pb2.ZonalDatabase: ...
    @property
    def regional_database(self) -> yandex.cloud.ydb.v1.database_pb2.RegionalDatabase: ...
    @property
    def dedicated_database(self) -> yandex.cloud.ydb.v1.database_pb2.DedicatedDatabase: ...
    @property
    def serverless_database(self) -> yandex.cloud.ydb.v1.database_pb2.ServerlessDatabase: ...
    assign_public_ips: builtins.bool
    location_id: typing.Text
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    @property
    def backup_config(self) -> yandex.cloud.ydb.v1.backup_pb2.BackupConfig: ...
    @property
    def monitoring_config(self) -> yandex.cloud.ydb.v1.database_pb2.MonitoringConfig: ...
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        database_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        resource_preset_id: typing.Text = ...,
        storage_config: typing.Optional[yandex.cloud.ydb.v1.database_pb2.StorageConfig] = ...,
        scale_policy: typing.Optional[yandex.cloud.ydb.v1.database_pb2.ScalePolicy] = ...,
        network_id: typing.Text = ...,
        subnet_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        zonal_database: typing.Optional[yandex.cloud.ydb.v1.database_pb2.ZonalDatabase] = ...,
        regional_database: typing.Optional[yandex.cloud.ydb.v1.database_pb2.RegionalDatabase] = ...,
        dedicated_database: typing.Optional[yandex.cloud.ydb.v1.database_pb2.DedicatedDatabase] = ...,
        serverless_database: typing.Optional[yandex.cloud.ydb.v1.database_pb2.ServerlessDatabase] = ...,
        assign_public_ips: builtins.bool = ...,
        location_id: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        backup_config: typing.Optional[yandex.cloud.ydb.v1.backup_pb2.BackupConfig] = ...,
        monitoring_config: typing.Optional[yandex.cloud.ydb.v1.database_pb2.MonitoringConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["backup_config",b"backup_config","database_type",b"database_type","dedicated_database",b"dedicated_database","monitoring_config",b"monitoring_config","regional_database",b"regional_database","scale_policy",b"scale_policy","serverless_database",b"serverless_database","storage_config",b"storage_config","update_mask",b"update_mask","zonal_database",b"zonal_database"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_public_ips",b"assign_public_ips","backup_config",b"backup_config","database_id",b"database_id","database_type",b"database_type","dedicated_database",b"dedicated_database","description",b"description","folder_id",b"folder_id","labels",b"labels","location_id",b"location_id","monitoring_config",b"monitoring_config","name",b"name","network_id",b"network_id","regional_database",b"regional_database","resource_preset_id",b"resource_preset_id","scale_policy",b"scale_policy","serverless_database",b"serverless_database","storage_config",b"storage_config","subnet_ids",b"subnet_ids","update_mask",b"update_mask","zonal_database",b"zonal_database"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["database_type",b"database_type"]) -> typing.Optional[typing_extensions.Literal["zonal_database","regional_database","dedicated_database","serverless_database"]]: ...
global___UpdateDatabaseRequest = UpdateDatabaseRequest

class UpdateDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    database_name: typing.Text
    def __init__(self,
        *,
        database_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id","database_name",b"database_name"]) -> None: ...
global___UpdateDatabaseMetadata = UpdateDatabaseMetadata

class DeleteDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    def __init__(self,
        *,
        database_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id"]) -> None: ...
global___DeleteDatabaseRequest = DeleteDatabaseRequest

class DeleteDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: typing.Text
    database_name: typing.Text
    def __init__(self,
        *,
        database_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_id",b"database_id","database_name",b"database_name"]) -> None: ...
global___DeleteDatabaseMetadata = DeleteDatabaseMetadata
