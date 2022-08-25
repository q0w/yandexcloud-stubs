"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ValidationContext(google.protobuf.message.Message):
    """A TLS validation context resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRUSTED_CA_ID_FIELD_NUMBER: builtins.int
    TRUSTED_CA_BYTES_FIELD_NUMBER: builtins.int
    trusted_ca_id: builtins.str
    trusted_ca_bytes: builtins.str
    """X.509 certificate contents in PEM format."""
    def __init__(
        self,
        *,
        trusted_ca_id: builtins.str = ...,
        trusted_ca_bytes: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["trusted_ca", b"trusted_ca", "trusted_ca_bytes", b"trusted_ca_bytes", "trusted_ca_id", b"trusted_ca_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["trusted_ca", b"trusted_ca", "trusted_ca_bytes", b"trusted_ca_bytes", "trusted_ca_id", b"trusted_ca_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["trusted_ca", b"trusted_ca"]) -> typing_extensions.Literal["trusted_ca_id", "trusted_ca_bytes"] | None: ...

global___ValidationContext = ValidationContext
