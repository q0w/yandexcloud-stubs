"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.billing.v1.sku_pb2
import yandex.cloud.billing.v1.sku_service_pb2

class SkuServiceStub:
    """A set of methods for managing Sku resources."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.sku_service_pb2.GetSkuRequest,
        yandex.cloud.billing.v1.sku_pb2.Sku]
    """Returns the specified SKU."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.sku_service_pb2.ListSkusRequest,
        yandex.cloud.billing.v1.sku_service_pb2.ListSkusResponse]
    """Retrieves the list of SKUs."""


class SkuServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Sku resources."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.billing.v1.sku_service_pb2.GetSkuRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.billing.v1.sku_pb2.Sku:
        """Returns the specified SKU."""
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.billing.v1.sku_service_pb2.ListSkusRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.billing.v1.sku_service_pb2.ListSkusResponse:
        """Retrieves the list of SKUs."""
        pass


def add_SkuServiceServicer_to_server(servicer: SkuServiceServicer, server: grpc.Server) -> None: ...