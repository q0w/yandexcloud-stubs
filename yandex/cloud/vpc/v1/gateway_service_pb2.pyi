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
import yandex.cloud.operation.operation_pb2
import yandex.cloud.vpc.v1.gateway_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetGatewayRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    """ID of the Gateway resource to return.

    To get Gateway resource ID make a [GatewayService.List] request.
    """

    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gateway_id",b"gateway_id"]) -> None: ...
global___GetGatewayRequest = GetGatewayRequest

class ListGatewaysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list gateways in.

    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListGatewaysResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set `page_token` to the
    [ListGatewaysResponse.next_page_token] returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters Gateway listed in the response.

    The expression must specify:
    1. The field name. Currently you can use filtering only on [Gateway.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    Example of a filter: `name=my-gateway`.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListGatewaysRequest = ListGatewaysRequest

class ListGatewaysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAYS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def gateways(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.gateway_pb2.Gateway]:
        """List of gateways."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListGatewaysRequest.page_size], use `next_page_token` as the value
    for the [ListGatewaysRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        gateways: typing.Optional[typing.Iterable[yandex.cloud.vpc.v1.gateway_pb2.Gateway]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gateways",b"gateways","next_page_token",b"next_page_token"]) -> None: ...
global___ListGatewaysResponse = ListGatewaysResponse

class ListGatewayOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    """ID of the gateway to list operations for.

    To get a gateway ID make a [GatewayService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListGatewayOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListGatewayOperationsResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gateway_id",b"gateway_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListGatewayOperationsRequest = ListGatewayOperationsRequest

class ListGatewayOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified gateway."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListGatewayOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListGatewayOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListGatewayOperationsResponse = ListGatewayOperationsResponse

class SharedEgressGatewaySpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___SharedEgressGatewaySpec = SharedEgressGatewaySpec

class CreateGatewayRequest(google.protobuf.message.Message):
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
    SHARED_EGRESS_GATEWAY_SPEC_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to create a gateway in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    name: typing.Text
    """Name of the gateway.
    The name must be unique within the folder.
    """

    description: typing.Text
    """Description of the gateway."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Gateway labels as `key:value` pairs."""
        pass
    @property
    def shared_egress_gateway_spec(self) -> global___SharedEgressGatewaySpec: ...
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        shared_egress_gateway_spec: typing.Optional[global___SharedEgressGatewaySpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gateway",b"gateway","shared_egress_gateway_spec",b"shared_egress_gateway_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","folder_id",b"folder_id","gateway",b"gateway","labels",b"labels","name",b"name","shared_egress_gateway_spec",b"shared_egress_gateway_spec"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["gateway",b"gateway"]) -> typing.Optional[typing_extensions.Literal["shared_egress_gateway_spec"]]: ...
global___CreateGatewayRequest = CreateGatewayRequest

class CreateGatewayMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    """ID of the gateway that is being created."""

    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gateway_id",b"gateway_id"]) -> None: ...
global___CreateGatewayMetadata = CreateGatewayMetadata

class UpdateGatewayRequest(google.protobuf.message.Message):
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

    GATEWAY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SHARED_EGRESS_GATEWAY_SPEC_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    """ID of the gateway to update.

    To get the gateway ID make a [GatewayService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the Gateway should be updated."""
        pass
    name: typing.Text
    """New name for the gateway.
    The name must be unique within the folder.
    """

    description: typing.Text
    """New description of the gateway."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Gateway labels as `key:value` pairs.

        Existing set of labels is completely replaced by the provided set, so if you just want
        to add or remove a label:
        1. Get the current set of labels with a [GatewayService.Get] request.
        2. Add or remove a label in this set.
        3. Send the new set in this field.
        """
        pass
    @property
    def shared_egress_gateway_spec(self) -> global___SharedEgressGatewaySpec: ...
    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        shared_egress_gateway_spec: typing.Optional[global___SharedEgressGatewaySpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gateway",b"gateway","shared_egress_gateway_spec",b"shared_egress_gateway_spec","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","gateway",b"gateway","gateway_id",b"gateway_id","labels",b"labels","name",b"name","shared_egress_gateway_spec",b"shared_egress_gateway_spec","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["gateway",b"gateway"]) -> typing.Optional[typing_extensions.Literal["shared_egress_gateway_spec"]]: ...
global___UpdateGatewayRequest = UpdateGatewayRequest

class UpdateGatewayMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    """ID of the Gateway that is being updated."""

    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gateway_id",b"gateway_id"]) -> None: ...
global___UpdateGatewayMetadata = UpdateGatewayMetadata

class DeleteGatewayRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    """ID of the gateway to delete.

    To get a gateway ID make a [GatewayService.List] request.
    """

    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gateway_id",b"gateway_id"]) -> None: ...
global___DeleteGatewayRequest = DeleteGatewayRequest

class DeleteGatewayMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    """ID of the gateway that is being deleted."""

    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gateway_id",b"gateway_id"]) -> None: ...
global___DeleteGatewayMetadata = DeleteGatewayMetadata

class MoveGatewayRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    destination_folder_id: typing.Text
    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        destination_folder_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["destination_folder_id",b"destination_folder_id","gateway_id",b"gateway_id"]) -> None: ...
global___MoveGatewayRequest = MoveGatewayRequest

class MoveGatewayMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    gateway_id: typing.Text
    def __init__(self,
        *,
        gateway_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gateway_id",b"gateway_id"]) -> None: ...
global___MoveGatewayMetadata = MoveGatewayMetadata
