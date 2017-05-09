import datetime


def get_beginning_of_the_week_date():
    beginning_of_the_week = datetime.datetime.now() - datetime.timedelta(days=7)
    return beginning_of_the_week.strftime("%Y-%m-%d 00:00:00")

