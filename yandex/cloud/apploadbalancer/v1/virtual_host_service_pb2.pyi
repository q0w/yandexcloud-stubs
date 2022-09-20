"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import yandex.cloud.apploadbalancer.v1.virtual_host_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetVirtualHostRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router that the virtual host belongs to.

    To get the HTTP router ID, make a [HttpRouterService.List] request.
    """
    virtual_host_name: builtins.str
    """Name of the virtual host to return.

    To get the virtual host name, make a [VirtualHostService.List] request.
    """
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___GetVirtualHostRequest = GetVirtualHostRequest

class ListVirtualHostsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router to list virtual hosts in.

    To get the HTTP router ID, make a [HttpRouterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListVirtualHostsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListVirtualHostsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListVirtualHostsRequest = ListVirtualHostsRequest

class ListVirtualHostsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VIRTUAL_HOSTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def virtual_hosts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.VirtualHost]:
        """List of virtual hosts of the specified HTTP router."""
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListVirtualHostsRequest.page_size], use `next_page_token` as the value
    for the [ListVirtualHostsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        virtual_hosts: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.VirtualHost] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "virtual_hosts", b"virtual_hosts"]) -> None: ...

global___ListVirtualHostsResponse = ListVirtualHostsResponse

class CreateVirtualHostRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    AUTHORITY_FIELD_NUMBER: builtins.int
    ROUTES_FIELD_NUMBER: builtins.int
    MODIFY_REQUEST_HEADERS_FIELD_NUMBER: builtins.int
    MODIFY_RESPONSE_HEADERS_FIELD_NUMBER: builtins.int
    ROUTE_OPTIONS_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router to create a virtual host in.

    To get the HTTP router ID, make a [HttpRouterService.List] request.
    """
    name: builtins.str
    """Name of the virtual host. The name must be unique within the HTTP router and cannot be changed after creation."""
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
    def routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.Route]:
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
    def modify_request_headers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HeaderModification]:
        """Modifications that are made to the headers of incoming HTTP requests before they are forwarded to backends."""
    @property
    def modify_response_headers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HeaderModification]:
        """Modifications that are made to the headers of HTTP responses received from backends
        before responses are forwarded to clients.
        """
    @property
    def route_options(self) -> yandex.cloud.apploadbalancer.v1.virtual_host_pb2.RouteOptions:
        """Route options for the virtual host."""
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        name: builtins.str = ...,
        authority: collections.abc.Iterable[builtins.str] | None = ...,
        routes: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.Route] | None = ...,
        modify_request_headers: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HeaderModification] | None = ...,
        modify_response_headers: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HeaderModification] | None = ...,
        route_options: yandex.cloud.apploadbalancer.v1.virtual_host_pb2.RouteOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["route_options", b"route_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["authority", b"authority", "http_router_id", b"http_router_id", "modify_request_headers", b"modify_request_headers", "modify_response_headers", b"modify_response_headers", "name", b"name", "route_options", b"route_options", "routes", b"routes"]) -> None: ...

global___CreateVirtualHostRequest = CreateVirtualHostRequest

class CreateVirtualHostMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router that the virtual host is being created in."""
    virtual_host_name: builtins.str
    """Name of the virtual host that is being created."""
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___CreateVirtualHostMetadata = CreateVirtualHostMetadata

class UpdateVirtualHostRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    AUTHORITY_FIELD_NUMBER: builtins.int
    ROUTES_FIELD_NUMBER: builtins.int
    MODIFY_REQUEST_HEADERS_FIELD_NUMBER: builtins.int
    MODIFY_RESPONSE_HEADERS_FIELD_NUMBER: builtins.int
    ROUTE_OPTIONS_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router to update a virtual host in.

    To get the HTTP router ID, make a [HttpRouterService.List] request.
    """
    virtual_host_name: builtins.str
    """Name of the virtual host.

    Used only to refer to the virtual host. The name of a host cannot be changed.

    To get the virtual host name, make a [VirtualHostService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the virtual host should be updated."""
    @property
    def authority(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """New list of domains to attribute to the virtual host.

        The host is selected to process the request received by the load balancer
        if the domain specified in the HTTP/1.1 `Host` header or the HTTP/2 `:authority` pseudo-header matches a domain
        specified in the host.

        A wildcard asterisk character (`*`) matches 0 or more characters.

        Existing list of domains is completely replaced by the specified list.

        If not specified, all domains are attributed to the host, which is the same as specifying a `*` value.
        An HTTP router must not contain more than one virtual host to which all domains are attributed.
        """
    @property
    def routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.Route]:
        """New list of routes of the virtual host.

        A route contains a set of conditions (predicates) that are used by the load balancer to select the route
        for the request and an action on the request.
        For details about the concept, see [documentation](/docs/application-load-balancer/concepts/http-router#routes).

        The order of routes matters: the first route whose predicate matches the request is selected.
        The most specific routes should be at the top of the list, so that they are not overridden.
        For example, if the first HTTP route is configured, via [HttpRoute.match], to match paths prefixed with just `/`,
        other routes are never matched.

        Existing list of routes is completely replaced by the specified list, so if you just want to remove a route,
        make a [VirtualHostService.RemoveRoute] request.
        """
    @property
    def modify_request_headers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HeaderModification]:
        """New list of modifications that are made to the headers of incoming HTTP requests
        before they are forwarded to backends.

        Existing list of modifications is completely replaced by the specified list.
        """
    @property
    def modify_response_headers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HeaderModification]:
        """New list of modifications that are made to the headers of HTTP responses received from backends
        before responses are forwarded to clients.

        Existing list of modifications is completely replaced by the specified list.
        """
    @property
    def route_options(self) -> yandex.cloud.apploadbalancer.v1.virtual_host_pb2.RouteOptions:
        """New route options for the virtual host."""
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        authority: collections.abc.Iterable[builtins.str] | None = ...,
        routes: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.Route] | None = ...,
        modify_request_headers: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HeaderModification] | None = ...,
        modify_response_headers: collections.abc.Iterable[yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HeaderModification] | None = ...,
        route_options: yandex.cloud.apploadbalancer.v1.virtual_host_pb2.RouteOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["route_options", b"route_options", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["authority", b"authority", "http_router_id", b"http_router_id", "modify_request_headers", b"modify_request_headers", "modify_response_headers", b"modify_response_headers", "route_options", b"route_options", "routes", b"routes", "update_mask", b"update_mask", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___UpdateVirtualHostRequest = UpdateVirtualHostRequest

class UpdateVirtualHostMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router that the virtual host is being updated in."""
    virtual_host_name: builtins.str
    """Name of the virtual host that is being updated."""
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___UpdateVirtualHostMetadata = UpdateVirtualHostMetadata

class DeleteVirtualHostRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router to delete a virtual host from.

    To get the HTTP router ID, make a [HttpRouterService.List] request.
    """
    virtual_host_name: builtins.str
    """Name of the virtual host to delete.

    To get the virtual host name, make a [VirtualHostService.List] request.
    """
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___DeleteVirtualHostRequest = DeleteVirtualHostRequest

class DeleteVirtualHostMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router that the virtual host is being deleted from."""
    virtual_host_name: builtins.str
    """Name of the virtual host that is being deleted."""
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___DeleteVirtualHostMetadata = DeleteVirtualHostMetadata

class RemoveRouteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    ROUTE_NAME_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router to delete a route from.

    To get the HTTP router ID, make a [HttpRouterService.List] request.
    """
    virtual_host_name: builtins.str
    """Name of the virtual host to delete a route from.

    To get the virtual host name, make a [VirtualHostService.List] request.
    """
    route_name: builtins.str
    """Name of the route to delete.

    To get the route name, make a [VirtualHostService.Get] request.
    """
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
        route_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "route_name", b"route_name", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___RemoveRouteRequest = RemoveRouteRequest

class RemoveRouteMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    ROUTE_NAME_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router that the route is being deleted from."""
    virtual_host_name: builtins.str
    """Name of the virtual host that the route is being deleted from."""
    route_name: builtins.str
    """Name of the route that is being deleted."""
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
        route_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "route_name", b"route_name", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___RemoveRouteMetadata = RemoveRouteMetadata

class UpdateRouteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    ROUTE_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    HTTP_FIELD_NUMBER: builtins.int
    GRPC_FIELD_NUMBER: builtins.int
    ROUTE_OPTIONS_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router to update a route in.

    To get the HTTP router ID, make a [HttpRouterService.List] request.
    """
    virtual_host_name: builtins.str
    """Name of the virtual host to update a route in.

    To get the virtual host name, make a [VirtualHostService.List] request.
    """
    route_name: builtins.str
    """Name of the route to update.

    To get the route name, make a [VirtualHostService.Get] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the route should be updated."""
    @property
    def http(self) -> yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HttpRoute:
        """New settings of the HTTP route."""
    @property
    def grpc(self) -> yandex.cloud.apploadbalancer.v1.virtual_host_pb2.GrpcRoute:
        """New settings of the gRPC route."""
    @property
    def route_options(self) -> yandex.cloud.apploadbalancer.v1.virtual_host_pb2.RouteOptions:
        """New route options for the route."""
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
        route_name: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        http: yandex.cloud.apploadbalancer.v1.virtual_host_pb2.HttpRoute | None = ...,
        grpc: yandex.cloud.apploadbalancer.v1.virtual_host_pb2.GrpcRoute | None = ...,
        route_options: yandex.cloud.apploadbalancer.v1.virtual_host_pb2.RouteOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["grpc", b"grpc", "http", b"http", "route", b"route", "route_options", b"route_options", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["grpc", b"grpc", "http", b"http", "http_router_id", b"http_router_id", "route", b"route", "route_name", b"route_name", "route_options", b"route_options", "update_mask", b"update_mask", "virtual_host_name", b"virtual_host_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["route", b"route"]) -> typing_extensions.Literal["http", "grpc"] | None: ...

global___UpdateRouteRequest = UpdateRouteRequest

class UpdateRouteMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_ROUTER_ID_FIELD_NUMBER: builtins.int
    VIRTUAL_HOST_NAME_FIELD_NUMBER: builtins.int
    ROUTE_NAME_FIELD_NUMBER: builtins.int
    http_router_id: builtins.str
    """ID of the HTTP router that the route is being updated in."""
    virtual_host_name: builtins.str
    """Name of the virtual host that the route is being updated in."""
    route_name: builtins.str
    """Name of the route that is being updated."""
    def __init__(
        self,
        *,
        http_router_id: builtins.str = ...,
        virtual_host_name: builtins.str = ...,
        route_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_router_id", b"http_router_id", "route_name", b"route_name", "virtual_host_name", b"virtual_host_name"]) -> None: ...

global___UpdateRouteMetadata = UpdateRouteMetadata
