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

class AccessKey(google.protobuf.message.Message):
    """An access key.
    For more information, see [AWS-compatible access keys](/docs/iam/concepts/authorization/access-key).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    KEY_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the AccessKey resource.
    It is used to manage secret credentials: an access key ID and a secret access key.
    """
    service_account_id: builtins.str
    """ID of the service account that the access key belongs to."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
    description: builtins.str
    """Description of the access key. 0-256 characters long."""
    key_id: builtins.str
    """ID of the access key.
    The key is AWS compatible.
    """
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        service_account_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        description: builtins.str = ...,
        key_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "description", b"description", "id", b"id", "key_id", b"key_id", "service_account_id", b"service_account_id"]) -> None: ...

global___AccessKey = AccessKey
