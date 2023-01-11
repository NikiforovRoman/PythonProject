import random

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


@register.filter(name='strip_tags')
def strip_tags(val):
	import re
	clean = re.compile('<.*?>')
	return re.sub(clean, '', val)


@register.simple_tag
def random_int(a, b=None):
	if b is None:
		a, b = 0, a
	return random.randint(a, b)