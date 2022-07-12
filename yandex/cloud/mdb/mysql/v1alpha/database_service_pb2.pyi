"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.mdb.mysql.v1alpha.database_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MySQL cluster that the database belongs to.
    To get the cluster ID use a [ClusterService.List] request.
    """

    database_name: typing.Text
    """Name of the MySQL database to return.
    To get the name of the database use a [DatabaseService.List] request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","database_name",b"database_name"]) -> None: ...
global___GetDatabaseRequest = GetDatabaseRequest

class ListDatabasesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MySQL cluster to list databases in.
    To get the cluster ID use a [ClusterService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListDatabasesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results, Set [page_token] to the [ListDatabasesResponse.next_page_token]
    returned by the previous list request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListDatabasesRequest = ListDatabasesRequest

class ListDatabasesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATABASES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def databases(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.mysql.v1alpha.database_pb2.Database]:
        """List of MySQL databases."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListDatabasesRequest.page_size], use the [next_page_token] as the value
    for the [ListDatabasesRequest.page_token] parameter in the next list request. Each subsequent
    list request will have its own [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        databases: typing.Optional[typing.Iterable[yandex.cloud.mdb.mysql.v1alpha.database_pb2.Database]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["databases",b"databases","next_page_token",b"next_page_token"]) -> None: ...
global___ListDatabasesResponse = ListDatabasesResponse

class CreateDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MySQL cluster to create a database in.
    To get the cluster ID use a [ClusterService.List] request.
    """

    @property
    def database_spec(self) -> yandex.cloud.mdb.mysql.v1alpha.database_pb2.DatabaseSpec:
        """Configuration of the database to create."""
        pass
    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        database_spec: typing.Optional[yandex.cloud.mdb.mysql.v1alpha.database_pb2.DatabaseSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["database_spec",b"database_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","database_spec",b"database_spec"]) -> None: ...
global___CreateDatabaseRequest = CreateDatabaseRequest

class CreateDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MySQL cluster where a database is being created."""

    database_name: typing.Text
    """Name of the MySQL database that is being created."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","database_name",b"database_name"]) -> None: ...
global___CreateDatabaseMetadata = CreateDatabaseMetadata

class DeleteDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MySQL cluster to delete a database in.
    To get the cluster ID, use a [ClusterService.List] request.
    """

    database_name: typing.Text
    """Name of the database to delete.
    To get the name of the database, use a [DatabaseService.List] request.
    """

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","database_name",b"database_name"]) -> None: ...
global___DeleteDatabaseRequest = DeleteDatabaseRequest

class DeleteDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: typing.Text
    """ID of the MySQL cluster where a database is being deleted."""

    database_name: typing.Text
    """Name of the MySQL database that is being deleted."""

    def __init__(self,
        *,
        cluster_id: typing.Text = ...,
        database_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_id",b"cluster_id","database_name",b"database_name"]) -> None: ...
global___DeleteDatabaseMetadata = DeleteDatabaseMetadata
