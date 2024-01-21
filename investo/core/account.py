from deposit import Deposit
from withdraw import Withdraw
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
                 withdraws: [Withdraw],
                 returns_generator: ReturnsGenerator,
                 chart_generator: ChartGenerator,
                 report_generator: ReportGenerator
                 ) -> None:
        self._compound = compound
        self._report_interval = report_interval
        self._interest_rate = interest_rate
        self._deposit_transactions = deposits
        self._withdraw_transactions = withdraws
        self._returns_generator = returns_generator(compound, report_interval, deposits, withdraws, interest_rate)
        self._chart_generator = chart_generator(compound, report_interval, deposits, withdraws, interest_rate)
        self._report_generator = report_generator(compound, report_interval, deposits, withdraws, interest_rate)

    def calculate_returns(self):
        returns = self._returns_generator.generate()
        return returns

    def chart_data(self):
        pass

    def account_report(self):
        pass
