"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.loadbalancer.v1.network_load_balancer_pb2
import yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2
import yandex.cloud.operation.operation_pb2

class NetworkLoadBalancerServiceStub:
    """A set of methods for managing NetworkLoadBalancer resources."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.GetNetworkLoadBalancerRequest,
        yandex.cloud.loadbalancer.v1.network_load_balancer_pb2.NetworkLoadBalancer,
    ]
    """Returns the specified NetworkLoadBalancer resource.

    Get the list of available NetworkLoadBalancer resources by making a [List] request.
    """
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.ListNetworkLoadBalancersRequest,
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.ListNetworkLoadBalancersResponse,
    ]
    """Retrieves the list of NetworkLoadBalancer resources in the specified folder."""
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.CreateNetworkLoadBalancerRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a network load balancer in the specified folder using the data specified in the request."""
    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.UpdateNetworkLoadBalancerRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified network load balancer."""
    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.DeleteNetworkLoadBalancerRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified network load balancer."""
    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.StartNetworkLoadBalancerRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts load balancing and health checking with the specified network load balancer with specified settings.
    Changes network load balancer status to `` ACTIVE ``.
    """
    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.StopNetworkLoadBalancerRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops load balancing and health checking with the specified network load balancer.
    Changes load balancer status to `` STOPPED ``.
    """
    AttachTargetGroup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.AttachNetworkLoadBalancerTargetGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Attaches a target group to the specified network load balancer."""
    DetachTargetGroup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.DetachNetworkLoadBalancerTargetGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Detaches the target group from the specified network load balancer."""
    GetTargetStates: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.GetTargetStatesRequest,
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.GetTargetStatesResponse,
    ]
    """Gets states of target resources in the attached target group."""
    AddListener: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.AddNetworkLoadBalancerListenerRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds a listener to the specified network load balancer."""
    RemoveListener: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.RemoveNetworkLoadBalancerListenerRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes the listener from the specified network load balancer."""
    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.ListNetworkLoadBalancerOperationsRequest,
        yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.ListNetworkLoadBalancerOperationsResponse,
    ]
    """Lists operations for the specified network load balancer."""

class NetworkLoadBalancerServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing NetworkLoadBalancer resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.GetNetworkLoadBalancerRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.loadbalancer.v1.network_load_balancer_pb2.NetworkLoadBalancer:
        """Returns the specified NetworkLoadBalancer resource.

        Get the list of available NetworkLoadBalancer resources by making a [List] request.
        """
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.ListNetworkLoadBalancersRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.ListNetworkLoadBalancersResponse:
        """Retrieves the list of NetworkLoadBalancer resources in the specified folder."""
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.CreateNetworkLoadBalancerRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a network load balancer in the specified folder using the data specified in the request."""
    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.UpdateNetworkLoadBalancerRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified network load balancer."""
    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.DeleteNetworkLoadBalancerRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified network load balancer."""
    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.StartNetworkLoadBalancerRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Starts load balancing and health checking with the specified network load balancer with specified settings.
        Changes network load balancer status to `` ACTIVE ``.
        """
    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.StopNetworkLoadBalancerRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Stops load balancing and health checking with the specified network load balancer.
        Changes load balancer status to `` STOPPED ``.
        """
    @abc.abstractmethod
    def AttachTargetGroup(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.AttachNetworkLoadBalancerTargetGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Attaches a target group to the specified network load balancer."""
    @abc.abstractmethod
    def DetachTargetGroup(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.DetachNetworkLoadBalancerTargetGroupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Detaches the target group from the specified network load balancer."""
    @abc.abstractmethod
    def GetTargetStates(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.GetTargetStatesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.GetTargetStatesResponse:
        """Gets states of target resources in the attached target group."""
    @abc.abstractmethod
    def AddListener(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.AddNetworkLoadBalancerListenerRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Adds a listener to the specified network load balancer."""
    @abc.abstractmethod
    def RemoveListener(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.RemoveNetworkLoadBalancerListenerRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Removes the listener from the specified network load balancer."""
    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.ListNetworkLoadBalancerOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2.ListNetworkLoadBalancerOperationsResponse:
        """Lists operations for the specified network load balancer."""

def add_NetworkLoadBalancerServiceServicer_to_server(servicer: NetworkLoadBalancerServiceServicer, server: grpc.Server) -> None: ...
