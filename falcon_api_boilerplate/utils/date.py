from datetime import datetime
from math import ceil


def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """

    diff = None

    def format_str(multiple, singular, plural):
        delta = ceil(day_diff / multiple)
        return f'{delta if delta > 1 else "a"} {plural if delta > 1 else singular} ago'

    now = datetime.now()

    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(ceil(second_diff / 60)) + " minutes ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return format_str(60, 'hour', 'hours')
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return format_str(86400, 'hour', 'hours')
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return format_str(7, 'day', 'days')
    if day_diff < 31:
        return format_str(31, 'week', 'weeks')
    return format_str(365, 'year', 'years')
