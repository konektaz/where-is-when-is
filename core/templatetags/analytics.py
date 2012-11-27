# -*- coding: utf-8 -*-

from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag('googleanalytics.html')
def google_analytics():
    ga_code = getattr(settings, 'GOOGLE_ANALYTICS', None)
    return {'google_analytics': ga_code}
