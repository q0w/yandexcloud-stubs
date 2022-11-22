"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing
import yandex.cloud.storage.v1.bucket_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetBucketRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _View:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[GetBucketRequest._View.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        VIEW_UNSPECIFIED: GetBucketRequest._View.ValueType  # 0
        VIEW_BASIC: GetBucketRequest._View.ValueType  # 1
        """Returns basic information about a bucket.

        The following fields will _not_ be returned: [Bucket.acl], [Bucket.cors], [Bucket.website_settings],
        [Bucket.lifecycle_rules].
        """
        VIEW_ACL: GetBucketRequest._View.ValueType  # 2
        """Returns basic information and access control list (ACL) for the bucket.

        The following fields will _not_ be returned: [Bucket.cors], [Bucket.website_settings], [Bucket.lifecycle_rules].
        """
        VIEW_FULL: GetBucketRequest._View.ValueType  # 3
        """Returns full information about a bucket."""

    class View(_View, metaclass=_ViewEnumTypeWrapper): ...
    VIEW_UNSPECIFIED: GetBucketRequest.View.ValueType  # 0
    VIEW_BASIC: GetBucketRequest.View.ValueType  # 1
    """Returns basic information about a bucket.

    The following fields will _not_ be returned: [Bucket.acl], [Bucket.cors], [Bucket.website_settings],
    [Bucket.lifecycle_rules].
    """
    VIEW_ACL: GetBucketRequest.View.ValueType  # 2
    """Returns basic information and access control list (ACL) for the bucket.

    The following fields will _not_ be returned: [Bucket.cors], [Bucket.website_settings], [Bucket.lifecycle_rules].
    """
    VIEW_FULL: GetBucketRequest.View.ValueType  # 3
    """Returns full information about a bucket."""

    NAME_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket to return.

    To get the bucket name, make a [BucketService.List] request.
    """
    view: global___GetBucketRequest.View.ValueType
    """Scope of information about the bucket to return.

    Access to scopes is managed via [Identity and Access Management roles](/docs/storage/security),
    bucket [ACL](/docs/storage/concepts/acl) and [policies](/docs/storage/concepts/policy).
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        view: global___GetBucketRequest.View.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "view", b"view"]) -> None: ...

global___GetBucketRequest = GetBucketRequest

@typing_extensions.final
class ListBucketsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list buckets in.

    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_id", b"folder_id"]) -> None: ...

global___ListBucketsRequest = ListBucketsRequest

@typing_extensions.final
class ListBucketsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUCKETS_FIELD_NUMBER: builtins.int
    @property
    def buckets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.storage.v1.bucket_pb2.Bucket]:
        """List of buckets in the specified folder."""
    def __init__(
        self,
        *,
        buckets: collections.abc.Iterable[yandex.cloud.storage.v1.bucket_pb2.Bucket] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["buckets", b"buckets"]) -> None: ...

global___ListBucketsResponse = ListBucketsResponse

@typing_extensions.final
class CreateBucketRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    DEFAULT_STORAGE_CLASS_FIELD_NUMBER: builtins.int
    MAX_SIZE_FIELD_NUMBER: builtins.int
    ANONYMOUS_ACCESS_FLAGS_FIELD_NUMBER: builtins.int
    ACL_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket.

    The name must be unique within the platform. For naming limitations and rules, see
    [documentation](/docs/storage/concepts/bucket#naming).
    """
    folder_id: builtins.str
    """ID of the folder to create a bucket in.

    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    default_storage_class: builtins.str
    """Default storage class for objects in the bucket. Supported classes are standard storage (`STANDARD`), cold storage
    (`COLD`, `STANDARD_IA`, `NEARLINE` all synonyms), and ice storage (`ICE` and `GLACIER` are synonyms).
    For details, see [documentation](/docs/storage/concepts/storage-class).
    """
    max_size: builtins.int
    """Maximum size of the bucket.
    For details, see [documentation](/docs/storage/operations/buckets/limit-max-volume).
    """
    @property
    def anonymous_access_flags(self) -> yandex.cloud.storage.v1.bucket_pb2.AnonymousAccessFlags:
        """Flags for configuring public (anonymous) access to the bucket's content and settings.
        For details, see [documentation](/docs/storage/concepts/bucket#bucket-access).
        """
    @property
    def acl(self) -> yandex.cloud.storage.v1.bucket_pb2.ACL:
        """Access control list (ACL) of the bucket.
        For details, see [documentation](/docs/storage/concepts/acl).
        """
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.storage.v1.bucket_pb2.Tag]:
        """List of object tag for the bucket.
        TODO: documentation details.
        """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        folder_id: builtins.str = ...,
        default_storage_class: builtins.str = ...,
        max_size: builtins.int = ...,
        anonymous_access_flags: yandex.cloud.storage.v1.bucket_pb2.AnonymousAccessFlags | None = ...,
        acl: yandex.cloud.storage.v1.bucket_pb2.ACL | None = ...,
        tags: collections.abc.Iterable[yandex.cloud.storage.v1.bucket_pb2.Tag] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["acl", b"acl", "anonymous_access_flags", b"anonymous_access_flags"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["acl", b"acl", "anonymous_access_flags", b"anonymous_access_flags", "default_storage_class", b"default_storage_class", "folder_id", b"folder_id", "max_size", b"max_size", "name", b"name", "tags", b"tags"]) -> None: ...

