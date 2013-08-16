# -*- coding: utf-8 -*-

import urllib2
import json
from django.core.management.base import BaseCommand
from world.models import Location


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        A function to fetch address data for objects in the database.
        Further info: http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding_.2F_Address_lookup
        args: locID = id of specific Location object you wish to update.
        """

        if args:
            for locID in args:
                try:
                    location = Location.objects.get(id=locID)
                    action = updateAddress(location)
                    print action
                except location.DoesNotExist:
                    print u'Location with id=%s does not exist' % locID
        else:
            locations = Location.objects.all()
            for location in locations:
                action = updateAddress(location)
                print action


def updateAddress(location):
    base_url = 'http://nominatim.openstreetmap.org/reverse?format=json&zoom=18&addressdetails=1&email=info@konektaz.info'
    headers = {'Content-type': 'application/json'}

    # Check location for a name and lon/lat
    no_name = False
    no_point = False
    if not location.name:
        no_name = True
    if not location.point:
        no_point = True

    # Specify ident (just in case location.name=None)
    if no_name:
        ident = location.id
    else:
        ident = location.name

    # Delete locations with no name and no lon/lat
    if no_name and no_point:
        location.delete()
        return 'A location was deleted as it had no ' \
              'name and no lon/lat'

    if location.external_id:
        osm_id = location.external_id
        url = '%s&osm_id=%s&osm_type=N' % (base_url, osm_id)

    # If no external_id, fallback to lon/lat
    elif location.point:
        lat = str(location.point.y)
        lon = str(location.point.x)
        url = '%s&lat=%s&lon=%s' % (base_url, lat, lon)

    # If no external_id and no lon/lat delete it
    else:
        location.delete()
        return 'Location %s has no external_id and no lon/lat' % ident

    # Send the request
    request = urllib2.Request(url, '', headers)
    response = urllib2.urlopen(request)

    # Parse the response
    if (response.getcode() == 200):
        comeback = response.read()
        jdata = json.loads(comeback)
        address = jdata['address']
        try:
            house = address['house']
        except:
            house = None
        try:
            road = address['road']
        except:
            road = None
        try:
            suburb = address['suburb']
        except:
            suburb = None
        try:
            city = address['city']
        except:
            city = None
        try:
            county = address['county']
        except:
            county = None
        try:
            state_district = address['state_district']
        except:
            state_district = None
        try:
            state = address['state']
        except:
            state = None
        try:
            country = address['country']
        except:
            country = None
        try:
            code = address['postcode']
        except:
            code = None

        if house and road:
            location.street_address = u'%s, %s' % (house, road)
        elif road:
            location.street_address = u'%s' % road
        if suburb:
            location.locality = u'%s' % suburb
        if city:
            location.region = u'%s' % city
        if state_district and not city:
            location.region = u'%s' % state_district
        elif state and not city:
            location.region = u'%s' % state
        elif county and not city:
            location.region = u'%s' % county
        if country:
            location.country = u'%s' % country
        if code:
            location.postal_code = u'%s' % code

        location.save()

        return u'Updated details for %s' % ident
