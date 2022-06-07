"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.mysql.v1alpha.resource_preset_pb2
import yandex.cloud.mdb.mysql.v1alpha.resource_preset_service_pb2

class ResourcePresetServiceStub:
    """A set of methods for managing resource presets."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.resource_preset_service_pb2.GetResourcePresetRequest,
        yandex.cloud.mdb.mysql.v1alpha.resource_preset_pb2.ResourcePreset]
    """Returns the specified resource preset.

    To get the list of available resource presets, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.resource_preset_service_pb2.ListResourcePresetsRequest,
        yandex.cloud.mdb.mysql.v1alpha.resource_preset_service_pb2.ListResourcePresetsResponse]
    """Retrieves the list of available resource presets."""


class ResourcePresetServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing resource presets."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.mdb.mysql.v1alpha.resource_preset_service_pb2.GetResourcePresetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mysql.v1alpha.resource_preset_pb2.ResourcePreset:
        """Returns the specified resource preset.

        To get the list of available resource presets, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.mdb.mysql.v1alpha.resource_preset_service_pb2.ListResourcePresetsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.mysql.v1alpha.resource_preset_service_pb2.ListResourcePresetsResponse:
        """Retrieves the list of available resource presets."""
        pass


def add_ResourcePresetServiceServicer_to_server(servicer: ResourcePresetServiceServicer, server: grpc.Server) -> None: ...