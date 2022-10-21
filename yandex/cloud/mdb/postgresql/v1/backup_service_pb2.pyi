"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import yandex.cloud.mdb.postgresql.v1.backup_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetBackupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_ID_FIELD_NUMBER: builtins.int
    backup_id: builtins.str
    """ID of the backup to return information about.
    To get the backup ID, use a [ClusterService.ListBackups] request.
    """
    def __init__(
        self,
        *,
        backup_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_id", b"backup_id"]) -> None: ...

global___GetBackupRequest = GetBackupRequest

@typing_extensions.final
class ListBackupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list backups in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListBackupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token.  To get the next page of results, Set [page_token] to the [ListBackupsResponse.next_page_token]
    returned by the previous list request.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListBackupsRequest = ListBackupsRequest

@typing_extensions.final
class ListBackupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def backups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.postgresql.v1.backup_pb2.Backup]:
        """List of PostgreSQL Backup resources."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListBackupsRequest.page_size], use the [next_page_token] as the value
    for the [ListBackupsRequest.page_token] parameter in the next list request. Each subsequent
    list request will have its own [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        backups: collections.abc.Iterable[yandex.cloud.mdb.postgresql.v1.backup_pb2.Backup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backups", b"backups", "next_page_token", b"next_page_token"]) -> None: ...

global___ListBackupsResponse = ListBackupsResponse

@typing_extensions.final
class DeleteBackupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_ID_FIELD_NUMBER: builtins.int
    backup_id: builtins.str
    """Required. ID of the backup to delete."""
    def __init__(
        self,
        *,
        backup_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_id", b"backup_id"]) -> None: ...

global___DeleteBackupRequest = DeleteBackupRequest

@typing_extensions.final
class DeleteBackupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_ID_FIELD_NUMBER: builtins.int
    backup_id: builtins.str
    """Required. ID of the PostgreSQL backup that is currently being deleted."""
    def __init__(
        self,
        *,
        backup_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_id", b"backup_id"]) -> None: ...

global___DeleteBackupMetadata = DeleteBackupMetadata
