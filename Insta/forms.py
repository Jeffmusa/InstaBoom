from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date','comments','likes']
       