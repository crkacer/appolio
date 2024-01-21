import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from investo.core.constants.interval import REPORT_INTERVAL
from investo.core.deposit import Deposit
from investo.core.withdraw import Withdraw

class Generator:

    def __init__(self, 
        compound: bool, 
        report_interval: REPORT_INTERVAL,
        deposits: Deposit,
        withdraws: Withdraw,
        interest_rate: float) -> None:

        self._compound = compound
        self._report_interval = report_interval
        self._deposits = deposits
        self._withdraws = withdraws
        self._interest_rate = interest_rate
