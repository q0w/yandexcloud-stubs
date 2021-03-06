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
import typing
import typing_extensions
import yandex.cloud.apploadbalancer.v1.target_group_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class LoadBalancer(google.protobuf.message.Message):
    """An application load balancer resource.
    For details about the concept, see [documentation](/docs/application-load-balancer/concepts/application-load-balancer).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LoadBalancer._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: LoadBalancer._Status.ValueType  # 0
        CREATING: LoadBalancer._Status.ValueType  # 1
        """The application load balancer is being created."""

        STARTING: LoadBalancer._Status.ValueType  # 2
        """The application load balancer is being started."""

        ACTIVE: LoadBalancer._Status.ValueType  # 3
        """The application load balancer is active and sends traffic to the targets."""

        STOPPING: LoadBalancer._Status.ValueType  # 4
        """The application load balancer is being stopped."""

        STOPPED: LoadBalancer._Status.ValueType  # 5
        """The application load balancer is stopped and doesn't send traffic to the targets."""

        DELETING: LoadBalancer._Status.ValueType  # 6
        """The application load balancer is being deleted."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNSPECIFIED: LoadBalancer.Status.ValueType  # 0
    CREATING: LoadBalancer.Status.ValueType  # 1
    """The application load balancer is being created."""

    STARTING: LoadBalancer.Status.ValueType  # 2
    """The application load balancer is being started."""

    ACTIVE: LoadBalancer.Status.ValueType  # 3
    """The application load balancer is active and sends traffic to the targets."""

    STOPPING: LoadBalancer.Status.ValueType  # 4
    """The application load balancer is being stopped."""

    STOPPED: LoadBalancer.Status.ValueType  # 5
    """The application load balancer is stopped and doesn't send traffic to the targets."""

    DELETING: LoadBalancer.Status.ValueType  # 6
    """The application load balancer is being deleted."""


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
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    LISTENERS_FIELD_NUMBER: builtins.int
    ALLOCATION_POLICY_FIELD_NUMBER: builtins.int
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the application load balancer. Generated at creation time."""

    name: typing.Text
    """Name of the application load balancer. The name is unique within the folder."""

    description: typing.Text
    """Description of the application load balancer."""

    folder_id: typing.Text
    """ID of the folder that the application load balancer belongs to."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Application load balancer labels as `key:value` pairs.
        For details about the concept, see [documentation](/docs/overview/concepts/services#labels).
        """
        pass
    status: global___LoadBalancer.Status.ValueType
    """Status of the application load balancer."""

    region_id: typing.Text
    """ID of the region that the application load balancer is located at."""

    network_id: typing.Text
    """ID of the network that the application load balancer belongs to."""

    @property
    def listeners(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Listener]:
        """Listeners that belong to the application load balancer.

        For details about the concept, see [documentation](/docs/application-load-balancer/concepts/application-load-balancer#listener).
        """
        pass
    @property
    def allocation_policy(self) -> global___AllocationPolicy:
        """Locality settings of the application load balancer.

        For details about the concept, see [documentation](/docs/application-load-balancer/concepts/application-load-balancer#lb-location).
        """
        pass
    log_group_id: typing.Text
    """ID of the log group that stores access logs of the application load balancer.

    The logs can be accessed using a Cloud Functions [trigger for Cloud Logs](/docs/functions/operations/trigger/cloudlogs-trigger-create).
    """

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """ID's of the security groups attributed to the application load balancer.

        For details about the concept,
        see [documentation](/docs/application-load-balancer/concepts/application-load-balancer#security-groups).
        """
        pass
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        folder_id: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        status: global___LoadBalancer.Status.ValueType = ...,
        region_id: typing.Text = ...,
        network_id: typing.Text = ...,
        listeners: typing.Optional[typing.Iterable[global___Listener]] = ...,
        allocation_policy: typing.Optional[global___AllocationPolicy] = ...,
        log_group_id: typing.Text = ...,
        security_group_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["allocation_policy",b"allocation_policy","created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allocation_policy",b"allocation_policy","created_at",b"created_at","description",b"description","folder_id",b"folder_id","id",b"id","labels",b"labels","listeners",b"listeners","log_group_id",b"log_group_id","name",b"name","network_id",b"network_id","region_id",b"region_id","security_group_ids",b"security_group_ids","status",b"status"]) -> None: ...
global___LoadBalancer = LoadBalancer

class Address(google.protobuf.message.Message):
    """An endpoint address resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXTERNAL_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    INTERNAL_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    EXTERNAL_IPV6_ADDRESS_FIELD_NUMBER: builtins.int
    @property
    def external_ipv4_address(self) -> global___ExternalIpv4Address:
        """Public IPv4 endpoint address."""
        pass
    @property
    def internal_ipv4_address(self) -> global___InternalIpv4Address:
        """Internal IPv4 endpoint address.

        To enable the use of listeners with internal addresses, [contact support](https://console.cloud.yandex.ru/support).
        """
        pass
    @property
    def external_ipv6_address(self) -> global___ExternalIpv6Address:
        """Public IPv6 endpoint address."""
        pass
    def __init__(self,
        *,
        external_ipv4_address: typing.Optional[global___ExternalIpv4Address] = ...,
        internal_ipv4_address: typing.Optional[global___InternalIpv4Address] = ...,
        external_ipv6_address: typing.Optional[global___ExternalIpv6Address] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address",b"address","external_ipv4_address",b"external_ipv4_address","external_ipv6_address",b"external_ipv6_address","internal_ipv4_address",b"internal_ipv4_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","external_ipv4_address",b"external_ipv4_address","external_ipv6_address",b"external_ipv6_address","internal_ipv4_address",b"internal_ipv4_address"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["address",b"address"]) -> typing.Optional[typing_extensions.Literal["external_ipv4_address","internal_ipv4_address","external_ipv6_address"]]: ...
global___Address = Address

class ExternalIpv4Address(google.protobuf.message.Message):
    """A public (external) IPv4 endpoint address resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    address: typing.Text
    """IPv4 address."""

    def __init__(self,
        *,
        address: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address"]) -> None: ...
global___ExternalIpv4Address = ExternalIpv4Address

class InternalIpv4Address(google.protobuf.message.Message):
    """An internal IPv4 endpoint address resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    address: typing.Text
    """IPv4 address."""

    subnet_id: typing.Text
    """ID of the subnet that the address belongs to."""

    def __init__(self,
        *,
        address: typing.Text = ...,
        subnet_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","subnet_id",b"subnet_id"]) -> None: ...
global___InternalIpv4Address = InternalIpv4Address

class ExternalIpv6Address(google.protobuf.message.Message):
    """A public (external) IPv4 endpoint address resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    address: typing.Text
    """IPv6 address."""

    def __init__(self,
        *,
        address: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address"]) -> None: ...
global___ExternalIpv6Address = ExternalIpv6Address

class Location(google.protobuf.message.Message):
    """An application load balancer location resource.

    For details about the concept, see [documentation](/docs/application-load-balancer/concepts/application-load-balancer#lb-location).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ZONE_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    DISABLE_TRAFFIC_FIELD_NUMBER: builtins.int
    zone_id: typing.Text
    """ID of the availability zone where the application load balancer resides.

    Each availability zone can only be specified once.
    """

    subnet_id: typing.Text
    """ID of the subnet that the application load balancer belongs to."""

    disable_traffic: builtins.bool
    """Disables the load balancer node in the specified availability zone.

    Backends in the availability zone are not directly affected by this setting.
    They still may receive traffic from the load balancer nodes in other availability zones,
    subject to [LoadBalancingConfig.locality_aware_routing_percent] and [LoadBalancingConfig.strict_locality] settings.
    """

    def __init__(self,
        *,
        zone_id: typing.Text = ...,
        subnet_id: typing.Text = ...,
        disable_traffic: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disable_traffic",b"disable_traffic","subnet_id",b"subnet_id","zone_id",b"zone_id"]) -> None: ...
global___Location = Location

class AllocationPolicy(google.protobuf.message.Message):
    """A locality settings (allocation policy) resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCATIONS_FIELD_NUMBER: builtins.int
    @property
    def locations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Location]:
        """Availability zones and subnets that the application load balancer resides."""
        pass
    def __init__(self,
        *,
        locations: typing.Optional[typing.Iterable[global___Location]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locations",b"locations"]) -> None: ...
global___AllocationPolicy = AllocationPolicy

class Listener(google.protobuf.message.Message):
    """A listener resource.

    For details about the concept, see [documentation](/docs/application-load-balancer/concepts/application-load-balancer#listener).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ENDPOINTS_FIELD_NUMBER: builtins.int
    HTTP_FIELD_NUMBER: builtins.int
    TLS_FIELD_NUMBER: builtins.int
    STREAM_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the listener. The name is unique within the application load balancer.
    The string length in characters is 3-63.
    """

    @property
    def endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Endpoint]:
        """Endpoints of the listener.

        Endpoints are defined by their IP addresses and ports.
        """
        pass
    @property
    def http(self) -> global___HttpListener:
        """Unencrypted HTTP listener settings."""
        pass
    @property
    def tls(self) -> global___TlsListener:
        """TLS-encrypted HTTP or TCP stream listener settings.

        All handlers within a listener ([TlsListener.default_handler] and [TlsListener.sni_handlers]) must be of one
        type, [HttpHandler] or [StreamHandler]. Mixing HTTP and TCP stream traffic in a TLS-encrypted listener is not
        supported.
        """
        pass
    @property
    def stream(self) -> global___StreamListener:
        """Unencrypted stream (TCP) listener settings."""
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        endpoints: typing.Optional[typing.Iterable[global___Endpoint]] = ...,
        http: typing.Optional[global___HttpListener] = ...,
        tls: typing.Optional[global___TlsListener] = ...,
        stream: typing.Optional[global___StreamListener] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["http",b"http","listener",b"listener","stream",b"stream","tls",b"tls"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoints",b"endpoints","http",b"http","listener",b"listener","name",b"name","stream",b"stream","tls",b"tls"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["listener",b"listener"]) -> typing.Optional[typing_extensions.Literal["http","tls","stream"]]: ...
global___Listener = Listener

class Endpoint(google.protobuf.message.Message):
    """An endpoint resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESSES_FIELD_NUMBER: builtins.int
    PORTS_FIELD_NUMBER: builtins.int
    @property
    def addresses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Address]:
        """Endpoint public (external) and internal addresses."""
        pass
    @property
    def ports(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Endpoint ports."""
        pass
    def __init__(self,
        *,
        addresses: typing.Optional[typing.Iterable[global___Address]] = ...,
        ports: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["addresses",b"addresses","ports",b"ports"]) -> None: ...
global___Endpoint = Endpoint

class HttpListener(google.protobuf.message.Message):
    """An HTTP listener resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HANDLER_FIELD_NUMBER: builtins.int
    REDIRECTS_FIELD_NUMBER: builtins.int
    @property
    def handler(self) -> global___HttpHandler:
        """Settings for handling HTTP requests.

        Only one of `handler` and [redirects] can be specified.
        """
        pass
    @property
    def redirects(self) -> global___Redirects:
        """Redirects settings.

        Only one of `redirects` and [handler] can be specified.
        """
        pass
    def __init__(self,
        *,
        handler: typing.Optional[global___HttpHandler] = ...,
        redirects: typing.Optional[global___Redirects] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handler",b"handler","redirects",b"redirects"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["handler",b"handler","redirects",b"redirects"]) -> None: ...
global___HttpListener = HttpListener

class TlsListener(google.protobuf.message.Message):
    """TLS-encrypted (HTTP or TCP stream) listener resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEFAULT_HANDLER_FIELD_NUMBER: builtins.int
    SNI_HANDLERS_FIELD_NUMBER: builtins.int
    @property
    def default_handler(self) -> global___TlsHandler:
        """Settings for handling requests by default, with Server Name
        Indication (SNI) not matching any of the [sni_handlers].
        """
        pass
    @property
    def sni_handlers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SniMatch]:
        """Settings for handling requests with Server Name Indication (SNI)
        matching one of [SniMatch.server_names] values.
        """
        pass
    def __init__(self,
        *,
        default_handler: typing.Optional[global___TlsHandler] = ...,
        sni_handlers: typing.Optional[typing.Iterable[global___SniMatch]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default_handler",b"default_handler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_handler",b"default_handler","sni_handlers",b"sni_handlers"]) -> None: ...
global___TlsListener = TlsListener

class StreamListener(google.protobuf.message.Message):
    """A stream (TCP) listener resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HANDLER_FIELD_NUMBER: builtins.int
    @property
    def handler(self) -> global___StreamHandler:
        """Settings for handling stream (TCP) requests."""
        pass
    def __init__(self,
        *,
        handler: typing.Optional[global___StreamHandler] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handler",b"handler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["handler",b"handler"]) -> None: ...
global___StreamListener = StreamListener

class Http2Options(google.protobuf.message.Message):
    """An HTTP/2 options resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MAX_CONCURRENT_STREAMS_FIELD_NUMBER: builtins.int
    max_concurrent_streams: builtins.int
    """Maximum number of concurrent HTTP/2 streams in a connection."""

    def __init__(self,
        *,
        max_concurrent_streams: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_concurrent_streams",b"max_concurrent_streams"]) -> None: ...
global___Http2Options = Http2Options

class StreamHandler(google.protobuf.message.Message):
    """A stream (TCP) handler resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BACKEND_GROUP_ID_FIELD_NUMBER: builtins.int
    backend_group_id: typing.Text
    """ID of the backend group processing requests. For details about the concept, see
    [documentation](/docs/application-load-balancer/concepts/backend-group).

    The backend group type, specified via [BackendGroup.backend], must be `stream`.

    To get the list of all available backend groups, make a [BackendGroupService.List] request.
    """

    def __init__(self,
        *,
        backend_group_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backend_group_id",b"backend_group_id"]) -> None: ...
global___StreamHandler = StreamHandler

class HttpHandler(google.protobuf.message.Message):
    """An HTTP handler resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    HTTP2_OPTIONS_FIELD_NUMBER: builtins.int
    ALLOW_HTTP10_FIELD_NUMBER: builtins.int
    http_router_id: typing.Text
    """ID of the HTTP router processing requests. For details about the concept, see
    [documentation](/docs/application-load-balancer/concepts/http-router).

    To get the list of all available HTTP routers, make a [HttpRouterService.List] request.
    """

    @property
    def http2_options(self) -> global___Http2Options:
        """HTTP/2 settings.

        If specified, incoming HTTP/2 requests are supported by the listener.
        """
        pass
    allow_http10: builtins.bool
    """Enables support for incoming HTTP/1.0 and HTTP/1.1 requests and disables it for HTTP/2 requests."""

    def __init__(self,
        *,
        http_router_id: typing.Text = ...,
        http2_options: typing.Optional[global___Http2Options] = ...,
        allow_http10: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["allow_http10",b"allow_http10","http2_options",b"http2_options","protocol_settings",b"protocol_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_http10",b"allow_http10","http2_options",b"http2_options","http_router_id",b"http_router_id","protocol_settings",b"protocol_settings"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["protocol_settings",b"protocol_settings"]) -> typing.Optional[typing_extensions.Literal["http2_options","allow_http10"]]: ...
global___HttpHandler = HttpHandler

class Redirects(google.protobuf.message.Message):
    """A listener redirects resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HTTP_TO_HTTPS_FIELD_NUMBER: builtins.int
    http_to_https: builtins.bool
    """Redirects all unencrypted HTTP requests to the same URI with scheme changed to `https`.

    The setting has the same effect as a single, catch-all [HttpRoute]
    with [RedirectAction.replace_scheme] set to `https`.
    """

    def __init__(self,
        *,
        http_to_https: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_to_https",b"http_to_https"]) -> None: ...
global___Redirects = Redirects

class SniMatch(google.protobuf.message.Message):
    """A SNI handler resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    SERVER_NAMES_FIELD_NUMBER: builtins.int
    HANDLER_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the SNI handler."""

    @property
    def server_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Server names that are matched by the SNI handler."""
        pass
    @property
    def handler(self) -> global___TlsHandler:
        """Settings for handling requests with Server Name Indication (SNI) matching one of [server_names] values."""
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        server_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        handler: typing.Optional[global___TlsHandler] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handler",b"handler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["handler",b"handler","name",b"name","server_names",b"server_names"]) -> None: ...
global___SniMatch = SniMatch

class TlsHandler(google.protobuf.message.Message):
    """A TLS-encrypted (HTTP or TCP stream) handler resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HTTP_HANDLER_FIELD_NUMBER: builtins.int
    STREAM_HANDLER_FIELD_NUMBER: builtins.int
    CERTIFICATE_IDS_FIELD_NUMBER: builtins.int
    @property
    def http_handler(self) -> global___HttpHandler:
        """HTTP handler."""
        pass
    @property
    def stream_handler(self) -> global___StreamHandler:
        """Stream (TCP) handler."""
        pass
    @property
    def certificate_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """ID's of the TLS server certificates from [Certificate Manager](/docs/certificate-manager/).

        RSA and ECDSA certificates are supported, and only the first certificate of each type is used.
        """
        pass
    def __init__(self,
        *,
        http_handler: typing.Optional[global___HttpHandler] = ...,
        stream_handler: typing.Optional[global___StreamHandler] = ...,
        certificate_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handler",b"handler","http_handler",b"http_handler","stream_handler",b"stream_handler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_ids",b"certificate_ids","handler",b"handler","http_handler",b"http_handler","stream_handler",b"stream_handler"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["handler",b"handler"]) -> typing.Optional[typing_extensions.Literal["http_handler","stream_handler"]]: ...
global___TlsHandler = TlsHandler

class TargetState(google.protobuf.message.Message):
    """A target state resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TargetState._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: TargetState._Status.ValueType  # 0
        HEALTHY: TargetState._Status.ValueType  # 1
        """All of the health checks specified in [HttpBackend.healthchecks] or [GrpcBackend.healthchecks] are passed
        (the number depends on the [HealthCheck.healthy_threshold] setting) and the target is ready to receive traffic.
        """

        PARTIALLY_HEALTHY: TargetState._Status.ValueType  # 2
        """Some of the health checks specified in [HttpBackend.healthchecks] or [GrpcBackend.healthchecks] failed
        (the number depends on the [HealthCheck.unhealthy_threshold] setting).
        The target is ready to receive traffic from the load balancer nodes which, based on their health checks,
        consider the target healthy.
        """

        UNHEALTHY: TargetState._Status.ValueType  # 3
        """All of the health checks specified in [HttpBackend.healthchecks] or [GrpcBackend.healthchecks] failed
        (the number depends on the [HealthCheck.unhealthy_threshold] setting) and the target is not receiving traffic.
        """

        DRAINING: TargetState._Status.ValueType  # 4
        """Target is being deleted and the application load balancer is no longer sending traffic to this target."""

        TIMEOUT: TargetState._Status.ValueType  # 5
    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Supported target statuses."""
        pass

    STATUS_UNSPECIFIED: TargetState.Status.ValueType  # 0
    HEALTHY: TargetState.Status.ValueType  # 1
    """All of the health checks specified in [HttpBackend.healthchecks] or [GrpcBackend.healthchecks] are passed
    (the number depends on the [HealthCheck.healthy_threshold] setting) and the target is ready to receive traffic.
    """

    PARTIALLY_HEALTHY: TargetState.Status.ValueType  # 2
    """Some of the health checks specified in [HttpBackend.healthchecks] or [GrpcBackend.healthchecks] failed
    (the number depends on the [HealthCheck.unhealthy_threshold] setting).
    The target is ready to receive traffic from the load balancer nodes which, based on their health checks,
    consider the target healthy.
    """

    UNHEALTHY: TargetState.Status.ValueType  # 3
    """All of the health checks specified in [HttpBackend.healthchecks] or [GrpcBackend.healthchecks] failed
    (the number depends on the [HealthCheck.unhealthy_threshold] setting) and the target is not receiving traffic.
    """

    DRAINING: TargetState.Status.ValueType  # 4
    """Target is being deleted and the application load balancer is no longer sending traffic to this target."""

    TIMEOUT: TargetState.Status.ValueType  # 5

    class HealthcheckStatus(google.protobuf.message.Message):
        """Health of the target."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ZONE_STATUSES_FIELD_NUMBER: builtins.int
        @property
        def zone_statuses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TargetState.ZoneHealthcheckStatus]:
            """Statuses of the target in its availability zones."""
            pass
        def __init__(self,
            *,
            zone_statuses: typing.Optional[typing.Iterable[global___TargetState.ZoneHealthcheckStatus]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["zone_statuses",b"zone_statuses"]) -> None: ...

    class ZoneHealthcheckStatus(google.protobuf.message.Message):
        """Health of the target in the availability zone."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ZONE_ID_FIELD_NUMBER: builtins.int
        STATUS_FIELD_NUMBER: builtins.int
        FAILED_ACTIVE_HC_FIELD_NUMBER: builtins.int
        zone_id: typing.Text
        """ID of the availability zone."""

        status: global___TargetState.Status.ValueType
        """Status of the target in the availability zone."""

        failed_active_hc: builtins.bool
        """Indicates whether the target has been marked `UNHEALTHY` due to failing active health checks,
        which determine target statuses as configured in [HttpBackend.healthchecks] or [GrpcBackend.healthchecks].

        Currently the only type of health checks is active, as described above.
        Passive health checks, which determine the health of a target based on its responses to production requests
        (HTTP 5xx status codes, connection errors etc.), are not implemented yet.
        """

        def __init__(self,
            *,
            zone_id: typing.Text = ...,
            status: global___TargetState.Status.ValueType = ...,
            failed_active_hc: builtins.bool = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["failed_active_hc",b"failed_active_hc","status",b"status","zone_id",b"zone_id"]) -> None: ...

    STATUS_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    @property
    def status(self) -> global___TargetState.HealthcheckStatus:
        """Health of the target, i.e. its statuses in all availability zones."""
        pass
    @property
    def target(self) -> yandex.cloud.apploadbalancer.v1.target_group_pb2.Target:
        """Target."""
        pass
    def __init__(self,
        *,
        status: typing.Optional[global___TargetState.HealthcheckStatus] = ...,
        target: typing.Optional[yandex.cloud.apploadbalancer.v1.target_group_pb2.Target] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["status",b"status","target",b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["status",b"status","target",b"target"]) -> None: ...
global___TargetState = TargetState
