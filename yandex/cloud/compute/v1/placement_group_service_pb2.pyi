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
import yandex.cloud.compute.v1.instance_pb2
import yandex.cloud.compute.v1.placement_group_pb2
import yandex.cloud.operation.operation_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetPlacementGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    placement_group_id: builtins.str
    """ID of the placement group to return.

    To get a placement group ID make a [PlacementGroupService.List] request.
    """
    def __init__(
        self,
        *,
        placement_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["placement_group_id", b"placement_group_id"]) -> None: ...

global___GetPlacementGroupRequest = GetPlacementGroupRequest

class ListPlacementGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list placement groups in.

    To get the folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListPlacementGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListPlacementGroupsResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on the [PlacementGroup.name] field.
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

global___ListPlacementGroupsRequest = ListPlacementGroupsRequest

class ListPlacementGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACEMENT_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def placement_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.placement_group_pb2.PlacementGroup]:
        """Lists placement groups in the specified folder."""
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListPlacementGroupsRequest.page_size], use `next_page_token` as the value
    for the [ListPlacementGroupsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        placement_groups: collections.abc.Iterable[yandex.cloud.compute.v1.placement_group_pb2.PlacementGroup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "placement_groups", b"placement_groups"]) -> None: ...

global___ListPlacementGroupsResponse = ListPlacementGroupsResponse

class CreatePlacementGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

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
    SPREAD_PLACEMENT_STRATEGY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a placement group in.

    To get a folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the placement group."""
    description: builtins.str
    """Description of the placement group."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""
    @property
    def spread_placement_strategy(self) -> yandex.cloud.compute.v1.placement_group_pb2.SpreadPlacementStrategy:
        """Anti-affinity placement strategy (`spread`). Instances are distributed over distinct failure domains."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        spread_placement_strategy: yandex.cloud.compute.v1.placement_group_pb2.SpreadPlacementStrategy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["placement_strategy", b"placement_strategy", "spread_placement_strategy", b"spread_placement_strategy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "placement_strategy", b"placement_strategy", "spread_placement_strategy", b"spread_placement_strategy"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["placement_strategy", b"placement_strategy"]) -> typing_extensions.Literal["spread_placement_strategy"] | None: ...

global___CreatePlacementGroupRequest = CreatePlacementGroupRequest

class CreatePlacementGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    placement_group_id: builtins.str
    """ID of the placement group that is being created."""
    def __init__(
        self,
        *,
        placement_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["placement_group_id", b"placement_group_id"]) -> None: ...

global___CreatePlacementGroupMetadata = CreatePlacementGroupMetadata

class UpdatePlacementGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

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

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    placement_group_id: builtins.str
    """ID of the placement group to update.

    To get the placement group ID, use an [PlacementGroupService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the PlacementGroup resource should be updated."""
    name: builtins.str
    """Name of the placement group."""
    description: builtins.str
    """Description of the placement group."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        The existing set of `labels` is completely replaced by the provided set.
        """
    def __init__(
        self,
        *,
        placement_group_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "labels", b"labels", "name", b"name", "placement_group_id", b"placement_group_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdatePlacementGroupRequest = UpdatePlacementGroupRequest

class UpdatePlacementGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    placement_group_id: builtins.str
    """ID of the placement group that is being updated."""
    def __init__(
        self,
        *,
        placement_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["placement_group_id", b"placement_group_id"]) -> None: ...

global___UpdatePlacementGroupMetadata = UpdatePlacementGroupMetadata

class DeletePlacementGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    placement_group_id: builtins.str
    """ID of the placement group to delete.

    To get the placement group ID, use [PlacementGroupService.List] request.
    """
    def __init__(
        self,
        *,
        placement_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["placement_group_id", b"placement_group_id"]) -> None: ...

global___DeletePlacementGroupRequest = DeletePlacementGroupRequest

class DeletePlacementGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    placement_group_id: builtins.str
    """ID of the placement group that is being deleted."""
    def __init__(
        self,
        *,
        placement_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["placement_group_id", b"placement_group_id"]) -> None: ...

global___DeletePlacementGroupMetadata = DeletePlacementGroupMetadata

class ListPlacementGroupInstancesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    placement_group_id: builtins.str
    """ID of the placement group to list instances for.

    To get the placement group ID, use [PlacementGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListPlacementGroupInstancesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListPlacementGroupInstancesResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        placement_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size", b"page_size", "page_token", b"page_token", "placement_group_id", b"placement_group_id"]) -> None: ...

global___ListPlacementGroupInstancesRequest = ListPlacementGroupInstancesRequest

class ListPlacementGroupInstancesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INSTANCES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def instances(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.instance_pb2.Instance]:
        """Lists instances for the specified placement group."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is more than [ListPlacementGroupInstancesRequest.page_size], use
    [next_page_token] as the value
    for the [ListPlacementGroupInstancesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        instances: collections.abc.Iterable[yandex.cloud.compute.v1.instance_pb2.Instance] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["instances", b"instances", "next_page_token", b"next_page_token"]) -> None: ...

global___ListPlacementGroupInstancesResponse = ListPlacementGroupInstancesResponse

class ListPlacementGroupOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACEMENT_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    placement_group_id: builtins.str
    """ID of the placement group to list operations for.

    To get the placement group ID, use [PlacementGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListPlacementGroupOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListPlacementGroupOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        placement_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size", b"page_size", "page_token", b"page_token", "placement_group_id", b"placement_group_id"]) -> None: ...

global___ListPlacementGroupOperationsRequest = ListPlacementGroupOperationsRequest

class ListPlacementGroupOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified placement group."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListPlacementGroupOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListPlacementGroupOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListPlacementGroupOperationsResponse = ListPlacementGroupOperationsResponse
