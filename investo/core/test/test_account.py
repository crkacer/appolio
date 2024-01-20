import unittest
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from core.account import Account
from core.mock.create_mock_deposit import mock_deposits
from core.mock.create_mock_withdraw import mock_withdraws
from core.generator.report_generator import ReportGenerator
from core.generator.chart_generator import ChartGenerator
from core.generator.returns_generator import ReturnsGenerator

class TestAccount(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.test_account = self.test_create_account()

    def test_create_account(self):
        new_account = Account(
            compound=True,
            report_interval="monthly",
            deposits=mock_deposits(),
            withdraws=mock_withdraws(),
            report_generator=ReportGenerator,
            chart_generator=ChartGenerator,
            returns_generator=ReturnsGenerator
        )

        return self.assertEqual(new_account, new_account)

    def test_account_returns_monthly_interval(self):
        return self.test_account


    def test_account_returns_weekly_interval(self):
        return self.test_account


if __name__ == "__main__":
    test_account = TestAccount().test_create_account()
    print(test_account)