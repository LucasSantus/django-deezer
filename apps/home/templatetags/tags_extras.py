from django import template
import datetime

register = template.Library()

@register.filter
def convert_seconds_in_minutes(value):
    return str(datetime.timedelta(seconds=value))[2:]

@register.filter
def convert_seconds_in_hours(value):
    hours = str(datetime.timedelta(seconds=value))[:2]
    minutes = str(datetime.timedelta(seconds=value))[3:5]
    return f"{hours} hrs {minutes} min"

@register.filter
def convert_number_in_date(value):
    return str(datetime.date.fromtimestamp(value).strftime('%d/%m/%Y'))