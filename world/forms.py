# -*- coding: utf-8 -*-

import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Location
from .widgets import PointWidget


class LocationAddForm(forms.ModelForm):
    point = forms.gis.PointField(widget=PointWidget)

    class Meta:
        model = Location
        exclude = ('zone',)

    def __init__(self, *args, **kwargs):
        self.zone = kwargs.pop('zone', None)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(LocationAddForm, self).__init__(*args, **kwargs)

    def save(self, force_insert=False, force_update=False, commit=True):
        print self.zone
        location = super(LocationAddForm, self).save(commit=False)
        location.zone = self.zone

        if commit:
            location.save()

        return location
