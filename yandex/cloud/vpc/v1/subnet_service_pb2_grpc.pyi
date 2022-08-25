"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.operation.operation_pb2
import yandex.cloud.vpc.v1.subnet_pb2
import yandex.cloud.vpc.v1.subnet_service_pb2

class SubnetServiceStub:
    """A set of methods for managing Subnet resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.GetSubnetRequest,
        yandex.cloud.vpc.v1.subnet_pb2.Subnet,
    ]
    """Returns the specified Subnet resource.

    To get the list of available Subnet resources, make a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.ListSubnetsRequest,
        yandex.cloud.vpc.v1.subnet_service_pb2.ListSubnetsResponse,
    ]
    """Retrieves the list of Subnet resources in the specified folder."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.CreateSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a subnet in the specified folder and network.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.UpdateSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified subnet.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    AddCidrBlocks: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.AddSubnetCidrBlocksRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds CIDR blocks to the specified subnet.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    RemoveCidrBlocks: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.RemoveSubnetCidrBlocksRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes CIDR blocks from the specified subnet.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.DeleteSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified subnet."""
    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.ListSubnetOperationsRequest,
        yandex.cloud.vpc.v1.subnet_service_pb2.ListSubnetOperationsResponse,
    ]
    """List operations for the specified subnet."""
    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.MoveSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Move subnet to another folder."""
    ListUsedAddresses: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.vpc.v1.subnet_service_pb2.ListUsedAddressesRequest,
        yandex.cloud.vpc.v1.subnet_service_pb2.ListUsedAddressesResponse,
    ]
    """List used addresses in specified subnet."""

class SubnetServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Subnet resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.GetSubnetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.subnet_pb2.Subnet:
        """Returns the specified Subnet resource.

        To get the list of available Subnet resources, make a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.ListSubnetsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.subnet_service_pb2.ListSubnetsResponse:
        """Retrieves the list of Subnet resources in the specified folder."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.CreateSubnetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a subnet in the specified folder and network.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.UpdateSubnetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified subnet.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
    @abc.abstractmethod
    def AddCidrBlocks(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.AddSubnetCidrBlocksRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Adds CIDR blocks to the specified subnet.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
    @abc.abstractmethod
    def RemoveCidrBlocks(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.RemoveSubnetCidrBlocksRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Removes CIDR blocks from the specified subnet.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.DeleteSubnetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified subnet."""
    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.ListSubnetOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.subnet_service_pb2.ListSubnetOperationsResponse:
        """List operations for the specified subnet."""
    @abc.abstractmethod
    def Move(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.MoveSubnetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Move subnet to another folder."""
    @abc.abstractmethod
    def ListUsedAddresses(
        self,
        request: yandex.cloud.vpc.v1.subnet_service_pb2.ListUsedAddressesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.vpc.v1.subnet_service_pb2.ListUsedAddressesResponse:
        """List used addresses in specified subnet."""

def add_SubnetServiceServicer_to_server(servicer: SubnetServiceServicer, server: grpc.Server) -> None: ...
