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
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CodeType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CodeTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CodeType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CODE_TYPE_UNSPECIFIED: _CodeType.ValueType  # 0
    WORKING: _CodeType.ValueType  # 1
    """all good"""
    WARNING: _CodeType.ValueType  # 2
    """for example, if speech is sent not in real time. or unknown context (and we've made fallback)."""
    CLOSED: _CodeType.ValueType  # 3
    """after session was closed."""

class CodeType(_CodeType, metaclass=_CodeTypeEnumTypeWrapper): ...

CODE_TYPE_UNSPECIFIED: CodeType.ValueType  # 0
WORKING: CodeType.ValueType  # 1
"""all good"""
WARNING: CodeType.ValueType  # 2
"""for example, if speech is sent not in real time. or unknown context (and we've made fallback)."""
CLOSED: CodeType.ValueType  # 3
"""after session was closed."""
global___CodeType = CodeType

@typing_extensions.final
class TextNormalizationOptions(google.protobuf.message.Message):
    """options"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _TextNormalization:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TextNormalizationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TextNormalizationOptions._TextNormalization.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TEXT_NORMALIZATION_UNSPECIFIED: TextNormalizationOptions._TextNormalization.ValueType  # 0
        TEXT_NORMALIZATION_ENABLED: TextNormalizationOptions._TextNormalization.ValueType  # 1
        """Enable normalization"""
        TEXT_NORMALIZATION_DISABLED: TextNormalizationOptions._TextNormalization.ValueType  # 2
        """Disable normalization"""

    class TextNormalization(_TextNormalization, metaclass=_TextNormalizationEnumTypeWrapper):
        """Normalization"""

    TEXT_NORMALIZATION_UNSPECIFIED: TextNormalizationOptions.TextNormalization.ValueType  # 0
    TEXT_NORMALIZATION_ENABLED: TextNormalizationOptions.TextNormalization.ValueType  # 1
    """Enable normalization"""
    TEXT_NORMALIZATION_DISABLED: TextNormalizationOptions.TextNormalization.ValueType  # 2
    """Disable normalization"""

    TEXT_NORMALIZATION_FIELD_NUMBER: builtins.int
    PROFANITY_FILTER_FIELD_NUMBER: builtins.int
    LITERATURE_TEXT_FIELD_NUMBER: builtins.int
    text_normalization: global___TextNormalizationOptions.TextNormalization.ValueType
    profanity_filter: builtins.bool
    """Filter profanity (default: false)."""
    literature_text: builtins.bool
    """Rewrite text in literature style (default: false)."""
    def __init__(
        self,
        *,
        text_normalization: global___TextNormalizationOptions.TextNormalization.ValueType = ...,
        profanity_filter: builtins.bool = ...,
        literature_text: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["literature_text", b"literature_text", "profanity_filter", b"profanity_filter", "text_normalization", b"text_normalization"]) -> None: ...

global___TextNormalizationOptions = TextNormalizationOptions

@typing_extensions.final
class DefaultEouClassifier(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _EouSensitivity:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EouSensitivityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DefaultEouClassifier._EouSensitivity.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        EOU_SENSITIVITY_UNSPECIFIED: DefaultEouClassifier._EouSensitivity.ValueType  # 0
        DEFAULT: DefaultEouClassifier._EouSensitivity.ValueType  # 1
        HIGH: DefaultEouClassifier._EouSensitivity.ValueType  # 2

    class EouSensitivity(_EouSensitivity, metaclass=_EouSensitivityEnumTypeWrapper): ...
    EOU_SENSITIVITY_UNSPECIFIED: DefaultEouClassifier.EouSensitivity.ValueType  # 0
    DEFAULT: DefaultEouClassifier.EouSensitivity.ValueType  # 1
    HIGH: DefaultEouClassifier.EouSensitivity.ValueType  # 2

    TYPE_FIELD_NUMBER: builtins.int
    MAX_PAUSE_BETWEEN_WORDS_HINT_MS_FIELD_NUMBER: builtins.int
    type: global___DefaultEouClassifier.EouSensitivity.ValueType
    """EOU sensitivity. Currently two levels, faster with more error and more conservative (our default)."""
    max_pause_between_words_hint_ms: builtins.int
    """Hint for max pause between words. Our EoU detector could use this information to distinguish between end of utterance and slow speech (like one <long pause> two <long pause> three, etc)."""
    def __init__(
        self,
        *,
        type: global___DefaultEouClassifier.EouSensitivity.ValueType = ...,
        max_pause_between_words_hint_ms: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_pause_between_words_hint_ms", b"max_pause_between_words_hint_ms", "type", b"type"]) -> None: ...

global___DefaultEouClassifier = DefaultEouClassifier

@typing_extensions.final
class ExternalEouClassifier(google.protobuf.message.Message):
    """Use EOU provided by user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ExternalEouClassifier = ExternalEouClassifier

