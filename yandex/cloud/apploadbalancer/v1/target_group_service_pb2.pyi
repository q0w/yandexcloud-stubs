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
import yandex.cloud.apploadbalancer.v1.target_group_pb2
import yandex.cloud.operation.operation_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetTargetGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group to return.

    To get the target group ID, make a [TargetGroupService.List] request.
    """
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id"]) -> None: ...

global___GetTargetGroupRequest = GetTargetGroupRequest

class ListTargetGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list target groups in.

    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListTargetGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListTargetGroupsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters target groups listed in the response.

    The expression must specify:
    1. The field name. Currently you can use filtering only on [TargetGroup.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    Example of a filter: `name=my-target-group`.
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

global___ListTargetGroupsRequest = ListTargetGroupsRequest

class ListTargetGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def target_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.target_group_pb2.TargetGroup]:
        """List of target groups in the specified folder."""
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListTargetGroupsRequest.page_size], use `next_page_token` as the value
    for the [ListTargetGroupsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        target_groups: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.target_group_pb2.TargetGroup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "target_groups", b"target_groups"]) -> None: ...

global___ListTargetGroupsResponse = ListTargetGroupsResponse

class DeleteTargetGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group to delete.

    To get the target group ID, make a [TargetGroupService.List] request.
    """
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id"]) -> None: ...

global___DeleteTargetGroupRequest = DeleteTargetGroupRequest

class DeleteTargetGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group that is being deleted."""
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id"]) -> None: ...

global___DeleteTargetGroupMetadata = DeleteTargetGroupMetadata

class UpdateTargetGroupRequest(google.protobuf.message.Message):
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

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group to update.

    To get the target group ID, make a [TargetGroupService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the target group should be updated."""
    name: builtins.str
    """New name for the target group.
    The name must be unique within the folder.
    """
    description: builtins.str
    """New description of the target group."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Target group labels as `key:value` pairs.
        For details about the concept, see [documentation](/docs/overview/concepts/services#labels).

        Existing set of labels is completely replaced by the provided set, so if you just want
        to add or remove a label:
        1. Get the current set of labels with a [TargetGroupService.Get] request.
        2. Add or remove a label in this set.
        3. Send the new set in this field.
        """
    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target]:
        """New list of targets in the target group.

        Existing list of targets is completely replaced by the specified list, so if you just want to add or remove
        a target, make a [TargetGroupService.AddTargets] request or a [TargetGroupService.RemoveTargets] request.
        """
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        targets: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "labels", b"labels", "name", b"name", "target_group_id", b"target_group_id", "targets", b"targets", "update_mask", b"update_mask"]) -> None: ...

global___UpdateTargetGroupRequest = UpdateTargetGroupRequest

class UpdateTargetGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group that is being updated."""
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id"]) -> None: ...

global___UpdateTargetGroupMetadata = UpdateTargetGroupMetadata

class CreateTargetGroupRequest(google.protobuf.message.Message):
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
    TARGETS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a target group in.

    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the target group.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the target group."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Target group labels as `key:value` pairs.
        For details about the concept, see [documentation](/docs/overview/concepts/services#labels).
        """
    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target]:
        """List of targets in the target group."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        targets: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "targets", b"targets"]) -> None: ...

global___CreateTargetGroupRequest = CreateTargetGroupRequest

class CreateTargetGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group that is being created."""
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id"]) -> None: ...

global___CreateTargetGroupMetadata = CreateTargetGroupMetadata

class AddTargetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group to add targets to.

    To get the target group ID, make a [TargetGroupService.List] request.
    """
    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target]:
        """List of targets to add to the target group."""
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
        targets: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id", "targets", b"targets"]) -> None: ...

global___AddTargetsRequest = AddTargetsRequest

class AddTargetsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group that the targets are being added to."""
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id"]) -> None: ...

global___AddTargetsMetadata = AddTargetsMetadata

class RemoveTargetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group to remove targets from.

    To get the target group ID, make a [TargetGroupService.List] request.
    """
    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target]:
        """List of targets to remove from the target group."""
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
        targets: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id", "targets", b"targets"]) -> None: ...

global___RemoveTargetsRequest = RemoveTargetsRequest

class RemoveTargetsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group that the targets are being removed from."""
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id", b"target_group_id"]) -> None: ...

global___RemoveTargetsMetadata = RemoveTargetsMetadata

class ListTargetGroupOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    target_group_id: builtins.str
    """ID of the target group to get operations for.

    To get the target group ID, use a [TargetGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size], the service returns a [ListTargetGroupOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListTargetGroupOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        target_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size", b"page_size", "page_token", b"page_token", "target_group_id", b"target_group_id"]) -> None: ...

global___ListTargetGroupOperationsRequest = ListTargetGroupOperationsRequest

class ListTargetGroupOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified target group."""
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListTargetGroupOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListTargetGroupOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListTargetGroupOperationsResponse = ListTargetGroupOperationsResponse
