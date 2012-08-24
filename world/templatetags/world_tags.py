# -*- coding: utf-8 -*-

from django import template

from ..models import Zone


register = template.Library()


@register.inclusion_tag('world/zones_menu.html')
def zones_menu():
    zones = Zone.objects.all()
    return {'zones': zones}
