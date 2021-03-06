"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetFolderBudgetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to get a budget for."""

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id"]) -> None: ...
global___GetFolderBudgetRequest = GetFolderBudgetRequest

class GetFolderBudgetResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UNIT_BALANCE_FIELD_NUMBER: builtins.int
    MAX_UNITS_PER_HOUR_FIELD_NUMBER: builtins.int
    MAX_UNITS_PER_EXECUTION_FIELD_NUMBER: builtins.int
    @property
    def unit_balance(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of units available in the folder."""
        pass
    @property
    def max_units_per_hour(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of units that can be spent per hour."""
        pass
    @property
    def max_units_per_execution(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of units that can be spent on one execution."""
        pass
    def __init__(self,
        *,
        unit_balance: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        max_units_per_hour: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        max_units_per_execution: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["max_units_per_execution",b"max_units_per_execution","max_units_per_hour",b"max_units_per_hour","unit_balance",b"unit_balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_units_per_execution",b"max_units_per_execution","max_units_per_hour",b"max_units_per_hour","unit_balance",b"unit_balance"]) -> None: ...
global___GetFolderBudgetResponse = GetFolderBudgetResponse

class SetFolderBudgetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    SET_MASK_FIELD_NUMBER: builtins.int
    UNIT_BALANCE_FIELD_NUMBER: builtins.int
    MAX_UNITS_PER_HOUR_FIELD_NUMBER: builtins.int
    MAX_UNITS_PER_EXECUTION_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to set a budget for."""

    @property
    def set_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the budget are going to be set."""
        pass
    @property
    def unit_balance(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of units available in the folder."""
        pass
    @property
    def max_units_per_hour(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of units that can be spent per hour."""
        pass
    @property
    def max_units_per_execution(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of units that can be spent on one execution."""
        pass
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        set_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        unit_balance: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        max_units_per_hour: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        max_units_per_execution: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["max_units_per_execution",b"max_units_per_execution","max_units_per_hour",b"max_units_per_hour","set_mask",b"set_mask","unit_balance",b"unit_balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id","max_units_per_execution",b"max_units_per_execution","max_units_per_hour",b"max_units_per_hour","set_mask",b"set_mask","unit_balance",b"unit_balance"]) -> None: ...
global___SetFolderBudgetRequest = SetFolderBudgetRequest
