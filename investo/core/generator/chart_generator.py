from core.constants.interval import REPORT_INTERVAL
from core.deposit import Deposit
from core.withdraw import Withdraw
from .generator import Generator

class ChartGenerator(Generator):

    def __init__(self, compound: bool, report_interval: REPORT_INTERVAL, deposits: Deposit, withdraws: Withdraw, interest_rate: float) -> None:
        super().__init__(compound, report_interval, deposits, withdraws, interest_rate)

    def generate():
        pass