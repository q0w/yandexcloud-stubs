"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _IpPermissionAction:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _IpPermissionActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IpPermissionAction.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    IP_PERMISSION_ACTION_UNSPECIFIED: _IpPermissionAction.ValueType  # 0
    ADD: _IpPermissionAction.ValueType  # 1
    """Addition of an ip permission."""

    REMOVE: _IpPermissionAction.ValueType  # 2
    """Removal of an ip permission."""

class IpPermissionAction(_IpPermissionAction, metaclass=_IpPermissionActionEnumTypeWrapper):
    pass

IP_PERMISSION_ACTION_UNSPECIFIED: IpPermissionAction.ValueType  # 0
ADD: IpPermissionAction.ValueType  # 1
"""Addition of an ip permission."""

REMOVE: IpPermissionAction.ValueType  # 2
"""Removal of an ip permission."""

global___IpPermissionAction = IpPermissionAction


class IpPermission(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Action:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[IpPermission._Action.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ACTION_UNSPECIFIED: IpPermission._Action.ValueType  # 0
        PULL: IpPermission._Action.ValueType  # 1
        PUSH: IpPermission._Action.ValueType  # 2
    class Action(_Action, metaclass=_ActionEnumTypeWrapper):
        pass

    ACTION_UNSPECIFIED: IpPermission.Action.ValueType  # 0
    PULL: IpPermission.Action.ValueType  # 1
    PUSH: IpPermission.Action.ValueType  # 2

    ACTION_FIELD_NUMBER: builtins.int
    IP_FIELD_NUMBER: builtins.int
    action: global___IpPermission.Action.ValueType
    ip: typing.Text
    def __init__(self,
        *,
        action: global___IpPermission.Action.ValueType = ...,
        ip: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["action",b"action","ip",b"ip"]) -> None: ...
global___IpPermission = IpPermission

class IpPermissionDelta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACTION_FIELD_NUMBER: builtins.int
    IP_PERMISSION_FIELD_NUMBER: builtins.int
    action: global___IpPermissionAction.ValueType
    """The action that is being performed on an ip permission."""

    @property
    def ip_permission(self) -> global___IpPermission:
        """Ip permission."""
        pass
    def __init__(self,
        *,
        action: global___IpPermissionAction.ValueType = ...,
        ip_permission: typing.Optional[global___IpPermission] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ip_permission",b"ip_permission"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action",b"action","ip_permission",b"ip_permission"]) -> None: ...
global___IpPermissionDelta = IpPermissionDelta
