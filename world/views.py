# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from olwidget.widgets import InfoMap

from models import Zone


def zone_detail(request, slug):
    zone = get_object_or_404(Zone, slug=slug)

    worldborders = zone.worldborder_set.all()

    this_map = InfoMap([(wb.poly_simplify, wb.name_1) for wb in worldborders])

    return render(request, 'world/zone_detail.html', {'map': this_map})
    pass
