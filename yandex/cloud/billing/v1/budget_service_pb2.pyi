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
import yandex.cloud.billing.v1.budget_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetBudgetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """ID of the budget to return.
    To get the budget ID, use [BudgetService.List] request.
    """

    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___GetBudgetRequest = GetBudgetRequest

class ListBudgetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    billing_account_id: typing.Text
    """ID of the billing account to list budgets corresponding to.
    To get the billing account ID, use [BillingAccountService.List] request.
    """

    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListBudgetsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """

    page_token: typing.Text
    """Page token. To get the next page of results,
    set [page_token] to the [ListBudgetsResponse.next_page_token]
    returned by a previous list request.
    """

    def __init__(self,
        *,
        billing_account_id: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["billing_account_id",b"billing_account_id","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListBudgetsRequest = ListBudgetsRequest

class ListBudgetsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BUDGETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def budgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.billing.v1.budget_pb2.Budget]:
        """List of budgets."""
        pass
    next_page_token: typing.Text
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListBudgetsRequest.page_size], use
    [next_page_token] as the value
    for the [ListBudgetsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """

    def __init__(self,
        *,
        budgets: typing.Optional[typing.Iterable[yandex.cloud.billing.v1.budget_pb2.Budget]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["budgets",b"budgets","next_page_token",b"next_page_token"]) -> None: ...
global___ListBudgetsResponse = ListBudgetsResponse

class CreateBudgetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    COST_BUDGET_SPEC_FIELD_NUMBER: builtins.int
    EXPENSE_BUDGET_SPEC_FIELD_NUMBER: builtins.int
    BALANCE_BUDGET_SPEC_FIELD_NUMBER: builtins.int
    billing_account_id: typing.Text
    """ID of the billing account to list budgets corresponding to.
    To get the billing account ID, use [yandex.cloud.billing.v1.BillingAccountService.List] request.
    """

    name: typing.Text
    """Name of the budget."""

    @property
    def cost_budget_spec(self) -> yandex.cloud.billing.v1.budget_pb2.CostBudgetSpec:
        """Cost budget specification."""
        pass
    @property
    def expense_budget_spec(self) -> yandex.cloud.billing.v1.budget_pb2.ExpenseBudgetSpec:
        """Expense budget specification."""
        pass
    @property
    def balance_budget_spec(self) -> yandex.cloud.billing.v1.budget_pb2.BalanceBudgetSpec:
        """Balance budget specification."""
        pass
    def __init__(self,
        *,
        billing_account_id: typing.Text = ...,
        name: typing.Text = ...,
        cost_budget_spec: typing.Optional[yandex.cloud.billing.v1.budget_pb2.CostBudgetSpec] = ...,
        expense_budget_spec: typing.Optional[yandex.cloud.billing.v1.budget_pb2.ExpenseBudgetSpec] = ...,
        balance_budget_spec: typing.Optional[yandex.cloud.billing.v1.budget_pb2.BalanceBudgetSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["balance_budget_spec",b"balance_budget_spec","budget_spec",b"budget_spec","cost_budget_spec",b"cost_budget_spec","expense_budget_spec",b"expense_budget_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["balance_budget_spec",b"balance_budget_spec","billing_account_id",b"billing_account_id","budget_spec",b"budget_spec","cost_budget_spec",b"cost_budget_spec","expense_budget_spec",b"expense_budget_spec","name",b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["budget_spec",b"budget_spec"]) -> typing.Optional[typing_extensions.Literal["cost_budget_spec","expense_budget_spec","balance_budget_spec"]]: ...
global___CreateBudgetRequest = CreateBudgetRequest

class CreateBudgetMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BUDGET_ID_FIELD_NUMBER: builtins.int
    budget_id: typing.Text
    """ID of the budget."""

    def __init__(self,
        *,
        budget_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["budget_id",b"budget_id"]) -> None: ...
global___CreateBudgetMetadata = CreateBudgetMetadata
