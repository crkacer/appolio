import os
import sys
from investo.core.constants.interval import REPORT_INTERVAL
from investo.core.deposit import Deposit
from investo.core.withdraw import Withdraw

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from investo.core.utils.returns_quarter import calculated_quarterly_return_compound, \
    calculated_quarterly_return_non_compound
from investo.core.utils.returns_month import calculated_monthly_return_compound, calculated_monthly_return_non_compound
from .generator import Generator


class ReturnsGenerator(Generator):

    def __init__(self, compound: bool, report_interval: REPORT_INTERVAL, deposits: Deposit, withdraws: Withdraw,
                 interest_rate: float) -> None:
        super().__init__(compound, report_interval, deposits, withdraws, interest_rate)

        self._generator = self._set_generator(compound=compound, report_interval=report_interval)

    @staticmethod
    def _set_generator(compound, report_interval):
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

    def generate(self):
        initial_investment = super().get_deposit().filter(transaction_name="Initial Investment").first()

        initial_investment_calc = self._generator(
            start_amount=initial_investment.amount,
            start_day=1,
            start_month=1,
            start_year=2022,
            cal_day=30,
            cal_month=6,
            cal_year=2024,
            interest_rate=super().get_interest_rate()
        )

        return initial_investment_calc
