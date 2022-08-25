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
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Job(google.protobuf.message.Message):
    """A Data Proc job. For details about the concept, see [documentation](/docs/dataproc/concepts/jobs)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Job._Status.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Job._Status.ValueType  # 0
        PROVISIONING: Job._Status.ValueType  # 1
        """Job is logged in the database and is waiting for the agent to run it."""
        PENDING: Job._Status.ValueType  # 2
        """Job is acquired by the agent and is in the queue for execution."""
        RUNNING: Job._Status.ValueType  # 3
        """Job is being run in the cluster."""
        ERROR: Job._Status.ValueType  # 4
        """Job failed to finish the run properly."""
        DONE: Job._Status.ValueType  # 5
        """Job is finished."""
        CANCELLED: Job._Status.ValueType  # 6
        """Job is cancelled."""
        CANCELLING: Job._Status.ValueType  # 7
        """Job is waiting for cancellation."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Job.Status.ValueType  # 0
    PROVISIONING: Job.Status.ValueType  # 1
    """Job is logged in the database and is waiting for the agent to run it."""
    PENDING: Job.Status.ValueType  # 2
    """Job is acquired by the agent and is in the queue for execution."""
    RUNNING: Job.Status.ValueType  # 3
    """Job is being run in the cluster."""
    ERROR: Job.Status.ValueType  # 4
    """Job failed to finish the run properly."""
    DONE: Job.Status.ValueType  # 5
    """Job is finished."""
    CANCELLED: Job.Status.ValueType  # 6
    """Job is cancelled."""
    CANCELLING: Job.Status.ValueType  # 7
    """Job is waiting for cancellation."""

    ID_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MAPREDUCE_JOB_FIELD_NUMBER: builtins.int
    SPARK_JOB_FIELD_NUMBER: builtins.int
    PYSPARK_JOB_FIELD_NUMBER: builtins.int
    HIVE_JOB_FIELD_NUMBER: builtins.int
    APPLICATION_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the job. Generated at creation time."""
    cluster_id: builtins.str
    """ID of the Data Proc cluster that the job belongs to."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the job was started."""
    @property
    def finished_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the job was finished."""
    name: builtins.str
    """Name of the job, specified in the [JobService.Create] request."""
    created_by: builtins.str
    """The id of the user who created the job"""
    status: global___Job.Status.ValueType
    """Job status."""
    @property
    def mapreduce_job(self) -> global___MapreduceJob:
        """Specification for a MapReduce job."""
    @property
    def spark_job(self) -> global___SparkJob:
        """Specification for a Spark job."""
    @property
    def pyspark_job(self) -> global___PysparkJob:
        """Specification for a PySpark job."""
    @property
    def hive_job(self) -> global___HiveJob:
        """Specification for a Hive job."""
    @property
    def application_info(self) -> global___ApplicationInfo:
        """Attributes of YARN application."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        cluster_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finished_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        created_by: builtins.str = ...,
        status: global___Job.Status.ValueType = ...,
        mapreduce_job: global___MapreduceJob | None = ...,
        spark_job: global___SparkJob | None = ...,
        pyspark_job: global___PysparkJob | None = ...,
        hive_job: global___HiveJob | None = ...,
        application_info: global___ApplicationInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["application_info", b"application_info", "created_at", b"created_at", "finished_at", b"finished_at", "hive_job", b"hive_job", "job_spec", b"job_spec", "mapreduce_job", b"mapreduce_job", "pyspark_job", b"pyspark_job", "spark_job", b"spark_job", "started_at", b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_info", b"application_info", "cluster_id", b"cluster_id", "created_at", b"created_at", "created_by", b"created_by", "finished_at", b"finished_at", "hive_job", b"hive_job", "id", b"id", "job_spec", b"job_spec", "mapreduce_job", b"mapreduce_job", "name", b"name", "pyspark_job", b"pyspark_job", "spark_job", b"spark_job", "started_at", b"started_at", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["job_spec", b"job_spec"]) -> typing_extensions.Literal["mapreduce_job", "spark_job", "pyspark_job", "hive_job"] | None: ...

global___Job = Job

class ApplicationAttempt(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    AM_CONTAINER_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of YARN application attempt"""
    am_container_id: builtins.str
    """ID of YARN Application Master container"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        am_container_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["am_container_id", b"am_container_id", "id", b"id"]) -> None: ...

global___ApplicationAttempt = ApplicationAttempt

class ApplicationInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    APPLICATION_ATTEMPTS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of YARN application"""
    @property
    def application_attempts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApplicationAttempt]:
        """YARN application attempts"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        application_attempts: collections.abc.Iterable[global___ApplicationAttempt] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_attempts", b"application_attempts", "id", b"id"]) -> None: ...

