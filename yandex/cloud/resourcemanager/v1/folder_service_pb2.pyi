"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions
import yandex.cloud.operation.operation_pb2
import yandex.cloud.resourcemanager.v1.folder_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetFolderRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the Folder resource to return.
    To get the folder ID, use a [FolderService.List] request.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id"]) -> None: ...
global___GetFolderRequest = GetFolderRequest

class ListFoldersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLOUD_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    cloud_id: typing.Text
    """ID of the cloud to list folders in.
    To get the cloud ID, use a [yandex.cloud.resourcemanager.v1.CloudService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListFoldersResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. Set [page_token]
    to the [ListFoldersResponse.next_page_token]
    returned by a previous list request to get the next page of results.
    """

    filter: typing.Text
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [Folder.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """

    def __init__(self,
        *,
        cloud_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_id",b"cloud_id","filter",b"filter","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListFoldersRequest = ListFoldersRequest

class ListFoldersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def folders(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.resourcemanager.v1.folder_pb2.Folder]:
        """List of Folder resources."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListFoldersRequest.page_size], use
    the [next_page_token] as the value
    for the [ListFoldersRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        folders: typing.Optional[typing.Iterable[yandex.cloud.resourcemanager.v1.folder_pb2.Folder]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folders",b"folders","next_page_token",b"next_page_token"]) -> None: ...
global___ListFoldersResponse = ListFoldersResponse

class CreateFolderRequest(google.protobuf.message.Message):
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

    CLOUD_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    cloud_id: typing.Text
    """ID of the cloud to create a folder in.
    To get the cloud ID, use a [yandex.cloud.resourcemanager.v1.CloudService.List] request.
    """

    name: typing.Text
    """Name of the folder.
    The name must be unique within the cloud.
    """

    description: typing.Text
    """Description of the folder."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `` key:value `` pairs."""
        pass
    def __init__(self,
        *,
        cloud_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_id",b"cloud_id","description",b"description","labels",b"labels","name",b"name"]) -> None: ...
global___CreateFolderRequest = CreateFolderRequest

class CreateFolderMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder that is being created."""

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id"]) -> None: ...
global___CreateFolderMetadata = CreateFolderMetadata

class UpdateFolderRequest(google.protobuf.message.Message):
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
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the Folder resource to update.
    To get the folder ID, use a [FolderService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Folder resource are going to be updated."""
        pass
    name: typing.Text
    """Name of the folder.
    The name must be unique within the cloud.
    """

    description: typing.Text
    """Description of the folder."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `` key:value `` pairs."""
        pass
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","folder_id",b"folder_id","labels",b"labels","name",b"name","update_mask",b"update_mask"]) -> None: ...
global___UpdateFolderRequest = UpdateFolderRequest

class UpdateFolderMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the Folder resource that is being updated."""

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id"]) -> None: ...
global___UpdateFolderMetadata = UpdateFolderMetadata

class DeleteFolderRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    DELETE_AFTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to delete.
    To get the folder ID, use a [FolderService.List] request.
    """

    @property
    def delete_after(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp after which the process of deleting the folder should begin.
        Until this timestamp, the folder goes into the [Folder.Status.PENDING_DELETION] state and all resources in this
        folder are stopped. In this state, it is possible to cancel the delete operation without any loss.
        After this timestamp, the status of the folder will become [Folder.Status.DELETING] and the process of deleting
        all the resources  of the folder will be started. If [delete_after] is not specified it will be
        (now + 24 hours). To initiate an immediate deletion [delete_after] must be <= now.
        """
        pass
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        delete_after: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delete_after",b"delete_after"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delete_after",b"delete_after","folder_id",b"folder_id"]) -> None: ...
global___DeleteFolderRequest = DeleteFolderRequest

class DeleteFolderMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    DELETE_AFTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder that is being deleted."""

    @property
    def delete_after(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp after which the process of deleting the folder should begin."""
        pass
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        delete_after: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delete_after",b"delete_after"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delete_after",b"delete_after","folder_id",b"folder_id"]) -> None: ...
global___DeleteFolderMetadata = DeleteFolderMetadata

class ListFolderOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the Folder resource to list operations for."""

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListFolderOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. Set [page_token]
    to the [ListFolderOperationsResponse.next_page_token]
    returned by a previous list request to get the next page of results.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListFolderOperationsRequest = ListFolderOperationsRequest

class ListFolderOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified folder."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListFolderOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListFolderOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListFolderOperationsResponse = ListFolderOperationsResponse
