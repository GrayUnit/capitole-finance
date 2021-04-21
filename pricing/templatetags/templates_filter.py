from django import template

register = template.Library()

@register.filter
def to_dict(instance):
    return instance.__dict__

@register.filter
def items(dictionnary):
    return dictionnary.items()
