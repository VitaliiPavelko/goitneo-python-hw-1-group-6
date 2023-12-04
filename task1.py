from datetime import datetime, timedelta
from collections import defaultdict

CONGRATULATION_WEEKDAYS = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
]

# As far the task conditions aren't clear enough, so I've made some assumptions:
#
# - birthdays are chosen for the current working week, ending on Friday
#   (Saturday and Sunday are not included as those days are moved
#     to next week and should be put to Monday)
#
# - if current day is Saturday or Sunday,
#      then interval contains days from current day to closest Friday
#      (as Saturday and Sunday are put to Monday)
#
# - if current day is Monday, then birthdays are selected for the current week till Friday
#   + previous Saturday and Sunday


def get_birthdays_per_week(users):
    if not isinstance(users, list):
        raise TypeError("users must be a list")

    start_date = datetime.today().date()
    offset_days = 5 - start_date.weekday() - 1

    if start_date.weekday() == 0:
        start_date = start_date - timedelta(days=2)
        offset_days = 6

    if start_date.weekday() in [5, 6]:
        offset_days = 5 + 6 - start_date.weekday()

    finish_date = start_date + timedelta(days=offset_days)
    result = defaultdict(list)

    for user in users:
        birthday_date = user['birthday'].date()
        birhtday_this_year = birthday_date.replace(year=start_date.year)

        if start_date <= birhtday_this_year <= finish_date:
            weekday = 0

            if birhtday_this_year.weekday() not in [5, 6]:
                weekday = birthday_date.weekday()

            result[weekday].append(user['name'])

    for index, weekday in list(enumerate(CONGRATULATION_WEEKDAYS)):
        if len(result[index]):
            print(f"{weekday}: {', '.join(result[index])}")
