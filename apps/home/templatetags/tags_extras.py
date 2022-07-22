from django import template
import datetime

register = template.Library()

@register.filter
def convert_seconds_in_minutes(value):
    return str(datetime.timedelta(seconds=value))[2:]