# -*- coding: utf-8 -*-

import urllib
import urllib2
import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand
from world.models import Location, LocationType
from django.contrib.gis.geos import Point

class Command(BaseCommand):
    args = '<path_to_xml_query>'
    help = """Imports data from OpenStreetMap

use it with query located in world/fixtures folder like this:

python manage.py osm_import ./world/fixtures/sri_lanka_query.xml

The query XML file contains Overpass XML query.
- You can find examples here: http://wiki.openstreetmap.org/wiki/Overpass_API
- You can test your queries here: http://overpass-api.de/query_form.html
"""

    def handle(self, *args, **options):

        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/xml"}
        url = 'http://overpass-api.de/api/interpreter'

        for xml_path in args:

            with open (xml_path, "r") as myfile:
                xml_query = myfile.read()

            params = urllib.urlencode({'data': xml_query })
            request = urllib2.Request(url, params, headers)
            response = urllib2.urlopen(request)

            if(response.getcode() == 200):
                items = ET.fromstring(response.read())

                for node in items:
                    location_type = LocationType.objects.get(name="hospital")

                    if node.attrib.get('lon') is not None:

                        for tag in node:
                            if tag.attrib.get('k') == 'name':
                                name = tag.attrib.get('v')

                        point = Point(float(node.attrib.get('lon')), float(node.attrib.get('lat')))
                        location = Location(name=name, type=location_type, point=point)
                        location.save()


