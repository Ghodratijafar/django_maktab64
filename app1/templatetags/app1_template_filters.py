from django import template

register = template.Library()


def akbar(a , b):
    return a + b
register.filter('akbar_filter',akbar)