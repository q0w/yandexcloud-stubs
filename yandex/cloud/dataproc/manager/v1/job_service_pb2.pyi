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
import yandex.cloud.dataproc.manager.v1.job_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ListJobsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the cluster to list Data Proc jobs of."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a `next_page_token` that can be used
    to get the next page of results in subsequent ListJobs requests.
    Acceptable values are 0 to 1000, inclusive. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set `page_token` to the `next_page_token` returned by a previous ListJobs
    request to get the next page of results.
    """
    filter: builtins.str
    """String that describes a display filter."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id", b"cluster_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListJobsRequest = ListJobsRequest

@typing_extensions.final
class ListJobsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOBS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.dataproc.manager.v1.job_pb2.Job]:
        """Requested list of Data Proc jobs."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for ListJobs requests,
    if the number of results is larger than `page_size` specified in the request.
    To get the next page, specify the value of `next_page_token` as a value for
    the `page_token` parameter in the next ListClusters request. Subsequent ListClusters
    requests will have their own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        jobs: collections.abc.Iterable[yandex.cloud.dataproc.manager.v1.job_pb2.Job] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["jobs", b"jobs", "next_page_token", b"next_page_token"]) -> None: ...

global___ListJobsResponse = ListJobsResponse

@typing_extensions.final
class UpdateJobStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    APPLICATION_INFO_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the Data Proc cluster."""
    job_id: builtins.str
    """Required. ID of the Data Proc job to update."""
    status: yandex.cloud.dataproc.manager.v1.job_pb2.Job.Status.ValueType
    """Required. New status of the job."""
    @property
    def application_info(self) -> yandex.cloud.dataproc.manager.v1.job_pb2.ApplicationInfo:
        """Attributes of YARN application."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        job_id: builtins.str = ...,
        status: yandex.cloud.dataproc.manager.v1.job_pb2.Job.Status.ValueType = ...,
        application_info: yandex.cloud.dataproc.manager.v1.job_pb2.ApplicationInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["application_info", b"application_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_info", b"application_info", "cluster_id", b"cluster_id", "job_id", b"job_id", "status", b"status"]) -> None: ...

global___UpdateJobStatusRequest = UpdateJobStatusRequest

@typing_extensions.final
class UpdateJobStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UpdateJobStatusResponse = UpdateJobStatusResponse
