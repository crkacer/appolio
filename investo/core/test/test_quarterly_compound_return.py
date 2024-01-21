import unittest
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from investo.core.utils.returns_quarter import calculated_quarterly_return_compound

class TestQuarterlyCompoundReturn(unittest.TestCase):

    def test_returns_within_first_year(self):
        start_amount = 100_000
        start_day, start_month, start_year = 1, 1, 2022
        cal_day, cal_month, cal_year = 1, 6, 2022
        interest_rate = 0.09
        
        returns = calculated_quarterly_return_compound(start_amount, start_day, start_month, start_year, cal_day, cal_month, cal_year, interest_rate)
        
        
        self.assertEqual({
            'returns_amount': 2244, 
            'cal_diff_days': 91, 
            'principal': 100000, 
            'cal_month': 6, 
            'start_month': 1
        }, returns)


    def test_more_than_a_year(self):
        start_amount = 100_000
        start_day, start_month, start_year = 1, 1, 2022
        cal_day, cal_month, cal_year = 1, 6, 2023
        interest_rate = 0.09
        
        returns = calculated_quarterly_return_compound(start_amount, start_day, start_month, start_year, cal_day, cal_month, cal_year, interest_rate)
        
        print(returns)
        self.assertEqual({
            'returns_amount': 2446, 
            'cal_diff_days': 91, 
            'principal': 109000, 
            'cal_month': 6, 
            'start_month': 1
        }, returns)


if __name__ == "__main__":
    unittest.main()
