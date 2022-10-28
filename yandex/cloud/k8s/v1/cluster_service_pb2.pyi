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
import typing
import yandex.cloud.k8s.v1.cluster_pb2
import yandex.cloud.k8s.v1.node_group_pb2
import yandex.cloud.k8s.v1.node_pb2
import yandex.cloud.k8s.v1.version_pb2
import yandex.cloud.operation.operation_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to return."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___GetClusterRequest = GetClusterRequest

@typing_extensions.final
class ListClustersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list Kubernetes cluster in.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListClustersResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListClustersResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [Cluster.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
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

global___ListClustersRequest = ListClustersRequest

@typing_extensions.final
class ListClustersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def clusters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.k8s.v1.cluster_pb2.Cluster]:
        """List of Kubernetes cluster."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListClustersRequest.page_size], use
    the `next_page_token` as the value
    for the [ListClustersRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        clusters: collections.abc.Iterable[yandex.cloud.k8s.v1.cluster_pb2.Cluster] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["clusters", b"clusters", "next_page_token", b"next_page_token"]) -> None: ...

global___ListClustersResponse = ListClustersResponse

@typing_extensions.final
class DeleteClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to delete.
    To get Kubernetes cluster ID use a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___DeleteClusterRequest = DeleteClusterRequest

@typing_extensions.final
class DeleteClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster that is being deleted."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___DeleteClusterMetadata = DeleteClusterMetadata

@typing_extensions.final
class StopClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to stop.
    To get Kubernetes cluster ID use a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StopClusterRequest = StopClusterRequest

@typing_extensions.final
class StopClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster that is being stopped."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StopClusterMetadata = StopClusterMetadata

@typing_extensions.final
class StartClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to start.
    To get Kubernetes cluster ID use a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StartClusterRequest = StartClusterRequest

@typing_extensions.final
class StartClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster that is being started."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StartClusterMetadata = StartClusterMetadata

@typing_extensions.final
class UpdateClusterRequest(google.protobuf.message.Message):
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

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    GATEWAY_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    MASTER_SPEC_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    NODE_SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    NETWORK_POLICY_FIELD_NUMBER: builtins.int
    IP_ALLOCATION_POLICY_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to update.
    To get the Kubernetes cluster ID use a [ClusterService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    name: builtins.str
    """Name of the Kubernetes cluster.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the Kubernetes cluster."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """
    gateway_ipv4_address: builtins.str
    """Gateway IPv4 address."""
    @property
    def master_spec(self) -> global___MasterUpdateSpec:
        """Specification of the master update."""
    service_account_id: builtins.str
    """Service account to be used for provisioning Compute Cloud and VPC resources for Kubernetes cluster.
    Selected service account should have `edit` role on the folder where the Kubernetes cluster will be
    located and on the folder where selected network resides.
    """
    node_service_account_id: builtins.str
    """Service account to be used by the worker nodes of the Kubernetes cluster to access Container Registry
    or to push node logs and metrics.
    """
    @property
    def network_policy(self) -> yandex.cloud.k8s.v1.cluster_pb2.NetworkPolicy: ...
    @property
    def ip_allocation_policy(self) -> yandex.cloud.k8s.v1.cluster_pb2.IPAllocationPolicy: ...
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        gateway_ipv4_address: builtins.str = ...,
        master_spec: global___MasterUpdateSpec | None = ...,
        service_account_id: builtins.str = ...,
        node_service_account_id: builtins.str = ...,
        network_policy: yandex.cloud.k8s.v1.cluster_pb2.NetworkPolicy | None = ...,
        ip_allocation_policy: yandex.cloud.k8s.v1.cluster_pb2.IPAllocationPolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gateway_ipv4_address", b"gateway_ipv4_address", "internet_gateway", b"internet_gateway", "ip_allocation_policy", b"ip_allocation_policy", "master_spec", b"master_spec", "network_policy", b"network_policy", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "description", b"description", "gateway_ipv4_address", b"gateway_ipv4_address", "internet_gateway", b"internet_gateway", "ip_allocation_policy", b"ip_allocation_policy", "labels", b"labels", "master_spec", b"master_spec", "name", b"name", "network_policy", b"network_policy", "node_service_account_id", b"node_service_account_id", "service_account_id", b"service_account_id", "update_mask", b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["internet_gateway", b"internet_gateway"]) -> typing_extensions.Literal["gateway_ipv4_address"] | None: ...

