from django import template

register = template.Library()

# def cut(value, arg):
# 	''' Cuts out the string passed as argument from the string 'value' '''
# 	return value.replace(arg, '')

# # Filter registration method 1
# register.filter('cut', cut)

# Filter registration method 2: Using a decorator
@register.filter(name='cut')
def cut(value, arg):
	''' Cuts out the string passed as argument from the string 'value' '''
	return value.replace(arg, '')
