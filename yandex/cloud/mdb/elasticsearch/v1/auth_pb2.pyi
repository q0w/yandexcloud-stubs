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

class AuthProviders(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROVIDERS_FIELD_NUMBER: builtins.int
    @property
    def providers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AuthProvider]: ...
    def __init__(self,
        *,
        providers: typing.Optional[typing.Iterable[global___AuthProvider]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["providers",b"providers"]) -> None: ...
global___AuthProviders = AuthProviders

class AuthProvider(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AuthProvider._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: AuthProvider._Type.ValueType  # 0
        NATIVE: AuthProvider._Type.ValueType  # 1
        SAML: AuthProvider._Type.ValueType  # 2
        """OPENID = 3;
        ANONYMOUS = 4;
        """

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    TYPE_UNSPECIFIED: AuthProvider.Type.ValueType  # 0
    NATIVE: AuthProvider.Type.ValueType  # 1
    SAML: AuthProvider.Type.ValueType  # 2
    """OPENID = 3;
    ANONYMOUS = 4;
    """


    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    HIDDEN_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    HINT_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    SAML_FIELD_NUMBER: builtins.int
    type: global___AuthProvider.Type.ValueType
    name: typing.Text
    order: builtins.int
    enabled: builtins.bool
    hidden: builtins.bool
    """selector ui settings"""

    description: typing.Text
    hint: typing.Text
    icon: typing.Text
    @property
    def saml(self) -> global___SamlSettings: ...
    def __init__(self,
        *,
        type: global___AuthProvider.Type.ValueType = ...,
        name: typing.Text = ...,
        order: builtins.int = ...,
        enabled: builtins.bool = ...,
        hidden: builtins.bool = ...,
        description: typing.Text = ...,
        hint: typing.Text = ...,
        icon: typing.Text = ...,
        saml: typing.Optional[global___SamlSettings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["saml",b"saml","settings",b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","enabled",b"enabled","hidden",b"hidden","hint",b"hint","icon",b"icon","name",b"name","order",b"order","saml",b"saml","settings",b"settings","type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["settings",b"settings"]) -> typing.Optional[typing_extensions.Literal["saml"]]: ...
global___AuthProvider = AuthProvider

class SamlSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IDP_ENTITY_ID_FIELD_NUMBER: builtins.int
    IDP_METADATA_FILE_FIELD_NUMBER: builtins.int
    SP_ENTITY_ID_FIELD_NUMBER: builtins.int
    KIBANA_URL_FIELD_NUMBER: builtins.int
    ATTRIBUTE_PRINCIPAL_FIELD_NUMBER: builtins.int
    ATTRIBUTE_GROUPS_FIELD_NUMBER: builtins.int
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_EMAIL_FIELD_NUMBER: builtins.int
    ATTRIBUTE_DN_FIELD_NUMBER: builtins.int
    idp_entity_id: typing.Text
    idp_metadata_file: builtins.bytes
    sp_entity_id: typing.Text
    kibana_url: typing.Text
    attribute_principal: typing.Text
    attribute_groups: typing.Text
    attribute_name: typing.Text
    attribute_email: typing.Text
    attribute_dn: typing.Text
    def __init__(self,
        *,
        idp_entity_id: typing.Text = ...,
        idp_metadata_file: builtins.bytes = ...,
        sp_entity_id: typing.Text = ...,
        kibana_url: typing.Text = ...,
        attribute_principal: typing.Text = ...,
        attribute_groups: typing.Text = ...,
        attribute_name: typing.Text = ...,
        attribute_email: typing.Text = ...,
        attribute_dn: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attribute_dn",b"attribute_dn","attribute_email",b"attribute_email","attribute_groups",b"attribute_groups","attribute_name",b"attribute_name","attribute_principal",b"attribute_principal","idp_entity_id",b"idp_entity_id","idp_metadata_file",b"idp_metadata_file","kibana_url",b"kibana_url","sp_entity_id",b"sp_entity_id"]) -> None: ...
global___SamlSettings = SamlSettings
