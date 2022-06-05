"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MaintenanceWindow(google.protobuf.message.Message):
    """A maintenance window settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ANYTIME_FIELD_NUMBER: builtins.int
    WEEKLY_MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    @property
    def anytime(self) -> global___AnytimeMaintenanceWindow:
        """Maintenance operation can be scheduled anytime."""
        pass
    @property
    def weekly_maintenance_window(self) -> global___WeeklyMaintenanceWindow:
        """Maintenance operation can be scheduled on a weekly basis."""
        pass
    def __init__(self,
        *,
        anytime: typing.Optional[global___AnytimeMaintenanceWindow] = ...,
        weekly_maintenance_window: typing.Optional[global___WeeklyMaintenanceWindow] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["anytime",b"anytime","policy",b"policy","weekly_maintenance_window",b"weekly_maintenance_window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["anytime",b"anytime","policy",b"policy","weekly_maintenance_window",b"weekly_maintenance_window"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["policy",b"policy"]) -> typing.Optional[typing_extensions.Literal["anytime","weekly_maintenance_window"]]: ...
global___MaintenanceWindow = MaintenanceWindow

class AnytimeMaintenanceWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___AnytimeMaintenanceWindow = AnytimeMaintenanceWindow

class WeeklyMaintenanceWindow(google.protobuf.message.Message):
    """Weelky maintenance window settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _WeekDay:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _WeekDayEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WeeklyMaintenanceWindow._WeekDay.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        WEEK_DAY_UNSPECIFIED: WeeklyMaintenanceWindow._WeekDay.ValueType  # 0
        MON: WeeklyMaintenanceWindow._WeekDay.ValueType  # 1
        TUE: WeeklyMaintenanceWindow._WeekDay.ValueType  # 2
        WED: WeeklyMaintenanceWindow._WeekDay.ValueType  # 3
        THU: WeeklyMaintenanceWindow._WeekDay.ValueType  # 4
        FRI: WeeklyMaintenanceWindow._WeekDay.ValueType  # 5
        SAT: WeeklyMaintenanceWindow._WeekDay.ValueType  # 6
        SUN: WeeklyMaintenanceWindow._WeekDay.ValueType  # 7
    class WeekDay(_WeekDay, metaclass=_WeekDayEnumTypeWrapper):
        pass

    WEEK_DAY_UNSPECIFIED: WeeklyMaintenanceWindow.WeekDay.ValueType  # 0
    MON: WeeklyMaintenanceWindow.WeekDay.ValueType  # 1
    TUE: WeeklyMaintenanceWindow.WeekDay.ValueType  # 2
    WED: WeeklyMaintenanceWindow.WeekDay.ValueType  # 3
    THU: WeeklyMaintenanceWindow.WeekDay.ValueType  # 4
    FRI: WeeklyMaintenanceWindow.WeekDay.ValueType  # 5
    SAT: WeeklyMaintenanceWindow.WeekDay.ValueType  # 6
    SUN: WeeklyMaintenanceWindow.WeekDay.ValueType  # 7

    DAY_FIELD_NUMBER: builtins.int
    HOUR_FIELD_NUMBER: builtins.int
    day: global___WeeklyMaintenanceWindow.WeekDay.ValueType
    """Day of the week (in `DDD` format)."""

    hour: builtins.int
    """Hour of the day in UTC (in `HH` format)."""

    def __init__(self,
        *,
        day: global___WeeklyMaintenanceWindow.WeekDay.ValueType = ...,
        hour: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["day",b"day","hour",b"hour"]) -> None: ...
global___WeeklyMaintenanceWindow = WeeklyMaintenanceWindow

class MaintenanceOperation(google.protobuf.message.Message):
    """A planned maintenance operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INFO_FIELD_NUMBER: builtins.int
    DELAYED_UNTIL_FIELD_NUMBER: builtins.int
    info: typing.Text
    """Information about this maintenance operation."""

    @property
    def delayed_until(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time until which this maintenance operation is delayed."""
        pass
    def __init__(self,
        *,
        info: typing.Text = ...,
        delayed_until: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delayed_until",b"delayed_until"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delayed_until",b"delayed_until","info",b"info"]) -> None: ...
global___MaintenanceOperation = MaintenanceOperation
