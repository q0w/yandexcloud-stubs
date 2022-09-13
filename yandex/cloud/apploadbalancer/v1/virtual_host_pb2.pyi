"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing
import yandex.cloud.apploadbalancer.v1.payload_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class VirtualHost(google.protobuf.message.Message):
    """A virtual host resource.
    For details about the concept, see [documentation](/docs/application-load-balancer/concepts/http-router#virtual-host).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    AUTHORITY_FIELD_NUMBER: builtins.int
    ROUTES_FIELD_NUMBER: builtins.int
    MODIFY_REQUEST_HEADERS_FIELD_NUMBER: builtins.int
    MODIFY_RESPONSE_HEADERS_FIELD_NUMBER: builtins.int
    ROUTE_OPTIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the virtual host. The name is unique within the HTTP router."""
    @property
    def authority(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of domains that are attributed to the virtual host.

        The host is selected to process the request received by the load balancer
        if the domain specified in the HTTP/1.1 `Host` header or the HTTP/2 `:authority` pseudo-header matches a domain
        specified in the host.

        A wildcard asterisk character (`*`) matches 0 or more characters.

        If not specified, all domains are attributed to the host, which is the same as specifying a `*` value.
        An HTTP router must not contain more than one virtual host to which all domains are attributed.
        """
    @property
    def routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Route]:
        """Routes of the virtual host.

        A route contains a set of conditions (predicates) that are used by the load balancer to select the route
        for the request and an action on the request.
        For details about the concept, see [documentation](/docs/application-load-balancer/concepts/http-router#routes).

        The order of routes matters: the first route whose predicate matches the request is selected.
        The most specific routes should be at the top of the list, so that they are not overridden.
        For example, if the first HTTP route is configured, via [HttpRoute.match], to match paths prefixed with just `/`,
        other routes are never matched.
        """
    @property
    def modify_request_headers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HeaderModification]:
        """Deprecated, use route_options.modify_request_headers."""
    @property
    def modify_response_headers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HeaderModification]:
        """Deprecated, use route_options.modify_response_headers."""
    @property
    def route_options(self) -> global___RouteOptions: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        authority: collections.abc.Iterable[builtins.str] | None = ...,
        routes: collections.abc.Iterable[global___Route] | None = ...,
        modify_request_headers: collections.abc.Iterable[global___HeaderModification] | None = ...,
        modify_response_headers: collections.abc.Iterable[global___HeaderModification] | None = ...,
        route_options: global___RouteOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["route_options", b"route_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["authority", b"authority", "modify_request_headers", b"modify_request_headers", "modify_response_headers", b"modify_response_headers", "name", b"name", "route_options", b"route_options", "routes", b"routes"]) -> None: ...

global___VirtualHost = VirtualHost

class RouteOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODIFY_REQUEST_HEADERS_FIELD_NUMBER: builtins.int
    MODIFY_RESPONSE_HEADERS_FIELD_NUMBER: builtins.int
    RBAC_FIELD_NUMBER: builtins.int
    @property
    def modify_request_headers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HeaderModification]:
        """Apply the following modifications to the request headers."""
    @property
    def modify_response_headers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HeaderModification]:
        """Apply the following modifications to the response headers."""
    @property
    def rbac(self) -> global___RBAC: ...
    def __init__(
        self,
        *,
        modify_request_headers: collections.abc.Iterable[global___HeaderModification] | None = ...,
        modify_response_headers: collections.abc.Iterable[global___HeaderModification] | None = ...,
        rbac: global___RBAC | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rbac", b"rbac"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["modify_request_headers", b"modify_request_headers", "modify_response_headers", b"modify_response_headers", "rbac", b"rbac"]) -> None: ...

global___RouteOptions = RouteOptions

class RBAC(google.protobuf.message.Message):
    """Role Based Access Control (RBAC) provides router, virtual host, and route access control for the ALB
    service. Requests are allowed or denied based on the `action` and whether a matching principal is
    found. For instance, if the action is ALLOW and a matching principal is found the request should be
    allowed.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Action:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RBAC._Action.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ACTION_UNSPECIFIED: RBAC._Action.ValueType  # 0
        ALLOW: RBAC._Action.ValueType  # 1
        """Allows the request if and only if there is a principal that matches the request."""
        DENY: RBAC._Action.ValueType  # 2
        """Allows the request if and only if there are no principal that match the request."""

    class Action(_Action, metaclass=_ActionEnumTypeWrapper): ...
    ACTION_UNSPECIFIED: RBAC.Action.ValueType  # 0
    ALLOW: RBAC.Action.ValueType  # 1
    """Allows the request if and only if there is a principal that matches the request."""
    DENY: RBAC.Action.ValueType  # 2
    """Allows the request if and only if there are no principal that match the request."""

    ACTION_FIELD_NUMBER: builtins.int
    PRINCIPALS_FIELD_NUMBER: builtins.int
    action: global___RBAC.Action.ValueType
    """The action to take if a principal matches. Every action either allows or denies a request."""
    @property
    def principals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Principals]:
        """Required. A match occurs when at least one matches the request."""
    def __init__(
        self,
        *,
        action: global___RBAC.Action.ValueType = ...,
        principals: collections.abc.Iterable[global___Principals] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "principals", b"principals"]) -> None: ...

