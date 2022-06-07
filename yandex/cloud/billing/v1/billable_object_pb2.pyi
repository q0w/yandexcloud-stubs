"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class BillableObject(google.protobuf.message.Message):
    """Represents a link to an object in other service.
    This object is being billed in the scope of a billing account.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the object in other service."""

    type: typing.Text
    """Billable object type. Can be one of the following:
    * `cloud`
    """

    def __init__(self,
        *,
        id: typing.Text = ...,
        type: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","type",b"type"]) -> None: ...
global___BillableObject = BillableObject

class BillableObjectBinding(google.protobuf.message.Message):
    """Represents a binding of the BillableObject to a BillingAccount."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EFFECTIVE_TIME_FIELD_NUMBER: builtins.int
    BILLABLE_OBJECT_FIELD_NUMBER: builtins.int
    @property
    def effective_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp when binding was created."""
        pass
    @property
    def billable_object(self) -> global___BillableObject:
        """Object that is bound to billing account."""
        pass
    def __init__(self,
        *,
        effective_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        billable_object: typing.Optional[global___BillableObject] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["billable_object",b"billable_object","effective_time",b"effective_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["billable_object",b"billable_object","effective_time",b"effective_time"]) -> None: ...
global___BillableObjectBinding = BillableObjectBinding