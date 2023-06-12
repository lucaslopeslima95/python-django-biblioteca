from django import template

register = template.Library()

@register.filter
def is_special_user(user):
    return user.is_authenticated and user.is_staff