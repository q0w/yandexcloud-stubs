"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.iot.broker.v1.broker_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetBrokerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to return.

    To get a broker ID make a [BrokerService.List] request.
    """

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id"]) -> None: ...
global___GetBrokerRequest = GetBrokerRequest

class ListBrokersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list brokers in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a [ListBrokersResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set `page_token` to the
    [ListBrokersResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListBrokersRequest = ListBrokersRequest

class ListBrokersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def brokers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.broker.v1.broker_pb2.Broker]:
        """List of brokers."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListBrokersRequest.page_size], use `next_page_token` as the value
    for the [ListBrokersRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        brokers: typing.Optional[typing.Iterable[yandex.cloud.iot.broker.v1.broker_pb2.Broker]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["brokers",b"brokers","next_page_token",b"next_page_token"]) -> None: ...
global___ListBrokersResponse = ListBrokersResponse

class CreateBrokerRequest(google.protobuf.message.Message):
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

    class Certificate(google.protobuf.message.Message):
        """Specification of a broker certificate."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
        certificate_data: typing.Text
        """Public part of the broker certificate."""

        def __init__(self,
            *,
            certificate_data: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["certificate_data",b"certificate_data"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CERTIFICATES_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to create a broker in.

    To get a folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    name: typing.Text
    """Name of the broker. The name must be unique within the folder."""

    description: typing.Text
    """Description of the broker."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs."""
        pass
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CreateBrokerRequest.Certificate]:
        """Broker certificates."""
        pass
    password: typing.Text
    """Broker passwords.

    The password must contain at least three character categories among the following: upper case latin, lower case latin, numbers and special symbols.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        certificates: typing.Optional[typing.Iterable[global___CreateBrokerRequest.Certificate]] = ...,
        password: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificates",b"certificates","description",b"description","folder_id",b"folder_id","labels",b"labels","name",b"name","password",b"password"]) -> None: ...
global___CreateBrokerRequest = CreateBrokerRequest

class CreateBrokerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker that is being created."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id"]) -> None: ...
global___CreateBrokerMetadata = CreateBrokerMetadata

class UpdateBrokerRequest(google.protobuf.message.Message):
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

    BROKER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to update.

    To get a broker ID make a [BrokerService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the broker are going to be updated."""
        pass
    name: typing.Text
    """Name of the broker. The name must be unique within the folder."""

    description: typing.Text
    """Description of the broker."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """
        pass
    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","description",b"description","labels",b"labels","name",b"name","update_mask",b"update_mask"]) -> None: ...
global___UpdateBrokerRequest = UpdateBrokerRequest

class UpdateBrokerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker that is being updated."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id"]) -> None: ...
global___UpdateBrokerMetadata = UpdateBrokerMetadata

class DeleteBrokerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to delete.

    To get a broker ID make a [BrokerService.List] request.
    """

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id"]) -> None: ...
global___DeleteBrokerRequest = DeleteBrokerRequest

class DeleteBrokerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker that is being deleted."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id"]) -> None: ...
global___DeleteBrokerMetadata = DeleteBrokerMetadata

class ListBrokerCertificatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to list certificates for."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id"]) -> None: ...
global___ListBrokerCertificatesRequest = ListBrokerCertificatesRequest

class ListBrokerCertificatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CERTIFICATES_FIELD_NUMBER: builtins.int
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.broker.v1.broker_pb2.BrokerCertificate]:
        """List of certificates for the specified broker."""
        pass
    def __init__(self,
        *,
        certificates: typing.Optional[typing.Iterable[yandex.cloud.iot.broker.v1.broker_pb2.BrokerCertificate]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificates",b"certificates"]) -> None: ...
global___ListBrokerCertificatesResponse = ListBrokerCertificatesResponse

class AddBrokerCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker for which the certificate is being added.

    To get a broker ID make a [BrokerService.List] request.
    """

    certificate_data: typing.Text
    """Public part of the certificate that is being added."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        certificate_data: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","certificate_data",b"certificate_data"]) -> None: ...
global___AddBrokerCertificateRequest = AddBrokerCertificateRequest

class AddBrokerCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker certificate that is being added."""

    fingerprint: typing.Text
    """Fingerprint of the certificate that is being added."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        fingerprint: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","fingerprint",b"fingerprint"]) -> None: ...
global___AddBrokerCertificateMetadata = AddBrokerCertificateMetadata

class DeleteBrokerCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to delete a certificate for.

    To get a broker ID make a [BrokerService.List] request.
    """

    fingerprint: typing.Text
    """Fingerprint of the certificate that is being deleted."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        fingerprint: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","fingerprint",b"fingerprint"]) -> None: ...
global___DeleteBrokerCertificateRequest = DeleteBrokerCertificateRequest

class DeleteBrokerCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of a broker for which the certificate is being delete."""

    fingerprint: typing.Text
    """Fingerprint of the certificate to deleted."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        fingerprint: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","fingerprint",b"fingerprint"]) -> None: ...
global___DeleteBrokerCertificateMetadata = DeleteBrokerCertificateMetadata

class ListBrokerPasswordsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to list passwords in.

    To get a broker ID make a [BrokerService.List] request.
    """

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id"]) -> None: ...
global___ListBrokerPasswordsRequest = ListBrokerPasswordsRequest

class ListBrokerPasswordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PASSWORDS_FIELD_NUMBER: builtins.int
    @property
    def passwords(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.broker.v1.broker_pb2.BrokerPassword]:
        """List of passwords for the specified broker."""
        pass
    def __init__(self,
        *,
        passwords: typing.Optional[typing.Iterable[yandex.cloud.iot.broker.v1.broker_pb2.BrokerPassword]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["passwords",b"passwords"]) -> None: ...
global___ListBrokerPasswordsResponse = ListBrokerPasswordsResponse

class AddBrokerPasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to add a password for.

    To get a broker ID make a [BrokerService.List] request.
    """

    password: typing.Text
    """Passwords for the broker.

    The password must contain at least three character categories among the following: upper case latin, lower case latin, numbers and special symbols.
    """

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        password: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","password",b"password"]) -> None: ...
global___AddBrokerPasswordRequest = AddBrokerPasswordRequest

class AddBrokerPasswordMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker for which the password is being added."""

    password_id: typing.Text
    """ID of a password that is being added."""

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        password_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","password_id",b"password_id"]) -> None: ...
global___AddBrokerPasswordMetadata = AddBrokerPasswordMetadata

class DeleteBrokerPasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to delete a password for.

    To get a broker ID make a [BrokerService.List] request.
    """

    password_id: typing.Text
    """ID of the password to delete.

    To get a password ID make a [BrokerService.ListPasswords] request.
    """

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        password_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","password_id",b"password_id"]) -> None: ...
global___DeleteBrokerPasswordRequest = DeleteBrokerPasswordRequest

class DeleteBrokerPasswordMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of a broker for which the password is being delete."""

    password_id: typing.Text
    """ID of the password to delete.

    To get a password ID make a [BrokerService.ListPasswords] request.
    """

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        password_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","password_id",b"password_id"]) -> None: ...
global___DeleteBrokerPasswordMetadata = DeleteBrokerPasswordMetadata

class ListBrokerOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BROKER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    broker_id: typing.Text
    """ID of the broker to list operations for."""

    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a [ListBrokerOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set `page_token` to the
    [ListBrokerOperationsResponse.next_page_token] returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on [Broker.name] field.
    """

    def __init__(self,
        *,
        broker_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_id",b"broker_id","filter",b"filter","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListBrokerOperationsRequest = ListBrokerOperationsRequest

class ListBrokerOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified broker."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListBrokerOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListBrokerOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListBrokerOperationsResponse = ListBrokerOperationsResponse
