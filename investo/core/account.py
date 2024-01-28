from investo.core.deposit import Deposit
from investo.core.withdraw import Withdraw
from investo.core.constants.report_constants import REPORT_INTERVAL, REPORT_UNIT
from investo.core.generator.report_generator import ReportGenerator
from investo.core.generator.chart_generator import ChartGenerator
from investo.core.generator.returns_generator import ReturnsGenerator
from datetime import datetime, date

class Account:

    def __init__(self,
                 compound: bool,
                 report_interval: REPORT_INTERVAL,
                 report_unit: REPORT_UNIT,
                 interest_rate,
                 deposits: [Deposit],
                 withdraws: [Withdraw]
                 ) -> None:
        self._compound = compound
        self._report_interval = report_interval
        self._interest_rate = interest_rate
        self._deposit_transactions = deposits
        self._withdraw_transactions = withdraws
        self._report_unit = report_unit
        # Set generators
        self._returns_generator = ReturnsGenerator(compound=compound, report_interval=report_interval,
                                                   report_unit=report_unit, deposits=deposits,
                                                   withdraws=withdraws, interest_rate=interest_rate)
        self._chart_generator = ChartGenerator(compound=compound, report_interval=report_interval,
                                               report_unit=report_unit, deposits=deposits,
                                               withdraws=withdraws, interest_rate=interest_rate)
        self._report_generator = ReportGenerator(compound=compound, report_interval=report_interval,
                                                 report_unit=report_unit, deposits=deposits,
                                                 withdraws=withdraws, interest_rate=interest_rate)

    def returns_data(self, calc_date=datetime.now()):
        return self._returns_generator.generate_historical_data(calc_date)

    def chart_data(self):
        return self._chart_generator.generate()

    def report_data(self):
        return self._report_generator.generate()
