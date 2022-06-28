"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.ai.translate.v2.translation_service_pb2

class TranslationServiceStub:
    """A set of methods for the Translate service."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Translate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.translate.v2.translation_service_pb2.TranslateRequest,
        yandex.cloud.ai.translate.v2.translation_service_pb2.TranslateResponse]
    """Translates the text to the specified language."""

    DetectLanguage: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.translate.v2.translation_service_pb2.DetectLanguageRequest,
        yandex.cloud.ai.translate.v2.translation_service_pb2.DetectLanguageResponse]
    """Detects the language of the text."""

    ListLanguages: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.translate.v2.translation_service_pb2.ListLanguagesRequest,
        yandex.cloud.ai.translate.v2.translation_service_pb2.ListLanguagesResponse]
    """Retrieves the list of supported languages."""


class TranslationServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for the Translate service."""
    @abc.abstractmethod
    def Translate(self,
        request: yandex.cloud.ai.translate.v2.translation_service_pb2.TranslateRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.ai.translate.v2.translation_service_pb2.TranslateResponse:
        """Translates the text to the specified language."""
        pass

    @abc.abstractmethod
    def DetectLanguage(self,
        request: yandex.cloud.ai.translate.v2.translation_service_pb2.DetectLanguageRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.ai.translate.v2.translation_service_pb2.DetectLanguageResponse:
        """Detects the language of the text."""
        pass

    @abc.abstractmethod
    def ListLanguages(self,
        request: yandex.cloud.ai.translate.v2.translation_service_pb2.ListLanguagesRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.ai.translate.v2.translation_service_pb2.ListLanguagesResponse:
        """Retrieves the list of supported languages."""
        pass


def add_TranslationServiceServicer_to_server(servicer: TranslationServiceServicer, server: grpc.Server) -> None: ...
