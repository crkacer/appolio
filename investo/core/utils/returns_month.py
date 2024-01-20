from datetime import date

def calculated_monthly_return_compound(start_amount, start_day, start_month, start_year, cal_day, cal_month, cal_year, interest_rate):
    """
    Calculate the monthly returns for the given account
    """
    start_date = date(start_year, start_month, start_day)
    cal_date = date(cal_year, cal_month, cal_day)
    total_diff_days = (cal_date - start_date).days
    
    current_year_th = total_diff_days // 365
    prev_year_diff = current_year_th - 1 if current_year_th > 0 else 0
    
    current_balance = start_amount * pow((1 + interest_rate), current_year_th)
    prev_balance = start_amount * pow((1 + interest_rate), prev_year_diff)

    if (cal_month == 3 and start_month <= 3) or \
        (cal_month == 6 and 3 < start_month <= 6) or \
            (cal_month == 9 and 6 < start_month <= 9) or \
                (cal_month == 12 and 9 < start_month <= 12):
        
        if cal_month == 3:
            cal_prev_date = date(cal_year - 1, 12, 31)
        elif cal_month == 6:
            cal_prev_date = date(cal_year, 3, 31)
        elif cal_month == 9:
            cal_prev_date = date(cal_year, 6, 30)
        elif cal_month == 12:
            cal_prev_date = date(cal_year, 9, 30)
            
        cal_diff_days = (cal_date - date(cal_year, start_month, start_day)).days + 1 
        cal_diff_old_days = (date(cal_year, start_month, start_day) - cal_prev_date).days + 1
        
        returns_old_amount = prev_balance * (interest_rate * cal_diff_old_days / 365)
        returns_new_amount = current_balance * (interest_rate * cal_diff_days / 365)
        if current_year_th > 0:
            returns_amount = returns_new_amount + returns_old_amount
        else:
            returns_amount = returns_new_amount
    else:
        cal_diff_days = 365 / 4
        returns_amount = current_balance * (interest_rate/4)
        
    return {
        "returns_amount": int(round(returns_amount)),
        "cal_diff_days": cal_diff_days,
        "principal": int(round(current_balance)),
        "cal_month": cal_month,
        "cal_year": cal_year,
        "start_month": start_month
    }


def calculated_monthly_return_non_compound(start_amount, start_day, start_month, start_year, cal_day, cal_month, cal_year, interest_rate):
    """
    Calculate the monthly returns for the given account
    """
    
    start_date = date(start_year, start_month, start_day)
    cal_date = date(cal_year, cal_month, cal_day)
    total_diff_days = (cal_date - start_date).days
    
    current_year_th = total_diff_days // 365
    
    if ((cal_month == 3 and start_month <= 3) or \
        (cal_month == 6 and 3 < start_month <= 6) or \
            (cal_month == 9 and 6 < start_month <= 9) or \
                (cal_month == 12 and 9 < start_month <= 12)) and \
                    current_year_th == 0:
            
        cal_diff_days = (cal_date - date(cal_year, start_month, start_day)).days + 1
        
        returns_amount = start_amount * (interest_rate * cal_diff_days / 365)
    else:
        cal_diff_days = 365 / 4
        returns_amount = start_amount * (interest_rate/4)
        
    return {
        "returns_amount": int(round(returns_amount)),
        "cal_diff_days": cal_diff_days,
        "principal": int(round(start_amount))
    }

