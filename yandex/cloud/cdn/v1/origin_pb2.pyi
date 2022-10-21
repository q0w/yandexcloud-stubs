"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Origin(google.protobuf.message.Message):
    """An origin. For details about the concept, see [documentation](/docs/cdn/concepts/origins)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ORIGIN_GROUP_ID_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    BACKUP_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    id: builtins.int
    """ID of the origin."""
    origin_group_id: builtins.int
    """ID of the parent origin group."""
    source: builtins.str
    """IP address or Domain name of your origin and the port (if custom).
    Used if [meta] variant is `common`.
    """
    enabled: builtins.bool
    """The setting allows to enable or disable an Origin source in the Origins group.

    It has two possible values:

    True - The origin is enabled and used as a source for the CDN. An origins
    group must contain at least one enabled origin. 
    False - The origin is disabled and the CDN is not using it to pull content.
    """
    backup: builtins.bool
    """Specifies whether the origin is used in its origin group as backup. 
    A backup origin is used when one of active origins becomes unavailable.
    """
    @property
    def meta(self) -> global___OriginMeta:
        """Set up origin of the content."""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        origin_group_id: builtins.int = ...,
        source: builtins.str = ...,
        enabled: builtins.bool = ...,
        backup: builtins.bool = ...,
        meta: global___OriginMeta | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup", b"backup", "enabled", b"enabled", "id", b"id", "meta", b"meta", "origin_group_id", b"origin_group_id", "source", b"source"]) -> None: ...

global___Origin = Origin

@typing_extensions.final
class OriginParams(google.protobuf.message.Message):
    """Origin parameters. For details about the concept, see [documentation](/docs/cdn/concepts/origins)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    BACKUP_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    source: builtins.str
    """Source: IP address or Domain name of your origin and the port (if custom)."""
    enabled: builtins.bool
    """The setting allows to enable or disable an Origin source in the Origins group.

    It has two possible values:

    True - The origin is enabled and used as a source for the CDN. An origins
    group must contain at least one enabled origins. False - The origin is disabled
    and the CDN is not using it to pull content.
    """
    backup: builtins.bool
    """backup option has two possible values:

      True - The option is active. The origin will not be used until one of
             active origins become unavailable.
      False - The option is disabled.
    """
    @property
    def meta(self) -> global___OriginMeta:
        """Set up origin of the content."""
    def __init__(
        self,
        *,
        source: builtins.str = ...,
        enabled: builtins.bool = ...,
        backup: builtins.bool = ...,
        meta: global___OriginMeta | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup", b"backup", "enabled", b"enabled", "meta", b"meta", "source", b"source"]) -> None: ...

global___OriginParams = OriginParams

@typing_extensions.final
class OriginMeta(google.protobuf.message.Message):
    """Origin type. For details about the concept, see [documentation](/docs/cdn/concepts/origins)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMON_FIELD_NUMBER: builtins.int
    BUCKET_FIELD_NUMBER: builtins.int
    WEBSITE_FIELD_NUMBER: builtins.int
    BALANCER_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___OriginNamedMeta:
        """A server with a domain name linked to it"""
    @property
    def bucket(self) -> global___OriginNamedMeta:
        """An Object Storage bucket not configured as a static site hosting."""
    @property
    def website(self) -> global___OriginNamedMeta:
        """An Object Storage bucket configured as a static site hosting."""
    @property
    def balancer(self) -> global___OriginBalancerMeta:
        """An L7 load balancer from Application Load Balancer.
        CDN servers will access the load balancer at one of its IP addresses that must be selected in the origin settings.
        """
    def __init__(
        self,
        *,
        common: global___OriginNamedMeta | None = ...,
        bucket: global___OriginNamedMeta | None = ...,
        website: global___OriginNamedMeta | None = ...,
        balancer: global___OriginBalancerMeta | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["balancer", b"balancer", "bucket", b"bucket", "common", b"common", "origin_meta_variant", b"origin_meta_variant", "website", b"website"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["balancer", b"balancer", "bucket", b"bucket", "common", b"common", "origin_meta_variant", b"origin_meta_variant", "website", b"website"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["origin_meta_variant", b"origin_meta_variant"]) -> typing_extensions.Literal["common", "bucket", "website", "balancer"] | None: ...

global___OriginMeta = OriginMeta

@typing_extensions.final
class OriginNamedMeta(google.protobuf.message.Message):
    """Origin info. For details about the concept, see [documentation](/docs/cdn/concepts/origins)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the origin."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___OriginNamedMeta = OriginNamedMeta

@typing_extensions.final
class OriginBalancerMeta(google.protobuf.message.Message):
    """Application Load Balancer origin info. For details about the concept, see [documentation](/docs/cdn/concepts/origins)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the origin."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___OriginBalancerMeta = OriginBalancerMeta
