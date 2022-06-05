"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FormatSchemaType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _FormatSchemaTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FormatSchemaType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FORMAT_SCHEMA_TYPE_UNSPECIFIED: _FormatSchemaType.ValueType  # 0
    FORMAT_SCHEMA_TYPE_PROTOBUF: _FormatSchemaType.ValueType  # 1
    FORMAT_SCHEMA_TYPE_CAPNPROTO: _FormatSchemaType.ValueType  # 2
class FormatSchemaType(_FormatSchemaType, metaclass=_FormatSchemaTypeEnumTypeWrapper):
    pass

FORMAT_SCHEMA_TYPE_UNSPECIFIED: FormatSchemaType.ValueType  # 0
FORMAT_SCHEMA_TYPE_PROTOBUF: FormatSchemaType.ValueType  # 1
FORMAT_SCHEMA_TYPE_CAPNPROTO: FormatSchemaType.ValueType  # 2
global___FormatSchemaType = FormatSchemaType


class FormatSchema(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    name: typing.Text
    cluster_id: typing.Text
    type: global___FormatSchemaType.ValueType
    uri: typing.Text
    def __init__(self,
        *,
        name: typing.Text = ...,
        cluster_id: typing.Text = ...,
        type: global___FormatSchemaType.ValueType = ...,
        uri: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","name",b"name","type",b"type","uri",b"uri"]) -> None: ...
global___FormatSchema = FormatSchema
