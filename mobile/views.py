# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from world.models import Area, Location, LocationType


def home(request):
    return render(request, 'mobile/home.html')


class SearchView(ListView):
    template_name = 'mobile/location_list.html'

    def get_queryset(self):
        lat = float(self.request.GET['lat'])
        lng = float(self.request.GET['lng'])

        pnt = Point(lat, lng)

        return Location.objects.filter(point__distance_lte=(pnt, D(km=5)))


class NavigateView(DetailView):

    template_name = 'mobile/navigate.html'

    def get_object(self):
        return get_object_or_404(Area, path=self.kwargs['path'])

    def get_context_data(self, **kwargs):
        context = super(NavigateView, self).get_context_data(**kwargs)

        area = self.get_object()

        context['subareas'] = area.get_children()
        context['locations'] = Location.objects.filter(point__within=area.geom.geom)
        return context

class LocationDetailView(DetailView):

    model = Location
    template_name = 'mobile/location_detail.html'


class LocationTypeListView(ListView):

    model = LocationType
    template_name = 'mobile/locationtype_list.html'


class LocationTypeDetailView(DetailView):

    model = LocationType
    template_name = 'mobile/locationtype_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LocationTypeDetailView, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.filter(type=self.get_object())
        return context
