from django import forms
from django.utils.translation import ugettext_lazy as _
import re

class ProfileForm(forms.Form):
    fullName = forms.CharField(label = _("Full Name"), widget=forms.TextInput(attrs=dict(required=True, max_length=30)))
    phoneNumber = forms.RegexField(regex=r'^[0-9]*$', widget=forms.TextInput(attrs=dict(required=False, max_length=10)), label=_("Phone Number"),
                error_messages={ 'invalid': _("Invalid phone number") })
    #phoneNumber = forms.CharField(label = _("Phone Number"), widget=forms.TextInput(attrs=dict(required=False, max_length=10))
    website = forms.URLField(label=_("Website"))