global___UpdateClusterRequest = UpdateClusterRequest

@typing_extensions.final
class MasterUpdateSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    MASTER_LOGGING_FIELD_NUMBER: builtins.int
    @property
    def version(self) -> yandex.cloud.k8s.v1.version_pb2.UpdateVersionSpec:
        """Specification of the master update."""
    @property
    def maintenance_policy(self) -> yandex.cloud.k8s.v1.cluster_pb2.MasterMaintenancePolicy:
        """Maintenance policy of the master."""
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Master security groups."""
    @property
    def master_logging(self) -> yandex.cloud.k8s.v1.cluster_pb2.MasterLogging:
        """Cloud Logging for master components."""
    def __init__(
        self,
        *,
        version: yandex.cloud.k8s.v1.version_pb2.UpdateVersionSpec | None = ...,
        maintenance_policy: yandex.cloud.k8s.v1.cluster_pb2.MasterMaintenancePolicy | None = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        master_logging: yandex.cloud.k8s.v1.cluster_pb2.MasterLogging | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["maintenance_policy", b"maintenance_policy", "master_logging", b"master_logging", "version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["maintenance_policy", b"maintenance_policy", "master_logging", b"master_logging", "security_group_ids", b"security_group_ids", "version", b"version"]) -> None: ...

global___MasterUpdateSpec = MasterUpdateSpec

@typing_extensions.final
class UpdateClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster that is being updated."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___UpdateClusterMetadata = UpdateClusterMetadata

@typing_extensions.final
class CreateClusterRequest(google.protobuf.message.Message):
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
    NETWORK_ID_FIELD_NUMBER: builtins.int
    MASTER_SPEC_FIELD_NUMBER: builtins.int
    IP_ALLOCATION_POLICY_FIELD_NUMBER: builtins.int
    GATEWAY_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    NODE_SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    RELEASE_CHANNEL_FIELD_NUMBER: builtins.int
    NETWORK_POLICY_FIELD_NUMBER: builtins.int
    KMS_PROVIDER_FIELD_NUMBER: builtins.int
    CILIUM_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a Kubernetes cluster in.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the Kubernetes cluster.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the Kubernetes cluster."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""
    network_id: builtins.str
    """ID of the network."""
    @property
    def master_spec(self) -> global___MasterSpec:
        """Master specification of the Kubernetes cluster."""
    @property
    def ip_allocation_policy(self) -> yandex.cloud.k8s.v1.cluster_pb2.IPAllocationPolicy:
        """IP allocation policy of the Kubernetes cluster."""
    gateway_ipv4_address: builtins.str
    """Gateway IPv4 address."""
    service_account_id: builtins.str
    """Service account to be used for provisioning Compute Cloud and VPC resources for Kubernetes cluster.
    Selected service account should have `edit` role on the folder where the Kubernetes cluster will be
    located and on the folder where selected network resides.
    """
    node_service_account_id: builtins.str
    """Service account to be used by the worker nodes of the Kubernetes cluster to access Container Registry or to push node logs and metrics."""
    release_channel: yandex.cloud.k8s.v1.cluster_pb2.ReleaseChannel.ValueType
    """Release channel for the master."""
    @property
    def network_policy(self) -> yandex.cloud.k8s.v1.cluster_pb2.NetworkPolicy: ...
    @property
    def kms_provider(self) -> yandex.cloud.k8s.v1.cluster_pb2.KMSProvider:
        """KMS provider configuration."""
    @property
    def cilium(self) -> yandex.cloud.k8s.v1.cluster_pb2.Cilium: ...
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        network_id: builtins.str = ...,
        master_spec: global___MasterSpec | None = ...,
        ip_allocation_policy: yandex.cloud.k8s.v1.cluster_pb2.IPAllocationPolicy | None = ...,
        gateway_ipv4_address: builtins.str = ...,
        service_account_id: builtins.str = ...,
        node_service_account_id: builtins.str = ...,
        release_channel: yandex.cloud.k8s.v1.cluster_pb2.ReleaseChannel.ValueType = ...,
        network_policy: yandex.cloud.k8s.v1.cluster_pb2.NetworkPolicy | None = ...,
        kms_provider: yandex.cloud.k8s.v1.cluster_pb2.KMSProvider | None = ...,
        cilium: yandex.cloud.k8s.v1.cluster_pb2.Cilium | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cilium", b"cilium", "gateway_ipv4_address", b"gateway_ipv4_address", "internet_gateway", b"internet_gateway", "ip_allocation_policy", b"ip_allocation_policy", "kms_provider", b"kms_provider", "master_spec", b"master_spec", "network_implementation", b"network_implementation", "network_policy", b"network_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cilium", b"cilium", "description", b"description", "folder_id", b"folder_id", "gateway_ipv4_address", b"gateway_ipv4_address", "internet_gateway", b"internet_gateway", "ip_allocation_policy", b"ip_allocation_policy", "kms_provider", b"kms_provider", "labels", b"labels", "master_spec", b"master_spec", "name", b"name", "network_id", b"network_id", "network_implementation", b"network_implementation", "network_policy", b"network_policy", "node_service_account_id", b"node_service_account_id", "release_channel", b"release_channel", "service_account_id", b"service_account_id"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["internet_gateway", b"internet_gateway"]) -> typing_extensions.Literal["gateway_ipv4_address"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["network_implementation", b"network_implementation"]) -> typing_extensions.Literal["cilium"] | None: ...

global___CreateClusterRequest = CreateClusterRequest

@typing_extensions.final
class CreateClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster that is being created."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___CreateClusterMetadata = CreateClusterMetadata

@typing_extensions.final
class AutoUpgradeMasterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster that is being auto upgraded."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___AutoUpgradeMasterMetadata = AutoUpgradeMasterMetadata

@typing_extensions.final
class ListClusterOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size], the service returns a [ListClusterOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListClusterOperationsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on [Cluster.name] field.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListClusterOperationsRequest = ListClusterOperationsRequest

@typing_extensions.final
class ListClusterOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified Kubernetes cluster."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListClusterOperationsRequest.page_size], use the `next_page_token` as the value
    for the [ListClusterOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListClusterOperationsResponse = ListClusterOperationsResponse

@typing_extensions.final
class ListClusterNodeGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to list node groups in.
    To get the Kubernetes cluster ID use a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListClusterNodeGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListClusterNodeGroupsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on [Cluster.name] field.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListClusterNodeGroupsRequest = ListClusterNodeGroupsRequest

@typing_extensions.final
class ListClusterNodeGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def node_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.k8s.v1.node_group_pb2.NodeGroup]:
        """List of node groups for the specified Kubernetes cluster."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListClusterNodeGroupsRequest.page_size], use
    the `next_page_token` as the value
    for the [ListClusterNodeGroupsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        node_groups: collections.abc.Iterable[yandex.cloud.k8s.v1.node_group_pb2.NodeGroup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "node_groups", b"node_groups"]) -> None: ...

