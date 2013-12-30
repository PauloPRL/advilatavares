import datetime


def get_days_in_week(day=datetime.date.today()):
    monday = day + datetime.timedelta(days=-day.weekday())

    result = []
    for i in range(0, 7):
        result.append(monday + datetime.timedelta(days=i))

    return result