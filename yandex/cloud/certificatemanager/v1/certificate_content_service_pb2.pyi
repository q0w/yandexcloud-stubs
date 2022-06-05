"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetCertificateContentResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    CERTIFICATE_CHAIN_FIELD_NUMBER: builtins.int
    PRIVATE_KEY_FIELD_NUMBER: builtins.int
    certificate_id: typing.Text
    """ID of the certificate."""

    @property
    def certificate_chain(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """PEM-encoded certificate chain content of the certificate."""
        pass
    private_key: typing.Text
    """PEM-encoded private key content of the certificate."""

    def __init__(self,
        *,
        certificate_id: typing.Text = ...,
        certificate_chain: typing.Optional[typing.Iterable[typing.Text]] = ...,
        private_key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_chain",b"certificate_chain","certificate_id",b"certificate_id","private_key",b"private_key"]) -> None: ...
global___GetCertificateContentResponse = GetCertificateContentResponse

class GetCertificateContentRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    certificate_id: typing.Text
    """ID of the certificate to download content."""

    version_id: typing.Text
    """Optional ID of the version."""

    def __init__(self,
        *,
        certificate_id: typing.Text = ...,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_id",b"certificate_id","version_id",b"version_id"]) -> None: ...
global___GetCertificateContentRequest = GetCertificateContentRequest