@typing_extensions.final
class EouClassifierOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_CLASSIFIER_FIELD_NUMBER: builtins.int
    EXTERNAL_CLASSIFIER_FIELD_NUMBER: builtins.int
    @property
    def default_classifier(self) -> global___DefaultEouClassifier:
        """EOU classifier provided by SpeechKit. Default."""
    @property
    def external_classifier(self) -> global___ExternalEouClassifier:
        """EoU is enforced by external messages from user."""
    def __init__(
        self,
        *,
        default_classifier: global___DefaultEouClassifier | None = ...,
        external_classifier: global___ExternalEouClassifier | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Classifier", b"Classifier", "default_classifier", b"default_classifier", "external_classifier", b"external_classifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Classifier", b"Classifier", "default_classifier", b"default_classifier", "external_classifier", b"external_classifier"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["Classifier", b"Classifier"]) -> typing_extensions.Literal["default_classifier", "external_classifier"] | None: ...

global___EouClassifierOptions = EouClassifierOptions

@typing_extensions.final
class RawAudio(google.protobuf.message.Message):
    """RAW Audio format spec (no container to infer type). Used in AudioFormat options."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _AudioEncoding:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AudioEncodingEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RawAudio._AudioEncoding.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        AUDIO_ENCODING_UNSPECIFIED: RawAudio._AudioEncoding.ValueType  # 0
        LINEAR16_PCM: RawAudio._AudioEncoding.ValueType  # 1
        """Audio bit depth 16-bit signed little-endian (Linear PCM)."""

    class AudioEncoding(_AudioEncoding, metaclass=_AudioEncodingEnumTypeWrapper): ...
    AUDIO_ENCODING_UNSPECIFIED: RawAudio.AudioEncoding.ValueType  # 0
    LINEAR16_PCM: RawAudio.AudioEncoding.ValueType  # 1
    """Audio bit depth 16-bit signed little-endian (Linear PCM)."""

    AUDIO_ENCODING_FIELD_NUMBER: builtins.int
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: builtins.int
    AUDIO_CHANNEL_COUNT_FIELD_NUMBER: builtins.int
    audio_encoding: global___RawAudio.AudioEncoding.ValueType
    """ Type of audio encoding"""
    sample_rate_hertz: builtins.int
    """ PCM sample rate"""
    audio_channel_count: builtins.int
    """ PCM channel count. Currently only single channel audio is supported in real-time recognition."""
    def __init__(
        self,
        *,
        audio_encoding: global___RawAudio.AudioEncoding.ValueType = ...,
        sample_rate_hertz: builtins.int = ...,
        audio_channel_count: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["audio_channel_count", b"audio_channel_count", "audio_encoding", b"audio_encoding", "sample_rate_hertz", b"sample_rate_hertz"]) -> None: ...

global___RawAudio = RawAudio

@typing_extensions.final
class ContainerAudio(google.protobuf.message.Message):
    """Audio with fixed type in container. Used in AudioFormat options."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ContainerAudioType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ContainerAudioTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ContainerAudio._ContainerAudioType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CONTAINER_AUDIO_TYPE_UNSPECIFIED: ContainerAudio._ContainerAudioType.ValueType  # 0
        WAV: ContainerAudio._ContainerAudioType.ValueType  # 1
        """Audio bit depth 16-bit signed little-endian (Linear PCM)."""
        OGG_OPUS: ContainerAudio._ContainerAudioType.ValueType  # 2
        """Data is encoded using the OPUS audio codec and compressed using the OGG container format."""
        MP3: ContainerAudio._ContainerAudioType.ValueType  # 3
        """Data is encoded using MPEG-1/2 Layer III and compressed using the MP3 container format."""

    class ContainerAudioType(_ContainerAudioType, metaclass=_ContainerAudioTypeEnumTypeWrapper): ...
    CONTAINER_AUDIO_TYPE_UNSPECIFIED: ContainerAudio.ContainerAudioType.ValueType  # 0
    WAV: ContainerAudio.ContainerAudioType.ValueType  # 1
    """Audio bit depth 16-bit signed little-endian (Linear PCM)."""
    OGG_OPUS: ContainerAudio.ContainerAudioType.ValueType  # 2
    """Data is encoded using the OPUS audio codec and compressed using the OGG container format."""
    MP3: ContainerAudio.ContainerAudioType.ValueType  # 3
    """Data is encoded using MPEG-1/2 Layer III and compressed using the MP3 container format."""

    CONTAINER_AUDIO_TYPE_FIELD_NUMBER: builtins.int
    container_audio_type: global___ContainerAudio.ContainerAudioType.ValueType
    """ Type of audio container."""
    def __init__(
        self,
        *,
        container_audio_type: global___ContainerAudio.ContainerAudioType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_audio_type", b"container_audio_type"]) -> None: ...

global___ContainerAudio = ContainerAudio

@typing_extensions.final
class AudioFormatOptions(google.protobuf.message.Message):
    """Audio format options."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RAW_AUDIO_FIELD_NUMBER: builtins.int
    CONTAINER_AUDIO_FIELD_NUMBER: builtins.int
    @property
    def raw_audio(self) -> global___RawAudio:
        """Audio without container."""
    @property
    def container_audio(self) -> global___ContainerAudio:
        """Audio is wrapped in container."""
    def __init__(
        self,
        *,
        raw_audio: global___RawAudio | None = ...,
        container_audio: global___ContainerAudio | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["AudioFormat", b"AudioFormat", "container_audio", b"container_audio", "raw_audio", b"raw_audio"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["AudioFormat", b"AudioFormat", "container_audio", b"container_audio", "raw_audio", b"raw_audio"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["AudioFormat", b"AudioFormat"]) -> typing_extensions.Literal["raw_audio", "container_audio"] | None: ...

global___AudioFormatOptions = AudioFormatOptions

@typing_extensions.final
class LanguageRestrictionOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _LanguageRestrictionType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _LanguageRestrictionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LanguageRestrictionOptions._LanguageRestrictionType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        LANGUAGE_RESTRICTION_TYPE_UNSPECIFIED: LanguageRestrictionOptions._LanguageRestrictionType.ValueType  # 0
        WHITELIST: LanguageRestrictionOptions._LanguageRestrictionType.ValueType  # 1
        BLACKLIST: LanguageRestrictionOptions._LanguageRestrictionType.ValueType  # 2

    class LanguageRestrictionType(_LanguageRestrictionType, metaclass=_LanguageRestrictionTypeEnumTypeWrapper): ...
    LANGUAGE_RESTRICTION_TYPE_UNSPECIFIED: LanguageRestrictionOptions.LanguageRestrictionType.ValueType  # 0
    WHITELIST: LanguageRestrictionOptions.LanguageRestrictionType.ValueType  # 1
    BLACKLIST: LanguageRestrictionOptions.LanguageRestrictionType.ValueType  # 2

    RESTRICTION_TYPE_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    restriction_type: global___LanguageRestrictionOptions.LanguageRestrictionType.ValueType
    @property
    def language_code(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        restriction_type: global___LanguageRestrictionOptions.LanguageRestrictionType.ValueType = ...,
        language_code: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code", b"language_code", "restriction_type", b"restriction_type"]) -> None: ...

global___LanguageRestrictionOptions = LanguageRestrictionOptions

@typing_extensions.final
class RecognitionModelOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _AudioProcessingType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AudioProcessingTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RecognitionModelOptions._AudioProcessingType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        AUDIO_PROCESSING_TYPE_UNSPECIFIED: RecognitionModelOptions._AudioProcessingType.ValueType  # 0
        REAL_TIME: RecognitionModelOptions._AudioProcessingType.ValueType  # 1
        FULL_DATA: RecognitionModelOptions._AudioProcessingType.ValueType  # 2

    class AudioProcessingType(_AudioProcessingType, metaclass=_AudioProcessingTypeEnumTypeWrapper): ...
    AUDIO_PROCESSING_TYPE_UNSPECIFIED: RecognitionModelOptions.AudioProcessingType.ValueType  # 0
    REAL_TIME: RecognitionModelOptions.AudioProcessingType.ValueType  # 1
    FULL_DATA: RecognitionModelOptions.AudioProcessingType.ValueType  # 2

    MODEL_FIELD_NUMBER: builtins.int
    AUDIO_FORMAT_FIELD_NUMBER: builtins.int
    TEXT_NORMALIZATION_FIELD_NUMBER: builtins.int
    LANGUAGE_RESTRICTION_FIELD_NUMBER: builtins.int
    AUDIO_PROCESSING_TYPE_FIELD_NUMBER: builtins.int
    model: builtins.str
    """ Reserved for future, do not use."""
    @property
    def audio_format(self) -> global___AudioFormatOptions:
        """ Specified input audio."""
    @property
    def text_normalization(self) -> global___TextNormalizationOptions:
        """ Text normalization options."""
    @property
    def language_restriction(self) -> global___LanguageRestrictionOptions:
        """Possible languages in audio."""
    audio_processing_type: global___RecognitionModelOptions.AudioProcessingType.ValueType
    """How to deal with audio data (in real time, after all data is received, etc). Default is REAL_TIME."""
    def __init__(
        self,
        *,
        model: builtins.str = ...,
        audio_format: global___AudioFormatOptions | None = ...,
        text_normalization: global___TextNormalizationOptions | None = ...,
        language_restriction: global___LanguageRestrictionOptions | None = ...,
        audio_processing_type: global___RecognitionModelOptions.AudioProcessingType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["audio_format", b"audio_format", "language_restriction", b"language_restriction", "text_normalization", b"text_normalization"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["audio_format", b"audio_format", "audio_processing_type", b"audio_processing_type", "language_restriction", b"language_restriction", "model", b"model", "text_normalization", b"text_normalization"]) -> None: ...

global___RecognitionModelOptions = RecognitionModelOptions

@typing_extensions.final
class StreamingOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECOGNITION_MODEL_FIELD_NUMBER: builtins.int
    EOU_CLASSIFIER_FIELD_NUMBER: builtins.int
    @property
    def recognition_model(self) -> global___RecognitionModelOptions:
        """ Configuration for speech recognition model."""
    @property
    def eou_classifier(self) -> global___EouClassifierOptions:
        """ Configuration for end of utterance detection model."""
    def __init__(
        self,
        *,
        recognition_model: global___RecognitionModelOptions | None = ...,
        eou_classifier: global___EouClassifierOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["eou_classifier", b"eou_classifier", "recognition_model", b"recognition_model"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["eou_classifier", b"eou_classifier", "recognition_model", b"recognition_model"]) -> None: ...

global___StreamingOptions = StreamingOptions

@typing_extensions.final
class AudioChunk(google.protobuf.message.Message):
    """Data chunk with audio."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    """Bytes with audio data."""
    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___AudioChunk = AudioChunk

@typing_extensions.final
class SilenceChunk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DURATION_MS_FIELD_NUMBER: builtins.int
    duration_ms: builtins.int
    """Duration of silence chunk in ms."""
    def __init__(
        self,
        *,
        duration_ms: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration_ms", b"duration_ms"]) -> None: ...

global___SilenceChunk = SilenceChunk

@typing_extensions.final
class Eou(google.protobuf.message.Message):
    """Force EOU"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Eou = Eou

@typing_extensions.final
class StreamingRequest(google.protobuf.message.Message):
    """Streaming audio request
    Events are control messages from user.
    First message should be session options.
    The next messages are audio data chunks or control messages.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_OPTIONS_FIELD_NUMBER: builtins.int
    CHUNK_FIELD_NUMBER: builtins.int
    SILENCE_CHUNK_FIELD_NUMBER: builtins.int
    EOU_FIELD_NUMBER: builtins.int
    @property
    def session_options(self) -> global___StreamingOptions:
        """Session options. should be first message from user"""
    @property
    def chunk(self) -> global___AudioChunk:
        """Chunk with audio data."""
    @property
    def silence_chunk(self) -> global___SilenceChunk:
        """Chunk with silence."""
    @property
    def eou(self) -> global___Eou:
        """Request to end current utterance. Works only with external EoU detector."""
    def __init__(
        self,
        *,
        session_options: global___StreamingOptions | None = ...,
        chunk: global___AudioChunk | None = ...,
        silence_chunk: global___SilenceChunk | None = ...,
        eou: global___Eou | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Event", b"Event", "chunk", b"chunk", "eou", b"eou", "session_options", b"session_options", "silence_chunk", b"silence_chunk"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Event", b"Event", "chunk", b"chunk", "eou", b"eou", "session_options", b"session_options", "silence_chunk", b"silence_chunk"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["Event", b"Event"]) -> typing_extensions.Literal["session_options", "chunk", "silence_chunk", "eou"] | None: ...

global___StreamingRequest = StreamingRequest

@typing_extensions.final
class Word(google.protobuf.message.Message):
    """Now response

    Recognized word.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    START_TIME_MS_FIELD_NUMBER: builtins.int
    END_TIME_MS_FIELD_NUMBER: builtins.int
    text: builtins.str
    """ Word text."""
    start_time_ms: builtins.int
    """ Estimation of word start time in ms"""
    end_time_ms: builtins.int
    """ Estimation of word end time in ms"""
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        start_time_ms: builtins.int = ...,
        end_time_ms: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_time_ms", b"end_time_ms", "start_time_ms", b"start_time_ms", "text", b"text"]) -> None: ...

global___Word = Word

@typing_extensions.final
class LanguageEstimation(google.protobuf.message.Message):
    """Estimation of language probability"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PROBABILITY_FIELD_NUMBER: builtins.int
    language_code: builtins.str
    probability: builtins.float
    def __init__(
        self,
        *,
        language_code: builtins.str = ...,
        probability: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code", b"language_code", "probability", b"probability"]) -> None: ...

global___LanguageEstimation = LanguageEstimation

@typing_extensions.final
class Alternative(google.protobuf.message.Message):
    """Recognition of specific time frame."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORDS_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    START_TIME_MS_FIELD_NUMBER: builtins.int
    END_TIME_MS_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    LANGUAGES_FIELD_NUMBER: builtins.int
    @property
    def words(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Word]:
        """ Words in time frame."""
    text: builtins.str
    """ Text in time frame."""
    start_time_ms: builtins.int
    """Start of time frame."""
    end_time_ms: builtins.int
    """End of time frame."""
    confidence: builtins.float
    """Hypothesis confidence. Currently is not used."""
    @property
    def languages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LanguageEstimation]:
        """Distribution over possible languages"""
    def __init__(
        self,
        *,
        words: collections.abc.Iterable[global___Word] | None = ...,
        text: builtins.str = ...,
        start_time_ms: builtins.int = ...,
        end_time_ms: builtins.int = ...,
        confidence: builtins.float = ...,
        languages: collections.abc.Iterable[global___LanguageEstimation] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["confidence", b"confidence", "end_time_ms", b"end_time_ms", "languages", b"languages", "start_time_ms", b"start_time_ms", "text", b"text", "words", b"words"]) -> None: ...

global___Alternative = Alternative

@typing_extensions.final
class EouUpdate(google.protobuf.message.Message):
    """Update information from"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_MS_FIELD_NUMBER: builtins.int
    time_ms: builtins.int
    """End of utterance estimated time."""
    def __init__(
        self,
        *,
        time_ms: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["time_ms", b"time_ms"]) -> None: ...

global___EouUpdate = EouUpdate

@typing_extensions.final
class AlternativeUpdate(google.protobuf.message.Message):
    """Update of hypothesis."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALTERNATIVES_FIELD_NUMBER: builtins.int
    CHANNEL_TAG_FIELD_NUMBER: builtins.int
    @property
    def alternatives(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Alternative]:
        """List of hypothesis for timeframes."""
    channel_tag: builtins.str
    """Tag for distinguish audio channels."""
    def __init__(
        self,
        *,
        alternatives: collections.abc.Iterable[global___Alternative] | None = ...,
        channel_tag: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alternatives", b"alternatives", "channel_tag", b"channel_tag"]) -> None: ...

global___AlternativeUpdate = AlternativeUpdate

@typing_extensions.final
class AudioCursors(google.protobuf.message.Message):
    """AudioCursors are state of ASR recognition stream."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECEIVED_DATA_MS_FIELD_NUMBER: builtins.int
    RESET_TIME_MS_FIELD_NUMBER: builtins.int
    PARTIAL_TIME_MS_FIELD_NUMBER: builtins.int
    FINAL_TIME_MS_FIELD_NUMBER: builtins.int
    FINAL_INDEX_FIELD_NUMBER: builtins.int
    EOU_TIME_MS_FIELD_NUMBER: builtins.int
    received_data_ms: builtins.int
    """Amount of audio chunks server received. This cursor is moved after each audio chunk was received by server."""
    reset_time_ms: builtins.int
    """Input stream reset data."""
    partial_time_ms: builtins.int
    """ How much audio was processed. This time includes trimming silences as well. This cursor is moved after server received enough data
     to update recognition results (includes silence as well).
    """
    final_time_ms: builtins.int
    """ Time of last final. This cursor is moved when server decides that recognition from start of audio until final_time_ms will not change anymore
     usually this even is followed by EOU detection (but this could change in future).
    """
    final_index: builtins.int
    """ This is index of last final server send. Incremented after each new final."""
    eou_time_ms: builtins.int
    """ Estimated time of EOU. Cursor is updated after each new EOU is sent.
     For external classifier this equals to received_data_ms at the moment EOU event arrives.
     For internal classifier this is estimation of time. The time is not exact and has the same guarantees as word timings.
    """
    def __init__(
        self,
        *,
        received_data_ms: builtins.int = ...,
        reset_time_ms: builtins.int = ...,
        partial_time_ms: builtins.int = ...,
        final_time_ms: builtins.int = ...,
        final_index: builtins.int = ...,
        eou_time_ms: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["eou_time_ms", b"eou_time_ms", "final_index", b"final_index", "final_time_ms", b"final_time_ms", "partial_time_ms", b"partial_time_ms", "received_data_ms", b"received_data_ms", "reset_time_ms", b"reset_time_ms"]) -> None: ...

global___AudioCursors = AudioCursors

@typing_extensions.final
class FinalRefinement(google.protobuf.message.Message):
    """Refinement for final hypo. For example, text normalization is refinement."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FINAL_INDEX_FIELD_NUMBER: builtins.int
    NORMALIZED_TEXT_FIELD_NUMBER: builtins.int
    final_index: builtins.int
    """Index of final for which server sends additional information."""
    @property
    def normalized_text(self) -> global___AlternativeUpdate:
        """Normalized text instead of raw one."""
    def __init__(
        self,
        *,
        final_index: builtins.int = ...,
        normalized_text: global___AlternativeUpdate | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Type", b"Type", "normalized_text", b"normalized_text"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Type", b"Type", "final_index", b"final_index", "normalized_text", b"normalized_text"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["Type", b"Type"]) -> typing_extensions.Literal["normalized_text"] | None: ...

global___FinalRefinement = FinalRefinement

@typing_extensions.final
class StatusCode(google.protobuf.message.Message):
    """Status message"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_TYPE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code_type: global___CodeType.ValueType
    """Code type."""
    message: builtins.str
    """Human readable message."""
    def __init__(
        self,
        *,
        code_type: global___CodeType.ValueType = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code_type", b"code_type", "message", b"message"]) -> None: ...

global___StatusCode = StatusCode

@typing_extensions.final
class SessionUuid(google.protobuf.message.Message):
    """Session identifier."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    USER_REQUEST_ID_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    """Internal session identifier."""
    user_request_id: builtins.str
    """User session identifier."""
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        user_request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_request_id", b"user_request_id", "uuid", b"uuid"]) -> None: ...

global___SessionUuid = SessionUuid

@typing_extensions.final
class StreamingResponse(google.protobuf.message.Message):
    """Responses from server.
    Each response contains session uuid
    AudioCursors
    plus specific event
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_UUID_FIELD_NUMBER: builtins.int
    AUDIO_CURSORS_FIELD_NUMBER: builtins.int
    RESPONSE_WALL_TIME_MS_FIELD_NUMBER: builtins.int
    PARTIAL_FIELD_NUMBER: builtins.int
    FINAL_FIELD_NUMBER: builtins.int
    EOU_UPDATE_FIELD_NUMBER: builtins.int
    FINAL_REFINEMENT_FIELD_NUMBER: builtins.int
    STATUS_CODE_FIELD_NUMBER: builtins.int
    @property
    def session_uuid(self) -> global___SessionUuid:
        """Session identifier"""
    @property
    def audio_cursors(self) -> global___AudioCursors:
        """Progress bar for stream session recognition: how many data we obtained; final and partial times; etc."""
    response_wall_time_ms: builtins.int
    """Wall clock on server side. This is time when server wrote results to stream"""
    @property
    def partial(self) -> global___AlternativeUpdate:
        """Partial results, server will send them regularly after enough audio data was received from user. This are current text estimation
         from final_time_ms to partial_time_ms. Could change after new data will arrive.
        """
    @property
    def final(self) -> global___AlternativeUpdate:
        """ Final results, the recognition is now fixed until final_time_ms. For now, final is sent only if the EOU event was triggered. This could be change in future releases."""
    @property
    def eou_update(self) -> global___EouUpdate:
        """ After EOU classifier, send the message with final, send the EouUpdate with time of EOU
         before eou_update we send final with the same time. there could be several finals before eou update.
        """
    @property
    def final_refinement(self) -> global___FinalRefinement:
        """   For each final, if normalization is enabled, sent the normalized text (or some other advanced post-processing).
           Final normalization will introduce additional latency.
        """
    @property
    def status_code(self) -> global___StatusCode:
        """   Status messages, send by server with fixed interval (keep-alive)."""
    def __init__(
        self,
        *,
        session_uuid: global___SessionUuid | None = ...,
        audio_cursors: global___AudioCursors | None = ...,
        response_wall_time_ms: builtins.int = ...,
        partial: global___AlternativeUpdate | None = ...,
        final: global___AlternativeUpdate | None = ...,
        eou_update: global___EouUpdate | None = ...,
        final_refinement: global___FinalRefinement | None = ...,
        status_code: global___StatusCode | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Event", b"Event", "audio_cursors", b"audio_cursors", "eou_update", b"eou_update", "final", b"final", "final_refinement", b"final_refinement", "partial", b"partial", "session_uuid", b"session_uuid", "status_code", b"status_code"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Event", b"Event", "audio_cursors", b"audio_cursors", "eou_update", b"eou_update", "final", b"final", "final_refinement", b"final_refinement", "partial", b"partial", "response_wall_time_ms", b"response_wall_time_ms", "session_uuid", b"session_uuid", "status_code", b"status_code"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["Event", b"Event"]) -> typing_extensions.Literal["partial", "final", "eou_update", "final_refinement", "status_code"] | None: ...

global___StreamingResponse = StreamingResponse