global___RBAC = RBAC

class Principals(google.protobuf.message.Message):
    """Principals define a group of identities for a request."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AND_PRINCIPALS_FIELD_NUMBER: builtins.int
    @property
    def and_principals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Principal]:
        """Required. A match occurs when all principals match the request."""
    def __init__(
        self,
        *,
        and_principals: collections.abc.Iterable[global___Principal] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["and_principals", b"and_principals"]) -> None: ...

global___Principals = Principals

class Principal(google.protobuf.message.Message):
    """Principal defines an identity for a request."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class HeaderMatcher(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Specifies the name of the header in the request."""
        @property
        def value(self) -> global___StringMatch:
            """Specifies how the header match will be performed to route the request.
            In the absence of value a request that has specified header name will match,
            regardless of the header's value.
            """
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            value: global___StringMatch | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "value", b"value"]) -> None: ...

    HEADER_FIELD_NUMBER: builtins.int
    REMOTE_IP_FIELD_NUMBER: builtins.int
    ANY_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___Principal.HeaderMatcher:
        """A header (or pseudo-header such as :path or :method) of the incoming HTTP request."""
    remote_ip: builtins.str
    """A CIDR block or IP that describes the request remote/origin address, e.g. ``192.0.0.0/24`` or``192.0.0.4`` ."""
    any: builtins.bool
    """When any is set, it matches any request."""
    def __init__(
        self,
        *,
        header: global___Principal.HeaderMatcher | None = ...,
        remote_ip: builtins.str = ...,
        any: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["any", b"any", "header", b"header", "identifier", b"identifier", "remote_ip", b"remote_ip"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["any", b"any", "header", b"header", "identifier", b"identifier", "remote_ip", b"remote_ip"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["identifier", b"identifier"]) -> typing_extensions.Literal["header", "remote_ip", "any"] | None: ...

global___Principal = Principal

class HeaderModification(google.protobuf.message.Message):
    """A header modification resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    APPEND_FIELD_NUMBER: builtins.int
    REPLACE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    RENAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the header."""
    append: builtins.str
    """Appends the specified string to the header value.

    Variables [defined for Envoy proxy](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#custom-request-response-headers)
    are supported.
    """
    replace: builtins.str
    """Replaces the value of the header with the specified string.

    Variables [defined for Envoy proxy](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#custom-request-response-headers)
    are supported.
    """
    remove: builtins.bool
    """Removes the header."""
    rename: builtins.str
    """Replaces the name of the header with the specified string.
    This operation is only supported for ALB Virtual Hosts.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        append: builtins.str = ...,
        replace: builtins.str = ...,
        remove: builtins.bool = ...,
        rename: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["append", b"append", "operation", b"operation", "remove", b"remove", "rename", b"rename", "replace", b"replace"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["append", b"append", "name", b"name", "operation", b"operation", "remove", b"remove", "rename", b"rename", "replace", b"replace"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation", b"operation"]) -> typing_extensions.Literal["append", "replace", "remove", "rename"] | None: ...

global___HeaderModification = HeaderModification

class Route(google.protobuf.message.Message):
    """A route resource.
    For details about the concept, see [documentation](/docs/application-load-balancer/concepts/http-router#routes).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    HTTP_FIELD_NUMBER: builtins.int
    GRPC_FIELD_NUMBER: builtins.int
    ROUTE_OPTIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the route."""
    @property
    def http(self) -> global___HttpRoute:
        """HTTP route configuration."""
    @property
    def grpc(self) -> global___GrpcRoute:
        """gRPC route configuration."""
    @property
    def route_options(self) -> global___RouteOptions: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        http: global___HttpRoute | None = ...,
        grpc: global___GrpcRoute | None = ...,
        route_options: global___RouteOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["grpc", b"grpc", "http", b"http", "route", b"route", "route_options", b"route_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["grpc", b"grpc", "http", b"http", "name", b"name", "route", b"route", "route_options", b"route_options"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["route", b"route"]) -> typing_extensions.Literal["http", "grpc"] | None: ...

global___Route = Route

class HttpRoute(google.protobuf.message.Message):
    """An HTTP route configuration resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MATCH_FIELD_NUMBER: builtins.int
    ROUTE_FIELD_NUMBER: builtins.int
    REDIRECT_FIELD_NUMBER: builtins.int
    DIRECT_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def match(self) -> global___HttpRouteMatch:
        """Condition (predicate) used to select the route."""
    @property
    def route(self) -> global___HttpRouteAction:
        """Forwards the request to a backend group for processing as configured."""
    @property
    def redirect(self) -> global___RedirectAction:
        """Redirects the request as configured."""
    @property
    def direct_response(self) -> global___DirectResponseAction:
        """Instructs the load balancer to respond directly as configured."""
    def __init__(
        self,
        *,
        match: global___HttpRouteMatch | None = ...,
        route: global___HttpRouteAction | None = ...,
        redirect: global___RedirectAction | None = ...,
        direct_response: global___DirectResponseAction | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["action", b"action", "direct_response", b"direct_response", "match", b"match", "redirect", b"redirect", "route", b"route"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "direct_response", b"direct_response", "match", b"match", "redirect", b"redirect", "route", b"route"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["action", b"action"]) -> typing_extensions.Literal["route", "redirect", "direct_response"] | None: ...

global___HttpRoute = HttpRoute

class GrpcRoute(google.protobuf.message.Message):
    """A gRPC route configuration resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MATCH_FIELD_NUMBER: builtins.int
    ROUTE_FIELD_NUMBER: builtins.int
    STATUS_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def match(self) -> global___GrpcRouteMatch:
        """Condition (predicate) used to select the route."""
    @property
    def route(self) -> global___GrpcRouteAction:
        """Forwards the request to a backend group for processing as configured."""
    @property
    def status_response(self) -> global___GrpcStatusResponseAction:
        """Instructs the load balancer to respond directly with a specified status."""
    def __init__(
        self,
        *,
        match: global___GrpcRouteMatch | None = ...,
        route: global___GrpcRouteAction | None = ...,
        status_response: global___GrpcStatusResponseAction | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["action", b"action", "match", b"match", "route", b"route", "status_response", b"status_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "match", b"match", "route", b"route", "status_response", b"status_response"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["action", b"action"]) -> typing_extensions.Literal["route", "status_response"] | None: ...

global___GrpcRoute = GrpcRoute

class HttpRouteMatch(google.protobuf.message.Message):
    """An HTTP route condition (predicate) resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_METHOD_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    @property
    def http_method(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """HTTP method specified in the request."""
    @property
    def path(self) -> global___StringMatch:
        """Match settings for the path specified in the request.

        If not specified, the route matches all paths.
        """
    def __init__(
        self,
        *,
        http_method: collections.abc.Iterable[builtins.str] | None = ...,
        path: global___StringMatch | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["path", b"path"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_method", b"http_method", "path", b"path"]) -> None: ...

global___HttpRouteMatch = HttpRouteMatch

class GrpcRouteMatch(google.protobuf.message.Message):
    """A gRPC route condition (predicate) resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FQMN_FIELD_NUMBER: builtins.int
    @property
    def fqmn(self) -> global___StringMatch:
        """Match settings for gRPC service method called in the request.

        A match string must be a fully qualified method name, e.g. `foo.bar.v1.BazService/Get`, or a prefix of such.

        If not specified, the route matches all methods.
        """
    def __init__(
        self,
        *,
        fqmn: global___StringMatch | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fqmn", b"fqmn"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fqmn", b"fqmn"]) -> None: ...

global___GrpcRouteMatch = GrpcRouteMatch

class StringMatch(google.protobuf.message.Message):
    """A string matcher resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXACT_MATCH_FIELD_NUMBER: builtins.int
    PREFIX_MATCH_FIELD_NUMBER: builtins.int
    REGEX_MATCH_FIELD_NUMBER: builtins.int
    exact_match: builtins.str
    """Exact match string."""
    prefix_match: builtins.str
    """Prefix match string."""
    regex_match: builtins.str
    """Regular expression match string."""
    def __init__(
        self,
        *,
        exact_match: builtins.str = ...,
        prefix_match: builtins.str = ...,
        regex_match: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["exact_match", b"exact_match", "match", b"match", "prefix_match", b"prefix_match", "regex_match", b"regex_match"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exact_match", b"exact_match", "match", b"match", "prefix_match", b"prefix_match", "regex_match", b"regex_match"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["match", b"match"]) -> typing_extensions.Literal["exact_match", "prefix_match", "regex_match"] | None: ...

global___StringMatch = StringMatch

class RedirectAction(google.protobuf.message.Message):
    """A redirect action resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _RedirectResponseCode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RedirectResponseCodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RedirectAction._RedirectResponseCode.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        MOVED_PERMANENTLY: RedirectAction._RedirectResponseCode.ValueType  # 0
        """`301 Moved Permanently` status code."""
        FOUND: RedirectAction._RedirectResponseCode.ValueType  # 1
        """`302 Found` status code."""
        SEE_OTHER: RedirectAction._RedirectResponseCode.ValueType  # 2
        """`303 See Other` status code."""
        TEMPORARY_REDIRECT: RedirectAction._RedirectResponseCode.ValueType  # 3
        """`307 Temporary Redirect` status code."""
        PERMANENT_REDIRECT: RedirectAction._RedirectResponseCode.ValueType  # 4
        """`308 Permanent Redirect` status code."""

    class RedirectResponseCode(_RedirectResponseCode, metaclass=_RedirectResponseCodeEnumTypeWrapper):
        """HTTP status codes supported for use in redirect responses."""

    MOVED_PERMANENTLY: RedirectAction.RedirectResponseCode.ValueType  # 0
    """`301 Moved Permanently` status code."""
    FOUND: RedirectAction.RedirectResponseCode.ValueType  # 1
    """`302 Found` status code."""
    SEE_OTHER: RedirectAction.RedirectResponseCode.ValueType  # 2
    """`303 See Other` status code."""
    TEMPORARY_REDIRECT: RedirectAction.RedirectResponseCode.ValueType  # 3
    """`307 Temporary Redirect` status code."""
    PERMANENT_REDIRECT: RedirectAction.RedirectResponseCode.ValueType  # 4
    """`308 Permanent Redirect` status code."""

    REPLACE_SCHEME_FIELD_NUMBER: builtins.int
    REPLACE_HOST_FIELD_NUMBER: builtins.int
    REPLACE_PORT_FIELD_NUMBER: builtins.int
    REPLACE_PATH_FIELD_NUMBER: builtins.int
    REPLACE_PREFIX_FIELD_NUMBER: builtins.int
    REMOVE_QUERY_FIELD_NUMBER: builtins.int
    RESPONSE_CODE_FIELD_NUMBER: builtins.int
    replace_scheme: builtins.str
    """URI scheme replacement.

    If `http` or `https` scheme is to be replaced and `80` or `443` port is specified in the original URI,
    the port is also removed.

    If not specified, the original scheme and port are used.
    """
    replace_host: builtins.str
    """URI host replacement.

    If not specified, the original host is used.
    """
    replace_port: builtins.int
    """URI host replacement.

    If not specified, the original host is used.
    """
    replace_path: builtins.str
    """Replacement for the whole path."""
    replace_prefix: builtins.str
    """Replacement for the path prefix matched by [StringMatch].

    For instance, if [StringMatch.prefix_match] value is `/foo` and `replace_prefix` value is `/bar`,
    a request with `https://example.com/foobaz` URI is redirected to `https://example.com/barbaz`.
    For [StringMatch.exact_match], the whole path is replaced.
    """
    remove_query: builtins.bool
    """Removes URI query."""
    response_code: global___RedirectAction.RedirectResponseCode.ValueType
    """HTTP status code to use in redirect responses."""
    def __init__(
        self,
        *,
        replace_scheme: builtins.str = ...,
        replace_host: builtins.str = ...,
        replace_port: builtins.int = ...,
        replace_path: builtins.str = ...,
        replace_prefix: builtins.str = ...,
        remove_query: builtins.bool = ...,
        response_code: global___RedirectAction.RedirectResponseCode.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["path", b"path", "replace_path", b"replace_path", "replace_prefix", b"replace_prefix"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path", "remove_query", b"remove_query", "replace_host", b"replace_host", "replace_path", b"replace_path", "replace_port", b"replace_port", "replace_prefix", b"replace_prefix", "replace_scheme", b"replace_scheme", "response_code", b"response_code"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["path", b"path"]) -> typing_extensions.Literal["replace_path", "replace_prefix"] | None: ...

global___RedirectAction = RedirectAction

class DirectResponseAction(google.protobuf.message.Message):
    """A direct response action resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    status: builtins.int
    """HTTP status code to use in responses."""
    @property
    def body(self) -> yandex.cloud.apploadbalancer.v1.payload_pb2.Payload:
        """Response body."""
    def __init__(
        self,
        *,
        status: builtins.int = ...,
        body: yandex.cloud.apploadbalancer.v1.payload_pb2.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body", b"body"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body", b"body", "status", b"status"]) -> None: ...

global___DirectResponseAction = DirectResponseAction

class GrpcStatusResponseAction(google.protobuf.message.Message):
    """A gRPC status response action resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[GrpcStatusResponseAction._Status.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        OK: GrpcStatusResponseAction._Status.ValueType  # 0
        """`OK` (0) status code."""
        INVALID_ARGUMENT: GrpcStatusResponseAction._Status.ValueType  # 1
        """`INVALID_ARGUMENT` (3) status code."""
        NOT_FOUND: GrpcStatusResponseAction._Status.ValueType  # 2
        """`NOT_FOUND` (5) status code."""
        PERMISSION_DENIED: GrpcStatusResponseAction._Status.ValueType  # 3
        """`PERMISSION_DENIED` (7) status code."""
        UNAUTHENTICATED: GrpcStatusResponseAction._Status.ValueType  # 4
        """`UNAUTHENTICATED` (16) status code."""
        UNIMPLEMENTED: GrpcStatusResponseAction._Status.ValueType  # 5
        """`UNIMPLEMENTED` (12) status code."""
        INTERNAL: GrpcStatusResponseAction._Status.ValueType  # 6
        """`INTERNAL` (13) status code."""
        UNAVAILABLE: GrpcStatusResponseAction._Status.ValueType  # 7
        """`UNAVAILABLE` (14) status code."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """gRPC status code supported for use in responses."""

    OK: GrpcStatusResponseAction.Status.ValueType  # 0
    """`OK` (0) status code."""
    INVALID_ARGUMENT: GrpcStatusResponseAction.Status.ValueType  # 1
    """`INVALID_ARGUMENT` (3) status code."""
    NOT_FOUND: GrpcStatusResponseAction.Status.ValueType  # 2
    """`NOT_FOUND` (5) status code."""
    PERMISSION_DENIED: GrpcStatusResponseAction.Status.ValueType  # 3
    """`PERMISSION_DENIED` (7) status code."""
    UNAUTHENTICATED: GrpcStatusResponseAction.Status.ValueType  # 4
    """`UNAUTHENTICATED` (16) status code."""
    UNIMPLEMENTED: GrpcStatusResponseAction.Status.ValueType  # 5
    """`UNIMPLEMENTED` (12) status code."""
    INTERNAL: GrpcStatusResponseAction.Status.ValueType  # 6
    """`INTERNAL` (13) status code."""
    UNAVAILABLE: GrpcStatusResponseAction.Status.ValueType  # 7
    """`UNAVAILABLE` (14) status code."""

    STATUS_FIELD_NUMBER: builtins.int
    status: global___GrpcStatusResponseAction.Status.ValueType
    """gRPC [status code](https://grpc.github.io/grpc/core/md_doc_statuscodes.html) to use in responses."""
    def __init__(
        self,
        *,
        status: global___GrpcStatusResponseAction.Status.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["status", b"status"]) -> None: ...

global___GrpcStatusResponseAction = GrpcStatusResponseAction

class HttpRouteAction(google.protobuf.message.Message):
    """An HTTP route action resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKEND_GROUP_ID_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    IDLE_TIMEOUT_FIELD_NUMBER: builtins.int
    HOST_REWRITE_FIELD_NUMBER: builtins.int
    AUTO_HOST_REWRITE_FIELD_NUMBER: builtins.int
    PREFIX_REWRITE_FIELD_NUMBER: builtins.int
    UPGRADE_TYPES_FIELD_NUMBER: builtins.int
    backend_group_id: builtins.str
    """Backend group to forward requests to.

    Stream (TCP) backend groups are not supported.
    """
    @property
    def timeout(self) -> google.protobuf.duration_pb2.Duration:
        """Overall timeout for an HTTP connection between a load balancer node an a backend from the backend group:
        the maximum time the connection is kept alive for, regardless of whether data is transferred over it.

        If a connection times out, the load balancer responds to the client with a `504 Gateway Timeout` status code.

        Default value: `60`.
        """
    @property
    def idle_timeout(self) -> google.protobuf.duration_pb2.Duration:
        """Idle timeout for an HTTP connection between a load balancer node an a backend from the backend group:
        the maximum time the connection is allowed to be idle, i.e. without any data transferred over it.

        Specifying meaningful values for both [timeout] and `idle_timeout` is useful for implementing
        server-push mechanisms such as long polling, server-sent events (`EventSource` interface) etc.

        If a connection times out, the load balancer responds to the client with a `504 Gateway Timeout` status code.

        If not specified, no idle timeout is used, and an alive connection may be idle for any duration (see [timeout]).
        """
    host_rewrite: builtins.str
    """Host replacement."""
    auto_host_rewrite: builtins.bool
    """Automatically replaces the host with that of the target."""
    prefix_rewrite: builtins.str
    """Replacement for the path prefix matched by [StringMatch].

    For instance, if [StringMatch.prefix_match] value is `/foo` and `replace_prefix` value is `/bar`,
    a request with `/foobaz` path is forwarded with `/barbaz` path.
    For [StringMatch.exact_match], the whole path is replaced.

    If not specified, the path is not changed.
    """
    @property
    def upgrade_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Supported values for HTTP `Upgrade` header. E.g. `websocket`."""
    def __init__(
        self,
        *,
        backend_group_id: builtins.str = ...,
        timeout: google.protobuf.duration_pb2.Duration | None = ...,
        idle_timeout: google.protobuf.duration_pb2.Duration | None = ...,
        host_rewrite: builtins.str = ...,
        auto_host_rewrite: builtins.bool = ...,
        prefix_rewrite: builtins.str = ...,
        upgrade_types: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["auto_host_rewrite", b"auto_host_rewrite", "host_rewrite", b"host_rewrite", "host_rewrite_specifier", b"host_rewrite_specifier", "idle_timeout", b"idle_timeout", "timeout", b"timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_host_rewrite", b"auto_host_rewrite", "backend_group_id", b"backend_group_id", "host_rewrite", b"host_rewrite", "host_rewrite_specifier", b"host_rewrite_specifier", "idle_timeout", b"idle_timeout", "prefix_rewrite", b"prefix_rewrite", "timeout", b"timeout", "upgrade_types", b"upgrade_types"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["host_rewrite_specifier", b"host_rewrite_specifier"]) -> typing_extensions.Literal["host_rewrite", "auto_host_rewrite"] | None: ...

global___HttpRouteAction = HttpRouteAction

class GrpcRouteAction(google.protobuf.message.Message):
    """A gRPC route action resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKEND_GROUP_ID_FIELD_NUMBER: builtins.int
    MAX_TIMEOUT_FIELD_NUMBER: builtins.int
    IDLE_TIMEOUT_FIELD_NUMBER: builtins.int
    HOST_REWRITE_FIELD_NUMBER: builtins.int
    AUTO_HOST_REWRITE_FIELD_NUMBER: builtins.int
    backend_group_id: builtins.str
    """Backend group to forward requests to."""
    @property
    def max_timeout(self) -> google.protobuf.duration_pb2.Duration:
        """Overall timeout for an underlying HTTP connection between a load balancer node an a backend from the backend group:
        the maximum time the connection is kept alive for, regardless of whether data is transferred over it.

        If a client specifies a lower timeout in HTTP `grpc-timeout` header, the `max_timeout` value is ignored.

        If a connection times out, the load balancer responds to the client with an `UNAVAILABLE` status code.

        Default value: `60`.
        """
    @property
    def idle_timeout(self) -> google.protobuf.duration_pb2.Duration:
        """Idle timeout for an underlying HTTP connection between a load balancer node an a backend from the backend group:
        the maximum time the connection is allowed to be idle, i.e. without any data transferred over it.

        Specifying meaningful values for both [max_timeout] and `idle_timeout` is useful for implementing
        server-push mechanisms such as long polling, server-sent events etc.

        If a connection times out, the load balancer responds to the client with an `UNAVAILABLE` status code.

        If not specified, no idle timeout is used, and an alive connection may be idle for any duration
        (see [max_timeout]).
        """
    host_rewrite: builtins.str
    """Host replacement."""
    auto_host_rewrite: builtins.bool
    """Automatically replaces the host with that of the target."""
    def __init__(
        self,
        *,
        backend_group_id: builtins.str = ...,
        max_timeout: google.protobuf.duration_pb2.Duration | None = ...,
        idle_timeout: google.protobuf.duration_pb2.Duration | None = ...,
        host_rewrite: builtins.str = ...,
        auto_host_rewrite: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["auto_host_rewrite", b"auto_host_rewrite", "host_rewrite", b"host_rewrite", "host_rewrite_specifier", b"host_rewrite_specifier", "idle_timeout", b"idle_timeout", "max_timeout", b"max_timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_host_rewrite", b"auto_host_rewrite", "backend_group_id", b"backend_group_id", "host_rewrite", b"host_rewrite", "host_rewrite_specifier", b"host_rewrite_specifier", "idle_timeout", b"idle_timeout", "max_timeout", b"max_timeout"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["host_rewrite_specifier", b"host_rewrite_specifier"]) -> typing_extensions.Literal["host_rewrite", "auto_host_rewrite"] | None: ...

global___GrpcRouteAction = GrpcRouteAction
