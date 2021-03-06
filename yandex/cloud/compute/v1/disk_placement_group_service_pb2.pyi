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
import yandex.cloud.compute.v1.disk_pb2
import yandex.cloud.compute.v1.disk_placement_group_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetDiskPlacementGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    disk_placement_group_id: typing.Text
    """ID of the placement group to return.
    To get the placement group ID, use [DiskPlacementGroupService.List] request.
    """

    def __init__(self,
        *,
        disk_placement_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_placement_group_id",b"disk_placement_group_id"]) -> None: ...
global___GetDiskPlacementGroupRequest = GetDiskPlacementGroupRequest

class ListDiskPlacementGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list placement groups in.
    To get the folder ID, use [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListDiskPlacementGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results,
    set [page_token] to the [ListDiskPlacementGroupsResponse.next_page_token]
    returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on the [DiskPlacementGroup.name] field.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListDiskPlacementGroupsRequest = ListDiskPlacementGroupsRequest

class ListDiskPlacementGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_PLACEMENT_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def disk_placement_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.disk_placement_group_pb2.DiskPlacementGroup]:
        """Lists placement groups for the specified folder."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListDiskPlacementGroupsRequest.page_size], use
    [next_page_token] as the value
    for the [ListDiskPlacementGroupsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        disk_placement_groups: typing.Optional[typing.Iterable[yandex.cloud.compute.v1.disk_placement_group_pb2.DiskPlacementGroup]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_placement_groups",b"disk_placement_groups","next_page_token",b"next_page_token"]) -> None: ...
global___ListDiskPlacementGroupsResponse = ListDiskPlacementGroupsResponse

class CreateDiskPlacementGroupRequest(google.protobuf.message.Message):
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
    ZONE_ID_FIELD_NUMBER: builtins.int
    SPREAD_PLACEMENT_STRATEGY_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to create a placement group in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    name: typing.Text
    """Name of the placement group."""

    description: typing.Text
    """Description of the placement group."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs."""
        pass
    zone_id: typing.Text
    """ID of the availability zone where the placement group resides.
    To get a list of available zones use the [yandex.cloud.compute.v1.ZoneService.List] request.
    """

    @property
    def spread_placement_strategy(self) -> yandex.cloud.compute.v1.disk_placement_group_pb2.DiskSpreadPlacementStrategy:
        """Distribute disks over distinct failure domains."""
        pass
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        zone_id: typing.Text = ...,
        spread_placement_strategy: typing.Optional[yandex.cloud.compute.v1.disk_placement_group_pb2.DiskSpreadPlacementStrategy] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["placement_strategy",b"placement_strategy","spread_placement_strategy",b"spread_placement_strategy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","folder_id",b"folder_id","labels",b"labels","name",b"name","placement_strategy",b"placement_strategy","spread_placement_strategy",b"spread_placement_strategy","zone_id",b"zone_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["placement_strategy",b"placement_strategy"]) -> typing.Optional[typing_extensions.Literal["spread_placement_strategy"]]: ...
global___CreateDiskPlacementGroupRequest = CreateDiskPlacementGroupRequest

class CreateDiskPlacementGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    disk_placement_group_id: typing.Text
    """ID of the placement group that is being created."""

    def __init__(self,
        *,
        disk_placement_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_placement_group_id",b"disk_placement_group_id"]) -> None: ...
global___CreateDiskPlacementGroupMetadata = CreateDiskPlacementGroupMetadata

class UpdateDiskPlacementGroupRequest(google.protobuf.message.Message):
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

    DISK_PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    disk_placement_group_id: typing.Text
    """ID of the placement group to update.
    To get the placement group ID, use an [DiskPlacementGroupService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the DiskPlacementGroup resource are going to be updated."""
        pass
    name: typing.Text
    """Name of the placement group."""

    description: typing.Text
    """Description of the placement group."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs.

        The existing set of `labels` is completely replaced by the provided set.
        """
        pass
    def __init__(self,
        *,
        disk_placement_group_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","disk_placement_group_id",b"disk_placement_group_id","labels",b"labels","name",b"name","update_mask",b"update_mask"]) -> None: ...
global___UpdateDiskPlacementGroupRequest = UpdateDiskPlacementGroupRequest

class UpdateDiskPlacementGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    disk_placement_group_id: typing.Text
    """ID of the placement group that is being updated."""

    def __init__(self,
        *,
        disk_placement_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_placement_group_id",b"disk_placement_group_id"]) -> None: ...
global___UpdateDiskPlacementGroupMetadata = UpdateDiskPlacementGroupMetadata

class DeleteDiskPlacementGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    disk_placement_group_id: typing.Text
    """ID of the placement group to delete.
    To get the placement group ID, use [DiskPlacementGroupService.List] request.
    """

    def __init__(self,
        *,
        disk_placement_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_placement_group_id",b"disk_placement_group_id"]) -> None: ...
global___DeleteDiskPlacementGroupRequest = DeleteDiskPlacementGroupRequest

class DeleteDiskPlacementGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    disk_placement_group_id: typing.Text
    """ID of the placement group that is being deleted."""

    def __init__(self,
        *,
        disk_placement_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_placement_group_id",b"disk_placement_group_id"]) -> None: ...
global___DeleteDiskPlacementGroupMetadata = DeleteDiskPlacementGroupMetadata

class ListDiskPlacementGroupDisksRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    disk_placement_group_id: typing.Text
    """ID of the placement group to list disks for.
    To get the placement group ID, use [DiskPlacementGroupService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListDiskPlacementGroupDisksResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results,
    set [page_token] to the [ListDiskPlacementGroupDisksResponse.next_page_token]
    returned by a previous list request.
    """

    def __init__(self,
        *,
        disk_placement_group_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_placement_group_id",b"disk_placement_group_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListDiskPlacementGroupDisksRequest = ListDiskPlacementGroupDisksRequest

class ListDiskPlacementGroupDisksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISKS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def disks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.disk_pb2.Disk]:
        """Lists disks for the specified placement group."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is more than [ListDiskPlacementGroupDisksRequest.page_size], use
    [next_page_token] as the value
    for the [ListDiskPlacementGroupDisksRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        disks: typing.Optional[typing.Iterable[yandex.cloud.compute.v1.disk_pb2.Disk]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disks",b"disks","next_page_token",b"next_page_token"]) -> None: ...
global___ListDiskPlacementGroupDisksResponse = ListDiskPlacementGroupDisksResponse

class ListDiskPlacementGroupOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISK_PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    disk_placement_group_id: typing.Text
    """ID of the placement group to list operations for.
    To get the placement group ID, use [DiskPlacementGroupService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListDiskPlacementGroupOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListDiskPlacementGroupOperationsResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        disk_placement_group_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_placement_group_id",b"disk_placement_group_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListDiskPlacementGroupOperationsRequest = ListDiskPlacementGroupOperationsRequest

class ListDiskPlacementGroupOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified placement group."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListDiskPlacementGroupOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListDiskPlacementGroupOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListDiskPlacementGroupOperationsResponse = ListDiskPlacementGroupOperationsResponse
