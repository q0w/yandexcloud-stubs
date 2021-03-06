"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import yandex.cloud.operation.operation_pb2
import yandex.cloud.serverless.containers.v1.container_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetContainerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id"]) -> None: ...
global___GetContainerRequest = GetContainerRequest

class ListContainersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    page_size: builtins.int
    page_token: typing.Text
    filter: typing.Text
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","folder_id",b"folder_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListContainersRequest = ListContainersRequest

class ListContainersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def containers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.serverless.containers.v1.container_pb2.Container]: ...
    next_page_token: typing.Text
    def __init__(self,
        *,
        containers: typing.Optional[typing.Iterable[yandex.cloud.serverless.containers.v1.container_pb2.Container]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["containers",b"containers","next_page_token",b"next_page_token"]) -> None: ...
global___ListContainersResponse = ListContainersResponse

class CreateContainerRequest(google.protobuf.message.Message):
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
    folder_id: typing.Text
    name: typing.Text
    description: typing.Text
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","folder_id",b"folder_id","labels",b"labels","name",b"name"]) -> None: ...
global___CreateContainerRequest = CreateContainerRequest

class CreateContainerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id"]) -> None: ...
global___CreateContainerMetadata = CreateContainerMetadata

class UpdateContainerRequest(google.protobuf.message.Message):
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

    CONTAINER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    name: typing.Text
    description: typing.Text
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id","description",b"description","labels",b"labels","name",b"name","update_mask",b"update_mask"]) -> None: ...
global___UpdateContainerRequest = UpdateContainerRequest

class UpdateContainerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id"]) -> None: ...
global___UpdateContainerMetadata = UpdateContainerMetadata

class DeleteContainerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id"]) -> None: ...
global___DeleteContainerRequest = DeleteContainerRequest

class DeleteContainerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id"]) -> None: ...
global___DeleteContainerMetadata = DeleteContainerMetadata

class GetContainerRevisionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_REVISION_ID_FIELD_NUMBER: builtins.int
    container_revision_id: typing.Text
    def __init__(self,
        *,
        container_revision_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_revision_id",b"container_revision_id"]) -> None: ...
global___GetContainerRevisionRequest = GetContainerRevisionRequest

class ListContainersRevisionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: typing.Text
    container_id: typing.Text
    page_size: builtins.int
    page_token: typing.Text
    filter: typing.Text
    def __init__(self,
        *,
        folder_id: typing.Text = ...,
        container_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["container_id",b"container_id","folder_id",b"folder_id","id",b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id","filter",b"filter","folder_id",b"folder_id","id",b"id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["id",b"id"]) -> typing.Optional[typing_extensions.Literal["folder_id","container_id"]]: ...
global___ListContainersRevisionsRequest = ListContainersRevisionsRequest

class ListContainersRevisionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REVISIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def revisions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.serverless.containers.v1.container_pb2.Revision]: ...
    next_page_token: typing.Text
    def __init__(self,
        *,
        revisions: typing.Optional[typing.Iterable[yandex.cloud.serverless.containers.v1.container_pb2.Revision]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","revisions",b"revisions"]) -> None: ...
global___ListContainersRevisionsResponse = ListContainersRevisionsResponse

class DeployContainerRevisionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    EXECUTION_TIMEOUT_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    IMAGE_SPEC_FIELD_NUMBER: builtins.int
    CONCURRENCY_FIELD_NUMBER: builtins.int
    SECRETS_FIELD_NUMBER: builtins.int
    CONNECTIVITY_FIELD_NUMBER: builtins.int
    PROVISION_POLICY_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    description: typing.Text
    @property
    def resources(self) -> yandex.cloud.serverless.containers.v1.container_pb2.Resources: ...
    @property
    def execution_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    service_account_id: typing.Text
    @property
    def image_spec(self) -> global___ImageSpec: ...
    concurrency: builtins.int
    @property
    def secrets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.serverless.containers.v1.container_pb2.Secret]: ...
    @property
    def connectivity(self) -> yandex.cloud.serverless.containers.v1.container_pb2.Connectivity: ...
    @property
    def provision_policy(self) -> yandex.cloud.serverless.containers.v1.container_pb2.ProvisionPolicy: ...
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        description: typing.Text = ...,
        resources: typing.Optional[yandex.cloud.serverless.containers.v1.container_pb2.Resources] = ...,
        execution_timeout: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        service_account_id: typing.Text = ...,
        image_spec: typing.Optional[global___ImageSpec] = ...,
        concurrency: builtins.int = ...,
        secrets: typing.Optional[typing.Iterable[yandex.cloud.serverless.containers.v1.container_pb2.Secret]] = ...,
        connectivity: typing.Optional[yandex.cloud.serverless.containers.v1.container_pb2.Connectivity] = ...,
        provision_policy: typing.Optional[yandex.cloud.serverless.containers.v1.container_pb2.ProvisionPolicy] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connectivity",b"connectivity","execution_timeout",b"execution_timeout","image_spec",b"image_spec","provision_policy",b"provision_policy","resources",b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["concurrency",b"concurrency","connectivity",b"connectivity","container_id",b"container_id","description",b"description","execution_timeout",b"execution_timeout","image_spec",b"image_spec","provision_policy",b"provision_policy","resources",b"resources","secrets",b"secrets","service_account_id",b"service_account_id"]) -> None: ...
global___DeployContainerRevisionRequest = DeployContainerRevisionRequest

class ImageSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class EnvironmentEntry(google.protobuf.message.Message):
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

    IMAGE_URL_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    WORKING_DIR_FIELD_NUMBER: builtins.int
    image_url: typing.Text
    @property
    def command(self) -> yandex.cloud.serverless.containers.v1.container_pb2.Command: ...
    @property
    def args(self) -> yandex.cloud.serverless.containers.v1.container_pb2.Args: ...
    @property
    def environment(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    working_dir: typing.Text
    def __init__(self,
        *,
        image_url: typing.Text = ...,
        command: typing.Optional[yandex.cloud.serverless.containers.v1.container_pb2.Command] = ...,
        args: typing.Optional[yandex.cloud.serverless.containers.v1.container_pb2.Args] = ...,
        environment: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        working_dir: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args",b"args","command",b"command"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","command",b"command","environment",b"environment","image_url",b"image_url","working_dir",b"working_dir"]) -> None: ...
global___ImageSpec = ImageSpec

class DeployContainerRevisionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_REVISION_ID_FIELD_NUMBER: builtins.int
    container_revision_id: typing.Text
    def __init__(self,
        *,
        container_revision_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_revision_id",b"container_revision_id"]) -> None: ...
global___DeployContainerRevisionMetadata = DeployContainerRevisionMetadata

class RollbackContainerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    REVISION_ID_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    revision_id: typing.Text
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        revision_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id","revision_id",b"revision_id"]) -> None: ...
global___RollbackContainerRequest = RollbackContainerRequest

class RollbackContainerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    REVISION_ID_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    revision_id: typing.Text
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        revision_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id","revision_id",b"revision_id"]) -> None: ...
global___RollbackContainerMetadata = RollbackContainerMetadata

class ListContainerOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    container_id: typing.Text
    page_size: builtins.int
    page_token: typing.Text
    filter: typing.Text
    def __init__(self,
        *,
        container_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_id",b"container_id","filter",b"filter","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListContainerOperationsRequest = ListContainerOperationsRequest

class ListContainerOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]: ...
    next_page_token: typing.Text
    def __init__(self,
        *,
        operations: typing.Optional[typing.Iterable[yandex.cloud.operation.operation_pb2.Operation]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","operations",b"operations"]) -> None: ...
global___ListContainerOperationsResponse = ListContainerOperationsResponse
