"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.iam.v1.role_pb2
import yandex.cloud.iam.v1.role_service_pb2

class RoleServiceStub:
    """A set of methods for managing Role resources."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.role_service_pb2.GetRoleRequest,
        yandex.cloud.iam.v1.role_pb2.Role]
    """Returns the specified Role resource.

    To get the list of available Role resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.role_service_pb2.ListRolesRequest,
        yandex.cloud.iam.v1.role_service_pb2.ListRolesResponse]
    """Retrieves the list of Role resources."""


class RoleServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Role resources."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.iam.v1.role_service_pb2.GetRoleRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iam.v1.role_pb2.Role:
        """Returns the specified Role resource.

        To get the list of available Role resources, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.iam.v1.role_service_pb2.ListRolesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iam.v1.role_service_pb2.ListRolesResponse:
        """Retrieves the list of Role resources."""
        pass


def add_RoleServiceServicer_to_server(servicer: RoleServiceServicer, server: grpc.Server) -> None: ...
