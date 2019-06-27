from django import template

register = template.Library()


@register.filter(name="get")
def get_filter(value, arg):
    return value.get(arg, "")


@register.filter(name="getattr")
def getattr_filter(value, arg):
    return getattr(value, arg, "")


@register.filter(name="dir")
def dir_filter(value):
    return dir(value)


@register.filter(name="vars")
def vars_filter(value):
    return vars(value)
