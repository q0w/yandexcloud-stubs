"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.rpc.status_pb2
import sys
import typing
import yandex.cloud.ai.vision.v1.classification_pb2
import yandex.cloud.ai.vision.v1.face_detection_pb2
import yandex.cloud.ai.vision.v1.image_copy_search_pb2
import yandex.cloud.ai.vision.v1.text_detection_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class BatchAnalyzeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ANALYZE_SPECS_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    @property
    def analyze_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AnalyzeSpec]:
        """A list of specifications. Each specification contains the file to analyze and features to use for analysis.

        Restrictions:
        * Supported file formats: JPEG, PNG.
        * Maximum file size: 1 MB.
        * Image size should not exceed 20M pixels (length x width).
        """
    folder_id: builtins.str
    """ID of the folder to which you have access.
    Required for authorization with a user account (see [yandex.cloud.iam.v1.UserAccount] resource).
    Don't specify this field if you make the request on behalf of a service account.
    """
    def __init__(
        self,
        *,
        analyze_specs: collections.abc.Iterable[global___AnalyzeSpec] | None = ...,
        folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["analyze_specs", b"analyze_specs", "folder_id", b"folder_id"]) -> None: ...

global___BatchAnalyzeRequest = BatchAnalyzeRequest

@typing_extensions.final
class AnalyzeSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    FEATURES_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    content: builtins.bytes
    """Image content, represented as a stream of bytes.
    Note: As with all bytes fields, protobuffers use a pure binary representation, whereas JSON representations use base64.
    """
    signature: builtins.str
    @property
    def features(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Feature]:
        """Requested features to use for analysis.

        Max count of requested features for one file is 8.
        """
    mime_type: builtins.str
    """[MIME type](https://en.wikipedia.org/wiki/Media_type) of content (for example, `` application/pdf ``)."""
    def __init__(
        self,
        *,
        content: builtins.bytes = ...,
        signature: builtins.str = ...,
        features: collections.abc.Iterable[global___Feature] | None = ...,
        mime_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["content", b"content", "signature", b"signature", "source", b"source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["content", b"content", "features", b"features", "mime_type", b"mime_type", "signature", b"signature", "source", b"source"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["source", b"source"]) -> typing_extensions.Literal["content", "signature"] | None: ...

global___AnalyzeSpec = AnalyzeSpec

@typing_extensions.final
class Feature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Feature._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Feature._Type.ValueType  # 0
        TEXT_DETECTION: Feature._Type.ValueType  # 1
        """Text detection (OCR) feature."""
        CLASSIFICATION: Feature._Type.ValueType  # 2
        """Classification feature."""
        FACE_DETECTION: Feature._Type.ValueType  # 3
        """Face detection feature."""
        IMAGE_COPY_SEARCH: Feature._Type.ValueType  # 4
        """Image copy search."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: Feature.Type.ValueType  # 0
    TEXT_DETECTION: Feature.Type.ValueType  # 1
    """Text detection (OCR) feature."""
    CLASSIFICATION: Feature.Type.ValueType  # 2
    """Classification feature."""
    FACE_DETECTION: Feature.Type.ValueType  # 3
    """Face detection feature."""
    IMAGE_COPY_SEARCH: Feature.Type.ValueType  # 4
    """Image copy search."""

    TYPE_FIELD_NUMBER: builtins.int
    CLASSIFICATION_CONFIG_FIELD_NUMBER: builtins.int
    TEXT_DETECTION_CONFIG_FIELD_NUMBER: builtins.int
    type: global___Feature.Type.ValueType
    """Type of requested feature."""
    @property
    def classification_config(self) -> global___FeatureClassificationConfig:
        """Required for the `CLASSIFICATION` type. Specifies configuration for the classification feature."""
    @property
    def text_detection_config(self) -> global___FeatureTextDetectionConfig:
        """Required for the `TEXT_DETECTION` type. Specifies configuration for the text detection (OCR) feature."""
    def __init__(
        self,
        *,
        type: global___Feature.Type.ValueType = ...,
        classification_config: global___FeatureClassificationConfig | None = ...,
        text_detection_config: global___FeatureTextDetectionConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["classification_config", b"classification_config", "config", b"config", "text_detection_config", b"text_detection_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["classification_config", b"classification_config", "config", b"config", "text_detection_config", b"text_detection_config", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config", b"config"]) -> typing_extensions.Literal["classification_config", "text_detection_config"] | None: ...

global___Feature = Feature

@typing_extensions.final
class FeatureClassificationConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_FIELD_NUMBER: builtins.int
    model: builtins.str
    """Model to use for image classification."""
    def __init__(
        self,
        *,
        model: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model", b"model"]) -> None: ...

global___FeatureClassificationConfig = FeatureClassificationConfig

@typing_extensions.final
class FeatureTextDetectionConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LANGUAGE_CODES_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    @property
    def language_codes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of the languages to recognize text.
        Specified in [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) format (for example, `` ru ``).
        """
    model: builtins.str
    """Model to use for text detection.
    Possible values:
    * page (default) - this model is suitable for detecting multiple text entries in an image.
    * line - this model is suitable for cropped images with one line of text.
    """
    def __init__(
        self,
        *,
        language_codes: collections.abc.Iterable[builtins.str] | None = ...,
        model: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_codes", b"language_codes", "model", b"model"]) -> None: ...

global___FeatureTextDetectionConfig = FeatureTextDetectionConfig

@typing_extensions.final
class BatchAnalyzeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AnalyzeResult]:
        """Request results.
        Results have the same order as specifications in the request.
        """
    def __init__(
        self,
        *,
        results: collections.abc.Iterable[global___AnalyzeResult] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["results", b"results"]) -> None: ...

global___BatchAnalyzeResponse = BatchAnalyzeResponse

@typing_extensions.final
class AnalyzeResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULTS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeatureResult]:
        """Results for each requested feature.
        Feature results have the same order as in the request.
        """
    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """Return error in case of error with file processing."""
    def __init__(
        self,
        *,
        results: collections.abc.Iterable[global___FeatureResult] | None = ...,
        error: google.rpc.status_pb2.Status | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "results", b"results"]) -> None: ...

