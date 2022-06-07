"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _BudgetStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _BudgetStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BudgetStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    BUDGET_STATUS_UNSPECIFIED: _BudgetStatus.ValueType  # 0
    CREATING: _BudgetStatus.ValueType  # 1
    """The budget is being created."""

    ACTIVE: _BudgetStatus.ValueType  # 2
    """The budget is active."""

    FINISHED: _BudgetStatus.ValueType  # 3
    """The budget is finished."""

class BudgetStatus(_BudgetStatus, metaclass=_BudgetStatusEnumTypeWrapper):
    pass

BUDGET_STATUS_UNSPECIFIED: BudgetStatus.ValueType  # 0
CREATING: BudgetStatus.ValueType  # 1
"""The budget is being created."""

ACTIVE: BudgetStatus.ValueType  # 2
"""The budget is active."""

FINISHED: BudgetStatus.ValueType  # 3
"""The budget is finished."""

global___BudgetStatus = BudgetStatus


class _ResetPeriodType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ResetPeriodTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ResetPeriodType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESET_PERIOD_TYPE_UNSPECIFIED: _ResetPeriodType.ValueType  # 0
    MONTHLY: _ResetPeriodType.ValueType  # 1
    """Reset budget every month."""

    QUARTER: _ResetPeriodType.ValueType  # 2
    """Reset budget every quarter."""

    ANNUALLY: _ResetPeriodType.ValueType  # 3
    """Reset budget every year."""

class ResetPeriodType(_ResetPeriodType, metaclass=_ResetPeriodTypeEnumTypeWrapper):
    pass

RESET_PERIOD_TYPE_UNSPECIFIED: ResetPeriodType.ValueType  # 0
MONTHLY: ResetPeriodType.ValueType  # 1
"""Reset budget every month."""

QUARTER: ResetPeriodType.ValueType  # 2
"""Reset budget every quarter."""

ANNUALLY: ResetPeriodType.ValueType  # 3
"""Reset budget every year."""

global___ResetPeriodType = ResetPeriodType


class _ThresholdType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ThresholdTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ThresholdType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    THRESHOLD_TYPE_UNSPECIFIED: _ThresholdType.ValueType  # 0
    PERCENT: _ThresholdType.ValueType  # 1
    """Percent."""

    AMOUNT: _ThresholdType.ValueType  # 2
    """The same as budget amount."""

class ThresholdType(_ThresholdType, metaclass=_ThresholdTypeEnumTypeWrapper):
    """Define the unit of the [ThesholdRule.amount]."""
    pass

THRESHOLD_TYPE_UNSPECIFIED: ThresholdType.ValueType  # 0
PERCENT: ThresholdType.ValueType  # 1
"""Percent."""

AMOUNT: ThresholdType.ValueType  # 2
"""The same as budget amount."""

global___ThresholdType = ThresholdType


