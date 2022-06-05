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
import yandex.cloud.mdb.mysql.v1.backup_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetBackupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BACKUP_ID_FIELD_NUMBER: builtins.int
    backup_id: typing.Text
    """ID of the backup to return information about.

    To get this ID, make a [BackupService.List] request (lists all backups in a folder) or a [ClusterService.ListBackups] request (lists all backups for an existing cluster).
    """

    def __init__(self,
        *,
        backup_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_id",b"backup_id"]) -> None: ...
global___GetBackupRequest = GetBackupRequest

class ListBackupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list backups in.

    To get this ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the API returns a [ListBackupsResponse.next_page_token] that can be used to get the next page of results in the subsequent [BackupService.List] requests.
    """

    page_token: typing.Text
    """Page token that can be used to iterate through multiple pages of results.

    To get the next page of results, set [page_token] to the [ListBackupsResponse.next_page_token] returned by the previous [BackupService.List] request.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListBackupsRequest = ListBackupsRequest

class ListBackupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BACKUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def backups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.mysql.v1.backup_pb2.Backup]:
        """List of backups."""
        pass
    next_page_token: typing.Text
    """The token that can be used to get the next page of results.

    If the number of results is larger than [ListBackupsRequest.page_size], use the [next_page_token] as the value for the [ListBackupsRequest.page_token] in the subsequent [BackupService.List] request to iterate through multiple pages of results.

    Each of the subsequent [BackupService.List] requests should use the [next_page_token] value returned by the previous request to continue paging through the results.
    """

    def __init__(self,
        *,
        backups: typing.Optional[typing.Iterable[yandex.cloud.mdb.mysql.v1.backup_pb2.Backup]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backups",b"backups","next_page_token",b"next_page_token"]) -> None: ...
global___ListBackupsResponse = ListBackupsResponse
