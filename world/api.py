from tastypie.resources import ModelResource

from models import Location


class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
