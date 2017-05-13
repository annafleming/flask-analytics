import datetime


def subtract_from_today_days(days):
    beginning_of_the_week = datetime.datetime.now() - datetime.timedelta(days=days)
    return beginning_of_the_week.strftime("%Y-%m-%d 00:00:00")


def _lambda_get_first_day_of_the_month(date_str, format_in, format_out):
    original_date = datetime.datetime.strptime(str(date_str), format_in)
    return datetime.datetime(int(original_date.year), int(original_date.month), 1).strftime(format_out)


def get_beginning_of_the_month(column, format_in="%Y-%m-%d %H:%M:%S", format_out="%Y-%m-%d"):
    return column.apply(lambda x: _lambda_get_first_day_of_the_month(x, format_in, format_out))
