"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import yandex.cloud.mdb.redis.v1.backup_pb2
import yandex.cloud.mdb.redis.v1.backup_service_pb2

class BackupServiceStub:
    """A set of methods for managing Redis backups."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.backup_service_pb2.GetBackupRequest,
        yandex.cloud.mdb.redis.v1.backup_pb2.Backup]
    """Returns the specified Redis backup.

    To get the list of available Redis backups, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsResponse]
    """Retrieves the list of Redis backups available for the specified folder."""


class BackupServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Redis backups."""
    @abc.abstractmethod
    def Get(self,
        request: yandex.cloud.mdb.redis.v1.backup_service_pb2.GetBackupRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.backup_pb2.Backup:
        """Returns the specified Redis backup.

        To get the list of available Redis backups, make a [List] request.
        """
        pass

    @abc.abstractmethod
    def List(self,
        request: yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsRequest,
        context: grpc.ServicerContext,
    ) -> yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsResponse:
        """Retrieves the list of Redis backups available for the specified folder."""
        pass


def add_BackupServiceServicer_to_server(servicer: BackupServiceServicer, server: grpc.Server) -> None: ...
