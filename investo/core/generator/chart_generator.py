from investo.core.constants.interval import REPORT_INTERVAL
from investo.core.deposit import Deposit
from investo.core.withdraw import Withdraw
from investo.core.generator.generator import Generator

class ChartGenerator(Generator):

    def __init__(self, compound: bool, report_interval: REPORT_INTERVAL, deposits: Deposit, withdraws: Withdraw, interest_rate: float) -> None:
        super().__init__(compound, report_interval, deposits, withdraws, interest_rate)

    def generate(self):
        pass