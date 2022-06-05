"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.containerregistry.v1.image_pb2
import yandex.cloud.containerregistry.v1.image_service_pb2
import yandex.cloud.operation.operation_pb2

class ImageServiceStub:
    """A set of methods for managing Image resources."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.image_service_pb2.ListImagesRequest,
        yandex.cloud.containerregistry.v1.image_service_pb2.ListImagesResponse]
    """Retrieves the list of Image resources in the specified registry or repository."""

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.image_service_pb2.GetImageRequest,
        yandex.cloud.containerregistry.v1.image_pb2.Image]
    """Returns the specified Image resource.

    To get the list of available Image resources, make a [List] request.
    """

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.image_service_pb2.DeleteImageRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified Docker image."""


class ImageServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Image resources."""
    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.containerregistry.v1.image_service_pb2.ListImagesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.image_service_pb2.ListImagesResponse:
        """Retrieves the list of Image resources in the specified registry or repository."""
        pass

    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.containerregistry.v1.image_service_pb2.GetImageRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.image_pb2.Image:
        """Returns the specified Image resource.

        To get the list of available Image resources, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.containerregistry.v1.image_service_pb2.DeleteImageRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified Docker image."""
        pass


def add_ImageServiceServicer_to_server(servicer: ImageServiceServicer, server: grpc.Server) -> None: ...
