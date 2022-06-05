"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.compute.v1.image_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: typing.Text
    """ID of the Image resource to return.
    To get the image ID, use a [ImageService.List] request.
    """

    def __init__(self,
        *,
        image_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_id",b"image_id"]) -> None: ...
global___GetImageRequest = GetImageRequest

class GetImageLatestByFamilyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    FAMILY_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to get the image from.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    family: typing.Text
    """Name of the image family to search for."""

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        family: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["family",b"family","folder_id",b"folder_id"]) -> None: ...
global___GetImageLatestByFamilyRequest = GetImageLatestByFamilyRequest

class ListImagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to list images in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListImagesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListImagesResponse.next_page_token] returned by a previous list request.
    """

    filter: typing.Text
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [Image.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z]([-a-z0-9]{,61}[a-z0-9])?`.
    """

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListImagesRequest = ListImagesRequest

class ListImagesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def images(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.image_pb2.Image]:
        """List of images."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListSnapshotsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListSnapshotsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        images: typing.Optional[typing.Iterable[yandex.cloud.compute.v1.image_pb2.Image]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["images",b"images","next_page_token",b"next_page_token"]) -> None: ...
global___ListImagesResponse = ListImagesResponse

class CreateImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    FAMILY_FIELD_NUMBER: builtins.int
    MIN_DISK_SIZE_FIELD_NUMBER: builtins.int
    PRODUCT_IDS_FIELD_NUMBER: builtins.int
    IMAGE_ID_FIELD_NUMBER: builtins.int
    DISK_ID_FIELD_NUMBER: builtins.int
    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    OS_FIELD_NUMBER: builtins.int
    POOLED_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    """ID of the folder to create an image in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """

    name: typing.Text
    """Name of the image."""

    description: typing.Text
    """Description of the image."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs."""
        pass
    family: typing.Text
    """The name of the image family to which this image belongs. For more information, see [Image family](/docs/compute/concepts/image#family).

    To get an information about the most recent image from a family, use a [ImageService.GetLatestByFamily] request.
    """

    min_disk_size: builtins.int
    """Minimum size of the disk that will be created from this image.
    Specified in bytes. Should be more than the volume of source data.
    optional, should be > source data
    """

    @property
    def product_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """License IDs that indicate which licenses are attached to this resource.
        License IDs are used to calculate additional charges for the use of the virtual machine.

        The correct license ID is generated by Yandex Cloud. IDs are inherited by new resources created from this resource.

        If you know the license IDs, specify them when you create the image.
        For example, if you create a disk image using a third-party utility and load it into Yandex Object Storage, the license IDs will be lost.
        You can specify them in this request.
        """
        pass
    image_id: typing.Text
    """ID of the source image to create the new image from."""

    disk_id: typing.Text
    """ID of the disk to create the image from."""

    snapshot_id: typing.Text
    """ID of the snapshot to create the image from."""

    uri: typing.Text
    """URI of the source image to create the new image from.
    Currently only supports links to images that are stored in Yandex Object Storage.
    Currently only supports Qcow2, VMDK, and VHD formats.
    """

    @property
    def os(self) -> yandex.cloud.compute.v1.image_pb2.Os:
        """Operating system that is contained in the image.

        If not specified and you used the `image_id` or `disk_id` field to set the source, then the value can be inherited from the source resource.
        """
        pass
    pooled: builtins.bool
    """When true, an image pool will be created for fast creation disks from the image."""

    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        family: typing.Text = ...,
        min_disk_size: builtins.int = ...,
        product_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        image_id: typing.Text = ...,
        disk_id: typing.Text = ...,
        snapshot_id: typing.Text = ...,
        uri: typing.Text = ...,
        os: typing.Optional[yandex.cloud.compute.v1.image_pb2.Os] = ...,
        pooled: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disk_id",b"disk_id","image_id",b"image_id","os",b"os","snapshot_id",b"snapshot_id","source",b"source","uri",b"uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","disk_id",b"disk_id","family",b"family","folder_id",b"folder_id","image_id",b"image_id","labels",b"labels","min_disk_size",b"min_disk_size","name",b"name","os",b"os","pooled",b"pooled","product_ids",b"product_ids","snapshot_id",b"snapshot_id","source",b"source","uri",b"uri"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["source",b"source"]) -> typing.Optional[typing_extensions.Literal["image_id","disk_id","snapshot_id","uri"]]: ...
global___CreateImageRequest = CreateImageRequest

class CreateImageMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: typing.Text
    """ID of the image that is being created."""

    def __init__(self,
        *,
        image_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_id",b"image_id"]) -> None: ...
global___CreateImageMetadata = CreateImageMetadata

class UpdateImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    IMAGE_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    MIN_DISK_SIZE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    image_id: typing.Text
    """ID of the Image resource to update.
    To get the image ID, use a [ImageService.List] request.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Image resource are going to be updated."""
        pass
    name: typing.Text
    """Name of the image."""

    description: typing.Text
    """Description of the image."""

    min_disk_size: builtins.int
    """Minimum size of the disk that can be created from this image.
    Specified in bytes. Should be more than the volume of source data and more than the virtual disk size.
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """
        pass
    def __init__(self,
        *,
        image_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        min_disk_size: builtins.int = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","image_id",b"image_id","labels",b"labels","min_disk_size",b"min_disk_size","name",b"name","update_mask",b"update_mask"]) -> None: ...
global___UpdateImageRequest = UpdateImageRequest

class UpdateImageMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: typing.Text
    """ID of the Image resource that is being updated."""

    def __init__(self,
        *,
        image_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_id",b"image_id"]) -> None: ...
global___UpdateImageMetadata = UpdateImageMetadata

class DeleteImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: typing.Text
    """ID of the image to delete.
    To get the image ID, use a [ImageService.List] request.
    """

    def __init__(self,
        *,
        image_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_id",b"image_id"]) -> None: ...
global___DeleteImageRequest = DeleteImageRequest

class DeleteImageMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: typing.Text
    """ID of the image that is being deleted."""

    def __init__(self,
        *,
        image_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_id",b"image_id"]) -> None: ...
global___DeleteImageMetadata = DeleteImageMetadata

class ListImageOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGE_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    image_id: typing.Text
    """ID of the Image resource to list operations for."""

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListImageOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, set [page_token] to the
    [ListImageOperationsResponse.next_page_token] returned by a previous list request.
    """

    def __init__(self,
        *,
        image_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_id",b"image_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListImageOperationsRequest = ListImageOperationsRequest

class ListImageOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified image."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListImageOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListImageOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListImageOperationsResponse = ListImageOperationsResponse
