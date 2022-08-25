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
import yandex.cloud.datatransfer.v1.endpoint_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENDPOINT_ID_FIELD_NUMBER: builtins.int
    endpoint_id: builtins.str
    def __init__(
        self,
        *,
        endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_id", b"endpoint_id"]) -> None: ...

global___GetEndpointRequest = GetEndpointRequest

class ListEndpointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Identifier of the folder containing the endpoints to be listed."""
    page_size: builtins.int
    """The maximum number of endpoints to be sent in the response message. If the
    folder contains more endpoints than page_size, next_page_token will be included
    in the response message. Include it into the subsequent ListEndpointRequest to
    fetch the next page. Defaults to 100 if not specified. The maximum allowed value
    for this field is 500.
    """
    page_token: builtins.str
    """Opaque value identifying the endpoints page to be fetched. Should be empty in
    the first ListEndpointsRequest. Subsequent request should have this field filled
    with the next_page_token from the previous ListEndpointsResponse.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListEndpointsRequest = ListEndpointsRequest

class ListEndpointsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENDPOINTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datatransfer.v1.endpoint_pb2.Endpoint]:
        """The list of endpoints. If there are more endpoints in the folder, then
        next_page_token is a non-empty string to be included into the subsequent
        ListEndpointsRequest to fetch the next endpoints page.
        """
    next_page_token: builtins.str
    """Opaque value identifying the next endpoints page. This field is empty if there
    are no more endpoints in the folder. Otherwise it is non-empty and should be
    included in the subsequent ListEndpointsRequest to fetch the next endpoints
    page.
    """
    def __init__(
        self,
        *,
        endpoints: collections.abc.Iterable[yandex.cloud.datatransfer.v1.endpoint_pb2.Endpoint] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoints", b"endpoints", "next_page_token", b"next_page_token"]) -> None: ...

global___ListEndpointsResponse = ListEndpointsResponse

class CreateEndpointRequest(google.protobuf.message.Message):
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
    SETTINGS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    name: builtins.str
    description: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def settings(self) -> yandex.cloud.datatransfer.v1.endpoint_pb2.EndpointSettings: ...
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        settings: yandex.cloud.datatransfer.v1.endpoint_pb2.EndpointSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "settings", b"settings"]) -> None: ...

global___CreateEndpointRequest = CreateEndpointRequest

class CreateEndpointMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENDPOINT_ID_FIELD_NUMBER: builtins.int
    endpoint_id: builtins.str
    def __init__(
        self,
        *,
        endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_id", b"endpoint_id"]) -> None: ...

global___CreateEndpointMetadata = CreateEndpointMetadata

class UpdateEndpointRequest(google.protobuf.message.Message):
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

    ENDPOINT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    endpoint_id: builtins.str
    """Identifier of the endpoint to be updated."""
    name: builtins.str
    """The new endpoint name. Must be unique within the folder."""
    description: builtins.str
    """The new description for the endpoint."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def settings(self) -> yandex.cloud.datatransfer.v1.endpoint_pb2.EndpointSettings:
        """The new endpoint name. Must be unique within the folder."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask specifying endpoint fields to be updated. Semantics for this field is
        described here:
        https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask
        The only exception is that if the repeated field is specified in the mask, then
        the new value replaces the old one instead of being appended to the old one.
        """
    def __init__(
        self,
        *,
        endpoint_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        settings: yandex.cloud.datatransfer.v1.endpoint_pb2.EndpointSettings | None = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["settings", b"settings", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "endpoint_id", b"endpoint_id", "labels", b"labels", "name", b"name", "settings", b"settings", "update_mask", b"update_mask"]) -> None: ...

global___UpdateEndpointRequest = UpdateEndpointRequest

class UpdateEndpointMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENDPOINT_ID_FIELD_NUMBER: builtins.int
    endpoint_id: builtins.str
    def __init__(
        self,
        *,
        endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_id", b"endpoint_id"]) -> None: ...

global___UpdateEndpointMetadata = UpdateEndpointMetadata

class DeleteEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENDPOINT_ID_FIELD_NUMBER: builtins.int
    endpoint_id: builtins.str
    def __init__(
        self,
        *,
        endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_id", b"endpoint_id"]) -> None: ...

global___DeleteEndpointRequest = DeleteEndpointRequest

class DeleteEndpointMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENDPOINT_ID_FIELD_NUMBER: builtins.int
    endpoint_id: builtins.str
    def __init__(
        self,
        *,
        endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_id", b"endpoint_id"]) -> None: ...

global___DeleteEndpointMetadata = DeleteEndpointMetadata
