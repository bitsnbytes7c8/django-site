from django import forms
from django.utils.translation import ugettext_lazy as _
import re

class UserSearchForm(forms.Form):
    name = forms.CharField(label = _("Name"), widget = forms.TextInput(attrs=dict(required=True, max_length=40)))
