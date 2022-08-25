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
import yandex.cloud.compute.v1.host_group_pb2
import yandex.cloud.compute.v1.instance_pb2
import yandex.cloud.operation.operation_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetHostGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to return.
    To get the host group ID, use [HostGroupService.List] request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___GetHostGroupRequest = GetHostGroupRequest

class ListHostGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list host groups in.
    To get the folder ID, use [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListHostGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListHostGroupsResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on the [HostGroup.name] field.
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

global___ListHostGroupsRequest = ListHostGroupsRequest

class ListHostGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def host_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.host_group_pb2.HostGroup]:
        """Lists host groups for the specified folder."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListHostGroupsRequest.page_size], use
    [next_page_token] as the value
    for the [ListHostGroupsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        host_groups: collections.abc.Iterable[yandex.cloud.compute.v1.host_group_pb2.HostGroup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_groups", b"host_groups", "next_page_token", b"next_page_token"]) -> None: ...

global___ListHostGroupsResponse = ListHostGroupsResponse

class CreateHostGroupRequest(google.protobuf.message.Message):
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
    ZONE_ID_FIELD_NUMBER: builtins.int
    TYPE_ID_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a host group in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the group."""
    description: builtins.str
    """Description of the group."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""
    zone_id: builtins.str
    """Availability zone where all dedicated hosts will be allocated."""
    type_id: builtins.str
    """ID of host type. Resources provided by each host of the group."""
    maintenance_policy: yandex.cloud.compute.v1.host_group_pb2.MaintenancePolicy.ValueType
    """Behaviour on maintenance events."""
    @property
    def scale_policy(self) -> yandex.cloud.compute.v1.host_group_pb2.ScalePolicy:
        """Scale policy. Only fixed number of hosts are supported at this moment."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        zone_id: builtins.str = ...,
        type_id: builtins.str = ...,
        maintenance_policy: yandex.cloud.compute.v1.host_group_pb2.MaintenancePolicy.ValueType = ...,
        scale_policy: yandex.cloud.compute.v1.host_group_pb2.ScalePolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["scale_policy", b"scale_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "folder_id", b"folder_id", "labels", b"labels", "maintenance_policy", b"maintenance_policy", "name", b"name", "scale_policy", b"scale_policy", "type_id", b"type_id", "zone_id", b"zone_id"]) -> None: ...

global___CreateHostGroupRequest = CreateHostGroupRequest

class CreateHostGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group that is being created."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___CreateHostGroupMetadata = CreateHostGroupMetadata

class UpdateHostGroupRequest(google.protobuf.message.Message):
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

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to update.
    To get the host group ID, use an [HostGroupService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the HostGroup resource are going to be updated."""
    name: builtins.str
    """Name of the group."""
    description: builtins.str
    """Description of the group."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        The existing set of `labels` is completely replaced by the provided set.
        """
    maintenance_policy: yandex.cloud.compute.v1.host_group_pb2.MaintenancePolicy.ValueType
    """Behaviour on maintenance events"""
    @property
    def scale_policy(self) -> yandex.cloud.compute.v1.host_group_pb2.ScalePolicy:
        """Scale policy. Only fixed number of hosts are supported at this moment."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        maintenance_policy: yandex.cloud.compute.v1.host_group_pb2.MaintenancePolicy.ValueType = ...,
        scale_policy: yandex.cloud.compute.v1.host_group_pb2.ScalePolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["scale_policy", b"scale_policy", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "host_group_id", b"host_group_id", "labels", b"labels", "maintenance_policy", b"maintenance_policy", "name", b"name", "scale_policy", b"scale_policy", "update_mask", b"update_mask"]) -> None: ...

global___UpdateHostGroupRequest = UpdateHostGroupRequest

class UpdateHostGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group that is being updated."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___UpdateHostGroupMetadata = UpdateHostGroupMetadata

class DeleteHostGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to delete.
    To get the host group ID, use [HostGroupService.List] request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___DeleteHostGroupRequest = DeleteHostGroupRequest

class DeleteHostGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group that is being deleted."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___DeleteHostGroupMetadata = DeleteHostGroupMetadata

class ListHostGroupInstancesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to list instances for.
    To get the host group ID, use [HostGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListHostGroupInstancesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListHostGroupInstancesResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on the [Host.id] field.
    To get the host ID, use [HostGroupService.ListHosts] request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "host_group_id", b"host_group_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListHostGroupInstancesRequest = ListHostGroupInstancesRequest

class ListHostGroupInstancesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INSTANCES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def instances(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.instance_pb2.Instance]:
        """Lists instances for the specified host group."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is more than [ListHostGroupInstancesRequest.page_size], use
    [next_page_token] as the value
    for the [ListHostGroupInstancesRequest.page_token] query parameter
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

global___ListHostGroupInstancesResponse = ListHostGroupInstancesResponse

class ListHostGroupHostsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to list hosts for.
    To get the host group ID, use [HostGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListHostGroupHostsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListHostGroupHostsResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_group_id", b"host_group_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListHostGroupHostsRequest = ListHostGroupHostsRequest

class ListHostGroupHostsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOSTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def hosts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.host_group_pb2.Host]:
        """Lists hosts for the specified host group."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is more than [ListHostGroupHostsRequest.page_size], use
    [next_page_token] as the value
    for the [ListHostGroupHostsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        hosts: collections.abc.Iterable[yandex.cloud.compute.v1.host_group_pb2.Host] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hosts", b"hosts", "next_page_token", b"next_page_token"]) -> None: ...

global___ListHostGroupHostsResponse = ListHostGroupHostsResponse

class ListHostGroupOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to list operations for.
    To get the host group ID, use [HostGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListHostGroupOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListHostGroupOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_group_id", b"host_group_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListHostGroupOperationsRequest = ListHostGroupOperationsRequest

class ListHostGroupOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified host group."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListHostGroupOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListHostGroupOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListHostGroupOperationsResponse = ListHostGroupOperationsResponse
