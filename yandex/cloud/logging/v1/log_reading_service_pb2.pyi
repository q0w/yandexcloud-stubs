"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions
import yandex.cloud.logging.v1.log_entry_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ReadRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    CRITERIA_FIELD_NUMBER: builtins.int
    page_token: typing.Text
    """Page token. To get the next page of results, set `page_token` to the
    [ReadResponse.next_page_token] or [ReadResponse.previous_page_token] returned by a previous read request.
    """

    @property
    def criteria(self) -> global___Criteria:
        """Read criteria.

        See [Criteria] for details.
        """
        pass
    def __init__(self,
        *,
        page_token: typing.Text = ...,
        criteria: typing.Optional[global___Criteria] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["criteria",b"criteria","page_token",b"page_token","selector",b"selector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["criteria",b"criteria","page_token",b"page_token","selector",b"selector"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["selector",b"selector"]) -> typing.Optional[typing_extensions.Literal["page_token","criteria"]]: ...
global___ReadRequest = ReadRequest

class ReadResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    ENTRIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PREVIOUS_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """Log group ID the read was performed from."""

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.logging.v1.log_entry_pb2.LogEntry]:
        """List of matching log entries."""
        pass
    next_page_token: typing.Text
    """Token for getting the next page of the log entries.

    After getting log entries initially with [Criteria], you can use `next_page_token` as the value
    for the [ReadRequest.page_token] parameter in the next read request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    previous_page_token: typing.Text
    """Token for getting the previous page of the log entries.

    After getting log entries initially with [Criteria], you can use `previous_page_token` as the value
    for the [ReadRequest.page_token] parameter in the next read request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        entries: typing.Optional[typing.Iterable[yandex.cloud.logging.v1.log_entry_pb2.LogEntry]] = ...,
        next_page_token: typing.Text = ...,
        previous_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entries",b"entries","log_group_id",b"log_group_id","next_page_token",b"next_page_token","previous_page_token",b"previous_page_token"]) -> None: ...
global___ReadResponse = ReadResponse

class Criteria(google.protobuf.message.Message):
    """Read criteria. Should be used in initial [ReadRequest]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    RESOURCE_TYPES_FIELD_NUMBER: builtins.int
    RESOURCE_IDS_FIELD_NUMBER: builtins.int
    SINCE_FIELD_NUMBER: builtins.int
    UNTIL_FIELD_NUMBER: builtins.int
    LEVELS_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    STREAM_NAMES_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    MAX_RESPONSE_SIZE_FIELD_NUMBER: builtins.int
    log_group_id: typing.Text
    """ID of the log group to return.

    To get a log group ID make a [LogGroupService.List] request.
    """

    @property
    def resource_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List of resource types to limit log entries to.

        Empty list disables filter.
        """
        pass
    @property
    def resource_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List of resource IDs to limit log entries to.

        Empty list disables filter.
        """
        pass
    @property
    def since(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Lower bound of log entries timestamps."""
        pass
    @property
    def until(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Upper bound of log entries timestamps."""
        pass
    @property
    def levels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[yandex.cloud.logging.v1.log_entry_pb2.LogLevel.Level.ValueType]:
        """List of log levels to limit log entries to.

        Empty list disables filter.
        """
        pass
    filter: typing.Text
    """Filter expression. For details about filtering, see [documentation](/docs/logging/concepts/filter)."""

    @property
    def stream_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List of stream names to limit log entries to.

        Empty list disables filter.
        """
        pass
    page_size: builtins.int
    """The maximum number of results per page to return."""

    max_response_size: builtins.int
    """Limits response to maximum size in bytes. Prevents gRPC resource exhaustion.

    Default value for max response size is 3.5 MiB
    """

    def __init__(self,
        *,
        log_group_id: typing.Text = ...,
        resource_types: typing.Optional[typing.Iterable[typing.Text]] = ...,
        resource_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        since: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        until: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        levels: typing.Optional[typing.Iterable[yandex.cloud.logging.v1.log_entry_pb2.LogLevel.Level.ValueType]] = ...,
        filter: typing.Text = ...,
        stream_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        page_size: builtins.int = ...,
        max_response_size: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["since",b"since","until",b"until"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","levels",b"levels","log_group_id",b"log_group_id","max_response_size",b"max_response_size","page_size",b"page_size","resource_ids",b"resource_ids","resource_types",b"resource_types","since",b"since","stream_names",b"stream_names","until",b"until"]) -> None: ...
global___Criteria = Criteria