class Budget(google.protobuf.message.Message):
    """A Budget resource. For more information, see [/docs/billing/concepts/budget]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    COST_BUDGET_FIELD_NUMBER: builtins.int
    EXPENSE_BUDGET_FIELD_NUMBER: builtins.int
    BALANCE_BUDGET_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the budget."""

    name: typing.Text
    """Name of the budget."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""
        pass
    billing_account_id: typing.Text
    """ID of the billing account that the budget belongs to."""

    status: global___BudgetStatus.ValueType
    """Status of the budget."""

    @property
    def cost_budget(self) -> global___CostBudgetSpec:
        """Cost budget specification."""
        pass
    @property
    def expense_budget(self) -> global___ExpenseBudgetSpec:
        """Expense budget specification."""
        pass
    @property
    def balance_budget(self) -> global___BalanceBudgetSpec:
        """Balance budget specification."""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        name: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        billing_account_id: typing.Text = ...,
        status: global___BudgetStatus.ValueType = ...,
        cost_budget: typing.Optional[global___CostBudgetSpec] = ...,
        expense_budget: typing.Optional[global___ExpenseBudgetSpec] = ...,
        balance_budget: typing.Optional[global___BalanceBudgetSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["balance_budget",b"balance_budget","budget_spec",b"budget_spec","cost_budget",b"cost_budget","created_at",b"created_at","expense_budget",b"expense_budget"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["balance_budget",b"balance_budget","billing_account_id",b"billing_account_id","budget_spec",b"budget_spec","cost_budget",b"cost_budget","created_at",b"created_at","expense_budget",b"expense_budget","id",b"id","name",b"name","status",b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["budget_spec",b"budget_spec"]) -> typing.Optional[typing_extensions.Literal["cost_budget","expense_budget","balance_budget"]]: ...
global___Budget = Budget

class CostBudgetSpec(google.protobuf.message.Message):
    """Cost budget specification describes budget that can be used to control cost of cloud resources usage."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    AMOUNT_FIELD_NUMBER: builtins.int
    NOTIFICATION_USER_ACCOUNT_IDS_FIELD_NUMBER: builtins.int
    THRESHOLD_RULES_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    RESET_PERIOD_FIELD_NUMBER: builtins.int
    START_DATE_FIELD_NUMBER: builtins.int
    END_DATE_FIELD_NUMBER: builtins.int
    amount: typing.Text
    """Max cost threshold of the budget. Amount currency is the same as corresponding [yandex.cloud.billing.v1.BillingAccount.currency]."""

    @property
    def notification_user_account_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of the [yandex.cloud.iam.v1.UserAccount].
        Specified users will be be notified if the budget exceeds.
        """
        pass
    @property
    def threshold_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThresholdRule]:
        """List of the [ThresholdRule].
        Rules define intermediate cost thresholds of the budget.
        """
        pass
    @property
    def filter(self) -> global___ConsumptionFilter:
        """Filter that can be used for specific resources selection. Only consumption cost of selected resources are used for the budget calculation."""
        pass
    reset_period: global___ResetPeriodType.ValueType
    """Periodic start type that resets budget after specified period is finished.
    First time budget is calculated in the current period, i.e. current month, quarter or year.
    """

    start_date: typing.Text
    """Custom start date of the budget.
    Must be the first day of a month and must be formatted like YYYY-MM-DD.
    """

    end_date: typing.Text
    """End date of the budget.
    Must be the last day of a month and must be formatted like YYYY-MM-DD.
    """

    def __init__(self,
        *,
        amount: typing.Text = ...,
        notification_user_account_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        threshold_rules: typing.Optional[typing.Iterable[global___ThresholdRule]] = ...,
        filter: typing.Optional[global___ConsumptionFilter] = ...,
        reset_period: global___ResetPeriodType.ValueType = ...,
        start_date: typing.Text = ...,
        end_date: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter",b"filter","reset_period",b"reset_period","start_date",b"start_date","start_type",b"start_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount",b"amount","end_date",b"end_date","filter",b"filter","notification_user_account_ids",b"notification_user_account_ids","reset_period",b"reset_period","start_date",b"start_date","start_type",b"start_type","threshold_rules",b"threshold_rules"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["start_type",b"start_type"]) -> typing.Optional[typing_extensions.Literal["reset_period","start_date"]]: ...
global___CostBudgetSpec = CostBudgetSpec

class ExpenseBudgetSpec(google.protobuf.message.Message):
    """Expense budget specification describes budget that can be used to control expense of cloud resources usage."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    AMOUNT_FIELD_NUMBER: builtins.int
    NOTIFICATION_USER_ACCOUNT_IDS_FIELD_NUMBER: builtins.int
    THRESHOLD_RULES_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    RESET_PERIOD_FIELD_NUMBER: builtins.int
    START_DATE_FIELD_NUMBER: builtins.int
    END_DATE_FIELD_NUMBER: builtins.int
    amount: typing.Text
    """Max expense threshold of the budget. Amount currency is the same as corresponding [yandex.cloud.billing.v1.BillingAccount.currency]."""

    @property
    def notification_user_account_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of the [yandex.cloud.iam.v1.UserAccount].
        Specified users will be be notified if the budget exceeds.
        """
        pass
    @property
    def threshold_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThresholdRule]:
        """List of the [ThresholdRule].
        Rules define intermediate expense thresholds of the budget.
        """
        pass
    @property
    def filter(self) -> global___ConsumptionFilter:
        """Filter that can be used for specific resources selection. Only consumption expense of selected resources are used for the budget calculation."""
        pass
    reset_period: global___ResetPeriodType.ValueType
    """Periodic start type that resets budget after specified period is finished.
    First time budget is calculated in the current period, i.e. current month, quarter or year.
    """

    start_date: typing.Text
    """Custom start date of the budget.
    Must be the first day of a month and must be formatted like YYYY-MM-DD.
    """

    end_date: typing.Text
    """End date of the budget.
    Must be the last day of a month and must be formatted like YYYY-MM-DD.
    """

    def __init__(self,
        *,
        amount: typing.Text = ...,
        notification_user_account_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        threshold_rules: typing.Optional[typing.Iterable[global___ThresholdRule]] = ...,
        filter: typing.Optional[global___ConsumptionFilter] = ...,
        reset_period: global___ResetPeriodType.ValueType = ...,
        start_date: typing.Text = ...,
        end_date: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter",b"filter","reset_period",b"reset_period","start_date",b"start_date","start_type",b"start_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount",b"amount","end_date",b"end_date","filter",b"filter","notification_user_account_ids",b"notification_user_account_ids","reset_period",b"reset_period","start_date",b"start_date","start_type",b"start_type","threshold_rules",b"threshold_rules"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["start_type",b"start_type"]) -> typing.Optional[typing_extensions.Literal["reset_period","start_date"]]: ...
global___ExpenseBudgetSpec = ExpenseBudgetSpec

class BalanceBudgetSpec(google.protobuf.message.Message):
    """Balance budget specification describes budget that can be used to control [yandex.cloud.billing.v1.BillingAccount.balance]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    AMOUNT_FIELD_NUMBER: builtins.int
    NOTIFICATION_USER_ACCOUNT_IDS_FIELD_NUMBER: builtins.int
    THRESHOLD_RULES_FIELD_NUMBER: builtins.int
    START_DATE_FIELD_NUMBER: builtins.int
    END_DATE_FIELD_NUMBER: builtins.int
    amount: typing.Text
    """Max balance threshold of the budget. Amount currency is the same as corresponding [yandex.cloud.billing.v1.BillingAccount.currency]."""

    @property
    def notification_user_account_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of the [yandex.cloud.iam.v1.UserAccount].
        Specified users will be be notified if the budget exceeds.
        """
        pass
    @property
    def threshold_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThresholdRule]:
        """List of the [ThresholdRule].
        Rules define intermediate balance thresholds of the budget.
        """
        pass
    start_date: typing.Text
    """Start_date of the budget.
    Must be the first day of a month and must be formatted like YYYY-MM-DD.
    """

    end_date: typing.Text
    """End date of the budget.
    Must be the last day of a month and must be formatted like YYYY-MM-DD.
    """

    def __init__(self,
        *,
        amount: typing.Text = ...,
        notification_user_account_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        threshold_rules: typing.Optional[typing.Iterable[global___ThresholdRule]] = ...,
        start_date: typing.Text = ...,
        end_date: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount",b"amount","end_date",b"end_date","notification_user_account_ids",b"notification_user_account_ids","start_date",b"start_date","threshold_rules",b"threshold_rules"]) -> None: ...
global___BalanceBudgetSpec = BalanceBudgetSpec

class ConsumptionFilter(google.protobuf.message.Message):
    """Filter that can be used for specific resources selection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVICE_IDS_FIELD_NUMBER: builtins.int
    CLOUD_FOLDERS_FILTERS_FIELD_NUMBER: builtins.int
    @property
    def service_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of the [yandex.cloud.billing.v1.Service].
        Only consumption of resources corresponding to the given services is used for the budget calculation.
        Empty sequence means no services filters.
        """
        pass
    @property
    def cloud_folders_filters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CloudFoldersConsumptionFilter]:
        """Cloud and folders consumption filter.
        Only consumption within specified clouds and folders is used for the budget calculation.
        Empty sequence means no cloud and folders filters.
        """
        pass
    def __init__(self,
        *,
        service_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        cloud_folders_filters: typing.Optional[typing.Iterable[global___CloudFoldersConsumptionFilter]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_folders_filters",b"cloud_folders_filters","service_ids",b"service_ids"]) -> None: ...
global___ConsumptionFilter = ConsumptionFilter

class CloudFoldersConsumptionFilter(google.protobuf.message.Message):
    """Filter that can be used for specific cloud and its folders selection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLOUD_ID_FIELD_NUMBER: builtins.int
    FOLDER_IDS_FIELD_NUMBER: builtins.int
    cloud_id: typing.Text
    """ID of the [yandex.cloud.resourcemanager.v1.Cloud].
    Only consumption within specified cloud is used for the budget calculation.
    """

    @property
    def folder_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of the [yandex.cloud.resourcemanager.v1.Folder].
        Only consumption within specified folders of the given cloud is used for the budget calculation.
        Empty sequence means no folders filters and the whole cloud consumption will be used.
        """
        pass
    def __init__(self,
        *,
        cloud_id: typing.Text = ...,
        folder_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_id",b"cloud_id","folder_ids",b"folder_ids"]) -> None: ...
global___CloudFoldersConsumptionFilter = CloudFoldersConsumptionFilter

class ThresholdRule(google.protobuf.message.Message):
    """Rules that define intermediate cost thresholds of the budget."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    NOTIFICATION_USER_ACCOUNT_IDS_FIELD_NUMBER: builtins.int
    type: global___ThresholdType.ValueType
    """Type of the rule."""

    amount: typing.Text
    """Amount of the rule.
     * Must be less than 100 if type is PERCENT.
     * Must be less than budget's amount if type is AMOUNT.
    """

    @property
    def notification_user_account_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """IDs of the [yandex.cloud.iam.v1.UserAccount].
        Specified users will be be notified if the threshold exceeds.
        """
        pass
    def __init__(self,
        *,
        type: global___ThresholdType.ValueType = ...,
        amount: typing.Text = ...,
        notification_user_account_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount",b"amount","notification_user_account_ids",b"notification_user_account_ids","type",b"type"]) -> None: ...
global___ThresholdRule = ThresholdRule