"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.dataproc.v1.resource_preset_pb2
import yandex.cloud.dataproc.v1.resource_preset_service_pb2

class ResourcePresetServiceStub:
    """A set of methods for managing ResourcePreset resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.resource_preset_service_pb2.GetResourcePresetRequest,
        yandex.cloud.dataproc.v1.resource_preset_pb2.ResourcePreset,
    ]
    """Returns the specified ResourcePreset resource.

    To get the list of available ResourcePreset resources, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.resource_preset_service_pb2.ListResourcePresetsRequest,
        yandex.cloud.dataproc.v1.resource_preset_service_pb2.ListResourcePresetsResponse,
    ]
    """Retrieves the list of available ResourcePreset resources."""

class ResourcePresetServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing ResourcePreset resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.dataproc.v1.resource_preset_service_pb2.GetResourcePresetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.resource_preset_pb2.ResourcePreset:
        """Returns the specified ResourcePreset resource.

        To get the list of available ResourcePreset resources, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.dataproc.v1.resource_preset_service_pb2.ListResourcePresetsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.resource_preset_service_pb2.ListResourcePresetsResponse:
        """Retrieves the list of available ResourcePreset resources."""

def add_ResourcePresetServiceServicer_to_server(servicer: ResourcePresetServiceServicer, server: grpc.Server) -> None: ...