global___CreateBucketRequest = CreateBucketRequest

@typing_extensions.final
class CreateBucketMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket that is being created."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___CreateBucketMetadata = CreateBucketMetadata

@typing_extensions.final
class UpdateBucketRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    FIELD_MASK_FIELD_NUMBER: builtins.int
    ANONYMOUS_ACCESS_FLAGS_FIELD_NUMBER: builtins.int
    DEFAULT_STORAGE_CLASS_FIELD_NUMBER: builtins.int
    MAX_SIZE_FIELD_NUMBER: builtins.int
    CORS_FIELD_NUMBER: builtins.int
    WEBSITE_SETTINGS_FIELD_NUMBER: builtins.int
    VERSIONING_FIELD_NUMBER: builtins.int
    LIFECYCLE_RULES_FIELD_NUMBER: builtins.int
    POLICY_FIELD_NUMBER: builtins.int
    ACL_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket to update.

    The name cannot be updated.

    To get the bucket name, make a [BucketService.List] request.
    """
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the bucket should be updated."""
    @property
    def anonymous_access_flags(self) -> yandex.cloud.storage.v1.bucket_pb2.AnonymousAccessFlags:
        """Flags for configuring public (anonymous) access to the bucket's content and settings.
        For details, see [documentation](/docs/storage/concepts/bucket#bucket-access).
        """
    default_storage_class: builtins.str
    """Default storage class for objects in the bucket. Supported classes are standard storage (`STANDARD`), cold storage
    (`COLD`, `STANDARD_IA`, `NEARLINE` all synonyms), and ice storage (`ICE` and `GLACIER` are synonyms).
    For details, see [documentation](/docs/storage/concepts/storage-class).
    """
    max_size: builtins.int
    """Maximum size of the bucket, in bytes.
    For details, see [documentation](/docs/storage/operations/buckets/limit-max-volume).
    """
    @property
    def cors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.storage.v1.bucket_pb2.CorsRule]:
        """List of rules for cross-domain requests to objects in the bucket (cross-origin resource sharing, CORS).
        For details, see [documentation](/docs/storage/concepts/cors).
        """
    @property
    def website_settings(self) -> yandex.cloud.storage.v1.bucket_pb2.WebsiteSettings:
        """Configuration for hosting a static website in the bucket.
        For details, see [documentation](/docs/storage/concepts/hosting).
        """
    versioning: yandex.cloud.storage.v1.bucket_pb2.Versioning.ValueType
    """Bucket versioning status.
    For details, see [documentation](/docs/storage/concepts/versioning).
    """
    @property
    def lifecycle_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.storage.v1.bucket_pb2.LifecycleRule]:
        """List of object lifecycle rules for the bucket.
        For details, see [documentation](/docs/storage/concepts/lifecycles).
        """
    @property
    def policy(self) -> google.protobuf.struct_pb2.Struct:
        """Bucket policies that set permissions for actions with the bucket, its objects, and groups of objects.
        For details, see [documentation](/docs/storage/concepts/policy).
        """
    @property
    def acl(self) -> yandex.cloud.storage.v1.bucket_pb2.ACL:
        """Access control list (ACL) of the bucket.
        For details, see [documentation](/docs/storage/concepts/acl).
        """
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.storage.v1.bucket_pb2.Tag]:
        """List of object tag for the bucket.
        TODO: documentation details.
        """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        anonymous_access_flags: yandex.cloud.storage.v1.bucket_pb2.AnonymousAccessFlags | None = ...,
        default_storage_class: builtins.str = ...,
        max_size: builtins.int = ...,
        cors: collections.abc.Iterable[yandex.cloud.storage.v1.bucket_pb2.CorsRule] | None = ...,
        website_settings: yandex.cloud.storage.v1.bucket_pb2.WebsiteSettings | None = ...,
        versioning: yandex.cloud.storage.v1.bucket_pb2.Versioning.ValueType = ...,
        lifecycle_rules: collections.abc.Iterable[yandex.cloud.storage.v1.bucket_pb2.LifecycleRule] | None = ...,
        policy: google.protobuf.struct_pb2.Struct | None = ...,
        acl: yandex.cloud.storage.v1.bucket_pb2.ACL | None = ...,
        tags: collections.abc.Iterable[yandex.cloud.storage.v1.bucket_pb2.Tag] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["acl", b"acl", "anonymous_access_flags", b"anonymous_access_flags", "field_mask", b"field_mask", "policy", b"policy", "website_settings", b"website_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["acl", b"acl", "anonymous_access_flags", b"anonymous_access_flags", "cors", b"cors", "default_storage_class", b"default_storage_class", "field_mask", b"field_mask", "lifecycle_rules", b"lifecycle_rules", "max_size", b"max_size", "name", b"name", "policy", b"policy", "tags", b"tags", "versioning", b"versioning", "website_settings", b"website_settings"]) -> None: ...

global___UpdateBucketRequest = UpdateBucketRequest

@typing_extensions.final
class UpdateBucketMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket that is being updated."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___UpdateBucketMetadata = UpdateBucketMetadata

@typing_extensions.final
class DeleteBucketRequest(google.protobuf.message.Message):
    """DeleteBucketRequest deletes requested bucket from the Cloud."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket to update.

    To get the bucket name, make a [BucketService.List] request.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___DeleteBucketRequest = DeleteBucketRequest

@typing_extensions.final
class DeleteBucketMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket that is being deleted."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___DeleteBucketMetadata = DeleteBucketMetadata

@typing_extensions.final
class GetBucketStatsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket to return the statistics for."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___GetBucketStatsRequest = GetBucketStatsRequest

@typing_extensions.final
class GetBucketHTTPSConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket to return the HTTPS configuration for."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___GetBucketHTTPSConfigRequest = GetBucketHTTPSConfigRequest

@typing_extensions.final
class SelfManagedHTTPSConfigParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_PEM_FIELD_NUMBER: builtins.int
    PRIVATE_KEY_PEM_FIELD_NUMBER: builtins.int
    certificate_pem: builtins.str
    """[PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail)-encoded certificate."""
    private_key_pem: builtins.str
    """[PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail)-encoded private key for the certificate."""
    def __init__(
        self,
        *,
        certificate_pem: builtins.str = ...,
        private_key_pem: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_pem", b"certificate_pem", "private_key_pem", b"private_key_pem"]) -> None: ...

global___SelfManagedHTTPSConfigParams = SelfManagedHTTPSConfigParams

@typing_extensions.final
class CertificateManagerHTTPSConfigParams(google.protobuf.message.Message):
    """A resource for a TLS certificate from Certificate Manager."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate.

    To get the list of all available certificates, make a [yandex.cloud.certificatemanager.v1.CertificateService.List]
    request.
    """
    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_id", b"certificate_id"]) -> None: ...

global___CertificateManagerHTTPSConfigParams = CertificateManagerHTTPSConfigParams

@typing_extensions.final
class SetBucketHTTPSConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    SELF_MANAGED_FIELD_NUMBER: builtins.int
    CERTIFICATE_MANAGER_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket to update the HTTPS configuration for."""
    @property
    def self_managed(self) -> global___SelfManagedHTTPSConfigParams:
        """Your TLS certificate, uploaded directly.

        Object Storage only supports [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail)-encoded certificates.
        """
    @property
    def certificate_manager(self) -> global___CertificateManagerHTTPSConfigParams:
        """TLS certificate from Certificate Manager.

        To create a certificate in Certificate Manager, make a
        [yandex.cloud.certificatemanager.v1.CertificateService.Create] request.
        """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        self_managed: global___SelfManagedHTTPSConfigParams | None = ...,
        certificate_manager: global___CertificateManagerHTTPSConfigParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["certificate_manager", b"certificate_manager", "params", b"params", "self_managed", b"self_managed"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_manager", b"certificate_manager", "name", b"name", "params", b"params", "self_managed", b"self_managed"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["params", b"params"]) -> typing_extensions.Literal["self_managed", "certificate_manager"] | None: ...

global___SetBucketHTTPSConfigRequest = SetBucketHTTPSConfigRequest

@typing_extensions.final
class SetBucketHTTPSConfigMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket the HTTPS configuration is being updated for."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___SetBucketHTTPSConfigMetadata = SetBucketHTTPSConfigMetadata

@typing_extensions.final
class DeleteBucketHTTPSConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket to delete the HTTPS configuration for."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___DeleteBucketHTTPSConfigRequest = DeleteBucketHTTPSConfigRequest

@typing_extensions.final
class DeleteBucketHTTPSConfigMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the bucket the HTTPS configuration is being deleted for."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___DeleteBucketHTTPSConfigMetadata = DeleteBucketHTTPSConfigMetadata
