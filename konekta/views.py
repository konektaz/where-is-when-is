# -*- coding: utf-8 -*-

from django.shortcuts import render
from olwidget.widgets import InfoMap

from world.models import WorldBorder


def home(request):
    worldborders = WorldBorder.objects.all()#[1:15]

    this_map = InfoMap([(wb.poly_simplify, wb.name_1) for wb in worldborders])

    return render(request, 'home.html', {'map': this_map})
