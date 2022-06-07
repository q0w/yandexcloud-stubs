"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Gateway(google.protobuf.message.Message):
    """A Gateway resource. For more information, see [Gateway](/docs/vpc/concepts/gateway)."""
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

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SHARED_EGRESS_GATEWAY_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the gateway. Generated at creation time."""

    folder_id: typing.Text
    """ID of the folder that the gateway belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    name: typing.Text
    """Name of the gateway.
    The name is unique within the folder.
    """

    description: typing.Text
    """Description of the gateway."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs."""
        pass
    @property
    def shared_egress_gateway(self) -> global___SharedEgressGateway: ...
    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        shared_egress_gateway: typing.Optional[global___SharedEgressGateway] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","gateway",b"gateway","shared_egress_gateway",b"shared_egress_gateway"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","description",b"description","folder_id",b"folder_id","gateway",b"gateway","id",b"id","labels",b"labels","name",b"name","shared_egress_gateway",b"shared_egress_gateway"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["gateway",b"gateway"]) -> typing.Optional[typing_extensions.Literal["shared_egress_gateway"]]: ...
global___Gateway = Gateway

class SharedEgressGateway(google.protobuf.message.Message):
    """Shared Egress Gateway configuration"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___SharedEgressGateway = SharedEgressGateway