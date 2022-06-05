"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.access.access_pb2
import yandex.cloud.dns.v1.dns_zone_pb2
import yandex.cloud.dns.v1.dns_zone_service_pb2
import yandex.cloud.operation.operation_pb2

class DnsZoneServiceStub:
    """A set of methods for managing DNS zones."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.GetDnsZoneRequest,
        yandex.cloud.dns.v1.dns_zone_pb2.DnsZone]
    """Returns the specified DNS zone.

    To get the list of all available DNS zones, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZonesRequest,
        yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZonesResponse]
    """Retrieves the list of DNS zones in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.CreateDnsZoneRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Creates a DNS zone in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.UpdateDnsZoneRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates the specified DNS zone."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.DeleteDnsZoneRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Deletes the specified DNS zone."""

    GetRecordSet: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.GetDnsZoneRecordSetRequest,
        yandex.cloud.dns.v1.dns_zone_pb2.RecordSet]
    """Returns the specified record set."""

    ListRecordSets: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZoneRecordSetsRequest,
        yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZoneRecordSetsResponse]
    """Retrieves the list of record sets in the specified folder."""

    UpdateRecordSets: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.UpdateRecordSetsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Method with strict control for changing zone state. Returns error when:
    1. Deleted record is not found.
    2. Found record with matched type and name but different TTL or value.
    3. Attempted to add record with existing name and type.
    Deletions happen first. If a record with the same name and type exists in both lists,
    then the existing record will be deleted, and a new one added.
    """

    UpsertRecordSets: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.UpsertRecordSetsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Method without strict control for changing zone state. Nothing happens if deleted record doesn't exist.
    Deletes records that match all specified fields which allows to delete only specified records from a record set.
    """

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZoneOperationsRequest,
        yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZoneOperationsResponse]
    """Lists operations for the specified DNS zone."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse]
    """Lists existing access bindings for the specified DNS zone."""

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Sets access bindings for the specified DNS zone."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation]
    """Updates access bindings for the specified DNS zone."""


class DnsZoneServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing DNS zones."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.GetDnsZoneRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dns.v1.dns_zone_pb2.DnsZone:
        """Returns the specified DNS zone.

        To get the list of all available DNS zones, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZonesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZonesResponse:
        """Retrieves the list of DNS zones in the specified folder."""
        pass

    @abc.abstractmethod
    def Create(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.CreateDnsZoneRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Creates a DNS zone in the specified folder."""
        pass

    @abc.abstractmethod
    def Update(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.UpdateDnsZoneRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates the specified DNS zone."""
        pass

    @abc.abstractmethod
    def Delete(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.DeleteDnsZoneRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Deletes the specified DNS zone."""
        pass

    @abc.abstractmethod
    def GetRecordSet(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.GetDnsZoneRecordSetRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dns.v1.dns_zone_pb2.RecordSet:
        """Returns the specified record set."""
        pass

    @abc.abstractmethod
    def ListRecordSets(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZoneRecordSetsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZoneRecordSetsResponse:
        """Retrieves the list of record sets in the specified folder."""
        pass

    @abc.abstractmethod
    def UpdateRecordSets(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.UpdateRecordSetsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Method with strict control for changing zone state. Returns error when:
        1. Deleted record is not found.
        2. Found record with matched type and name but different TTL or value.
        3. Attempted to add record with existing name and type.
        Deletions happen first. If a record with the same name and type exists in both lists,
        then the existing record will be deleted, and a new one added.
        """
        pass

    @abc.abstractmethod
    def UpsertRecordSets(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.UpsertRecordSetsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Method without strict control for changing zone state. Nothing happens if deleted record doesn't exist.
        Deletes records that match all specified fields which allows to delete only specified records from a record set.
        """
        pass

    @abc.abstractmethod
    def ListOperations(self,
        request: yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZoneOperationsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.dns.v1.dns_zone_service_pb2.ListDnsZoneOperationsResponse:
        """Lists operations for the specified DNS zone."""
        pass

    @abc.abstractmethod
    def ListAccessBindings(self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.access.access_pb2.ListAccessBindingsResponse:
        """Lists existing access bindings for the specified DNS zone."""
        pass

    @abc.abstractmethod
    def SetAccessBindings(self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Sets access bindings for the specified DNS zone."""
        pass

    @abc.abstractmethod
    def UpdateAccessBindings(self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.operation.operation_pb2.Operation:
        """Updates access bindings for the specified DNS zone."""
        pass


def add_DnsZoneServiceServicer_to_server(servicer: DnsZoneServiceServicer, server: grpc.Server) -> None: ...
