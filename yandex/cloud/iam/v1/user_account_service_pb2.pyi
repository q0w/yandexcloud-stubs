"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetUserAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    user_account_id: typing.Text
    """ID of the UserAccount resource to return."""

    def __init__(self,
        *,
        user_account_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_account_id",b"user_account_id"]) -> None: ...
global___GetUserAccountRequest = GetUserAccountRequest