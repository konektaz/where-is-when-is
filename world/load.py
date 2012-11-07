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
    'id_2': 'ID_2',
    'name_2': 'NAME_2',
    'varname_2': 'VARNAME_2',
    'nl_name_2': 'NL_NAME_2',
    'hasc_2': 'HASC_2',
    'cc_2': 'CC_2',
    'type_2': 'TYPE_2',
    'engtype_2': 'ENGTYPE_2',
    'validfr_2': 'VALIDFR_2',
    'validto_2': 'VALIDTO_2',
    'remarks_2': 'REMARKS_2',
    'id_3': 'ID_3',
    'name_3': 'NAME_3',
    'varname_3': 'VARNAME_3',
    'nl_name_3': 'NL_NAME_3',
    'hasc_3': 'HASC_3',
    'type_3': 'TYPE_3',
    'engtype_3': 'ENGTYPE_3',
    'validfr_3': 'VALIDFR_3',
    'validto_3': 'VALIDTO_3',
    'remarks_3': 'REMARKS_3',
    'mpoly': 'MULTIPOLYGON',
}


world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/India_admin/IND_adm4.shp'))


def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                      transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
