import os
import sys
from investo.core.constants.report_constants import REPORT_INTERVAL, REPORT_UNIT, QUARTERS_MONTH, MONTHS
from investo.core.deposit import Deposit
from investo.core.withdraw import Withdraw
from investo.core.utils.datetime_utils import convert_date_time, prev_date
from datetime import datetime, date

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from investo.core.utils.returns_quarter import calculated_quarterly_return_compound_unit_month, \
    calculated_quarterly_return_non_compound_unit_month, calculated_quarterly_return_compound_unit_day, \
    calculated_quarterly_return_non_compound_unit_day
from investo.core.utils.returns_month import calculated_monthly_return_compound, calculated_monthly_return_non_compound
from .generator import Generator
import calendar


class ReturnsGenerator(Generator):

    def __init__(self, compound: bool, report_interval: REPORT_INTERVAL, report_unit: REPORT_UNIT, deposits: Deposit,
                 withdraws: Withdraw, interest_rate: float) -> None:
        super().__init__(compound, report_interval, report_unit, deposits, withdraws, interest_rate)

        self._generator = self._set_generator(compound=compound,
                                              report_interval=report_interval,
                                              report_unit=report_unit
                                              )
        self._historical_data = []

    @staticmethod
    def _set_generator(compound, report_interval, report_unit):
        if report_interval == "quarterly":
            if compound and report_unit == "month":
                return calculated_quarterly_return_compound_unit_month
            elif compound and report_unit == "day":
                return calculated_quarterly_return_compound_unit_day
            elif not compound and report_unit == "month":
                return calculated_quarterly_return_non_compound_unit_month
            elif not compound and report_unit == "day":
                return calculated_quarterly_return_non_compound_unit_day
        elif report_interval == "monthly":
            if compound and report_unit == "month":
                return calculated_monthly_return_compound
            elif compound and report_unit == "day":
                return calculated_monthly_return_compound
            elif not compound and report_unit == "month":
                return calculated_monthly_return_non_compound
            elif not compound and report_unit == "day":
                return calculated_monthly_return_non_compound

    def generate(self, amount, start_date, calc_date):
        return self._generator(
            start_amount=amount,
            start_day=start_date.day,
            start_month=start_date.month,
            start_year=start_date.year,
            cal_day=calc_date.day,
            cal_month=calc_date.month,
            cal_year=calc_date.year,
            interest_rate=super().get_interest_rate()
        )

    def generate_historical_data(self, calc_date):
        initial_investment = super().get_deposit().filter(transaction_name="Initial Investment").first()
        # initial_investment_datetime = convert_date_time(initial_investment.datetime)
        initial_investment_datetime = initial_investment.datetime

        calc_day, calc_month, calc_year = calc_date.day, calc_date.month, calc_date.year
        start_day, start_month, start_year = initial_investment_datetime.day, initial_investment_datetime.month, \
            initial_investment_datetime.year
        total_returns = 0

        if self.get_report_interval() == "monthly":
            months = MONTHS
        else:
            months = QUARTERS_MONTH

        for year in range(initial_investment_datetime.year, calc_year):
            for month in months:
                quarter_day = calendar.monthrange(year, month)[1]
                if datetime(year, month, quarter_day) < datetime(start_year, start_month, start_day):
                    continue

                else:
                    calculated_returns = self.generate(
                        amount=initial_investment.amount,
                        start_date=initial_investment_datetime,
                        calc_date=date(year=year, month=month, day=quarter_day)
                    )
                    total_returns += calculated_returns.get("returns_amount")
                    self._historical_data.append({
                        "return_date": date(year, month, quarter_day),
                        "prev_date": prev_date(year, month),
                        "returns": calculated_returns,
                        "sum_returns": total_returns
                    })
        return self._historical_data
