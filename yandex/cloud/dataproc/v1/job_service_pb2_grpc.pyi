"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.dataproc.v1.job_pb2
import yandex.cloud.dataproc.v1.job_service_pb2
import yandex.cloud.operation.operation_pb2

class JobServiceStub:
    """A set of methods for managing Data Proc jobs."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.job_service_pb2.ListJobsRequest,
        yandex.cloud.dataproc.v1.job_service_pb2.ListJobsResponse,
    ]
    """Retrieves a list of jobs for a cluster."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.job_service_pb2.CreateJobRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a job for a cluster."""
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.job_service_pb2.GetJobRequest,
        yandex.cloud.dataproc.v1.job_pb2.Job,
    ]
    """Returns the specified job."""
    ListLog: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.job_service_pb2.ListJobLogRequest,
        yandex.cloud.dataproc.v1.job_service_pb2.ListJobLogResponse,
    ]
    """Returns a log for specified job."""
    Cancel: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dataproc.v1.job_service_pb2.CancelJobRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Cancels the specified Dataproc job."""

class JobServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Data Proc jobs."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.dataproc.v1.job_service_pb2.ListJobsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.job_service_pb2.ListJobsResponse:
        """Retrieves a list of jobs for a cluster."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.dataproc.v1.job_service_pb2.CreateJobRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a job for a cluster."""
    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.dataproc.v1.job_service_pb2.GetJobRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.job_pb2.Job:
        """Returns the specified job."""
    @abc.abstractmethod
    def ListLog(
        self,
        request: yandex.cloud.dataproc.v1.job_service_pb2.ListJobLogRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dataproc.v1.job_service_pb2.ListJobLogResponse:
        """Returns a log for specified job."""
    @abc.abstractmethod
    def Cancel(
        self,
        request: yandex.cloud.dataproc.v1.job_service_pb2.CancelJobRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Cancels the specified Dataproc job."""

def add_JobServiceServicer_to_server(servicer: JobServiceServicer, server: grpc.Server) -> None: ...
