from django import forms
from cab.models import Cab
class CabForm(forms.ModelForm):
        class Meta:
               model=Cab
               fields="__all__"
