from datetime import date, datetime


def convert_date_time(db_datetime):
    # Sample value 2024-01-20 17:08:00.685966
    datetime_format = "%Y-%m-%d %H:%M:%S.%f"
    datetime_obj = datetime.strptime(db_datetime, datetime_format)
    return datetime_obj


def prev_date(current_year, current_month):
    prev_d, prev_m, prev_y = 0, 0, 0
    if current_month == 3:
        prev_d, prev_m, prev_y = 31, 12, current_year - 1
    elif current_month == 6:
        prev_d, prev_m, prev_y = 31, 3, current_year
    elif current_month == 9:
        prev_d, prev_m, prev_y = 30, 6, current_year
    elif current_month == 12:
        prev_d, prev_m, prev_y = 30, 9, current_year
    elif current_month == 1:
        prev_d, prev_m, prev_y = 31, 12, current_year - 1
    elif current_month == 2:
        prev_d, prev_m, prev_y = 30, 1, current_year
    elif current_month == 4:
        prev_d, prev_m, prev_y = 31, 3, current_year

    elif current_month == 5:
        prev_d, prev_m, prev_y = 30, 4, current_year

    elif current_month == 7:
        prev_d, prev_m, prev_y = 30, 6, current_year

    elif current_month == 8:
        prev_d, prev_m, prev_y = 31, 7, current_year

    elif current_month == 10:
        prev_d, prev_m, prev_y = 30, 9, current_year

    elif current_month == 11:
        prev_d, prev_m, prev_y = 31, 10, current_year

    return date(prev_y, prev_m, prev_d)
