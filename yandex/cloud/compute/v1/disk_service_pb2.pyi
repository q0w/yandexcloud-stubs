"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import yandex.cloud.compute.v1.disk_pb2
import yandex.cloud.compute.v1.snapshot_schedule_pb2
import yandex.cloud.operation.operation_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetDiskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the Disk resource to return.
    To get the disk ID use a [DiskService.List] request.
    """
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_id", b"disk_id"]) -> None: ...

global___GetDiskRequest = GetDiskRequest

@typing_extensions.final
class ListDisksRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list disks in.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListDisksResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListDisksResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [Disk.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z]([-a-z0-9]{,61}[a-z0-9])?`.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDisksRequest = ListDisksRequest

@typing_extensions.final
class ListDisksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISKS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def disks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.disk_pb2.Disk]:
        """List of Disk resources."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListDisksRequest.page_size], use
    the [next_page_token] as the value
    for the [ListDisksRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        disks: collections.abc.Iterable[yandex.cloud.compute.v1.disk_pb2.Disk] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disks", b"disks", "next_page_token", b"next_page_token"]) -> None: ...

global___ListDisksResponse = ListDisksResponse

@typing_extensions.final
class CreateDiskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TYPE_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    IMAGE_ID_FIELD_NUMBER: builtins.int
    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    BLOCK_SIZE_FIELD_NUMBER: builtins.int
    DISK_PLACEMENT_POLICY_FIELD_NUMBER: builtins.int
    SNAPSHOT_SCHEDULE_IDS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a disk in.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the disk."""
    description: builtins.str
    """Description of the disk."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""
    type_id: builtins.str
    """ID of the disk type.
    To get a list of available disk types use the [yandex.cloud.compute.v1.DiskTypeService.List] request.
    """
    zone_id: builtins.str
    """ID of the availability zone where the disk resides.
    To get a list of available zones use the [yandex.cloud.compute.v1.ZoneService.List] request.
    """
    size: builtins.int
    """Size of the disk, specified in bytes.
    If the disk was created from a image, this value should be more than the
    [yandex.cloud.compute.v1.Image.min_disk_size] value.
    """
    image_id: builtins.str
    """ID of the image to create the disk from."""
    snapshot_id: builtins.str
    """ID of the snapshot to restore the disk from."""
    block_size: builtins.int
    """Block size used for disk, specified in bytes. The default is 4096."""
    @property
    def disk_placement_policy(self) -> yandex.cloud.compute.v1.disk_pb2.DiskPlacementPolicy:
        """Placement policy configuration."""
    @property
    def snapshot_schedule_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of IDs of the snapshot schedules to attach the disk to."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        type_id: builtins.str = ...,
        zone_id: builtins.str = ...,
        size: builtins.int = ...,
        image_id: builtins.str = ...,
        snapshot_id: builtins.str = ...,
        block_size: builtins.int = ...,
        disk_placement_policy: yandex.cloud.compute.v1.disk_pb2.DiskPlacementPolicy | None = ...,
        snapshot_schedule_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disk_placement_policy", b"disk_placement_policy", "image_id", b"image_id", "snapshot_id", b"snapshot_id", "source", b"source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_size", b"block_size", "description", b"description", "disk_placement_policy", b"disk_placement_policy", "folder_id", b"folder_id", "image_id", b"image_id", "labels", b"labels", "name", b"name", "size", b"size", "snapshot_id", b"snapshot_id", "snapshot_schedule_ids", b"snapshot_schedule_ids", "source", b"source", "type_id", b"type_id", "zone_id", b"zone_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["source", b"source"]) -> typing_extensions.Literal["image_id", "snapshot_id"] | None: ...

global___CreateDiskRequest = CreateDiskRequest

