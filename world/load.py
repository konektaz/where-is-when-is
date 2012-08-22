# -*- coding: utf-8 -*-

import os
from django.contrib.gis.utils import LayerMapping

from models import WorldBorder


world_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'varname_1': 'VARNAME_1',
    'nl_name_1': 'NL_NAME_1',
    'hasc_1': 'HASC_1',
    'cc_1': 'CC_1',
    'type_1': 'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    'validfr_1': 'VALIDFR_1',
    'validto_1': 'VALIDTO_1',
    'remarks_1': 'REMARKS_1',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'mpoly': 'MULTIPOLYGON',
}


world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/India_admin/IND_adm1.shp'))


def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                      transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
