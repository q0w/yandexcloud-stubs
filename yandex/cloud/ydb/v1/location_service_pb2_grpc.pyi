"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.ydb.v1.location_pb2
import yandex.cloud.ydb.v1.location_service_pb2

class LocationServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.location_service_pb2.GetLocationRequest,
        yandex.cloud.ydb.v1.location_pb2.Location,
    ]
    """Returns the specified location."""
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ydb.v1.location_service_pb2.ListLocationsRequest,
        yandex.cloud.ydb.v1.location_service_pb2.ListLocationsResponse,
    ]
    """Returns the list of available locations."""

class LocationServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.ydb.v1.location_service_pb2.GetLocationRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.ydb.v1.location_pb2.Location:
        """Returns the specified location."""
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.ydb.v1.location_service_pb2.ListLocationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.ydb.v1.location_service_pb2.ListLocationsResponse:
        """Returns the list of available locations."""

def add_LocationServiceServicer_to_server(servicer: LocationServiceServicer, server: grpc.Server) -> None: ...
