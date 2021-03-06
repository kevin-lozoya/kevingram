"""Users forms."""

from django import forms


class ProfileForm(forms.Form):
    """Profile form."""

    website = forms.URLField(max_length=200, required=True)
    biografy = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
