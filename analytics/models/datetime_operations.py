import datetime


def subtract_from_today_days(days):
    beginning_of_the_week = datetime.datetime.now() - datetime.timedelta(days=days)
    return beginning_of_the_week.strftime("%Y-%m-%d 00:00:00")

