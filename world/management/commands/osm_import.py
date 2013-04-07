# -*- coding: utf-8 -*-

import urllib
import urllib2
import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand
from world.models import Location, LocationType
from django.contrib.gis.geos import Point
from django.db.utils import DatabaseError
from django.db import transaction


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
                    location_type = LocationType.objects.get(name="Hospital")

                    with transaction.commit_on_success():

                        if node.attrib.get('lon') is not None:

                            for tag in node:
                                if tag.attrib.get('k') == 'name':
                                    name = tag.attrib.get('v')

                            point = Point(float(node.attrib.get('lon')), float(node.attrib.get('lat')))

                            if node.attrib.get('id') is not None:
                                locations = Location.objects.filter(external_id__exact=node.attrib.get('id'))
                                if locations:
                                    location = locations[0]
                                else:
                                    location = Location(name=name, type=location_type, point=point, external_id = node.attrib.get('id'))


                                # some manual mapping
                                for tag in node:

                                    if tag.attrib.get('k') == 'phone':
                                        if location.phone is None:
                                            location.phone = tag.attrib.get('v')

                                    if tag.attrib.get('k') == 'addr:city':
                                        if location.locality is None:
                                            location.locality = tag.attrib.get('v')

                                    if tag.attrib.get('k') == 'addr:street':
                                        if location.street_address is None:
                                            location.street_address = tag.attrib.get('v')

                                    if tag.attrib.get('k') == 'addr:postcode':
                                        if location.postal_code is None:
                                            location.postal_code = tag.attrib.get('v')

                                    if tag.attrib.get('k') == 'email':
                                        if location.email is None:
                                            location.email = tag.attrib.get('v')

                                    if tag.attrib.get('k') == 'addr:website':
                                        if location.url is None:
                                            location.url = tag.attrib.get('v')

                                    if tag.attrib.get('k') == 'address':
                                        if location.street_address is None:
                                            location.street_address = tag.attrib.get('v')

                                try:
                                    location.save()
                                except DatabaseError as e:
                                    print "Cannot add record", e


