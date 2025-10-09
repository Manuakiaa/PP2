import datetime


def subtract_date(date=None, days=5):
    if date is None:
        date = datetime.datetime.now()
    return date - datetime.timedelta(days=days)


def print_sibling_days(date=None):
    if date is None:
        date = datetime.datetime.now()
    print("Yesterday:", (date - datetime.timedelta(days=1)).strftime("%A, %d %B %Y, %H:%M:%S"))
    print("Today:", date.strftime("%A, %d %B %Y, %H:%M:%S"))
    print("Tomorrow:", (date + datetime.timedelta(days=1)).strftime("%A, %d %B %Y, %H:%M:%S"))


def drop_ms(date):
    return date.replace(microsecond=0)


def seconds_diff(date1, date2):
    return round(abs((date1 - date2).total_seconds()))


if __name__ == "__main__":
    now = datetime.datetime.now()
    print(now)
    print(subtract_date(now))

    print_sibling_days(now)

    print(drop_ms(now))

    past = subtract_date(now, 2)
    print("Seconds difference:", seconds_diff(now, past))