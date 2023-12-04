from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "David", "birthday": datetime(2023, 12, 1)},
    {"name": "Eve", "birthday": datetime(2023, 12, 2)},
    {"name": "Frank", "birthday": datetime(2023, 12, 3)},
    {"name": "Grace", "birthday": datetime(2023, 12, 4)},
    {"name": "Harry", "birthday": datetime(2023, 12, 5)},
    {"name": "Ivy", "birthday": datetime(2023, 12, 6)},
    {"name": "Jack", "birthday": datetime(2023, 12, 7)},
    {"name": "Katie", "birthday": datetime(2023, 12, 8)},
    {"name": "Liam", "birthday": datetime(2023, 12, 9)},
    {"name": "Mia", "birthday": datetime(2023, 12, 10)},
    {"name": "Noah", "birthday": datetime(2023, 12, 11)},
]

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

  print('start', start_date)
  print('finish', finish_date)

  return result



a = get_birthdays_per_week(users)
print(a)