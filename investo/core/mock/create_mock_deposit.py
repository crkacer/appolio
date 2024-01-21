import os
import sys
from datetime import datetime
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
print(parent)
sys.path.append(parent)

from investo.core.deposit import Deposit

def mock_single_deposit(amount, datetime, name):
    return Deposit(
        amount=amount,
        date_time=datetime,
        transaction_name=name,
        transaction_type="Account_Deposit"
    )

def mock_deposits():
    initial_deposit = mock_single_deposit(100_000, datetime=datetime(2022, 1, 1, 0, 0, 0), name="Initial Investment")
    second_deposit = mock_single_deposit(50_000, datetime=datetime(2022, 6, 1, 0, 0, 0), name="Investor Deposit")
    third_deposit = mock_single_deposit(25_000, datetime=datetime(2023, 6, 1, 0, 0, 0), name="Investor Deposit")

    return [initial_deposit, second_deposit, third_deposit]
    