import os
import sys
from core.constants.interval import REPORT_INTERVAL
from core.deposit import Deposit
from core.withdraw import Withdraw
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from core.utils.returns_quarter import calculated_quarterly_return_compound, calculated_quarterly_return_non_compound
from core.utils.returns_month import calculated_monthly_return_compound, calculated_monthly_return_non_compound
from .generator import Generator

class ReturnsGenerator(Generator):

    def __init__(self, compound: bool, report_interval: REPORT_INTERVAL, deposits: Deposit, withdraws: Withdraw, interest_rate: float) -> None:
        super().__init__(compound, report_interval, deposits, withdraws, interest_rate)
        
        self._generator = self._set_generator(compound=compound, report_interval=report_interval)

    def _set_generator(self, compound, report_interval):
        if report_interval == "quarterly":
            if compound:
                return calculated_quarterly_return_compound
            else:
                return calculated_quarterly_return_non_compound
        elif report_interval == "monthly":
            if compound:
                return calculated_monthly_return_compound
            else:
                return calculated_monthly_return_non_compound