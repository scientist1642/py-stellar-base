from stellar_sdk.call_builder import OperationsCallBuilder
from tests.call_builder import horizon_url, client


class TestOperationsCallBuilder:
    def test_init(self):
        builder = OperationsCallBuilder(horizon_url, client)
        assert builder.endpoint == "operations"
        assert builder.params == {}

    def test_operation(self):
        operation_id = 2243214
        builder = OperationsCallBuilder(horizon_url, client).operation(operation_id)
        assert builder.endpoint == "operations/{operation}".format(
            operation=operation_id
        )
        assert builder.params == {}

    def test_for_account(self):
        account_id = "GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH"
        builder = OperationsCallBuilder(horizon_url, client).for_account(account_id)
        assert builder.endpoint == "accounts/{account_id}/operations".format(
            account_id=account_id
        )
        assert builder.params == {}

    def test_for_ledger(self):
        ledger = 123456
        builder = OperationsCallBuilder(horizon_url, client).for_ledger(ledger)
        assert builder.endpoint == "ledgers/{ledger}/operations".format(ledger=ledger)
        assert builder.params == {}

    def test_for_transaction(self):
        transaction_hash = (
            "3389e9f0f1a65f19736cacf544c2e825313e8447f569233bb8db39aa607c8889"
        )
        builder = OperationsCallBuilder(horizon_url, client).for_transaction(
            transaction_hash
        )
        assert builder.endpoint == "transactions/{transaction}/operations".format(
            transaction=transaction_hash
        )
        assert builder.params == {}

    def test_include_failed(self):
        account_id = "GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH"
        builder = (
            OperationsCallBuilder(horizon_url, client)
            .for_account(account_id)
            .include_failed(True)
        )
        assert builder.endpoint == "accounts/{account_id}/operations".format(
            account_id=account_id
        )
        assert builder.params == {"include_failed": "true"}

    def test_not_include_failed(self):
        account_id = "GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH"
        builder = (
            OperationsCallBuilder(horizon_url, client)
            .for_account(account_id)
            .include_failed(False)
        )
        assert builder.endpoint == "accounts/{account_id}/operations".format(
            account_id=account_id
        )
        assert builder.params == {"include_failed": "false"}
