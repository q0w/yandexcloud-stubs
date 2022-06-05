"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions
import yandex.cloud.dataproc.v1.common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Role:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _RoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Role.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ROLE_UNSPECIFIED: _Role.ValueType  # 0
    MASTERNODE: _Role.ValueType  # 1
    """The subcluster fulfills the master role.

    Master can run the following services, depending on the requested components:
    * HDFS: Namenode, Secondary Namenode
    * YARN: ResourceManager, Timeline Server
    * HBase Master
    * Hive: Server, Metastore, HCatalog
    * Spark History Server
    * Zeppelin
    * ZooKeeper
    """

    DATANODE: _Role.ValueType  # 2
    """The subcluster is a DATANODE in a Data Proc cluster.

    DATANODE can run the following services, depending on the requested components:
    * HDFS DataNode
    * YARN NodeManager
    * HBase RegionServer
    * Spark libraries
    """

    COMPUTENODE: _Role.ValueType  # 3
    """The subcluster is a COMPUTENODE in a Data Proc cluster.

    COMPUTENODE can run the following services, depending on the requested components:
    * YARN NodeManager
    * Spark libraries
    """

class Role(_Role, metaclass=_RoleEnumTypeWrapper):
    pass

ROLE_UNSPECIFIED: Role.ValueType  # 0
MASTERNODE: Role.ValueType  # 1
"""The subcluster fulfills the master role.

Master can run the following services, depending on the requested components:
* HDFS: Namenode, Secondary Namenode
* YARN: ResourceManager, Timeline Server
* HBase Master
* Hive: Server, Metastore, HCatalog
* Spark History Server
* Zeppelin
* ZooKeeper
"""

DATANODE: Role.ValueType  # 2
"""The subcluster is a DATANODE in a Data Proc cluster.

DATANODE can run the following services, depending on the requested components:
* HDFS DataNode
* YARN NodeManager
* HBase RegionServer
* Spark libraries
"""

COMPUTENODE: Role.ValueType  # 3
"""The subcluster is a COMPUTENODE in a Data Proc cluster.

COMPUTENODE can run the following services, depending on the requested components:
* YARN NodeManager
* Spark libraries
"""

global___Role = Role


class AutoscalingConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MAX_HOSTS_COUNT_FIELD_NUMBER: builtins.int
    PREEMPTIBLE_FIELD_NUMBER: builtins.int
    MEASUREMENT_DURATION_FIELD_NUMBER: builtins.int
    WARMUP_DURATION_FIELD_NUMBER: builtins.int
    STABILIZATION_DURATION_FIELD_NUMBER: builtins.int
    CPU_UTILIZATION_TARGET_FIELD_NUMBER: builtins.int
    DECOMMISSION_TIMEOUT_FIELD_NUMBER: builtins.int
    max_hosts_count: builtins.int
    """Upper limit for total instance subcluster count."""

    preemptible: builtins.bool
    """Preemptible instances are stopped at least once every 24 hours, and can be stopped at any time
    if their resources are needed by Compute.
    For more information, see [Preemptible Virtual Machines](/docs/compute/concepts/preemptible-vm).
    """

    @property
    def measurement_duration(self) -> google.protobuf.duration_pb2.Duration:
        """Time in seconds allotted for averaging metrics."""
        pass
    @property
    def warmup_duration(self) -> google.protobuf.duration_pb2.Duration:
        """The warmup time of the instance in seconds. During this time,
        traffic is sent to the instance, but instance metrics are not collected.
        """
        pass
    @property
    def stabilization_duration(self) -> google.protobuf.duration_pb2.Duration:
        """Minimum amount of time in seconds allotted for monitoring before
        Instance Groups can reduce the number of instances in the group.
        During this time, the group size doesn't decrease, even if the new metric values
        indicate that it should.
        """
        pass
    cpu_utilization_target: builtins.float
    """Defines an autoscaling rule based on the average CPU utilization of the instance group."""

    decommission_timeout: builtins.int
    """Timeout to gracefully decommission nodes during downscaling. In seconds. Default value: 120"""

    def __init__(self,
        *,
        max_hosts_count: builtins.int = ...,
        preemptible: builtins.bool = ...,
        measurement_duration: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        warmup_duration: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        stabilization_duration: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        cpu_utilization_target: builtins.float = ...,
        decommission_timeout: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["measurement_duration",b"measurement_duration","stabilization_duration",b"stabilization_duration","warmup_duration",b"warmup_duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cpu_utilization_target",b"cpu_utilization_target","decommission_timeout",b"decommission_timeout","max_hosts_count",b"max_hosts_count","measurement_duration",b"measurement_duration","preemptible",b"preemptible","stabilization_duration",b"stabilization_duration","warmup_duration",b"warmup_duration"]) -> None: ...
