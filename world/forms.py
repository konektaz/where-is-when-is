# -*- coding: utf-8 -*-

from braces.forms import UserKwargModelFormMixin
import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Location
from .widgets import PointWidget


class LocationAddForm(UserKwargModelFormMixin, forms.ModelForm):
    point = forms.gis.PointField(widget=PointWidget)

    class Meta:
        model = Location
        exclude = ('created_by', 'validated_by')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(LocationAddForm, self).__init__(*args, **kwargs)

    def save(self, force_insert=False, force_update=False, commit=True):
        location = super(LocationAddForm, self).save(commit=False)
        location.created_by = self.user

        if commit:
            location.save()

        return location