global___AnalyzeResult = AnalyzeResult

@typing_extensions.final
class FeatureResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_DETECTION_FIELD_NUMBER: builtins.int
    CLASSIFICATION_FIELD_NUMBER: builtins.int
    FACE_DETECTION_FIELD_NUMBER: builtins.int
    IMAGE_COPY_SEARCH_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def text_detection(self) -> yandex.cloud.ai.vision.v1.text_detection_pb2.TextAnnotation:
        """Text detection (OCR) result."""
    @property
    def classification(self) -> yandex.cloud.ai.vision.v1.classification_pb2.ClassAnnotation:
        """Classification result."""
    @property
    def face_detection(self) -> yandex.cloud.ai.vision.v1.face_detection_pb2.FaceAnnotation:
        """Face detection result."""
    @property
    def image_copy_search(self) -> yandex.cloud.ai.vision.v1.image_copy_search_pb2.ImageCopySearchAnnotation:
        """Image Copy Search result."""
    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """Return error in case of error during the specified feature processing."""
    def __init__(
        self,
        *,
        text_detection: yandex.cloud.ai.vision.v1.text_detection_pb2.TextAnnotation | None = ...,
        classification: yandex.cloud.ai.vision.v1.classification_pb2.ClassAnnotation | None = ...,
        face_detection: yandex.cloud.ai.vision.v1.face_detection_pb2.FaceAnnotation | None = ...,
        image_copy_search: yandex.cloud.ai.vision.v1.image_copy_search_pb2.ImageCopySearchAnnotation | None = ...,
        error: google.rpc.status_pb2.Status | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["classification", b"classification", "error", b"error", "face_detection", b"face_detection", "feature", b"feature", "image_copy_search", b"image_copy_search", "text_detection", b"text_detection"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["classification", b"classification", "error", b"error", "face_detection", b"face_detection", "feature", b"feature", "image_copy_search", b"image_copy_search", "text_detection", b"text_detection"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["feature", b"feature"]) -> typing_extensions.Literal["text_detection", "classification", "face_detection", "image_copy_search"] | None: ...

global___FeatureResult = FeatureResult
