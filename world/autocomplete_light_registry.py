import autocomplete_light

from .models import Area

autocomplete_light.register(Area, search_fields=('search_names',),
    autocomplete_js_attributes={'placeholder': 'area name ..'})
