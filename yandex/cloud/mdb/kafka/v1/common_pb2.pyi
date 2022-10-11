"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CompressionType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CompressionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CompressionType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    COMPRESSION_TYPE_UNSPECIFIED: _CompressionType.ValueType  # 0
    COMPRESSION_TYPE_UNCOMPRESSED: _CompressionType.ValueType  # 1
    """no codec (uncompressed)."""
    COMPRESSION_TYPE_ZSTD: _CompressionType.ValueType  # 2
    """Zstandard codec."""
    COMPRESSION_TYPE_LZ4: _CompressionType.ValueType  # 3
    """LZ4 codec."""
    COMPRESSION_TYPE_SNAPPY: _CompressionType.ValueType  # 4
    """Snappy codec."""
    COMPRESSION_TYPE_GZIP: _CompressionType.ValueType  # 5
    """GZip codec."""
    COMPRESSION_TYPE_PRODUCER: _CompressionType.ValueType  # 6
    """the codec to use is set by a producer (can be any of `ZSTD`, `LZ4`, `GZIP` or `SNAPPY` codecs)."""

class CompressionType(_CompressionType, metaclass=_CompressionTypeEnumTypeWrapper): ...

COMPRESSION_TYPE_UNSPECIFIED: CompressionType.ValueType  # 0
COMPRESSION_TYPE_UNCOMPRESSED: CompressionType.ValueType  # 1
"""no codec (uncompressed)."""
COMPRESSION_TYPE_ZSTD: CompressionType.ValueType  # 2
"""Zstandard codec."""
COMPRESSION_TYPE_LZ4: CompressionType.ValueType  # 3
"""LZ4 codec."""
COMPRESSION_TYPE_SNAPPY: CompressionType.ValueType  # 4
"""Snappy codec."""
COMPRESSION_TYPE_GZIP: CompressionType.ValueType  # 5
"""GZip codec."""
COMPRESSION_TYPE_PRODUCER: CompressionType.ValueType  # 6
"""the codec to use is set by a producer (can be any of `ZSTD`, `LZ4`, `GZIP` or `SNAPPY` codecs)."""
global___CompressionType = CompressionType

class _SaslMechanism:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SaslMechanismEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SaslMechanism.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SASL_MECHANISM_UNSPECIFIED: _SaslMechanism.ValueType  # 0
    SASL_MECHANISM_SCRAM_SHA_256: _SaslMechanism.ValueType  # 1
    SASL_MECHANISM_SCRAM_SHA_512: _SaslMechanism.ValueType  # 2

class SaslMechanism(_SaslMechanism, metaclass=_SaslMechanismEnumTypeWrapper): ...

SASL_MECHANISM_UNSPECIFIED: SaslMechanism.ValueType  # 0
SASL_MECHANISM_SCRAM_SHA_256: SaslMechanism.ValueType  # 1
SASL_MECHANISM_SCRAM_SHA_512: SaslMechanism.ValueType  # 2
global___SaslMechanism = SaslMechanism
