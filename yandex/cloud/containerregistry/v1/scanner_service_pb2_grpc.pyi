"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.containerregistry.v1.scanner_pb2
import yandex.cloud.containerregistry.v1.scanner_service_pb2
import yandex.cloud.operation.operation_pb2

class ScannerServiceStub:
    """A set of methods for scanning Docker images."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Scan: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scanner_service_pb2.ScanRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Executes scanning of specified image."""

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scanner_service_pb2.GetScanResultRequest,
        yandex.cloud.containerregistry.v1.scanner_pb2.ScanResult]
    """Returns the specified ScanResult resource.

    To get the list of ScanResults for specified Image, make a [List] request.
    """

    GetLast: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scanner_service_pb2.GetLastScanResultRequest,
        yandex.cloud.containerregistry.v1.scanner_pb2.ScanResult]
    """Returns the last finished ScanResult for the specified Image."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scanner_service_pb2.ListScanResultsRequest,
        yandex.cloud.containerregistry.v1.scanner_service_pb2.ListScanResultsResponse]
    """Retrieves the list of ScanResults for specified Image."""

    ListVulnerabilities: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scanner_service_pb2.ListVulnerabilitiesRequest,
        yandex.cloud.containerregistry.v1.scanner_service_pb2.ListVulnerabilitiesResponse]
    """Retrieves the list of vulnerabilities found in particular scan."""


class ScannerServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for scanning Docker images."""
    @abc.abstractmethod
    def Scan(self,
        request: yandex.cloud.containerregistry.v1.scanner_service_pb2.ScanRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Executes scanning of specified image."""
        pass

    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.containerregistry.v1.scanner_service_pb2.GetScanResultRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.scanner_pb2.ScanResult:
        """Returns the specified ScanResult resource.

        To get the list of ScanResults for specified Image, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def GetLast(self,
        request: yandex.cloud.containerregistry.v1.scanner_service_pb2.GetLastScanResultRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.scanner_pb2.ScanResult:
        """Returns the last finished ScanResult for the specified Image."""
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.containerregistry.v1.scanner_service_pb2.ListScanResultsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.scanner_service_pb2.ListScanResultsResponse:
        """Retrieves the list of ScanResults for specified Image."""
        pass

    @abc.abstractmethod
    def ListVulnerabilities(self,
        request: yandex.cloud.containerregistry.v1.scanner_service_pb2.ListVulnerabilitiesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.containerregistry.v1.scanner_service_pb2.ListVulnerabilitiesResponse:
        """Retrieves the list of vulnerabilities found in particular scan."""
        pass


def add_ScannerServiceServicer_to_server(servicer: ScannerServiceServicer, server: grpc.Server) -> None: ...