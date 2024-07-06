from datetime import datetime, timedelta, date


def get_upcoming_birthdays():
    users = get_users_list()
    today = date.today()
    result = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        congratulation_date = date(today.year, birthday.month, birthday.day)

        count_days_to_congratulation = (congratulation_date - today).days

        if count_days_to_congratulation < 0 or count_days_to_congratulation > 7:
            continue

        weekday = congratulation_date.weekday()

        if weekday in [5, 6]:
            addDays = 2 if weekday == 5 else 1
            congratulation_date = congratulation_date + timedelta(days=addDays)

        result.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

        # print(f"{birthday}   {congratulation_date}")

    return result


def get_users_list():
    return [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Jane Smith2", "birthday": "1990.07.05"},
        {"name": "Jane Smith2", "birthday": "1990.07.06"},
        {"name": "Jane Smith2", "birthday": "1990.07.07"},
        {"name": "Jane Smith2", "birthday": "1990.07.08"},
        {"name": "Jane Smith2", "birthday": "1990.07.13"},
        {"name": "Jane Smith2", "birthday": "1990.07.14"},
    ]


# print(get_upcoming_birthdays())
