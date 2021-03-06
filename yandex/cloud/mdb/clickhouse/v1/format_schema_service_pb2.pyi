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
import yandex.cloud.mdb.clickhouse.v1.format_schema_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetFormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    format_schema_name: typing.Text
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        format_schema_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","format_schema_name",b"format_schema_name"]) -> None: ...
global___GetFormatSchemaRequest = GetFormatSchemaRequest

class ListFormatSchemasRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    page_size: builtins.int
    page_token: typing.Text
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListFormatSchemasRequest = ListFormatSchemasRequest

class ListFormatSchemasResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FORMAT_SCHEMAS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def format_schemas(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchema]: ...
    next_page_token: typing.Text
    def __init__(self,
        *,
        format_schemas: typing.Optional[typing.Iterable[yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchema]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["format_schemas",b"format_schemas","next_page_token",b"next_page_token"]) -> None: ...
global___ListFormatSchemasResponse = ListFormatSchemasResponse

class CreateFormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    format_schema_name: typing.Text
    type: yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchemaType.ValueType
    uri: typing.Text
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        format_schema_name: typing.Text = ...,
        type: yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchemaType.ValueType = ...,
        uri: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","format_schema_name",b"format_schema_name","type",b"type","uri",b"uri"]) -> None: ...
global___CreateFormatSchemaRequest = CreateFormatSchemaRequest

class CreateFormatSchemaMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    format_schema_name: typing.Text
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        format_schema_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","format_schema_name",b"format_schema_name"]) -> None: ...
global___CreateFormatSchemaMetadata = CreateFormatSchemaMetadata

class UpdateFormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    format_schema_name: typing.Text
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    uri: typing.Text
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        format_schema_name: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        uri: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","format_schema_name",b"format_schema_name","update_mask",b"update_mask","uri",b"uri"]) -> None: ...
global___UpdateFormatSchemaRequest = UpdateFormatSchemaRequest

class UpdateFormatSchemaMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    format_schema_name: typing.Text
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        format_schema_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","format_schema_name",b"format_schema_name"]) -> None: ...
global___UpdateFormatSchemaMetadata = UpdateFormatSchemaMetadata

class DeleteFormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    format_schema_name: typing.Text
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        format_schema_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","format_schema_name",b"format_schema_name"]) -> None: ...
global___DeleteFormatSchemaRequest = DeleteFormatSchemaRequest

class DeleteFormatSchemaMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    format_schema_name: typing.Text
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        format_schema_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","format_schema_name",b"format_schema_name"]) -> None: ...
global___DeleteFormatSchemaMetadata = DeleteFormatSchemaMetadata
