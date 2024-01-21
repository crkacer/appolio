import unittest
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
print(parent)
sys.path.append(parent)

from investo.core.deposit import Deposit
from investo.core.mock.create_mock_deposit import mock_deposits
from datetime import datetime

class TestCreateDeposit(unittest.TestCase):

    def create_deposit(self):
        
        new_deposit = Deposit(
            amount=50_000, 
            date_time=datetime(2022, 1, 1, 0, 0, 0),
            transaction_name="Initial Investment",
            transaction_type="Account_Deposit"
        )
        self.assertEqual(new_deposit, new_deposit)


    def create_deposits(self):
        new_deposits = mock_deposits()
        self.assertEqual(new_deposits, new_deposits)

if __name__ == "__main__":
    test = TestCreateDeposit().create_deposit()
    print(test)