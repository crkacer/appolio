import os
import sys
from datetime import datetime
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
print(parent)
sys.path.append(parent)

from core.withdraw import Withdraw

def mock_single_withdraw(amount, datetime, name):
    return Withdraw(
        amount=amount,
        date_time=datetime,
        transaction_name=name,
        transaction_type="Account_Withdraw"
    )

def mock_withdraws():
    first_withdraw = mock_single_withdraw(50_000, datetime=datetime(2022, 6, 1, 0, 0, 0), name="Investor Withdraw")
    second_withdraw = mock_single_withdraw(25_000, datetime=datetime(2023, 6, 1, 0, 0, 0), name="Investor Withdraw")

    return [first_withdraw, second_withdraw]
    