"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class UserAccount(google.protobuf.message.Message):
    """Currently represents only [Yandex account](/docs/iam/concepts/#passport)."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    YANDEX_PASSPORT_USER_ACCOUNT_FIELD_NUMBER: builtins.int
    SAML_USER_ACCOUNT_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the user account."""

    @property
    def yandex_passport_user_account(self) -> global___YandexPassportUserAccount:
        """A YandexPassportUserAccount resource."""
        pass
    @property
    def saml_user_account(self) -> global___SamlUserAccount:
        """A SAML federated user."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        yandex_passport_user_account: typing.Optional[global___YandexPassportUserAccount] = ...,
        saml_user_account: typing.Optional[global___SamlUserAccount] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["saml_user_account",b"saml_user_account","user_account",b"user_account","yandex_passport_user_account",b"yandex_passport_user_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","saml_user_account",b"saml_user_account","user_account",b"user_account","yandex_passport_user_account",b"yandex_passport_user_account"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["user_account",b"user_account"]) -> typing.Optional[typing_extensions.Literal["yandex_passport_user_account","saml_user_account"]]: ...
global___UserAccount = UserAccount

class YandexPassportUserAccount(google.protobuf.message.Message):
    """A YandexPassportUserAccount resource.
    For more information, see [Yandex account](/docs/iam/concepts/#passport).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOGIN_FIELD_NUMBER: builtins.int
    DEFAULT_EMAIL_FIELD_NUMBER: builtins.int
    login: typing.Text
    """Login of the Yandex user account."""

    default_email: typing.Text
    """Default email of the Yandex user account."""

    def __init__(self,
        *,
        login: typing.Text = ...,
        default_email: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_email",b"default_email","login",b"login"]) -> None: ...
global___YandexPassportUserAccount = YandexPassportUserAccount

class SamlUserAccount(google.protobuf.message.Message):
    """A SAML federated user.
    For more information, see [federations](/docs/iam/concepts/users/saml-federations).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Attribute(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        VALUE_FIELD_NUMBER: builtins.int
        @property
        def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
        def __init__(self,
            *,
            value: typing.Optional[typing.Iterable[typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...

    class AttributesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> global___SamlUserAccount.Attribute: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___SamlUserAccount.Attribute] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    NAME_ID_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    federation_id: typing.Text
    """ID of the federation that the federation belongs to."""

    name_id: typing.Text
    """Name Id of the SAML federated user.
    The name is unique within the federation. 1-256 characters long.
    """

    @property
    def attributes(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___SamlUserAccount.Attribute]:
        """Additional attributes of the SAML federated user."""
        pass
    def __init__(self,
        *,
        federation_id: typing.Text = ...,
        name_id: typing.Text = ...,
        attributes: typing.Optional[typing.Mapping[typing.Text, global___SamlUserAccount.Attribute]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attributes",b"attributes","federation_id",b"federation_id","name_id",b"name_id"]) -> None: ...
global___SamlUserAccount = SamlUserAccount