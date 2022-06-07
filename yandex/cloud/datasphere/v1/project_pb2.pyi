"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Project(google.protobuf.message.Message):
    """A Project resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Settings(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _CommitMode:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _CommitModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Project.Settings._CommitMode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            COMMIT_MODE_UNSPECIFIED: Project.Settings._CommitMode.ValueType  # 0
            STANDARD: Project.Settings._CommitMode.ValueType  # 1
            """Commit happens after the execution of a cell or group of cells or after completion with an error."""

            AUTO: Project.Settings._CommitMode.ValueType  # 2
            """Commit happens periodically.
            Also, automatic saving of state occurs when switching to another type of computing resource.
            """

        class CommitMode(_CommitMode, metaclass=_CommitModeEnumTypeWrapper):
            pass

        COMMIT_MODE_UNSPECIFIED: Project.Settings.CommitMode.ValueType  # 0
        STANDARD: Project.Settings.CommitMode.ValueType  # 1
        """Commit happens after the execution of a cell or group of cells or after completion with an error."""

        AUTO: Project.Settings.CommitMode.ValueType  # 2
        """Commit happens periodically.
        Also, automatic saving of state occurs when switching to another type of computing resource.
        """


        SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
        SUBNET_ID_FIELD_NUMBER: builtins.int
        DATA_PROC_CLUSTER_ID_FIELD_NUMBER: builtins.int
        COMMIT_MODE_FIELD_NUMBER: builtins.int
        SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
        service_account_id: typing.Text
        """ID of the service account, on whose behalf all operations with clusters will be performed."""

        subnet_id: typing.Text
        """ID of the subnet where the DataProc cluster resides.
        Currently only subnets created in the availability zone ru-central1-a are supported.
        """

        data_proc_cluster_id: typing.Text
        """ID of the DataProc cluster."""

        commit_mode: global___Project.Settings.CommitMode.ValueType
        """Commit mode that is assigned to the project."""

        @property
        def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """Network interfaces security groups."""
            pass
        def __init__(self,
            *,
            service_account_id: typing.Text = ...,
            subnet_id: typing.Text = ...,
            data_proc_cluster_id: typing.Text = ...,
            commit_mode: global___Project.Settings.CommitMode.ValueType = ...,
            security_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["commit_mode",b"commit_mode","data_proc_cluster_id",b"data_proc_cluster_id","security_group_ids",b"security_group_ids","service_account_id",b"service_account_id","subnet_id",b"subnet_id"]) -> None: ...

    class Limits(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        MAX_UNITS_PER_HOUR_FIELD_NUMBER: builtins.int
        MAX_UNITS_PER_EXECUTION_FIELD_NUMBER: builtins.int
        @property
        def max_units_per_hour(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The number of units that can be spent per hour."""
            pass
        @property
        def max_units_per_execution(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The number of units that can be spent on the one execution."""
            pass
        def __init__(self,
            *,
            max_units_per_hour: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
            max_units_per_execution: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["max_units_per_execution",b"max_units_per_execution","max_units_per_hour",b"max_units_per_hour"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["max_units_per_execution",b"max_units_per_execution","max_units_per_hour",b"max_units_per_hour"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the project."""

    folder_id: typing.Text
    """ID of the folder that the project belongs to."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    name: typing.Text
    """Name of the project. 1-63 characters long."""

    description: typing.Text
    """Description of the project. 0-256 characters long."""

    @property
    def settings(self) -> global___Project.Settings:
        """Settings of the project."""
        pass
    @property
    def limits(self) -> global___Project.Limits:
        """Limits of the project."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        folder_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        settings: typing.Optional[global___Project.Settings] = ...,
        limits: typing.Optional[global___Project.Limits] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","limits",b"limits","settings",b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","description",b"description","folder_id",b"folder_id","id",b"id","limits",b"limits","name",b"name","settings",b"settings"]) -> None: ...
global___Project = Project