@typing_extensions.final
class CreateDiskMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the disk that is being created."""
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_id", b"disk_id"]) -> None: ...

global___CreateDiskMetadata = CreateDiskMetadata

@typing_extensions.final
class UpdateDiskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DISK_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    DISK_PLACEMENT_POLICY_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the Disk resource to update.
    To get the disk ID use a [DiskService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Disk resource are going to be updated."""
    name: builtins.str
    """Name of the disk."""
    description: builtins.str
    """Description of the disk."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """
    size: builtins.int
    """Size of the disk, specified in bytes."""
    @property
    def disk_placement_policy(self) -> yandex.cloud.compute.v1.disk_pb2.DiskPlacementPolicy:
        """Placement policy configuration."""
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        size: builtins.int = ...,
        disk_placement_policy: yandex.cloud.compute.v1.disk_pb2.DiskPlacementPolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disk_placement_policy", b"disk_placement_policy", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "disk_id", b"disk_id", "disk_placement_policy", b"disk_placement_policy", "labels", b"labels", "name", b"name", "size", b"size", "update_mask", b"update_mask"]) -> None: ...

global___UpdateDiskRequest = UpdateDiskRequest

@typing_extensions.final
class UpdateDiskMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the Disk resource that is being updated."""
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_id", b"disk_id"]) -> None: ...

global___UpdateDiskMetadata = UpdateDiskMetadata

@typing_extensions.final
class DeleteDiskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the disk to delete.
    To get the disk ID use a [DiskService.List] request.
    """
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_id", b"disk_id"]) -> None: ...

global___DeleteDiskRequest = DeleteDiskRequest

@typing_extensions.final
class DeleteDiskMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the disk that is being deleted."""
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_id", b"disk_id"]) -> None: ...

global___DeleteDiskMetadata = DeleteDiskMetadata

@typing_extensions.final
class ListDiskOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the Disk resource to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListDiskOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListDiskOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_id", b"disk_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDiskOperationsRequest = ListDiskOperationsRequest

@typing_extensions.final
class ListDiskOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified disk."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListDiskOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListDiskOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListDiskOperationsResponse = ListDiskOperationsResponse

@typing_extensions.final
class MoveDiskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the disk to move.

    To get the disk ID, make a [DiskService.List] request.
    """
    destination_folder_id: builtins.str
    """ID of the folder to move the disk to.

    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
        destination_folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["destination_folder_id", b"destination_folder_id", "disk_id", b"disk_id"]) -> None: ...

global___MoveDiskRequest = MoveDiskRequest

@typing_extensions.final
class MoveDiskMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    SOURCE_FOLDER_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the disk that is being moved."""
    source_folder_id: builtins.str
    """ID of the folder that the disk is being moved from."""
    destination_folder_id: builtins.str
    """ID of the folder that the disk is being moved to."""
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
        source_folder_id: builtins.str = ...,
        destination_folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["destination_folder_id", b"destination_folder_id", "disk_id", b"disk_id", "source_folder_id", b"source_folder_id"]) -> None: ...

global___MoveDiskMetadata = MoveDiskMetadata

@typing_extensions.final
class ListDiskSnapshotSchedulesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """ID of the disk to list snapshot schedules for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListDiskSnapshotSchedulesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.

    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListDiskSnapshotSchedulesResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_id", b"disk_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDiskSnapshotSchedulesRequest = ListDiskSnapshotSchedulesRequest

@typing_extensions.final
class ListDiskSnapshotSchedulesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SNAPSHOT_SCHEDULES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def snapshot_schedules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.snapshot_schedule_pb2.SnapshotSchedule]:
        """List of snapshot schedules the specified disk is attached to."""
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListDiskSnapshotSchedulesRequest.page_size], use `next_page_token` as the value
    for the [ListDiskSnapshotSchedulesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        snapshot_schedules: collections.abc.Iterable[yandex.cloud.compute.v1.snapshot_schedule_pb2.SnapshotSchedule] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "snapshot_schedules", b"snapshot_schedules"]) -> None: ...

global___ListDiskSnapshotSchedulesResponse = ListDiskSnapshotSchedulesResponse
