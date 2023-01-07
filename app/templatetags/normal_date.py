from django import template

register = template.Library()


@register.filter(name='to_normal_date')
def normalize_date(val):
    date, time = val.split('T')
    time = time.split('+')[0]
    return f'{date} в {time}'


@register.filter(name='normal_cur')
def normal_cur(val):
    return val.replace('RUR', 'RUB')