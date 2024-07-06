import datetime

import syslog


# task 1
def get_days_from_today(date: str):
    try:
        passed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError as e:
        syslog.syslog(syslog.LOG_ERR, f"Failed to parse date '{str}'\nError: {e}")
        return None  # case when we cannot parce a passed date

    distance = datetime.datetime.today() - passed_date

    return distance.days


# res = get_days_from_today('2024-07-01')
# print(f"result {res}")

