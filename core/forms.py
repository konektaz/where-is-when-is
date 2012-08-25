# -*- coding: utf-8 -*-

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        super(FeedbackForm, self).__init__(*args, **kwargs)
