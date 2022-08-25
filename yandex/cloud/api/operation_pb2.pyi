"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.descriptor_pb2
import google.protobuf.internal.extension_dict
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Operation(google.protobuf.message.Message):
    """Operation is annotation for rpc that returns longrunning operation, describes
    message types that will be returned in metadata [google.protobuf.Any], and
    in response [google.protobuf.Any] (for successful operation).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    RESPONSE_FIELD_NUMBER: builtins.int
    metadata: builtins.str
    """Optional. If present, rpc returns operation which metadata field will
    contains message of specified type.
    Optional.
    """
    response: builtins.str
    """Required. rpc returns operation, in case of success response will contains message of
    specified field.
    Required.
    """
    def __init__(
        self,
        *,
        metadata: builtins.str = ...,
        response: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "response", b"response"]) -> None: ...

global___Operation = Operation

OPERATION_FIELD_NUMBER: builtins.int
operation: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.MethodOptions, global___Operation]
