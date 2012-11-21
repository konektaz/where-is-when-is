from tastypie.resources import ModelResource

from world.models import Area, Location


class LocationResource(ModelResource):

    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        allowed_methods = ['get']
        include_absolute_url = True


class AreaResource(ModelResource):

    class Meta:
        queryset = Area.objects.all()
        resource_name = 'area'
        allowed_methods = ['get']
        include_absolute_url = True
        excludes = ['id', 'tree_id', 'lft', 'rght', 'slug', 'varname']
