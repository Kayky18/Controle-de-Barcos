import datetime

def is_last_day_of_month():
    today = datetime.date.today()
    next_day = today + datetime.timedelta(days=1)

    return today.month != next_day.month

