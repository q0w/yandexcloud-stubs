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
import yandex.cloud.loadbalancer.v1.target_group_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetTargetGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the TargetGroup resource to return.
    To get the target group ID, use a [TargetGroupService.List] request.
    """

    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id"]) -> None: ...
global___GetTargetGroupRequest = GetTargetGroupRequest

class ListTargetGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list target groups in. 
    To get the folder ID, use a [TargetGroupService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListTargetGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the 
    [ListTargetGroupsResponse.next_page_token] returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters resources listed in the response.
    The expression must specify: 
    1. The field name. Currently you can only filter by the [TargetGroup.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListTargetGroupsRequest = ListTargetGroupsRequest

class ListTargetGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def target_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadbalancer.v1.target_group_pb2.TargetGroup]:
        """List of TargetGroup resources."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListTargetGroupsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListTargetGroupsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        target_groups: typing.Optional[typing.Iterable[yandex.cloud.loadbalancer.v1.target_group_pb2.TargetGroup]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","target_groups",b"target_groups"]) -> None: ...
global___ListTargetGroupsResponse = ListTargetGroupsResponse

class CreateTargetGroupRequest(google.protobuf.message.Message):
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
    REGION_ID_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list target groups in. 
    To get the folder ID, use a [TargetGroupService.List] request.
    """

    name: typing.Text
    """Name of the target group. 
    The name must be unique within the folder.
    """

    description: typing.Text
    """Description of the target group."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `` key:value `` pairs."""
        pass
    region_id: typing.Text
    """ID of the availability zone where the target group resides."""

    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadbalancer.v1.target_group_pb2.Target]:
        """List of targets within the target group."""
        pass
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        region_id: typing.Text = ...,
        targets: typing.Optional[typing.Iterable[yandex.cloud.loadbalancer.v1.target_group_pb2.Target]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","folder_id",b"folder_id","labels",b"labels","name",b"name","region_id",b"region_id","targets",b"targets"]) -> None: ...
global___CreateTargetGroupRequest = CreateTargetGroupRequest

class CreateTargetGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the target group that is being created."""

    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id"]) -> None: ...
global___CreateTargetGroupMetadata = CreateTargetGroupMetadata

class UpdateTargetGroupRequest(google.protobuf.message.Message):
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

    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the TargetGroup resource to update.
    To get the target group ID, use a [TargetGroupService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the TargetGroup resource are going to be updated."""
        pass
    name: typing.Text
    """Name of the target group. 
    The name must be unique within the folder.
    """

    description: typing.Text
    """Description of the target group."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `` key:value `` pairs.

        The existing set of `` labels `` is completely replaced with the provided set.
        """
        pass
    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadbalancer.v1.target_group_pb2.Target]:
        """A new list of targets for this target group."""
        pass
    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        targets: typing.Optional[typing.Iterable[yandex.cloud.loadbalancer.v1.target_group_pb2.Target]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","labels",b"labels","name",b"name","target_group_id",b"target_group_id","targets",b"targets","update_mask",b"update_mask"]) -> None: ...
global___UpdateTargetGroupRequest = UpdateTargetGroupRequest

class UpdateTargetGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the target group that is being updated."""

    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id"]) -> None: ...
global___UpdateTargetGroupMetadata = UpdateTargetGroupMetadata

class DeleteTargetGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the target group to delete.
    To get the target group ID, use a [TargetGroupService.List] request.
    """

    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id"]) -> None: ...
global___DeleteTargetGroupRequest = DeleteTargetGroupRequest

class DeleteTargetGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the target group that is being deleted."""

    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id"]) -> None: ...
global___DeleteTargetGroupMetadata = DeleteTargetGroupMetadata

class AddTargetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the TargetGroup resource to add targets to.
    To get the target group ID, use a [TargetGroupService.List] request.
    """

    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadbalancer.v1.target_group_pb2.Target]:
        """List of targets to add to the target group."""
        pass
    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        targets: typing.Optional[typing.Iterable[yandex.cloud.loadbalancer.v1.target_group_pb2.Target]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id","targets",b"targets"]) -> None: ...
global___AddTargetsRequest = AddTargetsRequest

class AddTargetsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the target group that targets are being added to."""

    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id"]) -> None: ...
global___AddTargetsMetadata = AddTargetsMetadata

class RemoveTargetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the target group to remove targets from.
    To get the target group ID, use a [TargetGroupService.List] request.
    """

    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadbalancer.v1.target_group_pb2.Target]:
        """List of targets to remove from the target group."""
        pass
    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        targets: typing.Optional[typing.Iterable[yandex.cloud.loadbalancer.v1.target_group_pb2.Target]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id","targets",b"targets"]) -> None: ...
global___RemoveTargetsRequest = RemoveTargetsRequest

class RemoveTargetsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the target group that targets are being removed from."""

    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_group_id",b"target_group_id"]) -> None: ...
global___RemoveTargetsMetadata = RemoveTargetsMetadata

class ListTargetGroupOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    target_group_id: typing.Text
    """ID of the TargetGroup resource to update.
    To get the target group ID, use a [TargetGroupService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size], the service returns a [ListTargetGroupOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the 
    [ListTargetGroupOperationsResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        target_group_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","target_group_id",b"target_group_id"]) -> None: ...
global___ListTargetGroupOperationsRequest = ListTargetGroupOperationsRequest

class ListTargetGroupOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified target group."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListTargetGroupOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListTargetGroupOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListTargetGroupOperationsResponse = ListTargetGroupOperationsResponse
