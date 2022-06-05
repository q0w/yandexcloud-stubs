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

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class User(google.protobuf.message.Message):
    """A Kafka user.
    For more information, see the [Operations -> Accounts](/docs/managed-kafka/operations/cluster-accounts) section of the documentation.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the Kafka user."""

    cluster_id: typing.Text
    """ID of the Apache Kafka® cluster the user belongs to.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """

    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Permission]:
        """Set of permissions granted to this user."""
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        cluster_id: typing.Text = ...,
        permissions: typing.Optional[typing.Iterable[global___Permission]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","name",b"name","permissions",b"permissions"]) -> None: ...
global___User = User

class UserSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the Kafka user."""

    password: typing.Text
    """Password of the Kafka user."""

    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Permission]:
        """Set of permissions granted to the user."""
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        password: typing.Text = ...,
        permissions: typing.Optional[typing.Iterable[global___Permission]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","password",b"password","permissions",b"permissions"]) -> None: ...
global___UserSpec = UserSpec

class Permission(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _AccessRole:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AccessRoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Permission._AccessRole.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ACCESS_ROLE_UNSPECIFIED: Permission._AccessRole.ValueType  # 0
        ACCESS_ROLE_PRODUCER: Permission._AccessRole.ValueType  # 1
        """producer role for the user."""

        ACCESS_ROLE_CONSUMER: Permission._AccessRole.ValueType  # 2
        """consumer role for the user."""

        ACCESS_ROLE_ADMIN: Permission._AccessRole.ValueType  # 3
        """admin role for the user."""

    class AccessRole(_AccessRole, metaclass=_AccessRoleEnumTypeWrapper):
        pass

    ACCESS_ROLE_UNSPECIFIED: Permission.AccessRole.ValueType  # 0
    ACCESS_ROLE_PRODUCER: Permission.AccessRole.ValueType  # 1
    """producer role for the user."""

    ACCESS_ROLE_CONSUMER: Permission.AccessRole.ValueType  # 2
    """consumer role for the user."""

    ACCESS_ROLE_ADMIN: Permission.AccessRole.ValueType  # 3
    """admin role for the user."""


    TOPIC_NAME_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    topic_name: typing.Text
    """Name or prefix-pattern with wildcard for the topic that the permission grants access to.

    To get the topic name, make a [TopicService.List] request.
    """

    role: global___Permission.AccessRole.ValueType
    """Access role type to grant to the user."""

    def __init__(self,
        *,
        topic_name: typing.Text = ...,
        role: global___Permission.AccessRole.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["role",b"role","topic_name",b"topic_name"]) -> None: ...
global___Permission = Permission
