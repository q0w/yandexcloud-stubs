"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _BindingType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _BindingTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BindingType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    BINDING_TYPE_UNSPECIFIED: _BindingType.ValueType  # 0
    POST: _BindingType.ValueType  # 1
    """HTTP POST binding."""

    REDIRECT: _BindingType.ValueType  # 2
    """HTTP redirect binding."""

    ARTIFACT: _BindingType.ValueType  # 3
    """HTTP artifact binding."""

class BindingType(_BindingType, metaclass=_BindingTypeEnumTypeWrapper):
    pass

BINDING_TYPE_UNSPECIFIED: BindingType.ValueType  # 0
POST: BindingType.ValueType  # 1
"""HTTP POST binding."""

REDIRECT: BindingType.ValueType  # 2
"""HTTP redirect binding."""

ARTIFACT: BindingType.ValueType  # 3
"""HTTP artifact binding."""

global___BindingType = BindingType


class Federation(google.protobuf.message.Message):
    """A federation.
    For more information, see [SAML-compatible identity federations](/docs/iam/concepts/users/identity-federations).
    """
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
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    COOKIE_MAX_AGE_FIELD_NUMBER: builtins.int
    AUTO_CREATE_ACCOUNT_ON_LOGIN_FIELD_NUMBER: builtins.int
    ISSUER_FIELD_NUMBER: builtins.int
    SSO_BINDING_FIELD_NUMBER: builtins.int
    SSO_URL_FIELD_NUMBER: builtins.int
    SECURITY_SETTINGS_FIELD_NUMBER: builtins.int
    CASE_INSENSITIVE_NAME_IDS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the federation."""

    organization_id: typing.Text
    """ID of the organization that the federation belongs to."""

    name: typing.Text
    """Name of the federation."""

    description: typing.Text
    """Description of the federation."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    @property
    def cookie_max_age(self) -> google.protobuf.duration_pb2.Duration:
        """Browser cookie lifetime in seconds.
        If the cookie is still valid, the management console
        authenticates the user immediately and redirects them to the home page.
        """
        pass
    auto_create_account_on_login: builtins.bool
    """Add new users automatically on successful authentication.
    The user becomes member of the organization automatically,
    but you need to grant other roles to them.

    If the value is `false`, users who aren't added to the organization
    can't log in, even if they have authenticated on your server.
    """

    issuer: typing.Text
    """ID of the IdP server to be used for authentication.
    The IdP server also responds to IAM with this ID after the user authenticates.
    """

    sso_binding: global___BindingType.ValueType
    """Single sign-on endpoint binding type. Most Identity Providers support the `POST` binding type.

    SAML Binding is a mapping of a SAML protocol message onto standard messaging
    formats and/or communications protocols.
    """

    sso_url: typing.Text
    """Single sign-on endpoint URL.
    Specify the link to the IdP login page here.
    """

    @property
    def security_settings(self) -> global___FederationSecuritySettings:
        """Federation security settings."""
        pass
    case_insensitive_name_ids: builtins.bool
    """Use case insensitive Name IDs."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `` key:value `` pairs. Maximum of 64 per resource."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        organization_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        cookie_max_age: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        auto_create_account_on_login: builtins.bool = ...,
        issuer: typing.Text = ...,
        sso_binding: global___BindingType.ValueType = ...,
        sso_url: typing.Text = ...,
        security_settings: typing.Optional[global___FederationSecuritySettings] = ...,
        case_insensitive_name_ids: builtins.bool = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cookie_max_age",b"cookie_max_age","created_at",b"created_at","security_settings",b"security_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_create_account_on_login",b"auto_create_account_on_login","case_insensitive_name_ids",b"case_insensitive_name_ids","cookie_max_age",b"cookie_max_age","created_at",b"created_at","description",b"description","id",b"id","issuer",b"issuer","labels",b"labels","name",b"name","organization_id",b"organization_id","security_settings",b"security_settings","sso_binding",b"sso_binding","sso_url",b"sso_url"]) -> None: ...
global___Federation = Federation

class FederationSecuritySettings(google.protobuf.message.Message):
    """Federation security settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENCRYPTED_ASSERTIONS_FIELD_NUMBER: builtins.int
    encrypted_assertions: builtins.bool
    """Enable encrypted assertions."""

    def __init__(self,
        *,
        encrypted_assertions: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["encrypted_assertions",b"encrypted_assertions"]) -> None: ...
global___FederationSecuritySettings = FederationSecuritySettings