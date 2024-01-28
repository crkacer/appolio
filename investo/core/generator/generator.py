import os
import sys
from datetime import datetime, date

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from investo.core.constants.report_constants import REPORT_INTERVAL, REPORT_UNIT
from investo.core.deposit import Deposit
from investo.core.withdraw import Withdraw


class Generator:

    def __init__(self,
                 compound: bool,
                 report_interval: REPORT_INTERVAL,
                 report_unit: REPORT_UNIT,
                 deposits: Deposit,
                 withdraws: Withdraw,
                 interest_rate: float) -> None:
        self._compound = compound
        self._report_interval = report_interval
        self._report_unit = report_unit
        self._deposits = deposits
        self._withdraws = withdraws
        self._interest_rate = interest_rate

    def get_deposit(self):
        return self._deposits

    def get_withdraw(self):
        return self._withdraws

    def get_interest_rate(self):
        return self._interest_rate

    def get_report_interval(self):
        return self._report_interval

    def get_report_unit(self):
        return self._report_unit
