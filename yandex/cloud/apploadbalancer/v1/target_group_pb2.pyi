"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class TargetGroup(google.protobuf.message.Message):
    """A target group resource.
    For details about the concept, see [documentation](/docs/application-load-balancer/concepts/target-group).
    """

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

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the target group. Generated at creation time."""
    name: builtins.str
    """Name of the target group. The name is unique within the folder."""
    description: builtins.str
    """Description of the target group."""
    folder_id: builtins.str
    """ID of the folder that the target group belongs to."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Target group labels as `key:value` pairs.
        For details about the concept, see [documentation](/docs/overview/concepts/services#labels).
        """
    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Target]:
        """List of targets in the target group."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        folder_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        targets: collections.abc.Iterable[global___Target] | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "targets", b"targets"]) -> None: ...

global___TargetGroup = TargetGroup

class Target(google.protobuf.message.Message):
    """A target resource.
    For details about the concept, see [documentation](/docs/application-load-balancer/concepts/target-group).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IP_ADDRESS_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    PRIVATE_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    ip_address: builtins.str
    """IP address of the target."""
    subnet_id: builtins.str
    """ID of the subnet that the target is connected to."""
    private_ipv4_address: builtins.bool
    """If set, will not require `subnet_id` to validate the target.
    Instead, the address should belong to one of the following ranges:
    10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
    Only one of `subnet_id` or `private_ipv4_address` should be set.
    """
    def __init__(
        self,
        *,
        ip_address: builtins.str = ...,
        subnet_id: builtins.str = ...,
        private_ipv4_address: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address_type", b"address_type", "ip_address", b"ip_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_type", b"address_type", "ip_address", b"ip_address", "private_ipv4_address", b"private_ipv4_address", "subnet_id", b"subnet_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["address_type", b"address_type"]) -> typing_extensions.Literal["ip_address"] | None: ...

global___Target = Target
