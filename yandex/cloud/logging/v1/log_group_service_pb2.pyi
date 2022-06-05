"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.logging.v1.log_group_pb2
import yandex.cloud.logging.v1.log_resource_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetLogGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group to return.

    To get a log group ID make a [LogGroupService.List] request.
    """

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_group_id",b"log_group_id"]) -> None: ...
global___GetLogGroupRequest = GetLogGroupRequest

class GetLogGroupStatsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group to return stats for.

    To get a log group ID make a [LogGroupService.List] request.
    """

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_group_id",b"log_group_id"]) -> None: ...
global___GetLogGroupStatsRequest = GetLogGroupStatsRequest

class ListLogGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """Folder ID of the log groups to return.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListLogGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.

    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set `page_token` to the
    [ListLogGroupsResponse.next_page_token] returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters log groups listed in the response.

    The expression must specify:
    1. The field name. Currently filtering can only be applied to the [LogGroup.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    Example of a filter: `name=my-log-group`.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListLogGroupsRequest = ListLogGroupsRequest

class ListLogGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.logging.v1.log_group_pb2.LogGroup]:
        """List of log groups in the specified folder."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListLogGroupsRequest.page_size], use `next_page_token` as the value
    for the [ListLogGroupsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        groups: typing.Optional[typing.Iterable[yandex.cloud.logging.v1.log_group_pb2.LogGroup]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["groups",b"groups","next_page_token",b"next_page_token"]) -> None: ...
global___ListLogGroupsResponse = ListLogGroupsResponse

class CreateLogGroupRequest(google.protobuf.message.Message):
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
    LABELS_FIELD_NUMBER: builtins.int
    RETENTION_PERIOD_FIELD_NUMBER: builtins.int
    DATA_STREAM_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to create a log group in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    name: typing.Text
    """Name of the log group.
    The name must be unique within the folder.
    """

    description: typing.Text
    """Description of the log group."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Log group labels as `key:value` pairs."""
        pass
    @property
    def retention_period(self) -> google.protobuf.duration_pb2.Duration:
        """Log group entry retention period.

        Entries will be present in group during this period.
        If specified, must be non-negative.
        Empty or zero value is treated as no limit.
        Data stream name
        """
        pass
    data_stream: typing.Text
    """If specified, all log records will be written to this data stream"""

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        retention_period: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        data_stream: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["retention_period",b"retention_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_stream",b"data_stream","description",b"description","folder_id",b"folder_id","labels",b"labels","name",b"name","retention_period",b"retention_period"]) -> None: ...
global___CreateLogGroupRequest = CreateLogGroupRequest

class CreateLogGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group being created."""

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_group_id",b"log_group_id"]) -> None: ...
global___CreateLogGroupMetadata = CreateLogGroupMetadata

class UpdateLogGroupRequest(google.protobuf.message.Message):
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

    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    RETENTION_PERIOD_FIELD_NUMBER: builtins.int
    DATA_STREAM_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group to update.

    To get a log group ID make a [LogGroupService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the function should be updated."""
        pass
    name: typing.Text
    """New name of the log group.
    The name must be unique within the folder.
    """

    description: typing.Text
    """New Description of the log group."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """New log group labels as `key:value` pairs."""
        pass
    @property
    def retention_period(self) -> google.protobuf.duration_pb2.Duration:
        """New log group entry retention period.

        Entries will be present in group during this period.
        If specified, must be non-negative.
        Empty or zero value is treated as no limit.
        """
        pass
    data_stream: typing.Text
    """Data stream name

    If specified, log records will be written to this data stream
    """

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        retention_period: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        data_stream: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["retention_period",b"retention_period","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_stream",b"data_stream","description",b"description","labels",b"labels","log_group_id",b"log_group_id","name",b"name","retention_period",b"retention_period","update_mask",b"update_mask"]) -> None: ...
global___UpdateLogGroupRequest = UpdateLogGroupRequest

class UpdateLogGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group being updated."""

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_group_id",b"log_group_id"]) -> None: ...
global___UpdateLogGroupMetadata = UpdateLogGroupMetadata

class DeleteLogGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group to delete.

    To get a log group ID make a [LogGroupService.List] request.
    """

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_group_id",b"log_group_id"]) -> None: ...
global___DeleteLogGroupRequest = DeleteLogGroupRequest

class DeleteLogGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group being deleted."""

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_group_id",b"log_group_id"]) -> None: ...
global___DeleteLogGroupMetadata = DeleteLogGroupMetadata

class ListResourcesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group to list resources for.

    To get a log group ID make a [LogGroupService.List] request.
    """

    type: typing.Text
    """Resource type to return resources for.

    If not specified, [ListResourcesResponse] will contain information about all resource types.
    """

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        type: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_group_id",b"log_group_id","type",b"type"]) -> None: ...
global___ListResourcesRequest = ListResourcesRequest

class ListResourcesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCES_FIELD_NUMBER: builtins.int
    @property
    def resources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.logging.v1.log_resource_pb2.LogGroupResource]:
        """List of resources present in log group."""
        pass
    def __init__(self,
        *,
        resources: typing.Optional[typing.Iterable[yandex.cloud.logging.v1.log_resource_pb2.LogGroupResource]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resources",b"resources"]) -> None: ...
global___ListResourcesResponse = ListResourcesResponse

class ListOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group to list operations for.

    To get a log group ID make a [LogGroupService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.

    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set `page_token` to the
    [ListOperationsResponse.next_page_token] returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters resources listed in the response.

    The expression must specify:
    1. The field name. Currently filtering can be applied to the [operation.Operation.description], [operation.Operation.created_at], [operation.Operation.modified_at], [operation.Operation.created_by], [operation.Operation.done] fields.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    Examples of a filter: `done=false`, `created_by='John.Doe'`.
    """

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","log_group_id",b"log_group_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListOperationsRequest = ListOperationsRequest

class ListOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified log group."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListOperationsResponse = ListOperationsResponse

class GetLogGroupStatsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    RECORDS_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """Log group ID the stats are returned for."""

    bytes: builtins.int
    """Size of data in log group in bytes."""

    records: builtins.int
    """Amount of records in log group."""

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        bytes: builtins.int = ...,
        records: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bytes",b"bytes","log_group_id",b"log_group_id","records",b"records"]) -> None: ...
global___GetLogGroupStatsResponse = GetLogGroupStatsResponse
