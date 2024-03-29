"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.cdn.v1.cache_service_pb2
import yandex.cloud.operation.operation_pb2

class CacheServiceStub:
    """A set of methods for managing Cache Service resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Purge: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.cache_service_pb2.PurgeCacheRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes specified files from the cache of the specified resource. For details about purging, see [documentation](/docs/cdn/concepts/caching#purge).

    Purging may take up to 15 minutes.
    """
    Prefetch: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.cache_service_pb2.PrefetchCacheRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Uploads specified files from origins to cache of the specified resource. For defails about prefetching, see [documentation](/docs/cdn/concepts/caching#prefetch)."""

class CacheServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Cache Service resources."""

    @abc.abstractmethod
    def Purge(
        self,
        request: yandex.cloud.cdn.v1.cache_service_pb2.PurgeCacheRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Removes specified files from the cache of the specified resource. For details about purging, see [documentation](/docs/cdn/concepts/caching#purge).

        Purging may take up to 15 minutes.
        """
    @abc.abstractmethod
    def Prefetch(
        self,
        request: yandex.cloud.cdn.v1.cache_service_pb2.PrefetchCacheRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Uploads specified files from origins to cache of the specified resource. For defails about prefetching, see [documentation](/docs/cdn/concepts/caching#prefetch)."""

def add_CacheServiceServicer_to_server(servicer: CacheServiceServicer, server: grpc.Server) -> None: ...
