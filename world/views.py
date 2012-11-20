# -*- coding: utf-8 -*-

from django import http
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import CreateView, View
from django.shortcuts import render, get_object_or_404
from braces.views import LoginRequiredMixin, UserFormKwargsMixin
from olwidget.widgets import InfoLayer, Map, InfoMap

from forms import LocationAddForm
from models import Location, Area


def location_detail(request, slug):
    location = get_object_or_404(Location, slug=slug)

    this_map = InfoMap([(location.point, location.map_html)],
                   {'layers': ['google.streets', 'google.satellite', 'google.hybrid'],
                    'map_div_style': {'width': '570px', 'height': '400px'}})


    display_validate_it = not (request.user.is_authenticated() and location.is_validated_by(request.user))

    return render(request, 'world/location_detail.html', {
        'location': location,
        'map': this_map,
        'display_validate_it': display_validate_it,
    })


def details(request, slug):

    area = get_object_or_404(Area, path=slug)

    subareas = area.get_children()
    locations = Location.objects.filter(point__within=area.geom.geom)

    layers = []

    locations_layer = InfoLayer([(l.point, l.map_html) for l in locations])

    layers.append(locations_layer)

    if subareas:
        subareas_layer = InfoLayer([(sa.geom_simplify, sa.name) for sa in subareas])
        layers.append(subareas_layer)
    else:
        layers.append(InfoLayer([(area.geom_simplify, area.name)]))

    this_map = Map(layers,
                   {'layers': ['google.streets', 'google.satellite', 'google.hybrid'],
                    'map_div_style': {'width': '570px', 'height': '400px'}})

    return render(request, 'world/details.html', {
        'area': area,
        'map': this_map,
        'subareas': subareas,
        'locations': locations,
    })


class LocationAddView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
    model = Location
    form_class = LocationAddForm
    template_name = 'world/location_add.html'


class LocationValidateView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Location

    def get(self, request, *args, **kwargs):
        location = self.get_object()
        location.validated_by.add(request.user)
        location.save()

        return http.HttpResponseRedirect(location.get_absolute_url())
