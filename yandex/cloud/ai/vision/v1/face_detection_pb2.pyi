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
import yandex.cloud.ai.vision.v1.primitives_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FaceAnnotation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FACES_FIELD_NUMBER: builtins.int
    @property
    def faces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Face]:
        """An array of detected faces for the specified image."""
    def __init__(
        self,
        *,
        faces: collections.abc.Iterable[global___Face] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["faces", b"faces"]) -> None: ...

global___FaceAnnotation = FaceAnnotation

@typing_extensions.final
class Face(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    @property
    def bounding_box(self) -> yandex.cloud.ai.vision.v1.primitives_pb2.Polygon:
        """Area on the image where the face is located."""
    def __init__(
        self,
        *,
        bounding_box: yandex.cloud.ai.vision.v1.primitives_pb2.Polygon | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box", b"bounding_box"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_box", b"bounding_box"]) -> None: ...

global___Face = Face
