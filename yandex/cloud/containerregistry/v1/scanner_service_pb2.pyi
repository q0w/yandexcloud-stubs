"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import yandex.cloud.containerregistry.v1.scanner_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ScanRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the Image to be scanned for vulnerabilities."""
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_id", b"image_id"]) -> None: ...

global___ScanRequest = ScanRequest

@typing_extensions.final
class ScanMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_RESULT_ID_FIELD_NUMBER: builtins.int
    scan_result_id: builtins.str
    """ID of the ScanResult that is being created."""
    def __init__(
        self,
        *,
        scan_result_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["scan_result_id", b"scan_result_id"]) -> None: ...

global___ScanMetadata = ScanMetadata

@typing_extensions.final
class GetScanResultRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_RESULT_ID_FIELD_NUMBER: builtins.int
    scan_result_id: builtins.str
    """ID of the ScanResult to return."""
    def __init__(
        self,
        *,
        scan_result_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["scan_result_id", b"scan_result_id"]) -> None: ...

global___GetScanResultRequest = GetScanResultRequest

@typing_extensions.final
class GetLastScanResultRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the Image to get last finished ScanResult."""
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_id", b"image_id"]) -> None: ...

global___GetLastScanResultRequest = GetLastScanResultRequest

@typing_extensions.final
class ListScanResultsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    REPOSITORY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    repository_id: builtins.str
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListRegistriesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListRegistriesResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [ScanResult.status] field.
    2. An `=` operator.
    3. The value in double quotes (`"`).
    """
    order_by: builtins.str
    """An order expression that orders resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [ScanResult.status] field.
    2. Order selector. Currently you can use ordering only on `ScanResult.status` field (critical first).
    """
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
        repository_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
        order_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id", "image_id", b"image_id", "repository_id", b"repository_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "id", b"id", "image_id", b"image_id", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token", "repository_id", b"repository_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["id", b"id"]) -> typing_extensions.Literal["image_id", "repository_id"] | None: ...

global___ListScanResultsRequest = ListScanResultsRequest

@typing_extensions.final
class ListScanResultsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_RESULTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def scan_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.scanner_pb2.ScanResult]:
        """List of ScanResult resources."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListImagesRequest.page_size], use
    the [next_page_token] as the value
    for the [ListImagesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        scan_results: collections.abc.Iterable[yandex.cloud.containerregistry.v1.scanner_pb2.ScanResult] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "scan_results", b"scan_results"]) -> None: ...

global___ListScanResultsResponse = ListScanResultsResponse

@typing_extensions.final
class ListVulnerabilitiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_RESULT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    scan_result_id: builtins.str
    """ID of the ScanResult to get list of vulnerabilities for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListRegistriesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListRegistriesResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [Vulnerability.severity] and [PackageVulnerability.name] fields.
    2. An `=` operator.
    3. The value in double quotes (`"`).
    """
    order_by: builtins.str
    """An order expression that orders resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [Vulnerability.severity] and [PackageVulnerability.name] fields.
    2. Order selector. Currently you can use ordering only on `Vulnerability.severity` field (recent first).
    """
    def __init__(
        self,
        *,
        scan_result_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
        order_by: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token", "scan_result_id", b"scan_result_id"]) -> None: ...

global___ListVulnerabilitiesRequest = ListVulnerabilitiesRequest

@typing_extensions.final
class ListVulnerabilitiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VULNERABILITIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def vulnerabilities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.scanner_pb2.Vulnerability]:
        """List of Vulnerability resources."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListImagesRequest.page_size], use
    the [next_page_token] as the value
    for the [ListImagesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    def __init__(
        self,
        *,
        vulnerabilities: collections.abc.Iterable[yandex.cloud.containerregistry.v1.scanner_pb2.Vulnerability] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "vulnerabilities", b"vulnerabilities"]) -> None: ...

global___ListVulnerabilitiesResponse = ListVulnerabilitiesResponse
