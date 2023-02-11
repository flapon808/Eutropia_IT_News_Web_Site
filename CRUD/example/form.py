from django import forms
from example.models import registration

class registrationform(forms.ModelForm):
    class Meta:
        model = registration
        fields = "__all__"