global___AutoscalingConfig = AutoscalingConfig

class Subcluster(google.protobuf.message.Message):
    """A Data Proc subcluster. For details about the concept, see [documentation](/docs/data-proc/concepts/)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    HOSTS_COUNT_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    AUTOSCALING_CONFIG_FIELD_NUMBER: builtins.int
    INSTANCE_GROUP_ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the subcluster. Generated at creation time."""

    cluster_id: typing.Text
    """ID of the Data Proc cluster that the subcluster belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    name: typing.Text
    """Name of the subcluster. The name is unique within the cluster."""

    role: global___Role.ValueType
    """Role that is fulfilled by hosts of the subcluster."""

    @property
    def resources(self) -> yandex.cloud.dataproc.v1.common_pb2.Resources:
        """Resources allocated for each host in the subcluster."""
        pass
    subnet_id: typing.Text
    """ID of the VPC subnet used for hosts in the subcluster."""

    hosts_count: builtins.int
    """Number of hosts in the subcluster."""

    assign_public_ip: builtins.bool
    """Assign public ip addresses for all hosts in subcluter."""

    @property
    def autoscaling_config(self) -> global___AutoscalingConfig:
        """Configuration for instance group based subclusters"""
        pass
    instance_group_id: typing.Text
    """ID of Compute Instance Group for autoscaling subclusters"""

    def __init__(self,
        *,
        id: typing.Text = ...,
        cluster_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        role: global___Role.ValueType = ...,
        resources: typing.Optional[yandex.cloud.dataproc.v1.common_pb2.Resources] = ...,
        subnet_id: typing.Text = ...,
        hosts_count: builtins.int = ...,
        assign_public_ip: builtins.bool = ...,
        autoscaling_config: typing.Optional[global___AutoscalingConfig] = ...,
        instance_group_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["autoscaling_config",b"autoscaling_config","created_at",b"created_at","resources",b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_public_ip",b"assign_public_ip","autoscaling_config",b"autoscaling_config","cluster_id",b"cluster_id","created_at",b"created_at","hosts_count",b"hosts_count","id",b"id","instance_group_id",b"instance_group_id","name",b"name","resources",b"resources","role",b"role","subnet_id",b"subnet_id"]) -> None: ...
global___Subcluster = Subcluster

class Host(google.protobuf.message.Message):
    """A Data Proc host. For details about the concept, see [documentation](/docs/data-proc/concepts/)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    SUBCLUSTER_ID_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the Data Proc host. The host name is assigned by Data Proc at creation time
    and cannot be changed. The name is generated to be unique across all existing Data Proc
    hosts in Yandex Cloud, as it defines the FQDN of the host.
    """

    subcluster_id: typing.Text
    """ID of the Data Proc subcluster that the host belongs to."""

    health: yandex.cloud.dataproc.v1.common_pb2.Health.ValueType
    """Status code of the aggregated health of the host."""

    compute_instance_id: typing.Text
    """ID of the Compute virtual machine that is used as the Data Proc host."""

    role: global___Role.ValueType
    """Role of the host in the cluster."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        subcluster_id: typing.Text = ...,
        health: yandex.cloud.dataproc.v1.common_pb2.Health.ValueType = ...,
        compute_instance_id: typing.Text = ...,
        role: global___Role.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_instance_id",b"compute_instance_id","health",b"health","name",b"name","role",b"role","subcluster_id",b"subcluster_id"]) -> None: ...
global___Host = Host
