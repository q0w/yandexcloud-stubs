"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CreateIamTokenRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    YANDEX_PASSPORT_OAUTH_TOKEN_FIELD_NUMBER: builtins.int
    JWT_FIELD_NUMBER: builtins.int
    yandex_passport_oauth_token: builtins.str
    """OAuth token for a Yandex account.
    For more information, see [OAuth token](/docs/iam/concepts/authorization/oauth-token).
    """
    jwt: builtins.str
    """JSON Web Token (JWT) for a service account.
    For more information, see [Get IAM token for a service account](/docs/iam/operations/iam-token/create-for-sa).
    """
    def __init__(
        self,
        *,
        yandex_passport_oauth_token: builtins.str = ...,
        jwt: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["identity", b"identity", "jwt", b"jwt", "yandex_passport_oauth_token", b"yandex_passport_oauth_token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["identity", b"identity", "jwt", b"jwt", "yandex_passport_oauth_token", b"yandex_passport_oauth_token"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["identity", b"identity"]) -> typing_extensions.Literal["yandex_passport_oauth_token", "jwt"] | None: ...

global___CreateIamTokenRequest = CreateIamTokenRequest

class CreateIamTokenResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IAM_TOKEN_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    iam_token: builtins.str
    """IAM token for the specified identity.

    You should pass the token in the `Authorization` header for any further API requests.
    For example, `Authorization: Bearer [iam_token]`.
    """
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """IAM token expiration time."""
    def __init__(
        self,
        *,
        iam_token: builtins.str = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expires_at", b"expires_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expires_at", b"expires_at", "iam_token", b"iam_token"]) -> None: ...

global___CreateIamTokenResponse = CreateIamTokenResponse

class CreateIamTokenForServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["service_account_id", b"service_account_id"]) -> None: ...

global___CreateIamTokenForServiceAccountRequest = CreateIamTokenForServiceAccountRequest
