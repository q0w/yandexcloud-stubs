"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import typing
import yandex.cloud.ai.stt.v3.stt_pb2

class RecognizerStub:
    """A set of methods for voice recognition."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    RecognizeStreaming: grpc.StreamStreamMultiCallable[
        yandex.cloud.ai.stt.v3.stt_pb2.StreamingRequest,
        yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse]
    """Expects audio in real-time"""


class RecognizerServicer(metaclass=abc.ABCMeta):
    """A set of methods for voice recognition."""
    @abc.abstractmethod
    def RecognizeStreaming(self,
        request_iterator: typing.Iterator[yandex.cloud.ai.stt.v3.stt_pb2.StreamingRequest],
        context: grpc.ServicerContext,
    ) -> typing.Iterator[yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse]:
        """Expects audio in real-time"""
        pass


def add_RecognizerServicer_to_server(servicer: RecognizerServicer, server: grpc.Server) -> None: ...