global___ListClusterNodeGroupsResponse = ListClusterNodeGroupsResponse

@typing_extensions.final
class ListClusterNodesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to list nodes in.
    To get the Kubernetes cluster ID use a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListClusterNodesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListClusterNodeGroupsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListClusterNodesRequest = ListClusterNodesRequest

@typing_extensions.final
class ListClusterNodesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.k8s.v1.node_pb2.Node]:
        """List of nodes for the specified Kubernetes cluster."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListClusterNodesRequest.page_size], use
    the `next_page_token` as the value
    for the [ListClusterNodesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        nodes: collections.abc.Iterable[yandex.cloud.k8s.v1.node_pb2.Node] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "nodes", b"nodes"]) -> None: ...

global___ListClusterNodesResponse = ListClusterNodesResponse

@typing_extensions.final
class MasterSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONAL_MASTER_SPEC_FIELD_NUMBER: builtins.int
    REGIONAL_MASTER_SPEC_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    MASTER_LOGGING_FIELD_NUMBER: builtins.int
    @property
    def zonal_master_spec(self) -> global___ZonalMasterSpec:
        """Specification of the zonal master."""
    @property
    def regional_master_spec(self) -> global___RegionalMasterSpec:
        """Specification of the regional master."""
    version: builtins.str
    """Version of Kubernetes components that runs on the master."""
    @property
    def maintenance_policy(self) -> yandex.cloud.k8s.v1.cluster_pb2.MasterMaintenancePolicy:
        """Maintenance policy of the master."""
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Master security groups."""
    @property
    def master_logging(self) -> yandex.cloud.k8s.v1.cluster_pb2.MasterLogging:
        """Cloud Logging for master components."""
    def __init__(
        self,
        *,
        zonal_master_spec: global___ZonalMasterSpec | None = ...,
        regional_master_spec: global___RegionalMasterSpec | None = ...,
        version: builtins.str = ...,
        maintenance_policy: yandex.cloud.k8s.v1.cluster_pb2.MasterMaintenancePolicy | None = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        master_logging: yandex.cloud.k8s.v1.cluster_pb2.MasterLogging | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["maintenance_policy", b"maintenance_policy", "master_logging", b"master_logging", "master_type", b"master_type", "regional_master_spec", b"regional_master_spec", "zonal_master_spec", b"zonal_master_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["maintenance_policy", b"maintenance_policy", "master_logging", b"master_logging", "master_type", b"master_type", "regional_master_spec", b"regional_master_spec", "security_group_ids", b"security_group_ids", "version", b"version", "zonal_master_spec", b"zonal_master_spec"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["master_type", b"master_type"]) -> typing_extensions.Literal["zonal_master_spec", "regional_master_spec"] | None: ...

global___MasterSpec = MasterSpec

@typing_extensions.final
class ZonalMasterSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONE_ID_FIELD_NUMBER: builtins.int
    INTERNAL_V4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    EXTERNAL_V4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    zone_id: builtins.str
    """ID of the availability zone."""
    @property
    def internal_v4_address_spec(self) -> global___InternalAddressSpec:
        """Specification of parameters for internal IPv4 networking."""
    @property
    def external_v4_address_spec(self) -> global___ExternalAddressSpec:
        """Specification of parameters for external IPv4 networking."""
    def __init__(
        self,
        *,
        zone_id: builtins.str = ...,
        internal_v4_address_spec: global___InternalAddressSpec | None = ...,
        external_v4_address_spec: global___ExternalAddressSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["external_v4_address_spec", b"external_v4_address_spec", "internal_v4_address_spec", b"internal_v4_address_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["external_v4_address_spec", b"external_v4_address_spec", "internal_v4_address_spec", b"internal_v4_address_spec", "zone_id", b"zone_id"]) -> None: ...

global___ZonalMasterSpec = ZonalMasterSpec

@typing_extensions.final
class RegionalMasterSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGION_ID_FIELD_NUMBER: builtins.int
    LOCATIONS_FIELD_NUMBER: builtins.int
    EXTERNAL_V4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    EXTERNAL_V6_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    region_id: builtins.str
    """ID of the availability zone where the master resides."""
    @property
    def locations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MasterLocation]:
        """List of locations where the master will be allocated."""
    @property
    def external_v4_address_spec(self) -> global___ExternalAddressSpec:
        """Specify to allocate a static public IP for the master."""
    @property
    def external_v6_address_spec(self) -> global___ExternalAddressSpec:
        """Specification of parameters for external IPv6 networking."""
    def __init__(
        self,
        *,
        region_id: builtins.str = ...,
        locations: collections.abc.Iterable[global___MasterLocation] | None = ...,
        external_v4_address_spec: global___ExternalAddressSpec | None = ...,
        external_v6_address_spec: global___ExternalAddressSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["external_v4_address_spec", b"external_v4_address_spec", "external_v6_address_spec", b"external_v6_address_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["external_v4_address_spec", b"external_v4_address_spec", "external_v6_address_spec", b"external_v6_address_spec", "locations", b"locations", "region_id", b"region_id"]) -> None: ...

global___RegionalMasterSpec = RegionalMasterSpec

@typing_extensions.final
class InternalAddressSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the subnet. If no ID is specified, and there only one subnet in specified zone, an address in this subnet will be allocated."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet_id", b"subnet_id"]) -> None: ...

global___InternalAddressSpec = InternalAddressSpec

@typing_extensions.final
class ExternalAddressSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    """IP address."""
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address"]) -> None: ...

global___ExternalAddressSpec = ExternalAddressSpec

@typing_extensions.final
class MasterLocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONE_ID_FIELD_NUMBER: builtins.int
    INTERNAL_V4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    zone_id: builtins.str
    """ID of the availability zone."""
    @property
    def internal_v4_address_spec(self) -> global___InternalAddressSpec:
        """If not specified and there is a single subnet in specified zone, address
        in this subnet will be allocated.
        """
    def __init__(
        self,
        *,
        zone_id: builtins.str = ...,
        internal_v4_address_spec: global___InternalAddressSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["internal_v4_address_spec", b"internal_v4_address_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["internal_v4_address_spec", b"internal_v4_address_spec", "zone_id", b"zone_id"]) -> None: ...

global___MasterLocation = MasterLocation
