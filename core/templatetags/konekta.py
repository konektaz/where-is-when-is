# -*- coding: utf-8 -*-

from django import template
from django.conf import settings

from allauth.account.forms import LoginForm


register = template.Library()


@register.inclusion_tag('nav_login_form.html', takes_context=True)
def display_nav_login_form(context):
    form = LoginForm
    return {
        'form': form,
        'socialaccount': context['socialaccount'],
        'request': context['request'],
    }
