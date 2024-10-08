from datetime import date
import logging


def calculated_quarterly_return_compound_unit_day(start_amount, start_day, start_month, start_year, cal_day, cal_month,
                                                  cal_year,
                                                  interest_rate):
    """
    Calculate the quarterly returns for the given account

    Params: start_amount, start_day, start_month, start_year, cal_day, cal_month, cal_year, interest_rate 
    Returns: { returns_amount, cal_diff_days, principal, cal_month, start_month }
    Required: cal_month has to be 3, 6, 9 or 12.

    """
    if cal_month not in [3, 6, 9, 12]:
        raise Exception("Calc Quarter Month must be 3, 6, 9 or 12.")

    logger = logging.getLogger("django")

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
        # cal_diff_days = 91.25
        if cal_month == 3:
            cal_diff_days = 90  # 31 + 28 + 31
        elif cal_month == 6:
            cal_diff_days = 91  # 30 + 31 + 30
        elif cal_month == 9:
            cal_diff_days = 92  # 30 + 31 + 31
        elif cal_month == 12:
            cal_diff_days = 92  # 30 + 31 + 31
        returns_amount = current_balance * (interest_rate * cal_diff_days / 365)

    return {
        "returns_amount": int(round(returns_amount)),
        "cal_diff_days": cal_diff_days,
        "principal": int(round(current_balance)),
        "cal_month": cal_month,
        "start_month": start_month
    }


def calculated_quarterly_return_compound_unit_month(start_amount, start_day, start_month, start_year, cal_day,
                                                    cal_month, cal_year,
                                                    interest_rate):
    """
    Calculate the quarterly returns for the given account

    Params: start_amount, start_day, start_month, start_year, cal_day, cal_month, cal_year, interest_rate
    Returns: { returns_amount, cal_diff_days, principal, cal_month, start_month }
    Required: cal_month has to be 3, 6, 9 or 12.

    """

    if cal_month not in [3, 6, 9, 12]:
        raise Exception("Calc Quarter Month must be 3, 6, 9 or 12.")

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
        cal_diff_half_month = round(cal_diff_days / 15)
        cal_diff_old_days = (date(cal_year, start_month, start_day) - cal_prev_date).days + 1
        cal_diff_old_half_month = round(cal_diff_old_days / 15)

        returns_old_amount = prev_balance * (interest_rate / 12) * (cal_diff_half_month / 2)
        returns_new_amount = current_balance * (interest_rate / 12) * (cal_diff_old_half_month / 2)
        if current_year_th > 0:
            returns_amount = returns_new_amount + returns_old_amount
        else:
            returns_amount = returns_new_amount
    else:
        cal_diff_days = 90
        returns_amount = current_balance * (interest_rate * 0.25)  # 1/4 year

    return {
        "returns_amount": int(round(returns_amount)),
        "cal_diff_days": cal_diff_days,
        "principal": int(round(current_balance)),
        "cal_month": cal_month,
        "start_month": start_month
    }


def calculated_quarterly_return_non_compound_unit_day(start_amount, start_day, start_month, start_year, cal_day,
                                                      cal_month,
                                                      cal_year, interest_rate):
    """
    Calculate the quarterly returns for the given account
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
        # cal_diff_days = 91.25
        if cal_month == 3:
            cal_diff_days = 90  # 31 + 28 + 31
        elif cal_month == 6:
            cal_diff_days = 91  # 30 + 31 + 30
        elif cal_month == 9:
            cal_diff_days = 92  # 30 + 31 + 31
        elif cal_month == 12:
            cal_diff_days = 92  # 30 + 31 + 31
        returns_amount = start_amount * (interest_rate * cal_diff_days / 365)

    return {
        "returns_amount": int(round(returns_amount)),
        "cal_diff_days": cal_diff_days,
        "principal": int(round(start_amount))
    }


def calculated_quarterly_return_non_compound_unit_month(start_amount, start_day, start_month, start_year, cal_day,
                                                        cal_month, cal_year, interest_rate):
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
        cal_diff_half_month = round(cal_diff_days / 15)
        returns_amount = start_amount * (interest_rate / 12) * (cal_diff_half_month / 2)
    else:
        cal_diff_days = 90
        returns_amount = start_amount * (interest_rate * 0.25)  # 1/4 year

    return {
        "returns_amount": int(round(returns_amount)),
        "cal_diff_days": cal_diff_days,
        "principal": int(round(start_amount))
    }
