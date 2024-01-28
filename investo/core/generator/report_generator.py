from investo.core.constants.report_constants import REPORT_INTERVAL, REPORT_UNIT
from investo.core.deposit import Deposit
from investo.core.withdraw import Withdraw
from investo.core.generator.generator import Generator


class ReportGenerator(Generator):

    def __init__(self, compound: bool, report_interval: REPORT_INTERVAL, report_unit: REPORT_UNIT, deposits: Deposit,
                 withdraws: Withdraw, interest_rate: float) -> None:
        super().__init__(compound, report_interval, report_unit, deposits, withdraws, interest_rate)

    def generate(self):
        pass
