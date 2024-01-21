from investo.core.deposit import Deposit
from investo.core.withdraw import Withdraw
from investo.core.constants.interval import REPORT_INTERVAL
from investo.core.generator.report_generator import ReportGenerator
from investo.core.generator.chart_generator import ChartGenerator
from investo.core.generator.returns_generator import ReturnsGenerator


class Account:

    def __init__(self,
                 compound: bool,
                 report_interval: REPORT_INTERVAL,
                 interest_rate,
                 deposits: [Deposit],
                 withdraws: [Withdraw]
                 ) -> None:
        self._compound = compound
        self._report_interval = report_interval
        self._interest_rate = interest_rate
        self._deposit_transactions = deposits
        self._withdraw_transactions = withdraws
        # Set generators
        self._returns_generator = ReturnsGenerator(compound, report_interval, deposits, withdraws, interest_rate)
        self._chart_generator = ChartGenerator(compound, report_interval, deposits, withdraws, interest_rate)
        self._report_generator = ReportGenerator(compound, report_interval, deposits, withdraws, interest_rate)

    def returns_data(self):
        returns = self._returns_generator.generate()
        return returns

    def chart_data(self):
        chart_data = self._chart_generator.generate()
        return chart_data

    def report_data(self):
        account_report = self._report_generator.generate()
        return account_report
