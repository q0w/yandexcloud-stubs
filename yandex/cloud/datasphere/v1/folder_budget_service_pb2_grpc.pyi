"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.protobuf.empty_pb2
import grpc
import yandex.cloud.datasphere.v1.folder_budget_service_pb2

class FolderBudgetServiceStub:
    """A set of methods for managing Datasphere folder budgets."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetRequest,
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetResponse]
    """Returns the specified folder budget."""

    Set: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.SetFolderBudgetRequest,
        google.protobuf.empty_pb2.Empty]
    """Sets the unit balance and the limits of the specified folder budget."""


class FolderBudgetServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Datasphere folder budgets."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetResponse:
        """Returns the specified folder budget."""
        pass

    @abc.abstractmethod
    def Set(self,
        request: yandex.cloud.datasphere.v1.folder_budget_service_pb2.SetFolderBudgetRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty:
        """Sets the unit balance and the limits of the specified folder budget."""
        pass


def add_FolderBudgetServiceServicer_to_server(servicer: FolderBudgetServiceServicer, server: grpc.Server) -> None: ...
