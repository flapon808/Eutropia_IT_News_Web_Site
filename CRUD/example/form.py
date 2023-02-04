from django import forms
from example.models import registration

class registrationform(forms.ModelForm):
    class meta:
        model = registration