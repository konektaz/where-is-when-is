# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from world.models import Area, Location


def home(request):
    return render(request, 'mobile/home.html')


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
