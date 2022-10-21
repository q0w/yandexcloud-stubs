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
import yandex.cloud.marketplace.v1.metering.usage_record_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class WriteImageProductUsageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    PRODUCT_ID_FIELD_NUMBER: builtins.int
    USAGE_RECORDS_FIELD_NUMBER: builtins.int
    validate_only: builtins.bool
    """Checks whether you have the access required for the emit usage."""
    product_id: builtins.str
    """Marketplace Product's ID."""
    @property
    def usage_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.marketplace.v1.metering.usage_record_pb2.UsageRecord]:
        """List of product usage records (up to 25 per request)."""
    def __init__(
        self,
        *,
        validate_only: builtins.bool = ...,
        product_id: builtins.str = ...,
        usage_records: collections.abc.Iterable[yandex.cloud.marketplace.v1.metering.usage_record_pb2.UsageRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["product_id", b"product_id", "usage_records", b"usage_records", "validate_only", b"validate_only"]) -> None: ...

global___WriteImageProductUsageRequest = WriteImageProductUsageRequest

@typing_extensions.final
class WriteImageProductUsageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCEPTED_FIELD_NUMBER: builtins.int
    REJECTED_FIELD_NUMBER: builtins.int
    @property
    def accepted(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.marketplace.v1.metering.usage_record_pb2.AcceptedUsageRecord]:
        """List of accepted product usage records."""
    @property
    def rejected(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.marketplace.v1.metering.usage_record_pb2.RejectedUsageRecord]:
        """List of rejected product usage records (with reason)."""
    def __init__(
        self,
        *,
        accepted: collections.abc.Iterable[yandex.cloud.marketplace.v1.metering.usage_record_pb2.AcceptedUsageRecord] | None = ...,
        rejected: collections.abc.Iterable[yandex.cloud.marketplace.v1.metering.usage_record_pb2.RejectedUsageRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accepted", b"accepted", "rejected", b"rejected"]) -> None: ...

global___WriteImageProductUsageResponse = WriteImageProductUsageResponse
