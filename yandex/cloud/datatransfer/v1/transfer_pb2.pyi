"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.datatransfer.v1.endpoint_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _TransferType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _TransferTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TransferType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TRANSFER_TYPE_UNSPECIFIED: _TransferType.ValueType  # 0
    SNAPSHOT_AND_INCREMENT: _TransferType.ValueType  # 1
    """Snapshot and increment"""

    SNAPSHOT_ONLY: _TransferType.ValueType  # 2
    """Snapshot"""

    INCREMENT_ONLY: _TransferType.ValueType  # 3
    """Increment"""

class TransferType(_TransferType, metaclass=_TransferTypeEnumTypeWrapper):
    pass

TRANSFER_TYPE_UNSPECIFIED: TransferType.ValueType  # 0
SNAPSHOT_AND_INCREMENT: TransferType.ValueType  # 1
"""Snapshot and increment"""

SNAPSHOT_ONLY: TransferType.ValueType  # 2
"""Snapshot"""

INCREMENT_ONLY: TransferType.ValueType  # 3
"""Increment"""

global___TransferType = TransferType


class _TransferStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _TransferStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TransferStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TRANSFER_STATUS_UNSPECIFIED: _TransferStatus.ValueType  # 0
    CREATING: _TransferStatus.ValueType  # 1
    CREATED: _TransferStatus.ValueType  # 2
    RUNNING: _TransferStatus.ValueType  # 3
    STOPPING: _TransferStatus.ValueType  # 4
    STOPPED: _TransferStatus.ValueType  # 5
    ERROR: _TransferStatus.ValueType  # 6
    SNAPSHOTTING: _TransferStatus.ValueType  # 7
    DONE: _TransferStatus.ValueType  # 8
class TransferStatus(_TransferStatus, metaclass=_TransferStatusEnumTypeWrapper):
    pass

TRANSFER_STATUS_UNSPECIFIED: TransferStatus.ValueType  # 0
CREATING: TransferStatus.ValueType  # 1
CREATED: TransferStatus.ValueType  # 2
RUNNING: TransferStatus.ValueType  # 3
STOPPING: TransferStatus.ValueType  # 4
STOPPED: TransferStatus.ValueType  # 5
ERROR: TransferStatus.ValueType  # 6
SNAPSHOTTING: TransferStatus.ValueType  # 7
DONE: TransferStatus.ValueType  # 8
global___TransferStatus = TransferStatus


class Transfer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    WARNING_FIELD_NUMBER: builtins.int
    id: typing.Text
    folder_id: typing.Text
    name: typing.Text
    description: typing.Text
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    @property
    def source(self) -> yandex.cloud.datatransfer.v1.endpoint_pb2.Endpoint: ...
    @property
    def target(self) -> yandex.cloud.datatransfer.v1.endpoint_pb2.Endpoint: ...
    status: global___TransferStatus.ValueType
    type: global___TransferType.ValueType
    warning: typing.Text
    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        source: typing.Optional[yandex.cloud.datatransfer.v1.endpoint_pb2.Endpoint] = ...,
        target: typing.Optional[yandex.cloud.datatransfer.v1.endpoint_pb2.Endpoint] = ...,
        status: global___TransferStatus.ValueType = ...,
        type: global___TransferType.ValueType = ...,
        warning: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["source",b"source","target",b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","folder_id",b"folder_id","id",b"id","labels",b"labels","name",b"name","source",b"source","status",b"status","target",b"target","type",b"type","warning",b"warning"]) -> None: ...
global___Transfer = Transfer
