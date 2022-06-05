"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.ai.vision.v2.image_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Label(google.protobuf.message.Message):
    """Description of single label"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    name: typing.Text
    """   Label name"""

    description: typing.Text
    """   human readable description of label"""

    def __init__(self,
        *,
        name: typing.Text = ...,
        description: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","name",b"name"]) -> None: ...
global___Label = Label

class ClassAnnotation(google.protobuf.message.Message):
    """Image annotation for specific label"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LABEL_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    @property
    def label(self) -> global___Label:
        """   list of annotated labels"""
        pass
    confidence: builtins.float
    """   confidence for each label"""

    def __init__(self,
        *,
        label: typing.Optional[global___Label] = ...,
        confidence: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["label",b"label"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["confidence",b"confidence","label",b"label"]) -> None: ...
global___ClassAnnotation = ClassAnnotation

class ClassifierSpecification(google.protobuf.message.Message):
    """Specification of model used for annotation"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _ClassificationType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ClassificationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ClassifierSpecification._ClassificationType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CLASSIFICATION_TYPE_UNSPECIFIED: ClassifierSpecification._ClassificationType.ValueType  # 0
        MULTI_LABEL: ClassifierSpecification._ClassificationType.ValueType  # 1
        MULTI_CLASS: ClassifierSpecification._ClassificationType.ValueType  # 2
    class ClassificationType(_ClassificationType, metaclass=_ClassificationTypeEnumTypeWrapper):
        pass

    CLASSIFICATION_TYPE_UNSPECIFIED: ClassifierSpecification.ClassificationType.ValueType  # 0
    MULTI_LABEL: ClassifierSpecification.ClassificationType.ValueType  # 1
    MULTI_CLASS: ClassifierSpecification.ClassificationType.ValueType  # 2

    LABELS_FIELD_NUMBER: builtins.int
    CLASSIFICATION_TYPE_FIELD_NUMBER: builtins.int
    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Label]:
        """ List of labels, annotated by service"""
        pass
    classification_type: global___ClassifierSpecification.ClassificationType.ValueType
    """   type of annotation: exclusive (multi-class) or non-exclusive (multi-label)"""

    def __init__(self,
        *,
        labels: typing.Optional[typing.Iterable[global___Label]] = ...,
        classification_type: global___ClassifierSpecification.ClassificationType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["classification_type",b"classification_type","labels",b"labels"]) -> None: ...
global___ClassifierSpecification = ClassifierSpecification

class AnnotationResponse(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REQUEST_ID_FIELD_NUMBER: builtins.int
    CLASSIFIER_SPECIFICATION_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    request_id: typing.Text
    """ internal service requestId"""

    @property
    def classifier_specification(self) -> global___ClassifierSpecification:
        """ class specification"""
        pass
    @property
    def annotations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClassAnnotation]:
        """   annotations for each class"""
        pass
    def __init__(self,
        *,
        request_id: typing.Text = ...,
        classifier_specification: typing.Optional[global___ClassifierSpecification] = ...,
        annotations: typing.Optional[typing.Iterable[global___ClassAnnotation]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["classifier_specification",b"classifier_specification"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotations",b"annotations","classifier_specification",b"classifier_specification","request_id",b"request_id"]) -> None: ...
global___AnnotationResponse = AnnotationResponse

class AnnotationRequest(google.protobuf.message.Message):
    """request for annotation"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGE_FIELD_NUMBER: builtins.int
    @property
    def image(self) -> yandex.cloud.ai.vision.v2.image_pb2.Image:
        """   image to annotate"""
        pass
    def __init__(self,
        *,
        image: typing.Optional[yandex.cloud.ai.vision.v2.image_pb2.Image] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["image",b"image"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["image",b"image"]) -> None: ...
global___AnnotationRequest = AnnotationRequest
