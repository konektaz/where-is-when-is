# -*- coding: utf-8 -*-

from django import template

from ..models import Area

register = template.Library()


@register.inclusion_tag('world/nav_countries.html')
def nav_countries():
    countries = Area.objects.filter(level=0)
    return {'countries': countries}
