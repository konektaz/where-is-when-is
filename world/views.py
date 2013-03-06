# -*- coding: utf-8 -*-

from django import http
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import CreateView, View
from django.shortcuts import render, get_object_or_404
from django.contrib.sites.models import Site
from braces.views import LoginRequiredMixin, UserFormKwargsMixin
from cms.views import details as cms_details
from olwidget.widgets import InfoLayer, Map, InfoMap

from forms import LocationAddForm
from models import Location, Area, Geom


def location_detail(request, slug):
    location = get_object_or_404(Location, slug=slug)

    this_map = InfoMap([(location.point, location.map_html)],
                   {#'layers': ['google.streets', 'google.satellite', 'google.hybrid'],
                    'map_div_style': {'width': '570px', 'height': '400px'}})


    display_validate_it = not (request.user.is_authenticated() and location.is_validated_by(request.user))

    areas = Geom.objects.filter(geom__contains=location.point).order_by('area__lft')
    country = areas[0]
    area = areas[areas.count()-1]
    tweet_url = 'http://%s%s' % (Site.objects.get_current().domain, location.get_absolute_url())
    tweet_text = 'See %s in %s, %s. Please validate this %s location' % (location.name, area, country, location.type.name)

    return render(request, 'world/location_detail.html', {
        'location': location,
        'map': this_map,
        'display_validate_it': display_validate_it,
        'tweet_url': tweet_url,
        'tweet_text': tweet_text,
    })


def details(request, path):

    try:
        area = Area.objects.get(path=path)
    except Area.DoesNotExist:
        # Dirty hack to try Django-CMS pages.
        return cms_details(request, slug=path)

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
                   {#'layers': ['google.streets', 'google.satellite', 'google.hybrid'],
                    'map_div_style': {'width': '570px', 'height': '400px'}})

    return render(request, 'world/details.html', {
        'area': area,
        'map': this_map,
        'subareas': subareas,
        'locations': locations,
    })


def global_autocomplete(request, template_name='global_autocomplete.html'):
    q = request.GET.get('q', '')
    context = {'q': q}

    queries = {}
    queries['areas'] = Area.objects.filter(name__icontains=q)[:10]
    print queries

    context.update(queries)

    return render(request, template_name, context)


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
