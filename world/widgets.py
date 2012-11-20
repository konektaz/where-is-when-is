import floppyforms as forms


class PointWidget(forms.gis.PointWidget, forms.gis.BaseOsmWidget):
    template_name = 'world/osm_map.html'
