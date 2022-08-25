"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.iam.v1.iam_token_service_pb2

class IamTokenServiceStub:
    """A set of methods for managing IAM tokens."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.iam_token_service_pb2.CreateIamTokenRequest,
        yandex.cloud.iam.v1.iam_token_service_pb2.CreateIamTokenResponse,
    ]
    """Creates an IAM token for the specified identity."""
    CreateForServiceAccount: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.iam_token_service_pb2.CreateIamTokenForServiceAccountRequest,
        yandex.cloud.iam.v1.iam_token_service_pb2.CreateIamTokenResponse,
    ]
    """Create iam token for service account."""

class IamTokenServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing IAM tokens."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.iam.v1.iam_token_service_pb2.CreateIamTokenRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iam.v1.iam_token_service_pb2.CreateIamTokenResponse:
        """Creates an IAM token for the specified identity."""
    @abc.abstractmethod
    def CreateForServiceAccount(
        self,
        request: yandex.cloud.iam.v1.iam_token_service_pb2.CreateIamTokenForServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.iam.v1.iam_token_service_pb2.CreateIamTokenResponse:
        """Create iam token for service account."""

def add_IamTokenServiceServicer_to_server(servicer: IamTokenServiceServicer, server: grpc.Server) -> None: ...
