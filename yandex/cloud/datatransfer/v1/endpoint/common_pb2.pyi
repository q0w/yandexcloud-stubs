"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.empty_pb2
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ObjectTransferStage:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ObjectTransferStageEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ObjectTransferStage.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OBJECT_TRANSFER_STAGE_UNSPECIFIED: _ObjectTransferStage.ValueType  # 0
    BEFORE_DATA: _ObjectTransferStage.ValueType  # 1
    AFTER_DATA: _ObjectTransferStage.ValueType  # 2
    NEVER: _ObjectTransferStage.ValueType  # 3

class ObjectTransferStage(_ObjectTransferStage, metaclass=_ObjectTransferStageEnumTypeWrapper): ...

OBJECT_TRANSFER_STAGE_UNSPECIFIED: ObjectTransferStage.ValueType  # 0
BEFORE_DATA: ObjectTransferStage.ValueType  # 1
AFTER_DATA: ObjectTransferStage.ValueType  # 2
NEVER: ObjectTransferStage.ValueType  # 3
global___ObjectTransferStage = ObjectTransferStage

class _CleanupPolicy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CleanupPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CleanupPolicy.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CLEANUP_POLICY_UNSPECIFIED: _CleanupPolicy.ValueType  # 0
    DISABLED: _CleanupPolicy.ValueType  # 1
    DROP: _CleanupPolicy.ValueType  # 2
    TRUNCATE: _CleanupPolicy.ValueType  # 3

class CleanupPolicy(_CleanupPolicy, metaclass=_CleanupPolicyEnumTypeWrapper): ...

CLEANUP_POLICY_UNSPECIFIED: CleanupPolicy.ValueType  # 0
DISABLED: CleanupPolicy.ValueType  # 1
DROP: CleanupPolicy.ValueType  # 2
TRUNCATE: CleanupPolicy.ValueType  # 3
global___CleanupPolicy = CleanupPolicy

class AltName(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FROM_NAME_FIELD_NUMBER: builtins.int
    TO_NAME_FIELD_NUMBER: builtins.int
    from_name: builtins.str
    """From table name"""
    to_name: builtins.str
    """To table name"""
    def __init__(
        self,
        *,
        from_name: builtins.str = ...,
        to_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["from_name", b"from_name", "to_name", b"to_name"]) -> None: ...

global___AltName = AltName

class Secret(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RAW_FIELD_NUMBER: builtins.int
    raw: builtins.str
    """Password"""
    def __init__(
        self,
        *,
        raw: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["raw", b"raw", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["raw", b"raw", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value", b"value"]) -> typing_extensions.Literal["raw"] | None: ...

global___Secret = Secret

class TLSMode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISABLED_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    @property
    def disabled(self) -> google.protobuf.empty_pb2.Empty: ...
    @property
    def enabled(self) -> global___TLSConfig: ...
    def __init__(
        self,
        *,
        disabled: google.protobuf.empty_pb2.Empty | None = ...,
        enabled: global___TLSConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disabled", b"disabled", "enabled", b"enabled", "tls_mode", b"tls_mode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["disabled", b"disabled", "enabled", b"enabled", "tls_mode", b"tls_mode"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["tls_mode", b"tls_mode"]) -> typing_extensions.Literal["disabled", "enabled"] | None: ...

global___TLSMode = TLSMode

class TLSConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CA_CERTIFICATE_FIELD_NUMBER: builtins.int
    ca_certificate: builtins.str
    """CA certificate

    X.509 certificate of the certificate authority which issued the server's
    certificate, in PEM format. When CA certificate is specified TLS is used to
    connect to the server.
    """
    def __init__(
        self,
        *,
        ca_certificate: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ca_certificate", b"ca_certificate"]) -> None: ...

global___TLSConfig = TLSConfig

class ColumnValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STRING_VALUE_FIELD_NUMBER: builtins.int
    string_value: builtins.str
    def __init__(
        self,
        *,
        string_value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["string_value", b"string_value", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["string_value", b"string_value", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value", b"value"]) -> typing_extensions.Literal["string_value"] | None: ...

global___ColumnValue = ColumnValue
