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

class GetUserAccountByLoginRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOGIN_FIELD_NUMBER: builtins.int
    login: builtins.str
    """Login of the YandexPassportUserAccount resource to return."""
    def __init__(
        self,
        *,
        login: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["login", b"login"]) -> None: ...

global___GetUserAccountByLoginRequest = GetUserAccountByLoginRequest