global___ApplicationInfo = ApplicationInfo

class MapreduceJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class PropertiesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ARGS_FIELD_NUMBER: builtins.int
    JAR_FILE_URIS_FIELD_NUMBER: builtins.int
    FILE_URIS_FIELD_NUMBER: builtins.int
    ARCHIVE_URIS_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    MAIN_JAR_FILE_URI_FIELD_NUMBER: builtins.int
    MAIN_CLASS_FIELD_NUMBER: builtins.int
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional arguments to pass to the driver."""
    @property
    def jar_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """JAR file URIs to add to CLASSPATH of the Data Proc driver and each task."""
    @property
    def file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of resource files to be copied to the working directory of Data Proc drivers
        and distributed Hadoop tasks.
        """
    @property
    def archive_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of archives to be extracted to the working directory of Data Proc drivers and tasks."""
    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Property names and values, used to configure Data Proc and MapReduce."""
    main_jar_file_uri: builtins.str
    """HCFS URI of the .jar file containing the driver class."""
    main_class: builtins.str
    """The name of the driver class."""
    def __init__(
        self,
        *,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        jar_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        archive_uris: collections.abc.Iterable[builtins.str] | None = ...,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        main_jar_file_uri: builtins.str = ...,
        main_class: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["driver", b"driver", "main_class", b"main_class", "main_jar_file_uri", b"main_jar_file_uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["archive_uris", b"archive_uris", "args", b"args", "driver", b"driver", "file_uris", b"file_uris", "jar_file_uris", b"jar_file_uris", "main_class", b"main_class", "main_jar_file_uri", b"main_jar_file_uri", "properties", b"properties"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["driver", b"driver"]) -> typing_extensions.Literal["main_jar_file_uri", "main_class"] | None: ...

global___MapreduceJob = MapreduceJob

class SparkJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class PropertiesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ARGS_FIELD_NUMBER: builtins.int
    JAR_FILE_URIS_FIELD_NUMBER: builtins.int
    FILE_URIS_FIELD_NUMBER: builtins.int
    ARCHIVE_URIS_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    MAIN_JAR_FILE_URI_FIELD_NUMBER: builtins.int
    MAIN_CLASS_FIELD_NUMBER: builtins.int
    PACKAGES_FIELD_NUMBER: builtins.int
    REPOSITORIES_FIELD_NUMBER: builtins.int
    EXCLUDE_PACKAGES_FIELD_NUMBER: builtins.int
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional arguments to pass to the driver."""
    @property
    def jar_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """JAR file URIs to add to CLASSPATH of the Data Proc driver and each task."""
    @property
    def file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of resource files to be copied to the working directory of Data Proc drivers
        and distributed Hadoop tasks.
        """
    @property
    def archive_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of archives to be extracted to the working directory of Data Proc drivers and tasks."""
    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Property names and values, used to configure Data Proc and Spark."""
    main_jar_file_uri: builtins.str
    """The HCFS URI of the JAR file containing the `main` class for the job."""
    main_class: builtins.str
    """The name of the driver class."""
    @property
    def packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of maven coordinates of jars to include on the driver and executor classpaths."""
    @property
    def repositories(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of additional remote repositories to search for the maven coordinates given with --packages."""
    @property
    def exclude_packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of groupId:artifactId, to exclude while resolving the dependencies provided in --packages to avoid dependency conflicts."""
    def __init__(
        self,
        *,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        jar_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        archive_uris: collections.abc.Iterable[builtins.str] | None = ...,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        main_jar_file_uri: builtins.str = ...,
        main_class: builtins.str = ...,
        packages: collections.abc.Iterable[builtins.str] | None = ...,
        repositories: collections.abc.Iterable[builtins.str] | None = ...,
        exclude_packages: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["archive_uris", b"archive_uris", "args", b"args", "exclude_packages", b"exclude_packages", "file_uris", b"file_uris", "jar_file_uris", b"jar_file_uris", "main_class", b"main_class", "main_jar_file_uri", b"main_jar_file_uri", "packages", b"packages", "properties", b"properties", "repositories", b"repositories"]) -> None: ...

global___SparkJob = SparkJob

class PysparkJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class PropertiesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ARGS_FIELD_NUMBER: builtins.int
    JAR_FILE_URIS_FIELD_NUMBER: builtins.int
    FILE_URIS_FIELD_NUMBER: builtins.int
    ARCHIVE_URIS_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    MAIN_PYTHON_FILE_URI_FIELD_NUMBER: builtins.int
    PYTHON_FILE_URIS_FIELD_NUMBER: builtins.int
    PACKAGES_FIELD_NUMBER: builtins.int
    REPOSITORIES_FIELD_NUMBER: builtins.int
    EXCLUDE_PACKAGES_FIELD_NUMBER: builtins.int
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional arguments to pass to the driver."""
    @property
    def jar_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """JAR file URIs to add to CLASSPATH of the Data Proc driver and each task."""
    @property
    def file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of resource files to be copied to the working directory of Data Proc drivers
        and distributed Hadoop tasks.
        """
    @property
    def archive_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of archives to be extracted to the working directory of Data Proc drivers and tasks."""
    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Property names and values, used to configure Data Proc and PySpark."""
    main_python_file_uri: builtins.str
    """URI of the file with the driver code. Must be a .py file."""
    @property
    def python_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of Python files to pass to the PySpark framework."""
    @property
    def packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of maven coordinates of jars to include on the driver and executor classpaths."""
    @property
    def repositories(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of additional remote repositories to search for the maven coordinates given with --packages."""
    @property
    def exclude_packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of groupId:artifactId, to exclude while resolving the dependencies provided in --packages to avoid dependency conflicts."""
    def __init__(
        self,
        *,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        jar_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        archive_uris: collections.abc.Iterable[builtins.str] | None = ...,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        main_python_file_uri: builtins.str = ...,
        python_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        packages: collections.abc.Iterable[builtins.str] | None = ...,
        repositories: collections.abc.Iterable[builtins.str] | None = ...,
        exclude_packages: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["archive_uris", b"archive_uris", "args", b"args", "exclude_packages", b"exclude_packages", "file_uris", b"file_uris", "jar_file_uris", b"jar_file_uris", "main_python_file_uri", b"main_python_file_uri", "packages", b"packages", "properties", b"properties", "python_file_uris", b"python_file_uris", "repositories", b"repositories"]) -> None: ...

global___PysparkJob = PysparkJob

class QueryList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERIES_FIELD_NUMBER: builtins.int
    @property
    def queries(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of Hive queries."""
    def __init__(
        self,
        *,
        queries: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["queries", b"queries"]) -> None: ...

global___QueryList = QueryList

class HiveJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class PropertiesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    class ScriptVariablesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    PROPERTIES_FIELD_NUMBER: builtins.int
    CONTINUE_ON_FAILURE_FIELD_NUMBER: builtins.int
    SCRIPT_VARIABLES_FIELD_NUMBER: builtins.int
    JAR_FILE_URIS_FIELD_NUMBER: builtins.int
    QUERY_FILE_URI_FIELD_NUMBER: builtins.int
    QUERY_LIST_FIELD_NUMBER: builtins.int
    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Property names and values, used to configure Data Proc and Hive."""
    continue_on_failure: builtins.bool
    """Flag indicating whether a job should continue to run if a query fails."""
    @property
    def script_variables(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Query variables and their values."""
    @property
    def jar_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """JAR file URIs to add to CLASSPATH of the Hive driver and each task."""
    query_file_uri: builtins.str
    """URI of the script with all the necessary Hive queries."""
    @property
    def query_list(self) -> global___QueryList:
        """List of Hive queries to be used in the job."""
    def __init__(
        self,
        *,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        continue_on_failure: builtins.bool = ...,
        script_variables: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        jar_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        query_file_uri: builtins.str = ...,
        query_list: global___QueryList | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["query_file_uri", b"query_file_uri", "query_list", b"query_list", "query_type", b"query_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["continue_on_failure", b"continue_on_failure", "jar_file_uris", b"jar_file_uris", "properties", b"properties", "query_file_uri", b"query_file_uri", "query_list", b"query_list", "query_type", b"query_type", "script_variables", b"script_variables"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["query_type", b"query_type"]) -> typing_extensions.Literal["query_file_uri", "query_list"] | None: ...

global___HiveJob = HiveJob
